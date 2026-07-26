import io
import logging
import os

import numpy as np
import soundfile as sf
import torch
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from huggingface_hub import hf_hub_download
from kokoro import KModel, KPipeline
from pydantic import BaseModel, Field

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("thorsten-kokoro")

REPO_ID = os.environ.get("HF_REPO_ID", "Thorsten-Voice/Kokoro")
EPOCH = os.environ.get("KOKORO_EPOCH", "5").strip()
DEVICE = os.environ.get("KOKORO_DEVICE", "cpu")
SAMPLE_RATE = 24000

_state: dict = {}


def _checkpoint_filenames(epoch: str) -> tuple[str, str]:
    """Map an epoch identifier to the (model, voicepack) filenames in the HF repo."""
    if epoch in ("5", "default", ""):
        return "model.pth", "voices/thorsten.pt"
    return f"model_ep{epoch}.pth", f"voices/thorsten_ep{epoch}.pt"


app = FastAPI(
    title="Thorsten-Voice Kokoro TTS API",
    description="Minimaler API-Server rund um das deutsche Kokoro-82M Fine-tune von Thorsten-Voice.",
    version="1.0.0",
)


@app.on_event("startup")
def load_model() -> None:
    model_file, voice_file = _checkpoint_filenames(EPOCH)
    log.info("Lade %s (Checkpoint %s) auf Gerät '%s' ...", REPO_ID, EPOCH, DEVICE)

    config_path = hf_hub_download(repo_id=REPO_ID, filename="config.json")
    model_path = hf_hub_download(repo_id=REPO_ID, filename=model_file)
    voice_path = hf_hub_download(repo_id=REPO_ID, filename=voice_file)

    kmodel = KModel(repo_id="hexgrad/Kokoro-82M", config=config_path, model=model_path)
    kmodel = kmodel.to(DEVICE).eval()

    pipeline = KPipeline(lang_code="d", repo_id="hexgrad/Kokoro-82M", model=kmodel)

    # Workaround: misaki's German G2P kann 'ʏ' (kurzes ü, z.B. in "Brücke")
    # erzeugen - dieses Symbol ist nicht im 178-Symbol-Vokabular von Kokoro
    # enthalten (nur das lange 'y'). Siehe Model Card "Known limitations".
    _original_g2p = pipeline.g2p
    pipeline.g2p = lambda text: (
        lambda ps, tok: (ps.replace("ʏ", "y"), tok)
    )(*_original_g2p(text))

    voice = torch.load(voice_path, map_location="cpu", weights_only=True)

    _state["pipeline"] = pipeline
    _state["voice"] = voice
    _state["epoch"] = EPOCH
    log.info("Modell geladen und einsatzbereit.")


class TTSRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Der zu sprechende Text.")
    speed: float = Field(
        1.0, gt=0.0, le=2.0, description="Sprechgeschwindigkeit (1.0 = normal)."
    )


@app.get("/health")
def health():
    ready = "pipeline" in _state
    return {
        "status": "ok" if ready else "loading",
        "repo_id": REPO_ID,
        "epoch": EPOCH,
        "device": DEVICE,
    }


@app.post("/tts")
def tts(req: TTSRequest):
    if "pipeline" not in _state:
        raise HTTPException(503, "Modell wird noch geladen, bitte kurz warten.")

    text = req.text.strip()
    if not text:
        raise HTTPException(400, "Feld 'text' darf nicht leer sein.")

    pipeline = _state["pipeline"]
    voice = _state["voice"]

    try:
        chunks = [audio for _, _, audio in pipeline(text, voice=voice, speed=req.speed)]
    except Exception as exc:  # noqa: BLE001
        log.exception("Inferenz fehlgeschlagen")
        raise HTTPException(500, f"Inferenzfehler: {exc}") from exc

    if not chunks:
        raise HTTPException(500, "Es wurde kein Audio erzeugt.")

    audio = np.concatenate(chunks)
    buf = io.BytesIO()
    sf.write(buf, audio, SAMPLE_RATE, format="WAV")
    buf.seek(0)

    return StreamingResponse(
        buf,
        media_type="audio/wav",
        headers={"Content-Disposition": 'attachment; filename="output.wav"'},
    )
