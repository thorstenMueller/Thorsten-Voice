FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    HF_HOME=/data/hf-cache \
    KOKORO_EPOCH=7 \
    KOKORO_DEVICE=cpu \
    HF_REPO_ID=Thorsten-Voice/Kokoro-Hessisch \
    PORT=8000

# espeak-ng: Phonemizer-Backend für misaki (G2P)
# libsndfile1: Laufzeitabhängigkeit von soundfile
# git: nötig für "pip install git+https://..." (misaki/kokoro Forks)
# curl: fürs HEALTHCHECK
RUN apt-get update && apt-get install -y --no-install-recommends \
        espeak-ng \
        libsndfile1 \
        curl \
        git \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

RUN mkdir -p /data/hf-cache

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=90s --retries=5 \
    CMD curl -f "http://localhost:${PORT}/health" || exit 1

CMD ["sh", "-c", "uvicorn app.server:app --host 0.0.0.0 --port ${PORT}"]
