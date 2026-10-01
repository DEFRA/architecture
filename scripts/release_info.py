"""Print the latest released version in CHANGELOG.md and write its release notes.

Used by .github/workflows/release.yml:

    python scripts/release_info.py notes.md
    # prints e.g. "0.2.0" and writes that version's changelog section to notes.md

Exits with status 3 if the changelog has unreleased changes. Main then holds
content newer than the latest version, so tagging it would be wrong.
"""

from __future__ import annotations

import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main() -> None:
    spec = importlib.util.spec_from_file_location("releases", os.path.join(ROOT, "hooks", "releases.py"))
    releases = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(releases)
    with open(os.path.join(ROOT, "CHANGELOG.md"), encoding="utf-8") as handle:
        sections = releases.parse(handle.read())
    current = releases.latest(sections)
    if any(s["version"] is None and s["body"] for s in sections):
        print(f"CHANGELOG.md has unreleased changes, so {current['version']} cannot be tagged here.", file=sys.stderr)
        sys.exit(3)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w", encoding="utf-8") as handle:
            handle.write(f"Released {current['date']}.\n\n{current['body']}\n")
    print(current["version"])


if __name__ == "__main__":
    main()
