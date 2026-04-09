import shutil
import subprocess
import tempfile
from pathlib import Path

import pytesseract
from PIL import Image


class ScreenshotError(RuntimeError):
    pass


def _run_capture(cmd: list[str], out_path: Path) -> bool:
    try:
        proc = subprocess.run(cmd, check=False, capture_output=True, text=True)
    except Exception:
        return False

    if proc.returncode != 0:
        return False

    return out_path.exists() and out_path.stat().st_size > 0


def capture_fullscreen() -> Path:
    tmp = tempfile.NamedTemporaryFile(prefix="quizshot_", suffix=".png", delete=False)
    tmp_path = Path(tmp.name)
    tmp.close()

    gnome_bin = shutil.which("gnome-screenshot") or "/usr/bin/gnome-screenshot"
    grim_bin = shutil.which("grim")
    import_bin = shutil.which("import")
    scrot_bin = shutil.which("scrot")

    commands: list[list[str]] = []
    if Path(gnome_bin).exists():
        commands.append([gnome_bin, "-f", str(tmp_path)])
    if grim_bin:
        commands.append([grim_bin, str(tmp_path)])
    if import_bin:
        commands.append([import_bin, "-window", "root", str(tmp_path)])
    if scrot_bin:
        commands.append([scrot_bin, str(tmp_path)])

    for cmd in commands:
        if _run_capture(cmd, tmp_path):
            return tmp_path

    raise ScreenshotError(
        "Could not capture screenshot. Install/enable one of: gnome-screenshot, grim, scrot, or ImageMagick import."
    )


def image_to_text(image_path: Path) -> str:
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return (text or "").strip()
