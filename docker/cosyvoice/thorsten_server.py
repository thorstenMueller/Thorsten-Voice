#!/usr/bin/env python3
# Thorsten-Voice TTS Server basierend auf CosyVoice3
# Verwendung:
#   docker run -p 8000:8000 -v ./models:/cache thorsten-voice-tts
#
# curl Beispiele:
#   curl -X POST http://localhost:8000/tts \
#        -F "text=Hallo, ich bin Thorsten." \
#        --output output.wav
#
#   curl -X POST http://localhost:8000/tts \
#        -F "text=Guten Morgen!" \
#        -F "speed=0.9" \
#        --output output.wav

import os
import sys
import argparse
import logging
import io
import numpy as np

logging.getLogger('matplotlib').setLevel(logging.WARNING)

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

app = FastAPI(title="Thorsten-Voice TTS Server", version="1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    return {"status": "ok", "model": "CosyVoice3-Thorsten"}


@app.post("/tts")
async def tts(
    text: str = Form(..., description="Text to synthesize"),
    speed: float = Form(1.0, description="Speech speed (0.5–2.0)"),
):
    """
    Synthesize German text with Thorsten-Voice.

    Returns a WAV audio file.

    Example:
        curl -X POST http://localhost:8000/tts \\
             -F "text=Hallo Welt" \\
             --output output.wav
    """
    if not text.strip():
        return JSONResponse(status_code=400, content={"error": "Text must not be empty"})

    try:
        all_audio = []
        for chunk in cosyvoice.inference_sft(text, 'thorsten', stream=False, speed=speed):
            all_audio.append(chunk['tts_speech'])

        if not all_audio:
            return JSONResponse(status_code=500, content={"error": "No audio output"})

        final_audio = torch.cat(all_audio, dim=1)
        duration = final_audio.shape[1] / cosyvoice.sample_rate
        wav_buffer = audio_to_wav_bytes(final_audio, cosyvoice.sample_rate)

        return StreamingResponse(
            wav_buffer,
            media_type="audio/wav",
            headers={
                "Content-Disposition": "attachment; filename=thorsten.wav",
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
):
    """
    Synthesize multiple texts and return a single WAV file.

    Example:
        curl -X POST http://localhost:8000/tts_batch \\
             -F $'texts=Erster Satz.\\nZweiter Satz.' \\
             --output batch.wav
    """
    text_list = [t.strip() for t in texts.split('\n') if t.strip()]
    if not text_list:
        return JSONResponse(status_code=400, content={"error": "No texts provided"})

    all_audio = []
    for text in text_list:
        for chunk in cosyvoice.inference_sft(text, 'thorsten', stream=False, speed=speed):
            all_audio.append(chunk['tts_speech'])

    final_audio = torch.cat(all_audio, dim=1)
    wav_buffer = audio_to_wav_bytes(final_audio, cosyvoice.sample_rate)

    return StreamingResponse(
        wav_buffer,
        media_type="audio/wav",
        headers={"Content-Disposition": "attachment; filename=thorsten_batch.wav"}
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Thorsten-Voice TTS Server")
    parser.add_argument('--port',       type=int, default=8000)
    parser.add_argument('--host',       type=str, default='0.0.0.0')
    parser.add_argument('--model_dir',  type=str, default='pretrained_models/CosyVoice3-0.5B')
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
