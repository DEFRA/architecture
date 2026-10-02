"""Warn about headings in docs/ that are not in sentence case.

Used by the prose job in .github/workflows/ci.yml, alongside Vale:

    python scripts/heading_case.py

Prints a GitHub Actions warning annotation for each heading with a capital
letter mid-heading that is not a proper noun, an acronym or an id. It never
fails the build. Add a proper noun to PROPER_NOUNS rather than lower-casing it.
"""

from __future__ import annotations

import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Words and phrases that keep their capitals in a heading.
PROPER_NOUNS = {
    "Defra",
    "DDTS",
    "GOV.UK",
    "GitHub",
    "Core",
    "Delivery",
    "Platform",
    "Customer",
    "Identity",
    "ID",
    "Forms",
    "Interactive",
    "Map",
    "Digital",
    "Service",
    "Manual",
    "Technical",
    "Design",
    "Authority",
    "Technology",
    "Governance",
    "Board",
    "Secure",
    "Standard",
    "Code",
    "Practice",
    "Microsoft",
    "Entra",
    "Notify",
    "Pay",
    "One",
    "Login",
    "Welsh",
    "English",
    "Power",
    "FinOps",
    "Vale",
    "MkDocs",
    "Must",
    "Should",
    "Could",
    "Architecture",
    "Community",
    "Enterprise",
    "Portfolio",
    "Assurance",
    "InvestCo",
    "Annex",
    "Kubernetes",
    "OpenAPI",
    "AsyncAPI",
    "Mermaid",
    "Playwright",
    "Python",
    "Node.js",
    "UK",
    "National",
    "Archives",
    "Government",
    "Gateway",
    "Algorithmic",
    "Transparency",
    "Recording",
    "Language",
    "Standards",
    "Office",
    "Data",
    "Protection",
    "Officer",
    "Agile",
    "Material",
    "SharePoint",
    "SaaS",
    "System",
    "Musts",
    "Shoulds",
    "I",
}
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.M)
FENCE = re.compile(r"^(```|~~~).*?^\1", re.M | re.S)
FRONT_MATTER = re.compile(r"\A---\n.*?\n---\n", re.S)


def problems(heading: str) -> list[str]:
    """Words in a heading that should be lower case."""
    text = re.sub(r"\{#[^}]*\}", "", heading)
    text = re.sub(r"`[^`]*`|\[([^\]]*)\]\([^)]*\)", lambda m: m.group(1) or "", text)
    text = re.sub(r"\b(?:GR|TC|BC|EX)-?[A-Z0-9-]*\d\b|\bDDTS-\d+\b", "", text)
    words = re.findall(r"[A-Za-z][A-Za-z.'’-]*", text)
    found = []
    for word in words[1:]:
        word = re.sub(r"['’]s$", "", word)
        if not word[0].isupper() or word in PROPER_NOUNS or len(word) == 1:
            continue
        if len(word) > 1 and (word.isupper() or word[:-1].isupper() or re.match(r"^[A-Z]{2,}s$", word)):
            continue  # an acronym such as API, APIs or NFRs
        if re.search(rf"[:?.]\s+{re.escape(word)}\b", text):
            continue  # starts a sentence or clause after a colon, full stop or question mark
        found.append(word)
    return found


def check(text: str) -> list[tuple[str, list[str]]]:
    text = FENCE.sub("", FRONT_MATTER.sub("", text))
    return [(m.group(1), p) for m in HEADING.finditer(text) if (p := problems(m.group(1)))]


def main() -> None:
    count = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "docs", "**", "*.md"), recursive=True)):
        with open(path, encoding="utf-8") as handle:
            for heading, words in check(handle.read()):
                count += 1
                rel = os.path.relpath(path, ROOT)
                print(f"::warning file={rel}::Use sentence case in '{heading}' - lower-case {', '.join(words)}")
    print(f"{count} heading(s) not in sentence case.")


if __name__ == "__main__":
    main()
