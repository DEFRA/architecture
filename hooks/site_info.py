"""MkDocs hook that sets ``extra.last_updated`` for the alpha phase banner.

Uses the date of the latest git commit, so the banner shows when the content
last changed rather than when the site happened to be built. Falls back to
today's date outside a git checkout.
"""

from __future__ import annotations

import datetime
import subprocess


def on_config(config):
    try:
        stamp = subprocess.run(
            ["git", "log", "-1", "--format=%cs"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        day = datetime.date.fromisoformat(stamp)
    except (OSError, ValueError, subprocess.CalledProcessError):
        day = datetime.date.today()
    config["extra"]["last_updated"] = f"{day.day} {day:%B %Y}"
    return config
