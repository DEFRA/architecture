"""MkDocs hook that collects facts still to be confirmed into one page.

Where a page needs a Defra fact that is not yet known - a name, a contact, a
lead time, an approval - write a visible admonition instead of guessing:

    !!! warning "To be confirmed"
        TODO: who approves platform access requests, and how long it takes.

This hook gives each one an anchor and lists them all, grouped by page, where
the Open questions page has the ``<div data-open-questions></div>`` marker.
Delete the admonition once the fact is confirmed and it drops off the list.
"""

from __future__ import annotations

import html
import re

from mkdocs.utils import get_relative_url

ADMONITION = re.compile(r'^!!! warning "To be confirmed"\n((?:(?: {4}.*)?\n)+)', re.M)
MARKER = "<div data-open-questions></div>"
LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")

_found: dict[str, dict] = {}


def _plain(text: str) -> str:
    text = LINK.sub(r"\1", " ".join(line.strip() for line in text.splitlines()))
    text = re.sub(r"^\*{0,2}TODO:?\*{0,2}:?\s*", "", text.strip())
    return text.replace("**", "").replace("`", "")


def on_config(config):
    _found.clear()
    return config


def on_page_markdown(markdown, page, config, files):
    questions: list[dict] = []

    def tag(match: re.Match) -> str:
        anchor = f"tbc-{len(questions) + 1}"
        questions.append({"anchor": anchor, "text": _plain(match.group(1))})
        return f'<div id="{anchor}"></div>\n\n{match.group(0)}'

    markdown = ADMONITION.sub(tag, markdown + "\n")
    if questions:
        _found[page.file.src_uri] = {"page": page, "questions": questions}
    return markdown


def on_post_page(output, page, config):
    if MARKER not in output:
        return output
    return output.replace(MARKER, _render(page))


def _render(here) -> str:
    e = html.escape
    total = sum(len(v["questions"]) for v in _found.values())
    if not total:
        return "<p>There are no open questions.</p>"
    pages = len(_found)
    parts = [
        f'<p class="oq-count"><strong>{total}</strong> open question{"" if total == 1 else "s"} '
        f"on {pages} page{'' if pages == 1 else 's'}.</p>"
    ]
    for src in sorted(_found, key=lambda s: _found[s]["page"].url):
        page = _found[src]["page"]
        href = get_relative_url(page.url, here.url)
        items = "".join(f'<li><a href="{href}#{q["anchor"]}">{e(q["text"])}</a></li>' for q in _found[src]["questions"])
        slug = re.sub(r"[^a-z0-9]+", "-", src.lower().removesuffix(".md")).strip("-")
        parts.append(f'<h2 id="oq-{slug}">{e(page.title or src)}</h2><ul class="oq-list">{items}</ul>')
    return "\n".join(parts)
