#!/usr/bin/env python3
# Thorsten-Voice TTS Server (Hessisch) basierend auf CosyVoice3
# Verwendung:
#   docker run -p 8000:8000 -v ./models:/cache thorstenvoice/cosyvoice-tts:hessisch
#
# curl Beispiele:
#   curl -X POST http://localhost:8000/tts \
#        -F "text=Ei guude, ich bin de Thorsten." \
#        --output output.wav
#
#   curl -X POST http://localhost:8000/tts \
#        -F "text=Guude Morje!" \
#        -F "speed=0.9" \
#        --output output.wav

import os
import sys
import argparse
import logging
import io
import numpy as np

logging.getLogger('matplotlib').setLevel(logging.WARNING)

import pyloudnorm as pyln
from german_transliterate.core import GermanTransliterate as _GermanTransliterate

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR)
sys.path.insert(0, os.path.join(ROOT_DIR, 'third_party/Matcha-TTS'))

import torch
import torchaudio
from fastapi import FastAPI, Form
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from cosyvoice.cli.cosyvoice import CosyVoice3

cosyvoice = None

# Speaker-ID des hessischen Finetunes
SPEAKER_ID = 'thorsten_hessisch'

# Lautstärkenormalisierung
TRUE_PEAK_DB = -1.5
SAMPLE_RATE  = 24000
meter        = pyln.Meter(SAMPLE_RATE)

# Textnormalisierung
transliterator = _GermanTransliterate(replace={';': ',', ':': ','}, sep_abbreviation=' -- ')

app = FastAPI(title="Thorsten-Voice TTS Server (Hessisch)", version="1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def normalize_text_fn(text: str) -> str:
    return transliterator.transliterate(text)


def apply_loudnorm(audio_tensor, sample_rate: int, lufs_target: float) -> "torch.Tensor":
    audio_np = audio_tensor.numpy().flatten().astype("float64")
    loudness = meter.integrated_loudness(audio_np)
    if not (float("-inf") < loudness < 0):
        return audio_tensor
    normalized = pyln.normalize.loudness(audio_np, loudness, lufs_target)
    tp_linear = 10 ** (TRUE_PEAK_DB / 20)
    peak = float(np.abs(normalized).max())
    if peak > tp_linear:
        normalized = normalized / peak * tp_linear
    return torch.from_numpy(normalized.astype("float32")).unsqueeze(0)


def patch_frontend(model):
    original_frontend_sft = model.frontend.frontend_sft
    def patched_frontend_sft(tts_text, spk_id):
        model_input = original_frontend_sft(tts_text, spk_id)
        instruct = 'You are a helpful assistant.<|endofprompt|>'
        prompt_token, prompt_token_len = model.frontend._extract_text_token(instruct)
        model_input['prompt_text'] = prompt_token
        model_input['prompt_text_len'] = prompt_token_len
        return model_input
    model.frontend.frontend_sft = patched_frontend_sft
    return model


def audio_to_wav_bytes(audio_tensor, sample_rate):
    buffer = io.BytesIO()
    torchaudio.save(buffer, audio_tensor, sample_rate, format="wav")
    buffer.seek(0)
    return buffer


@app.get("/health")
async def health():
    return {"status": "ok", "model": "CosyVoice3-Thorsten-Hessisch"}


@app.post("/tts")
async def tts(
    text: str = Form(..., description="Text to synthesize (Hochdeutsch eingeben, wird auf Hessisch gesprochen)"),
    speed: float = Form(1.0, description="Speech speed (0.5–2.0)"),
    normalize_text: bool = Form(False, description="Apply german_transliterate (numbers, abbreviations)"),
    normalize_loudness: bool = Form(False, description="Apply EBU R128 loudness normalization"),
    lufs_target: float = Form(-23.0, description="Target loudness in LUFS (e.g. -23 = broadcast, -16 = web)"),
):
    """
    Synthesize German text with the Thorsten-Voice Hessisch dialect model.

    Input text is standard German (Hochdeutsch); output speech is in Hessian dialect.
    Returns a WAV audio file.

    Examples:
        curl -X POST http://localhost:8000/tts \\
             -F "text=Hallo Welt" \\
             --output output.wav

        curl -X POST http://localhost:8000/tts \\
             -F "text=Am 26. Juni 2026 wurden 3 Mrd. Euro investiert." \\
             -F "normalize_text=true" \\
             -F "normalize_loudness=true" \\
             -F "lufs_target=-16" \\
             --output output.wav
    """
    if not text.strip():
        return JSONResponse(status_code=400, content={"error": "Text must not be empty"})

    try:
        input_text = normalize_text_fn(text) if normalize_text else text

        all_audio = []
        for chunk in cosyvoice.inference_sft(input_text, SPEAKER_ID, stream=False, speed=speed):
            all_audio.append(chunk['tts_speech'])

        if not all_audio:
            return JSONResponse(status_code=500, content={"error": "No audio output"})

        final_audio = torch.cat(all_audio, dim=1)
        if normalize_loudness:
            final_audio = apply_loudnorm(final_audio, cosyvoice.sample_rate, lufs_target)

        duration = final_audio.shape[1] / cosyvoice.sample_rate
        wav_buffer = audio_to_wav_bytes(final_audio, cosyvoice.sample_rate)

        return StreamingResponse(
            wav_buffer,
            media_type="audio/wav",
            headers={
                "Content-Disposition": "attachment; filename=thorsten_hessisch.wav",
                "X-Sample-Rate": str(cosyvoice.sample_rate),
                "X-Duration": f"{duration:.2f}",
            }
        )
    except Exception as e:
        logging.error(f"TTS error: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.post("/tts_batch")
async def tts_batch(
    texts: str = Form(..., description="Multiple texts separated by newline"),
    speed: float = Form(1.0),
    normalize_text: bool = Form(False, description="Apply german_transliterate"),
    normalize_loudness: bool = Form(False, description="Apply EBU R128 loudness normalization"),
    lufs_target: float = Form(-23.0, description="Target loudness in LUFS"),
):
    """
    Synthesize multiple texts and return a single WAV file.

    Example:
        curl -X POST http://localhost:8000/tts_batch \\
             -F $'texts=Erster Satz.\\nZweiter Satz.' \\
             -F "normalize_text=true" \\
             --output batch.wav
    """
    text_list = [t.strip() for t in texts.split('\n') if t.strip()]
    if not text_list:
        return JSONResponse(status_code=400, content={"error": "No texts provided"})

    all_audio = []
    for text in text_list:
        input_text = normalize_text_fn(text) if normalize_text else text
        for chunk in cosyvoice.inference_sft(input_text, SPEAKER_ID, stream=False, speed=speed):
            all_audio.append(chunk['tts_speech'])

    final_audio = torch.cat(all_audio, dim=1)
    if normalize_loudness:
        final_audio = apply_loudnorm(final_audio, cosyvoice.sample_rate, lufs_target)

    wav_buffer = audio_to_wav_bytes(final_audio, cosyvoice.sample_rate)

    return StreamingResponse(
        wav_buffer,
        media_type="audio/wav",
        headers={"Content-Disposition": "attachment; filename=thorsten_hessisch_batch.wav"}
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Thorsten-Voice TTS Server (Hessisch)")
    parser.add_argument('--port',       type=int, default=8000)
    parser.add_argument('--host',       type=str, default='0.0.0.0')
    parser.add_argument('--model_dir',  type=str, default='pretrained_models/CosyVoice3-Hessisch')
    parser.add_argument('--checkpoint', type=str, default=None,
                        help='Optional: path to fine-tuned LLM checkpoint (overrides model_dir/llm.pt)')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logging.info(f"Loading model from {args.model_dir} ...")
    cosyvoice = CosyVoice3(args.model_dir)
    cosyvoice = patch_frontend(cosyvoice)
    logging.info("Model ready ✓")
    logging.info(f"Server running on http://{args.host}:{args.port}")
    logging.info("Endpoints: POST /tts  POST /tts_batch  GET /health")

    uvicorn.run(app, host=args.host, port=args.port)
