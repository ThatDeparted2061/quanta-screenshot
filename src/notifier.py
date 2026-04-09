import os
import subprocess

from dotenv import load_dotenv

load_dotenv()

NOTIFY_TIMEOUT_MS = os.getenv("NOTIFY_TIMEOUT_MS", "4500")


def notify(title: str, body: str) -> None:
    subprocess.run(
        [
            "notify-send",
            title,
            body,
            "-t",
            str(NOTIFY_TIMEOUT_MS),
            "-u",
            "normal",
        ],
        check=False,
    )
