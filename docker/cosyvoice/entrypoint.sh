#!/bin/bash
set -e

MODEL_DIR="/app/CosyVoice/pretrained_models/CosyVoice3-0.5B"
BASE_MODEL="FunAudioLLM/Fun-CosyVoice3-0.5B-2512"
THORSTEN_MODEL="Thorsten-Voice/CosyVoice3"

echo "========================================="
echo "  Thorsten-Voice CosyVoice3 TTS Server"
echo "========================================="

# Download base model if CosyVoice-BlankEN tokenizer is missing
if [ ! -f "$MODEL_DIR/CosyVoice-BlankEN/config.json" ]; then
    echo "[1/2] Downloading base model (~5.5 GB, first run only)..."
    hf download "$BASE_MODEL" --local-dir "$MODEL_DIR"
    echo "Base model downloaded ✓"
else
    echo "[1/2] Base model already present ✓"
fi

# Download Thorsten weights if any of the three files is missing
if [ ! -f "$MODEL_DIR/llm.pt" ] || \
   [ ! -f "$MODEL_DIR/flow.pt" ] || \
   [ ! -f "$MODEL_DIR/spk2info.pt" ]; then
    echo "[2/2] Downloading Thorsten-Voice fine-tuned weights (~3.2 GB)..."
    hf download "$THORSTEN_MODEL" \
        --local-dir "$MODEL_DIR" \
        --include "llm.pt" "flow.pt" "spk2info.pt"
    echo "Thorsten weights downloaded ✓"
else
    echo "[2/2] Thorsten weights already present ✓"
fi

echo ""
echo "Starting TTS server on port ${PORT:-8000}..."
echo "API: POST http://localhost:${PORT:-8000}/tts"
echo ""

cd /app/CosyVoice
exec python3 thorsten_server.py \
    --host 0.0.0.0 \
    --port "${PORT:-8000}" \
    --model_dir "$MODEL_DIR"
