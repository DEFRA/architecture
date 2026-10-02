"""Warn about guardrails that have not been reviewed for more than 12 months.

Used by the build job in .github/workflows/ci.yml:

    python scripts/review_due.py

Prints a GitHub Actions warning annotation for each guardrail whose
``last_reviewed`` date is more than 12 months old. It never fails the build:
an overdue review is a prompt for the area owner, not a broken page.
"""

from __future__ import annotations

import datetime
import importlib.util
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MONTHS = 12


def overdue(guardrails: list[dict], today: datetime.date) -> list[dict]:
    """Guardrails, other than deprecated ones, last reviewed more than 12 months before today."""
    try:
        cutoff = today.replace(year=today.year - 1)
    except ValueError:  # 29 February
        cutoff = today.replace(year=today.year - 1, day=28)
    found = []
    for g in guardrails:
        last = g.get("last_reviewed")
        if g.get("status") == "deprecated" or not last:
            continue
        if datetime.date.fromisoformat(str(last)) < cutoff:
            found.append(g)
    return found


def main() -> None:
    spec = importlib.util.spec_from_file_location("guardrails", os.path.join(ROOT, "hooks", "guardrails.py"))
    hook = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hook)
    late = overdue(hook.parse(os.path.join(ROOT, "docs")), datetime.date.today())
    for g in late:
        print(
            f"::warning file=docs/{g['page']}::{g['id']} was last reviewed on {g['last_reviewed']}, "
            f"more than {MONTHS} months ago. Ask its owner ({g['owner']}) to review it."
        )
    print(f"{len(late)} guardrail(s) overdue for review.")


if __name__ == "__main__":
    main()
