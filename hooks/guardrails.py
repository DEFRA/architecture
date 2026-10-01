"""MkDocs hook that builds the searchable guardrail library.

Guardrails are written by hand in ``docs/guardrails/*.md`` (principles in
``docs/principles/architecture-principles.md``) using a fixed shape:

    ## GR-HOST-01 Use Defra's strategic delivery platform by default {#gr-host-01}

    <span class="rfc rfc--must">Must</span> New digital services are hosted on ...

Principles use the same shape with a ``rfc--principle`` badge.

This hook reads those pages so the library, the home page figures and the
guardrail pages can never drift apart. It:

* checks every guardrail has a unique id, a matching anchor and a level;
* replaces ``<!-- guardrails:library -->`` with a filterable list of all
  guardrails, and ``<!-- guardrails:count -->``, ``<!-- guardrails:principles -->``
  and ``<!-- guardrails:doctrines -->`` with the current figures; and
* gives pages that use the ``home.html`` template the figures shown in the hero.
"""

from __future__ import annotations

import html
import os
import re
from collections import Counter

import yaml
from mkdocs.exceptions import PluginError
from mkdocs.utils import get_relative_url

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HEADING = re.compile(r"^## (GR-[A-Z]+-\d{2}) (.+?) \{#([a-z0-9-]+)\}\s*$", re.M)
LEVEL = re.compile(r'<span class="rfc rfc--(principle|must|should|could)">\w+</span>\s*(.+)')
TITLE = re.compile(r"^# (.+)$", re.M)
LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")

LEVELS = {"principle": "Principle", "must": "Must", "should": "Should", "could": "Could"}

_guardrails: list[dict] = []
_stats: dict = {}


def _plain(text: str) -> str:
    """Strip Markdown links and emphasis so a statement reads as plain text."""
    text = LINK.sub(r"\1", text)
    return text.replace("**", "").replace("`", "").strip()


# Folders whose pages define guardrails, and pages in them that do not.
SOURCES = ("principles", "guardrails")
NOT_GUARDRAILS = ("index.md", "library.md", "doctrine.md")


def _guardrail_files(docs_dir: str):
    for section in SOURCES:
        folder = os.path.join(docs_dir, section)
        if not os.path.isdir(folder):
            continue
        for name in sorted(os.listdir(folder)):
            if name.endswith(".md") and name not in NOT_GUARDRAILS:
                yield section, name


def parse(docs_dir: str) -> list[dict]:
    found: list[dict] = []
    errors: list[str] = []
    for section, name in _guardrail_files(docs_dir):
        with open(os.path.join(docs_dir, section, name), encoding="utf-8") as handle:
            text = handle.read()
        area = TITLE.search(text).group(1)
        matches = list(HEADING.finditer(text))
        for i, match in enumerate(matches):
            gid, title, anchor = match.groups()
            if anchor != gid.lower():
                errors.append(f"{name}: {gid} has anchor #{anchor}, expected #{gid.lower()}")
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            body = text[match.end() : end]
            level = LEVEL.search(body)
            if not level:
                errors.append(f"{name}: {gid} has no Principle/Must/Should/Could badge")
                continue
            kind, statement = level.group(1), level.group(2)
            found.append(
                {
                    "id": gid,
                    "title": title,
                    "level": kind,
                    "statement": _plain(statement),
                    "area": area,
                    "page": f"{section}/{name}",
                }
            )
    ids = [g["id"] for g in found]
    errors += [f"duplicate guardrail id {i}" for i in sorted({i for i in ids if ids.count(i) > 1})]
    if errors:
        raise PluginError("Guardrails are invalid:\n  - " + "\n  - ".join(errors))
    return found


def on_config(config):
    _guardrails[:] = parse(config["docs_dir"])
    levels = Counter(g["level"] for g in _guardrails)

    def load(name):
        with open(os.path.join(ROOT, "capabilities", name), encoding="utf-8") as handle:
            return yaml.safe_load(handle)["capabilities"]

    tech = load("technology-capabilities.yaml")
    with open(os.path.join(config["docs_dir"], "principles", "doctrine.md"), encoding="utf-8") as handle:
        doctrines = len(re.findall(r"^## \d+\. .+\{#ddts-\d+\}$", handle.read(), re.M))
    _stats.clear()
    _stats.update(
        doctrines=doctrines,
        guardrails=sum(1 for g in _guardrails if g["level"] != "principle"),
        must=levels["must"],
        should=levels["should"],
        could=levels["could"],
        principles=levels["principle"],
        business=len(load("business-capabilities.yaml")),
        technology=len(tech),
        strategic=sum(1 for t in tech if t["status"] == "strategic"),
    )
    return config


def on_page_markdown(markdown, page, config, files):
    if page.meta.get("template") == "home.html":
        page.meta["stats"] = dict(_stats)
    for name, key in (("count", "guardrails"), ("principles", "principles"), ("doctrines", "doctrines")):
        markdown = markdown.replace(f"<!-- guardrails:{name} -->", str(_stats[key]))
    marker = "<!-- guardrails:library -->"
    if marker in markdown:
        markdown = markdown.replace(marker, _library(page, files))
    return markdown


def _library(page, files) -> str:
    e = html.escape
    areas = sorted({g["area"] for g in _guardrails}, key=lambda a: (a != "Architecture principles", a))
    options = "".join(f'<option value="{e(a)}">{e(a)}</option>' for a in areas)
    levels = Counter(g["level"] for g in _guardrails)
    chips = "".join(
        f'<label class="gl-chip"><input type="checkbox" name="gl-level" value="{k}" checked> '
        f'<span class="rfc rfc--{k}">{v}</span> <span class="gl-chip__n">{levels[k]}</span></label>'
        for k, v in LEVELS.items()
    )
    cards = []
    for g in _guardrails:
        target = files.get_file_from_path(g["page"])
        href = get_relative_url(target.url, page.url) + "#" + g["id"].lower()
        search = " ".join([g["id"], g["title"], g["statement"], g["area"]]).lower()
        cards.append(
            f'<article class="gl-card" data-level="{g["level"]}" data-area="{e(g["area"])}" data-search="{e(search)}">'
            f'<div class="gl-card__meta"><span class="rfc rfc--{g["level"]}">{LEVELS[g["level"]]}</span>'
            f'<code>{g["id"]}</code><span class="gl-card__area">{e(g["area"])}</span></div>'
            f'<h3 class="gl-card__title"><a href="{href}">{e(g["title"])}</a></h3>'
            f"<p>{e(g['statement'])}</p></article>"
        )
    return (
        '<div class="gl" data-guardrail-library>\n'
        '<div class="gl-tools" role="search">'
        '<label class="gl-field"><span>Search</span>'
        '<input type="search" id="gl-search" placeholder="e.g. secrets, hosting, GR-API-02" autocomplete="off"></label>'
        '<label class="gl-field"><span>Area</span><select id="gl-area">'
        f'<option value="">All areas</option>{options}</select></label>'
        f'<fieldset class="gl-levels"><legend>Level</legend>{chips}</fieldset>'
        "</div>\n"
        f'<p class="gl-count" aria-live="polite">Showing <strong id="gl-shown">{len(_guardrails)}</strong> '
        f"of {len(_guardrails)} guardrails</p>\n"
        f'<div class="gl-grid">{"".join(cards)}</div>\n'
        '<p class="gl-empty" hidden>No guardrails match. Try a different word, or clear the filters.</p>\n'
        "</div>\n"
    )
