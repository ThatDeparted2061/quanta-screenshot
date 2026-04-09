import traceback
from pathlib import Path

from answer_engine import solve_question
from notifier import notify
from ocr import capture_fullscreen, image_to_text


def run_once() -> None:
    shot_path: Path = capture_fullscreen()
    try:
        text = image_to_text(shot_path)

        if not text:
            notify("Quiz Assistant", "No text detected in screenshot")
            return

        qn, ans = solve_question(text)
        message = f"Q{qn}. {ans}"
        notify("Quiz Assistant Answer", message)
    finally:
        shot_path.unlink(missing_ok=True)


if __name__ == "__main__":
    try:
        run_once()
    except Exception as exc:
        traceback.print_exc()
        notify("Quiz Assistant Error", str(exc)[:180])
