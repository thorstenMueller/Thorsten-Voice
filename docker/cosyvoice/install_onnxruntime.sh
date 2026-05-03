#!/bin/bash
# Platform-aware onnxruntime installation
# - ARM64 (Mac M1/M2, ARM servers): onnxruntime (CPU only)
# - x86_64: onnxruntime-gpu if CUDA available, else onnxruntime

ARCH=$(uname -m)

if [ "$ARCH" = "aarch64" ] || [ "$ARCH" = "arm64" ]; then
    echo "ARM64 detected — installing onnxruntime (CPU)"
    pip install onnxruntime
else
    # x86_64: try GPU version first, fall back to CPU
    echo "x86_64 detected — trying onnxruntime-gpu..."
    pip install onnxruntime-gpu==1.18.0 \
        --index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/onnxruntime-cuda-12/pypi/simple/ \
        2>/dev/null || {
        echo "onnxruntime-gpu not available, falling back to CPU version"
        pip install onnxruntime
    }
fi

echo "onnxruntime installed ✓"
