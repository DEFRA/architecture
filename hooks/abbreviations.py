"""MkDocs hook that keeps abbreviation tooltips where they help, and nowhere else.

``includes/abbreviations.md`` is appended to every page, so the ``abbr``
extension wraps every match in ``<abbr title="...">``. Two cases are wrong:

- inside a guardrail id, such as GR-API-05, where "API" is part of a stable
  identifier, not a word to expand
- next to its own expansion, such as "Technical Design Authority (TDA)", where
  the tooltip repeats what the sentence already says, and some screen readers
  announce it twice

This hook removes the ``<abbr>`` wrapper in both cases, in the page content
(and so in the search index) and in the final page. After the build it checks
every page and fails the build if either case is left.
"""

from __future__ import annotations

import html
import os
import re

from mkdocs.exceptions import PluginError

ABBR = re.compile(r'<abbr title="([^"]*)">([^<]*)</abbr>')
# How much text either side of an abbreviation to compare with its expansion.
WINDOW = 200


def _text(fragment: str) -> str:
    """Visible text of an HTML fragment, with spacing collapsed."""
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", fragment)))


def in_guardrail_id(source: str, start: int, end: int) -> bool:
    """True if the abbreviation at source[start:end] is part of an id such as GR-API-05."""
    return source[max(0, start - 3) : start] == "GR-" or re.match(r"-\d", source[end : end + 2]) is not None


def next_to_expansion(source: str, start: int, end: int, title: str) -> bool:
    """True if the expansion is written just before "(ABBR)" or just after "ABBR (" in the text."""
    expansion = _text(title).strip().lower()
    before = _text(source[max(0, start - WINDOW) : start]).lower().rstrip()
    after = _text(source[end : end + WINDOW]).lower().lstrip()
    if before.endswith("(") and before[:-1].rstrip().endswith(expansion):
        return True
    return after.startswith("(") and after[1:].lstrip().startswith(expansion)


def problems(source: str) -> list[str]:
    """The abbreviations in a page that should not have a tooltip."""
    found = []
    for m in ABBR.finditer(source):
        if in_guardrail_id(source, m.start(), m.end()):
            found.append(f"{m.group(2)} inside a guardrail id")
        elif next_to_expansion(source, m.start(), m.end(), m.group(1)):
            found.append(f"{m.group(2)} next to its expansion")
    return found


def tidy(source: str) -> str:
    """Remove the abbr wrapper wherever it would be wrong."""
    out, last = [], 0
    for m in ABBR.finditer(source):
        out.append(source[last : m.start()])
        wrong = in_guardrail_id(source, m.start(), m.end()) or next_to_expansion(source, m.start(), m.end(), m.group(1))
        out.append(m.group(2) if wrong else m.group(0))
        last = m.end()
    out.append(source[last:])
    return "".join(out)


def on_page_content(content, page, config, files):
    return tidy(content)


def on_post_page(output, page, config):
    return tidy(output)


def on_post_build(config):
    errors = []
    for root, _dirs, names in os.walk(config["site_dir"]):
        for name in names:
            if name.endswith(".html"):
                path = os.path.join(root, name)
                with open(path, encoding="utf-8") as handle:
                    errors += [f"{os.path.relpath(path, config['site_dir'])}: {p}" for p in problems(handle.read())]
    if errors:
        raise PluginError("Abbreviation tooltips in the wrong place:\n  - " + "\n  - ".join(sorted(set(errors))[:20]))
