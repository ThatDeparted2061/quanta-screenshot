import subprocess
import tempfile
from pathlib import Path

import pytesseract
from PIL import Image


def capture_fullscreen() -> Path:
    tmp = tempfile.NamedTemporaryFile(prefix="quizshot_", suffix=".png", delete=False)
    tmp_path = Path(tmp.name)
    tmp.close()

    # GNOME screenshot tool (Ubuntu default)
    subprocess.run(["gnome-screenshot", "-f", str(tmp_path)], check=True)
    return tmp_path


def image_to_text(image_path: Path) -> str:
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return (text or "").strip()
