import json
import os
import re
from typing import Optional, Tuple

import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3.5:4b")


PROMPT_TEMPLATE = """
You are solving a multiple-choice quiz question extracted from a screenshot.

Return STRICT JSON only, with keys:
- question_number: string (prefer just the number like "2", otherwise "unknown")
- answer: one of "A", "B", "C", "D", or "UNKNOWN"

Rules:
- Only choose from A/B/C/D.
- If text is unclear, set answer to "UNKNOWN".
- No explanation text.

Question text:
---
{question_text}
---
""".strip()


def _extract_json(raw: str) -> Optional[dict]:
    raw = raw.strip()
    if raw.startswith("{") and raw.endswith("}"):
        try:
            return json.loads(raw)
        except Exception:
            pass

    match = re.search(r"\{[\s\S]*\}", raw)
    if match:
        try:
            return json.loads(match.group(0))
        except Exception:
            return None
    return None


def solve_question(question_text: str) -> Tuple[str, str]:
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": PROMPT_TEMPLATE.format(question_text=question_text[:6000]),
        "stream": False,
    }

    try:
        resp = requests.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload, timeout=45)
        resp.raise_for_status()
        data = resp.json()
        model_output = data.get("response", "").strip()
    except Exception:
        return "unknown", "UNKNOWN"

    parsed = _extract_json(model_output)
    if not parsed:
        return "unknown", "UNKNOWN"

    qn = str(parsed.get("question_number", "unknown")).strip()
    qn = qn.upper().replace("Q", "").replace(".", "").strip() or "unknown"

    ans = str(parsed.get("answer", "UNKNOWN")).upper().strip()
    if ans not in {"A", "B", "C", "D", "UNKNOWN"}:
        ans = "UNKNOWN"

    return qn, ans
