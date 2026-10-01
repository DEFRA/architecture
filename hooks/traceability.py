"""MkDocs hook that links the DDTS doctrine, the architecture principles and the guardrails.

Two small pieces of front matter hold the whole chain, next to the content
they describe:

* ``docs/principles/doctrine.md`` says which principles apply each doctrine:

      applies:
        ddts-01: [GR-PRIN-01, GR-PRIN-03]

* each guardrail page says which principles it puts into practice:

      principles: [GR-PRIN-05, GR-PRIN-06]

From these the hook:

* checks every doctrine, principle and guardrail page is linked into the chain;
* adds a breadcrumb to each guardrail page (doctrine -> principle -> guardrails);
* replaces ``<!-- trace:principle GR-PRIN-01 -->`` with that principle's
  doctrines and guardrail areas; and
* replaces ``<!-- trace:coverage -->`` with a coverage table that shows gaps.
"""

from __future__ import annotations

import os
import posixpath
import re

import yaml
from mkdocs.exceptions import PluginError

DOCTRINE_PAGE = "principles/doctrine.md"
PRINCIPLES_PAGE = "principles/architecture-principles.md"
GUARDRAIL_DIR = "guardrails"
NOT_GUARDRAIL_PAGES = ("index.md", "library.md")

FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
H1 = re.compile(r"^# (.+)$", re.M)
DOCTRINE_HEADING = re.compile(r"^## (\d+)\. (.+?) \{#(ddts-\d+)\}$", re.M)
PRINCIPLE_HEADING = re.compile(r"^## (GR-PRIN-\d+) (.+?) \{#gr-prin-\d+\}$", re.M)
GUARDRAIL_HEADING = re.compile(r"^## GR-", re.M)

# A principle applied by fewer guardrail areas than this is flagged as a gap.
THIN = 2

_chain: dict = {}


def _read(docs_dir: str, path: str) -> tuple[dict, str]:
    with open(os.path.join(docs_dir, path), encoding="utf-8") as handle:
        text = handle.read()
    match = FRONT_MATTER.match(text)
    meta = yaml.safe_load(match.group(1)) if match else {}
    return meta or {}, text


def build(docs_dir: str) -> dict:
    """Read the chain from the docs, raising PluginError if it is broken."""
    errors: list[str] = []

    _, principles_text = _read(docs_dir, PRINCIPLES_PAGE)
    principles = {pid: name for pid, name in PRINCIPLE_HEADING.findall(principles_text)}

    doctrine_meta, doctrine_text = _read(docs_dir, DOCTRINE_PAGE)
    doctrines = [
        {"anchor": anchor, "number": int(num), "name": name.rstrip(".")}
        for num, name, anchor in DOCTRINE_HEADING.findall(doctrine_text)
    ]
    applies = doctrine_meta.get("applies", {})
    for d in doctrines:
        d["principles"] = applies.get(d["anchor"], [])
        if not d["principles"]:
            errors.append(f"{DOCTRINE_PAGE}: doctrine {d['anchor']} has no principles under 'applies'")
        for pid in d["principles"]:
            if pid not in principles:
                errors.append(f"{DOCTRINE_PAGE}: {d['anchor']} refers to unknown principle {pid}")

    areas = []
    folder = os.path.join(docs_dir, GUARDRAIL_DIR)
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".md") or name in NOT_GUARDRAIL_PAGES:
            continue
        path = f"{GUARDRAIL_DIR}/{name}"
        meta, text = _read(docs_dir, path)
        supported = meta.get("principles") or []
        if not supported:
            errors.append(f"{path}: add 'principles: [GR-PRIN-..]' to the front matter")
        for pid in supported:
            if pid not in principles:
                errors.append(f"{path}: unknown principle {pid}")
        areas.append(
            {
                "page": path,
                "title": H1.search(text).group(1),
                "principles": supported,
                "count": len(GUARDRAIL_HEADING.findall(text)),
            }
        )

    if errors:
        raise PluginError("Doctrine, principle and guardrail links are broken:\n  - " + "\n  - ".join(errors))

    by_principle = {pid: [a for a in areas if pid in a["principles"]] for pid in principles}
    doctrines_for = {pid: [d for d in doctrines if pid in d["principles"]] for pid in principles}
    return {
        "principles": principles,
        "doctrines": doctrines,
        "areas": areas,
        "by_principle": by_principle,
        "doctrines_for": doctrines_for,
    }


# --- MkDocs events -----------------------------------------------------------


def on_config(config):
    _chain.clear()
    _chain.update(build(config["docs_dir"]))
    return config


def on_page_markdown(markdown, page, config, files):
    src = page.file.src_uri

    def link(target: str, anchor: str = "") -> str:
        rel = posixpath.relpath(target, posixpath.dirname(src))
        return rel + (f"#{anchor}" if anchor else "")

    area = next((a for a in _chain["areas"] if a["page"] == src), None)
    if area:
        markdown = _add_breadcrumb(markdown, area, link)

    for pid in _chain["principles"]:
        marker = f"<!-- trace:principle {pid} -->"
        if marker in markdown:
            markdown = markdown.replace(marker, _principle_trace(pid, link))

    if "<!-- trace:coverage -->" in markdown:
        markdown = markdown.replace("<!-- trace:coverage -->", _coverage(link))
    return markdown


# --- Renderers ---------------------------------------------------------------


def _doctrine_link(d, link) -> str:
    return f"[{d['number']}. {d['name']}]({link(DOCTRINE_PAGE, d['anchor'])})"


def _principle_link(pid, link) -> str:
    return f"[{pid[-2:].lstrip('0')}. {_chain['principles'][pid]}]({link(PRINCIPLES_PAGE, pid.lower())})"


def _add_breadcrumb(markdown: str, area: dict, link) -> str:
    """Insert 'Doctrine -> Principles' under the page's lead paragraph."""
    principles = ", ".join(_principle_link(pid, link) for pid in area["principles"])
    doctrines = []
    for pid in area["principles"]:
        for d in _chain["doctrines_for"][pid]:
            if d not in doctrines:
                doctrines.append(d)
    doctrine_links = ", ".join(_doctrine_link(d, link) for d in sorted(doctrines, key=lambda d: d["number"]))
    crumb = (
        '<div class="da-trace" markdown>\n\n'
        f"**Doctrine:** {doctrine_links or '-'}  \n"
        f"**Principles:** {principles}\n\n"
        "</div>\n"
    )
    lines = markdown.split("\n")
    anchor = next((i for i, line in enumerate(lines) if line.startswith('<p class="lead">')), None)
    if anchor is None:
        anchor = next(i for i, line in enumerate(lines) if line.startswith("# "))
    lines.insert(anchor + 1, "\n" + crumb)
    return "\n".join(lines)


def _principle_trace(pid: str, link) -> str:
    doctrines = ", ".join(_doctrine_link(d, link) for d in _chain["doctrines_for"][pid]) or "-"
    areas = _chain["by_principle"][pid]
    if areas:
        guardrails = ", ".join(f"[{a['title']}]({link(a['page'])}) ({a['count']})" for a in areas)
    else:
        guardrails = "none yet - see the [guardrail backlog](../about/roadmap.md#guardrail-backlog)"
    return f"**Applies doctrine:** {doctrines}\n\n**Guardrails:** {guardrails}\n"


def _coverage(link) -> str:
    rows = [
        "| Doctrine | Architecture principles | Guardrail areas | Guardrails |",
        "| --- | --- | --- | ---: |",
    ]
    for d in _chain["doctrines"]:
        areas = []
        for pid in d["principles"]:
            for a in _chain["by_principle"][pid]:
                if a not in areas:
                    areas.append(a)
        principles = "<br>".join(_principle_link(pid, link) for pid in d["principles"])
        area_links = ", ".join(f"[{a['title']}]({link(a['page'])})" for a in areas) or "**gap**"
        rows.append(f"| {_doctrine_link(d, link)} | {principles} | {area_links} | {sum(a['count'] for a in areas)} |")

    gaps = [pid for pid, areas in _chain["by_principle"].items() if len(areas) < THIN]
    note = ""
    if gaps:

        def described(pid):
            n = len(_chain["by_principle"][pid])
            return f"{_principle_link(pid, link)} ({n} area{'' if n == 1 else 's'})"

        listed = ", ".join(described(pid) for pid in gaps)
        note = (
            f'\n!!! warning "Thin coverage"\n'
            f"    These principles have fewer than {THIN} guardrail areas putting them into practice: {listed}. "
            f"New guardrails for them are in the [guardrail backlog](../about/roadmap.md#guardrail-backlog).\n"
        )
    return "\n".join(rows) + "\n" + note
