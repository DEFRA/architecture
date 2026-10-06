"""MkDocs hook that makes the site easy for machines, including AI tools, to read.

After the other hooks have filled in their generated content, this hook:

* writes a Markdown copy of every page next to its HTML, at ``<page>/index.md``,
  with links made absolute and a header giving its address, maturity and the
  site version;
* writes ``pages.json``, listing every page with its section and maturity; and
* writes ``llms.txt`` at the site root: a short guide for AI tools to the site,
  its data files and the Markdown copies (see https://llmstxt.org/).

Maturity is ``prototype`` for pages in a section listed under ``extra.prototype``
in ``mkdocs.yml``, ``draft`` for pages with ``status: draft``, and ``published``
otherwise. Published is not the same as endorsed: individual guardrails carry
their own ``status`` in ``guardrails.json``.

List this hook last in ``mkdocs.yml`` so it sees each page after every other hook.
"""

from __future__ import annotations

import html
import importlib.util
import json
import os
import re

_HOOKS = os.path.dirname(os.path.abspath(__file__))
SKIP = ("print/",)
LEAD = re.compile(r'<p class="lead">(.*?)</p>', re.S)
TAG = re.compile(r"<[^>]+>")

DATA_FILES = [
    (
        "guardrails.json",
        "Every guardrail and principle: id, level, statement, why, how to meet it, evidence by phase, status",
    ),
    ("nfrs.json", "Service tiers and the non-functional requirements catalogue"),
    ("capabilities.json", "Business capabilities and the technology capability model (TBM level 1 and level 2)"),
    ("pages.json", "Every page with its section, maturity and Markdown copy"),
]

_pages: dict[str, dict] = {}


def _load(name: str):
    spec = importlib.util.spec_from_file_location(f"_{name}_for_machine", os.path.join(_HOOKS, f"{name}.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_guardrails = _load("guardrails")
_page_status = _load("page_status")


def maturity(src_path: str, meta: dict, config) -> str:
    """How settled a page is: prototype, draft or published."""
    if _page_status.prototype_note(src_path, config):
        return "prototype"
    if meta.get("status") == "draft":
        return "draft"
    return "published"


def _description(markdown: str) -> str:
    match = LEAD.search(markdown)
    return html.unescape(TAG.sub("", match.group(1))).strip() if match else ""


def on_config(config):
    _pages.clear()
    return config


def on_page_markdown(markdown, page, config, files):
    src = page.file.src_uri
    if src.startswith(SKIP):
        return markdown
    top = page.ancestors[-1].title if page.ancestors else None
    _pages[src] = {
        "title": page.title or src,
        "section": top or ("Home" if src == "index.md" else "Other"),
        "maturity": maturity(src, page.meta, config),
        "description": _description(markdown),
        "markdown": markdown,
    }
    return markdown


def on_post_build(config):
    site_url = (config.get("site_url") or "").rstrip("/") + "/"
    extra = config.get("extra") or {}
    version = extra.get("version_in_force")
    unreleased = " plus changes not yet released" if extra.get("version_unreleased") else ""
    index = []
    for src, page in _pages.items():
        path = _guardrails.page_url(src)
        header = (
            f"<!-- {site_url}{path} | maturity: {page['maturity']} | "
            f"site version {version}{unreleased} | generated from {src} -->\n\n"
        )
        body = _guardrails.absolute_links(page["markdown"], src, site_url)
        target = os.path.join(config["site_dir"], path, "index.md")
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w", encoding="utf-8") as handle:
            handle.write(header + body)
        index.append(
            {
                "title": page["title"],
                "section": page["section"],
                "url": site_url + path,
                "markdown": f"{site_url}{path}index.md",
                "maturity": page["maturity"],
                "description": page["description"],
                "source": src,
            }
        )

    with open(os.path.join(config["site_dir"], "pages.json"), "w", encoding="utf-8") as handle:
        out = {"version": version, "includes_unreleased_changes": bool(unreleased), "pages": index}
        json.dump(out, handle, indent=2)

    lines = [
        f"# {config['site_name']}",
        "",
        f"> {config.get('site_description') or 'Defra architecture guidance.'}",
        "",
        f"Version in force: {version}{unreleased}. Every page has a Markdown copy at its address plus `index.md`.",
        "Each page's maturity is prototype, draft or published. Treat prototype and draft content as work in progress,",
        "not agreed policy. Guardrail ids such as GR-HOST-01 are stable and can be cited.",
        "",
        "## Data",
        "",
    ]
    lines += [f"- [{name}]({site_url}{name}): {about}" for name, about in DATA_FILES]
    sections: dict[str, list[dict]] = {}
    for item in index:
        sections.setdefault(item["section"], []).append(item)
    for section, items in sections.items():
        lines += ["", f"## {section}", ""]
        for item in items:
            about = f": {item['description']}" if item["description"] else ""
            lines.append(f"- [{item['title']}]({item['markdown']}) ({item['maturity']}){about}")
    with open(os.path.join(config["site_dir"], "llms.txt"), "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")
