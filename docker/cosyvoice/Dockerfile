FROM python:3.11-slim-bookworm

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# System dependencies
RUN apt-get update && apt-get install -y \
    git \
    sox \
    libsox-fmt-all \
    ffmpeg \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Clone CosyVoice at the tested commit
WORKDIR /app
RUN git clone https://github.com/FunAudioLLM/CosyVoice.git && \
    cd CosyVoice && \
    git checkout ace7c47 && \
    git submodule update --init --recursive

WORKDIR /app/CosyVoice

# Install Python dependencies
RUN pip install --upgrade pip setuptools

# openai-whisper separately (avoids pkg_resources build issue)
RUN pip install openai-whisper

# Filter out packages that are GPU/x86-only or cause build issues:
# - openai-whisper: installed above
# - onnxruntime-gpu: platform-specific, installed below
# - grpcio: pinned version has build issues, installed below
# - tensorrt*: NVIDIA TensorRT, x86+CUDA only
# - deepspeed: optional, requires CUDA toolkit to build
RUN grep -v -E \
    "openai-whisper|onnxruntime|grpcio|tensorrt|deepspeed" \
    requirements.txt > requirements_fixed.txt && \
    pip install -r requirements_fixed.txt

# grpcio in compatible version
RUN pip install "grpcio>=1.62.0" "grpcio-tools>=1.62.0"

# onnxruntime — platform-aware
COPY install_onnxruntime.sh /tmp/install_onnxruntime.sh
RUN chmod +x /tmp/install_onnxruntime.sh && /tmp/install_onnxruntime.sh

# Server dependencies
RUN pip install fastapi uvicorn python-multipart huggingface_hub

# Compatibility fix for Matcha-TTS
RUN echo "" > third_party/Matcha-TTS/matcha/utils/__init__.py

ENV PYTHONPATH=/app/CosyVoice:/app/CosyVoice/third_party/Matcha-TTS

COPY thorsten_server.py /app/CosyVoice/thorsten_server.py
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
