# Setup Guide — quanta-screenshot (Ubuntu 22.04+ GNOME)

## 1) Clone and enter project
```bash
git clone https://github.com/ThatDeparted2061/quanta-screenshot.git
cd quanta-screenshot
```

## 2) Install dependencies
```bash
./scripts/install.sh
```

This installs:
- Python venv + pip deps
- `tesseract-ocr` (OCR)
- `gnome-screenshot` (screen capture)
- `libnotify-bin` (`notify-send` notifications)

## 3) Configure model
```bash
cp .env.example .env
nano .env
```

Default values:
```env
OLLAMA_BASE_URL=http://127.0.0.1:11434
OLLAMA_MODEL=llama3.1:8b
NOTIFY_TIMEOUT_MS=4500
```

## 4) Start Ollama
```bash
ollama pull llama3.1:8b
ollama serve
```

## 5) Register hotkey
```bash
./scripts/register_hotkey_gnome.sh
```

Hotkey: `Ctrl + Shift + X`

## 6) Test once manually
```bash
./scripts/run_once.sh
```

Expected notification format:
- `Q2. A`

## Troubleshooting
- **No text detected**: increase font size / zoom question area.
- **UNKNOWN output**: OCR or prompt ambiguity; try a clearer screenshot.
- **No notification**: verify `libnotify-bin` is installed and desktop notifications are enabled.
- **Model call fails**: ensure Ollama is running on `127.0.0.1:11434`.
