# quanta-screenshot

A local Ubuntu app that:
1. Triggers on `Ctrl+Shift+X`
2. Captures full-screen screenshot
3. Runs OCR to read the question text
4. Sends text to local LLM (Ollama)
5. Shows answer in desktop notification (format: `Q2. A`)

## ⚠️ Use Responsibly
Use only for your own practice/testing environments where you have permission.

## Requirements
- Ubuntu (GNOME)
- Python 3.10+
- Ollama running locally

## Setup
```bash
cd quanta-screenshot
./scripts/install.sh
```

If needed, edit `.env`:
```bash
cp .env.example .env
nano .env
```

## Register Hotkey
```bash
./scripts/register_hotkey_gnome.sh
```

## Manual Test
```bash
./scripts/run_once.sh
```

You should see a notification like:
- `Q2. A`

## Output Format
- Strict notification format: `Q<number>. <A/B/C/UNKNOWN>`
- Examples: `Q2. A`, `Q11. C`, `Qunknown. UNKNOWN`

## Notes
- OCR quality depends on screenshot clarity.
- If question text is blurry, output may be `Qunknown. UNKNOWN`.
- Output is intentionally strict and short: only `Q<number>. <A/B/C/UNKNOWN>`.
- You can change model in `.env` (`OLLAMA_MODEL=...`).
