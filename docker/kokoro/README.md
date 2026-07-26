# Thorsten-Voice Kokoro – TTS API Docker Image

Ein minimaler API-Server rund um das deutsche Kokoro-82M Fine-tune
[`Thorsten-Voice/Kokoro`](https://huggingface.co/Thorsten-Voice/Kokoro).
Das Modell wird beim Containerstart **einmal geladen** und steht danach per
HTTP/cURL für beliebig viele Anfragen bereit. Läuft ohne GPU (CPU-Build von
PyTorch) auf Linux, Windows und macOS.

## Build

```bash
docker compose build
```

oder ohne Compose:

```bash
docker build -t thorsten-voice/kokoro-tts:latest .
```

## Start

```bash
docker compose up -d
```

oder ohne Compose:

```bash
docker run -d --name thorsten-kokoro-tts \
  -p 8000:8000 \
  -v hf-cache:/data/hf-cache \
  thorsten-voice/kokoro-tts:latest
```

Der erste Start lädt das Modell von Hugging Face herunter (~ein paar hundert
MB) und kann daher etwas dauern. Über das gemountete `hf-cache`-Volume bleibt
der Download bei künftigen Neustarts erhalten.

Fortschritt prüfen:

```bash
curl http://localhost:8000/health
```

Antwort, sobald bereit:

```json
{"status": "ok", "repo_id": "Thorsten-Voice/Kokoro", "epoch": "5", "device": "cpu"}
```

## Verwendung

```bash
curl -X POST http://localhost:8000/tts \
  -H "Content-Type: application/json" \
  -d '{"text": "Hallo, hier spricht Thorsten.", "speed": 1.0}' \
  --output output.wav
```

Mit angepasster Geschwindigkeit (langsamer):

```bash
curl -X POST http://localhost:8000/tts \
  -H "Content-Type: application/json" \
  -d '{"text": "Das hier klingt etwas gemütlicher.", "speed": 0.85}' \
  --output slow.wav
```

Schneller:

```bash
curl -X POST http://localhost:8000/tts \
  -H "Content-Type: application/json" \
  -d '{"text": "Und das hier etwas zügiger.", "speed": 1.3}' \
  --output fast.wav
```

`speed` ist optional, Standardwert ist `1.0`. Erlaubter Bereich: `> 0.0` bis `2.0`.

## Konfiguration (Umgebungsvariablen)

| Variable         | Standard                | Beschreibung                                                        |
| ---------------- | ------------------------ | -------------------------------------------------------------------- |
| `KOKORO_EPOCH`   | `5`                      | Welcher Stage-2-Checkpoint geladen wird (`1`–`10`, `5` = Standard).  |
| `KOKORO_DEVICE`  | `cpu`                    | `cpu` oder `cuda` (nur mit passendem GPU-Setup, siehe unten).        |
| `HF_REPO_ID`      | `Thorsten-Voice/Kokoro`  | Hugging-Face-Repo, aus dem das Modell geladen wird.                  |
| `PORT`           | `8000`                   | Port, auf dem der Server im Container lauscht.                      |

Andere Checkpoints wählen, z. B. Epoch 10 (etwas engere/schnellere Prosodie):

```bash
docker run -d --name thorsten-kokoro-tts \
  -p 8000:8000 \
  -e KOKORO_EPOCH=10 \
  -v hf-cache:/data/hf-cache \
  thorsten-voice/kokoro-tts:latest
```

Das Modell wird pro Container einmal beim Start geladen – ein Wechsel des
Checkpoints erfordert einen Neustart des Containers.

## GPU-Betrieb (optional, nur Linux + NVIDIA)

Das Image ist standardmäßig auf CPU ausgelegt, damit es überall ohne weitere
Voraussetzungen läuft. Für GPU-Beschleunigung unter Linux mit NVIDIA Container
Toolkit:

1. In `requirements.txt` die Zeile `--extra-index-url
   https://download.pytorch.org/whl/cpu` entfernen bzw. durch den passenden
   CUDA-Index ersetzen und `torch` entsprechend anpassen.
2. Beim Start `-e KOKORO_DEVICE=cuda --gpus all` ergänzen.

Da Kokoro-82M ohnehin CPU-freundlich und in Echtzeit oder schneller läuft, ist
GPU-Beschleunigung meist nicht notwendig.

## API-Referenz

- `GET /health` – Statuscheck (`ok` / `loading`), zeigt geladenen Checkpoint und Device.
- `POST /tts` – Body: `{"text": "...", "speed": 1.0}` → Antwort: `audio/wav` (24 kHz, mono).

## Bekannte Einschränkungen

Übernommen aus der [Model Card](https://huggingface.co/Thorsten-Voice/Kokoro):

- Bindestrich-Komposita-Adjektive (z. B. *„atmosphärisch-optisches“*) können an
  der Bindestrich-Grenze zu unnatürlicher Prosodie führen.
- Sehr lange Sätze können abgeschnitten werden – lange Texte am besten vorher
  auf Satzgrenzen aufteilen.
- Der `ʏ`→`y`-G2P-Workaround für kurzes ü (z. B. „Brücke“) ist bereits im
  Server enthalten.

## Credits

- Modell & Fine-tuning: [Thorsten-Voice/Kokoro](https://huggingface.co/Thorsten-Voice/Kokoro)
- Basis-Architektur: [hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)
- Trainings-Rezept: [kikiri-tts](https://github.com/semidark/kikiri-tts) von semidark
