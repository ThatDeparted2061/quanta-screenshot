#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

sudo apt-get update
sudo apt-get install -y python3-venv python3-pip tesseract-ocr gnome-screenshot libnotify-bin

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

if [[ ! -f .env ]]; then
  cp .env.example .env
  echo "[+] Created .env from .env.example"
fi

echo "[+] Install complete"
echo "[i] Ensure Ollama is running and model is pulled: ollama pull qwen3.5:4b"
