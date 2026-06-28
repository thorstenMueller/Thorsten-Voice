# Thorsten-Voice · CosyVoice TTS Server

German Text-to-Speech in a Docker container, powered by [CosyVoice3](https://github.com/FunAudioLLM/CosyVoice) and fine-tuned on the [Thorsten-Voice](https://www.thorsten-voice.de) dataset.

Send a text via HTTP and get a WAV audio file back. That's it.

## Quickstart

```bash
docker run -p 8000:8000 \
  -v cosyvoice_models:/app/CosyVoice/pretrained_models \
  thorstenvoice/cosyvoice-tts
```

**First start:** the models are downloaded automatically (~8.5 GB). This takes 5–15 minutes depending on your connection. Subsequent starts are fast (~30 seconds) since the models are cached in the volume.

Once you see `Uvicorn running on http://0.0.0.0:8000`, the server is ready.

## Generate audio

```bash
curl -X POST http://localhost:8000/tts \
     -F "text=Hallo, ich bin Thorsten. Schön, dass du da bist." \
     --output thorsten.wav
```

That's all — `thorsten.wav` contains the synthesized speech.

## Options

**Adjust speaking speed** (0.5 = slow, 1.0 = normal, 2.0 = fast):

```bash
curl -X POST http://localhost:8000/tts \
     -F "text=Das hier wird etwas langsamer gesprochen." \
     -F "speed=0.85" \
     --output output.wav
```

**Normalize text** — converts numbers, abbreviations and special characters to spoken words (e.g. "3 Mrd. Euro" → "drei Milliarden Euro"):

```bash
curl -X POST http://localhost:8000/tts \
     -F "text=Am 26. Juni 2026 wurden 3 Mrd. Euro investiert." \
     -F "normalize_text=true" \
     --output output.wav
```

**Normalize loudness** — applies EBU R128 loudness normalization, preventing clipping and intersample overloads during MP3 playback. Default target: -23 dB (broadcast standard):

```bash
curl -X POST http://localhost:8000/tts \
     -F "text=Hallo, ich bin Thorsten." \
     -F "normalize_loudness=true" \
     --output output.wav
```

Use `lufs_target` to adjust the loudness level (-10 = very loud, -23 = broadcast, -30 = quiet):

```bash
curl -X POST http://localhost:8000/tts \
     -F "text=Hallo, ich bin Thorsten." \
     -F "normalize_loudness=true" \
     -F "lufs_target=-16" \
     --output output.wav
```

**Combine all options:**

```bash
curl -X POST http://localhost:8000/tts \
     -F "text=Am 26. Juni 2026 wurden 3 Mrd. Euro investiert." \
     -F "speed=0.95" \
     -F "normalize_text=true" \
     -F "normalize_loudness=true" \
     -F "lufs_target=-16" \
     --output output.wav
```

**Synthesize multiple sentences into one file:**

```bash
curl -X POST http://localhost:8000/tts_batch \
     -F $'texts=Erster Satz.\nZweiter Satz.\nDritter Satz.' \
     -F "normalize_text=true" \
     --output batch.wav
```

**Check if the server is running:**

```bash
curl http://localhost:8000/health
# {"status":"ok","model":"CosyVoice3-Thorsten"}
```

## API reference

| Parameter | Endpoint | Type | Default | Description |
|---|---|---|---|---|
| `text` | `/tts` | string | required | Text to synthesize |
| `texts` | `/tts_batch` | string | required | Texts separated by newline |
| `speed` | both | float | `1.0` | Speaking speed (0.5–2.0) |
| `normalize_text` | both | bool | `false` | Apply german_transliterate |
| `normalize_loudness` | both | bool | `false` | Apply EBU R128 loudness normalization |
| `lufs_target` | both | float | `-23.0` | Target loudness in dB (-10 to -30) |

## docker-compose (recommended)

Create a `docker-compose.yml`:

```yaml
services:
  cosyvoice-tts:
    image: thorstenvoice/cosyvoice-tts:cosyvoice3
    ports:
      - "8000:8000"
    volumes:
      - cosyvoice_models:/app/CosyVoice/pretrained_models
    restart: unless-stopped

volumes:
  cosyvoice_models:
```

Then:

```bash
docker compose up
```

## GPU support (Linux + NVIDIA only)

Add the `deploy` section to your `docker-compose.yml`:

```yaml
services:
  cosyvoice-tts:
    image: thorstenvoice/cosyvoice-tts:cosyvoice3
    ports:
      - "8000:8000"
    volumes:
      - cosyvoice_models:/app/CosyVoice/pretrained_models
    restart: unless-stopped
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]

volumes:
  cosyvoice_models:
```

## Change the port

```bash
docker run -p 9000:9000 \
  -e PORT=9000 \
  -v cosyvoice_models:/app/CosyVoice/pretrained_models \
  thorstenvoice/cosyvoice-tts
```

## Performance

Benchmarked with these two test texts:

**Short** (~8 words):
> "Hallo, hier ist Thorsten. Schön, dass Du da bist."

**Long** (~80 words):
> "Für mich sind alle Menschen gleich, unabhängig von Geschlecht, sexueller Orientierung, Religion, Hautfarbe oder Geokoordinaten der Geburt. Ich glaube an eine globale Welt, wo jeder überall willkommen ist und freies Wissen und Bildung kostenfrei für jeden zur Verfügung steht. Ich habe meine Stimme der Allgemeinheit gespendet, in der Hoffnung darauf, dass sie in diesem Sinne genutzt wird."

| Hardware | Short text | Long text |
|----------|-----------|-----------|
| MacBook Air M1 (CPU) | 47s | 4:30 min |
| QNAP NAS Intel (CPU) | 50s | — |
| RunPod RTX 4090 (GPU) | **2.9s** | **12.9s** |

GPU is ~16x faster than CPU. Even a mid-range GPU will significantly outperform CPU inference.

## Model

This container uses the [Thorsten-Voice/CosyVoice3](https://huggingface.co/Thorsten-Voice/CosyVoice3) model, fine-tuned from [FunAudioLLM/Fun-CosyVoice3-0.5B-2512](https://huggingface.co/FunAudioLLM/Fun-CosyVoice3-0.5B-2512) on the [Thorsten-Voice 2022.10](https://www.thorsten-voice.de) dataset.

## Links

- [Thorsten-Voice Website](https://www.thorsten-voice.de)
- [HuggingFace Space (live demo)](https://huggingface.co/spaces/Thorsten-Voice/CosyVoice)
- [Model on HuggingFace](https://huggingface.co/Thorsten-Voice/CosyVoice3)
- [CosyVoice GitHub](https://github.com/FunAudioLLM/CosyVoice)
- [Source on GitHub](https://github.com/thorstenMueller/Thorsten-Voice/tree/main/docker/cosyvoice)
