"""MkDocs hook that builds the guardrail library from the guardrail pages.

Guardrails are written by hand in ``docs/guardrails/*.md`` (principles in
``docs/principles/architecture-principles.md``) using a fixed shape:

    ## GR-HOST-01 Use Defra's strategic delivery platform by default {#gr-host-01}

    <span class="rfc rfc--must">Must</span> New digital services are hosted on ...

Principles use the same shape with a ``rfc--principle`` badge.

Each page's front matter holds structured metadata for its guardrails, so the
prose and the data sit side by side:

    guardrail_defaults:          # applies to every guardrail on the page
      status: draft
      owner: Architecture team
      automated_check: manual
      last_reviewed: 2026-10-01
      since_version: 0.1.0
    guardrails:
      GR-HOST-01:
        phases: [discovery, alpha, beta, live]
        evidence: The service runs on the Core Delivery Platform, or an approved exception
        service_standard_points: [11]
        tcop_points: [5, 8]
        sbd_principles: []

The doctrine a guardrail applies is worked out from the page's ``principles``
and the ``applies`` front matter of the doctrine page, unless set explicitly.

This hook reads those pages so the library, the home page figures and the
guardrail pages can never drift apart. It:

* checks every guardrail has a unique id, a matching anchor, a level and valid
  metadata - and fails the build if a Must has no evidence;
* adds a metadata panel under each guardrail on its page;
* replaces ``<!-- guardrails:library -->`` with a filterable list of all
  guardrails, and ``<!-- guardrails:count -->``, ``<!-- guardrails:principles -->``
  and ``<!-- guardrails:doctrines -->`` with the current figures;
* gives pages that use the ``home.html`` template the figures shown in the hero; and
* publishes every guardrail and its metadata as ``guardrails.json``.
"""

from __future__ import annotations

import datetime
import html
import json
import os
import posixpath
import re
from collections import Counter

import yaml
from mkdocs.exceptions import PluginError
from mkdocs.utils import get_relative_url

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
HEADING = re.compile(r"^## (GR-[A-Z]+-\d{2}) (.+?) \{#([a-z0-9-]+)\}\s*$", re.M)
LEVEL = re.compile(r'<span class="rfc rfc--(principle|must|should|could)">\w+</span>\s*(.+)')
TITLE = re.compile(r"^# (.+)$", re.M)
LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")
DOCTRINE_HEADING = re.compile(r"^## (\d+)\. (.+?) \{#(ddts-\d+)\}$", re.M)
VERSION = re.compile(r"^\d+\.\d+\.\d+$")
SECTION = re.compile(r"^## ", re.M)

LEVELS = {"principle": "Principle", "must": "Must", "should": "Should", "could": "Could"}
STATUSES = {"draft": "Draft", "endorsed": "Endorsed", "deprecated": "Deprecated"}
PHASES = {"discovery": "Discovery", "alpha": "Alpha", "beta": "Beta", "live": "Live"}
# Phases plus the lifecycle events that have their own page in Deliver a service.
LIFECYCLE = {**PHASES, "significant-change": "Significant change", "retire": "Retire"}

# Reference lists the metadata points to. Names are from the published sources.
SERVICE_STANDARD = {
    1: "Understand users and their needs",
    2: "Solve a whole problem for users",
    3: "Provide a joined-up experience across all channels",
    4: "Make the service simple to use",
    5: "Make sure everyone can use the service",
    6: "Have a multidisciplinary team",
    7: "Use agile ways of working",
    8: "Iterate and improve frequently",
    9: "Create a secure service which protects users' privacy",
    10: "Define what success looks like and publish performance data",
    11: "Choose the right tools and technology",
    12: "Make new source code open",
    13: "Use and contribute to open standards, common components and patterns",
    14: "Operate a reliable service",
}
TCOP = {
    1: "Define user needs",
    2: "Make things accessible and inclusive",
    3: "Be open and use open source",
    4: "Make use of open standards",
    5: "Use cloud first",
    6: "Make things secure",
    7: "Make privacy integral",
    8: "Share, reuse and collaborate",
    9: "Integrate and adapt technology",
    10: "Make better use of data",
    11: "Define your purchasing strategy",
    12: "Make your technology sustainable",
    13: "Meet the Service Standard",
}
SBD = {
    1: "Create responsibility for cyber security risk",
    2: "Source secure technology products",
    3: "Adopt a risk-driven approach",
    4: "Design usable security controls",
    5: "Build in detect and respond security",
    6: "Design flexible architectures",
    7: "Minimise the attack surface",
    8: "Defend in depth",
    9: "Embed continuous assurance",
    10: "Make changes securely",
}
REFERENCES = {
    "service_standard_points": (
        "Service Standard",
        SERVICE_STANDARD,
        "https://www.gov.uk/service-manual/service-standard",
    ),
    "tcop_points": ("Technology Code of Practice", TCOP, "https://www.gov.uk/guidance/the-technology-code-of-practice"),
    "sbd_principles": (
        "Secure by Design principles",
        SBD,
        "https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/",
    ),
}
REQUIRED = ("status", "phases", "automated_check", "owner", "last_reviewed", "since_version")
FIELDS = set(REQUIRED) | set(REFERENCES) | {"evidence", "evidence_by_phase", "doctrine", "replaced_by"}

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


def _front_matter(text: str) -> dict:
    match = FRONT_MATTER.match(text)
    return (yaml.safe_load(match.group(1)) if match else None) or {}


def _doctrines(docs_dir: str) -> dict[str, list[str]]:
    """Map each principle to the doctrine anchors it applies."""
    path = os.path.join(docs_dir, "principles", "doctrine.md")
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    found: dict[str, list[str]] = {}
    for anchor, principles in (_front_matter(text).get("applies") or {}).items():
        for pid in principles:
            found.setdefault(pid, []).append(anchor)
    return found


def _check(gid: str, level: str, meta: dict, where: str) -> list[str]:
    """Return problems with one guardrail's metadata."""
    errors = [f"{where}: {gid} has unknown field '{k}'" for k in sorted(set(meta) - FIELDS)]
    errors += [f"{where}: {gid} is missing '{k}'" for k in REQUIRED if meta.get(k) in (None, "", [])]
    if meta.get("status") and meta["status"] not in STATUSES:
        errors.append(f"{where}: {gid} has status '{meta['status']}', expected one of {', '.join(STATUSES)}")
    for phase in meta.get("phases") or []:
        if phase not in PHASES:
            errors.append(f"{where}: {gid} has unknown phase '{phase}'")
    for field, (name, points, _) in REFERENCES.items():
        for point in meta.get(field) or []:
            if point not in points:
                errors.append(f"{where}: {gid} refers to {name} point {point}, which does not exist")
    by_phase = meta.get("evidence_by_phase") or {}
    if not isinstance(by_phase, dict):
        errors.append(f"{where}: {gid} evidence_by_phase must map phases to evidence")
        by_phase = {}
    for phase, text in by_phase.items():
        if phase not in LIFECYCLE:
            errors.append(f"{where}: {gid} has evidence for unknown phase '{phase}'")
        elif not str(text or "").strip():
            errors.append(f"{where}: {gid} has empty evidence for {phase}")
        elif phase in PHASES and phase not in (meta.get("phases") or []):
            errors.append(f"{where}: {gid} has evidence for {phase} but does not apply in {phase}")
    if level == "must":
        for phase in meta.get("phases") or []:
            if phase in PHASES and phase not in by_phase:
                errors.append(f"{where}: {gid} is a Must in {phase} but has no evidence_by_phase for {phase}")
    if level == "must" and not str(meta.get("evidence") or "").strip():
        errors.append(f"{where}: {gid} is a Must but has no 'evidence' - say how a team shows they meet it")
    if meta.get("status") == "deprecated" and not meta.get("replaced_by"):
        errors.append(f"{where}: {gid} is deprecated but has no 'replaced_by'")
    if meta.get("since_version") and not VERSION.match(str(meta["since_version"])):
        errors.append(f"{where}: {gid} since_version '{meta['since_version']}' is not a version like 0.1.0")
    return errors


def parse(docs_dir: str) -> list[dict]:
    found: list[dict] = []
    errors: list[str] = []
    doctrines_for = _doctrines(docs_dir)
    for section, name in _guardrail_files(docs_dir):
        with open(os.path.join(docs_dir, section, name), encoding="utf-8") as handle:
            text = handle.read()
        front = _front_matter(text)
        defaults = front.get("guardrail_defaults") or {}
        if section == "guardrails" and not front.get("applicability"):
            errors.append(f"{name}: add 'applicability:' to the front matter (who the guardrails apply to, or tbc)")
        metadata = front.get("guardrails") or {}
        match = FRONT_MATTER.match(text)
        text = text[match.end() :] if match else text
        area = TITLE.search(text).group(1)
        matches = list(HEADING.finditer(text))
        seen = {m.group(1) for m in matches}
        for gid in sorted(set(metadata) - seen):
            errors.append(f"{name}: metadata for {gid}, which has no heading on this page")
        page_doctrines = sorted({d for pid in front.get("principles") or [] for d in doctrines_for.get(pid, [])})
        for match in matches:
            gid, title, anchor = match.groups()
            if anchor != gid.lower():
                errors.append(f"{name}: {gid} has anchor #{anchor}, expected #{gid.lower()}")
            nxt = SECTION.search(text, match.end())
            end = nxt.start() if nxt else len(text)
            body = text[match.end() : end]
            level = LEVEL.search(body)
            if not level:
                errors.append(f"{name}: {gid} has no Principle/Must/Should/Could badge")
                continue
            kind, statement = level.group(1), level.group(2)
            if kind != "principle" and gid not in metadata:
                errors.append(f"{name}: {gid} has no metadata under 'guardrails:' in the front matter")
            meta = {**defaults, **(metadata.get(gid) or {})}
            if kind == "principle":
                meta.setdefault("phases", list(PHASES))
                meta.setdefault("doctrine", doctrines_for.get(gid, []))
            meta.setdefault("doctrine", page_doctrines)
            errors += _check(gid, kind, meta, name)
            by_phase = meta.get("evidence_by_phase") if isinstance(meta.get("evidence_by_phase"), dict) else {}
            last = meta.get("last_reviewed")
            found.append(
                {
                    "id": gid,
                    "title": title,
                    "level": kind,
                    "statement": _plain(statement),
                    "area": area,
                    "page": f"{section}/{name}",
                    "status": meta.get("status"),
                    "phases": meta.get("phases") or [],
                    "evidence": str(meta.get("evidence") or "").strip(),
                    "evidence_by_phase": {
                        k: str(by_phase[k]).strip() for k in LIFECYCLE if by_phase.get(k) is not None
                    },
                    "automated_check": meta.get("automated_check"),
                    "service_standard_points": meta.get("service_standard_points") or [],
                    "tcop_points": meta.get("tcop_points") or [],
                    "sbd_principles": meta.get("sbd_principles") or [],
                    "doctrine": meta.get("doctrine") or [],
                    "owner": meta.get("owner"),
                    "last_reviewed": last.isoformat() if isinstance(last, datetime.date) else last,
                    "since_version": str(meta.get("since_version")),
                    "replaced_by": meta.get("replaced_by"),
                    "body": body.strip(),
                }
            )
    ids = [g["id"] for g in found]
    errors += [f"duplicate guardrail id {i}" for i in sorted({i for i in ids if ids.count(i) > 1})]
    for g in found:
        if g["replaced_by"] and g["replaced_by"] not in ids:
            errors.append(f"{g['id']} is replaced by {g['replaced_by']}, which does not exist")
    if errors:
        raise PluginError("Guardrails are invalid:\n  - " + "\n  - ".join(errors))
    return found


def evidence_for(g: dict, phase: str) -> str:
    """What to show for a guardrail in a phase, falling back to its general evidence."""
    return g["evidence_by_phase"].get(phase) or g["evidence"]


def guardrails() -> list[dict]:
    """The guardrails read at the start of the build, for other hooks."""
    return _guardrails


# --- MkDocs events -----------------------------------------------------------


def on_config(config):
    _guardrails[:] = parse(config["docs_dir"])
    levels = Counter(g["level"] for g in _guardrails)

    def load(name):
        with open(os.path.join(ROOT, "capabilities", name), encoding="utf-8") as handle:
            return yaml.safe_load(handle)["capabilities"]

    tech = load("technology-capabilities.yaml")
    with open(os.path.join(config["docs_dir"], "principles", "doctrine.md"), encoding="utf-8") as handle:
        doctrines = len(DOCTRINE_HEADING.findall(handle.read()))
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
    marker = "<!-- guardrails:print -->"
    if marker in markdown:
        markdown = markdown.replace(marker, _print(page, config))
    marker = "<!-- guardrails:musts -->"
    if marker in markdown:
        markdown = markdown.replace(marker, _musts(page, files))
    on_page = [g for g in _guardrails if g["page"] == page.file.src_uri]
    if on_page:
        markdown = _add_panels(markdown, on_page, page, files)
        if page.file.src_uri.startswith("guardrails/"):
            markdown = _add_applicability(markdown, page.meta.get("applicability"), on_page[0]["area"])
    return markdown


def on_post_build(config):
    out = {
        "description": "Defra architecture guardrails and principles with their metadata",
        "source": "https://github.com/howellsr/architecture",
        "guardrails": [{k: v for k, v in g.items() if k != "body"} for g in _guardrails],
    }
    with open(os.path.join(config["site_dir"], "guardrails.json"), "w", encoding="utf-8") as handle:
        json.dump(out, handle, indent=2)


# --- Renderers ---------------------------------------------------------------


def _sentence_case(text: str) -> str:
    """Lower-case the first letter for use mid-sentence, unless it starts an acronym such as APIs."""
    return text if len(text) > 1 and text[1].isupper() else text[:1].lower() + text[1:]


def _add_applicability(markdown: str, applicability, area: str) -> str:
    """Say who an area's guardrails apply to, after the page's lead paragraph."""
    if not applicability or applicability == "tbc":
        box = (
            '!!! warning "To be confirmed"\n'
            f"    **TODO:** whether the {_sentence_case(area)} guardrails apply to Defra's arm's length bodies "
            "as well as the core department, and any differences.\n"
        )
    else:
        box = f'!!! info "Who these guardrails apply to"\n    {applicability}\n'
    lines = markdown.split("\n")
    anchor = next((i for i, line in enumerate(lines) if line.startswith('<p class="lead">')), None)
    if anchor is None:
        anchor = next(i for i, line in enumerate(lines) if line.startswith("# "))
    lines.insert(anchor + 1, "\n" + box)
    return "\n".join(lines)


def _evidence_html(g: dict) -> str:
    e = html.escape
    if not g["evidence_by_phase"]:
        return e(g["evidence"]) or "-"
    items = "".join(f"<li><strong>{LIFECYCLE[k]}:</strong> {e(v)}</li>" for k, v in g["evidence_by_phase"].items())
    return f'<ul class="gr-meta__phases">{items}</ul>'


def _href(g: dict, page, files) -> str:
    target = files.get_file_from_path(g["page"])
    return get_relative_url(target.url, page.url) + "#" + g["id"].lower()


def _references(g: dict) -> str:
    """Service Standard, TCoP and SbD points as links with their names."""
    e = html.escape
    parts = []
    for field, (name, points, url) in REFERENCES.items():
        if g[field]:
            items = ", ".join(f'<abbr title="{e(points[p])}">{p}</abbr>' for p in g[field])
            parts.append(f'<a href="{url}">{name}</a> {items}')
    return "; ".join(parts)


def _doctrine_links(g: dict, page, files) -> str:
    doctrine = files.get_file_from_path("principles/doctrine.md")
    href = get_relative_url(doctrine.url, page.url) if doctrine else ""
    return ", ".join(f'<a href="{href}#{d}">{d.replace("ddts-", "").lstrip("0")}</a>' for d in g["doctrine"])


def _add_panels(markdown: str, on_page: list[dict], page, files) -> str:
    """Add a metadata panel at the end of each guardrail section."""
    e = html.escape
    by_id = {g["id"]: g for g in on_page}
    out, last = [], 0
    for match in HEADING.finditer(markdown):
        g = by_id.get(match.group(1))
        # The section ends at the next level 2 heading of any kind.
        nxt = SECTION.search(markdown, match.end())
        end = nxt.start() if nxt else len(markdown)
        out.append(markdown[last:end])
        last = end
        if not g or g["level"] == "principle":
            continue
        rows = [
            ("Status", f'<span class="gr-status gr-status--{g["status"]}">{STATUSES[g["status"]]}</span>'),
            ("Phases", ", ".join(PHASES[p] for p in g["phases"])),
            ("Evidence", _evidence_html(g)),
            ("Automated check", "Manual" if g["automated_check"] == "manual" else e(g["automated_check"])),
        ]
        refs = _references(g)
        if refs:
            rows.append(("Maps to", refs))
        if g["doctrine"]:
            rows.append(("DDTS doctrine", _doctrine_links(g, page, files)))
        rows.append(
            ("Owner", f"{e(g['owner'])}, last reviewed {e(str(g['last_reviewed']))}, since v{e(g['since_version'])}")
        )
        if g["replaced_by"]:
            other = next(x for x in _guardrails if x["id"] == g["replaced_by"])
            rows.insert(0, ("Replaced by", f'<a href="{_href(other, page, files)}">{other["id"]}</a>'))
        cells = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
        out.append(
            f'\n<details class="gr-meta"><summary>Phases, evidence and status for {g["id"]}</summary>'
            f"<dl>{cells}</dl></details>\n\n"
        )
    out.append(markdown[last:])
    return "".join(out)


MD_LINK = re.compile(r"\]\((?!https?://|#|mailto:)([^)]+)\)")


def _print(page, config) -> str:
    """Every guardrail in full, on one page, for the release PDF."""
    here = posixpath.dirname(page.file.src_uri)
    extra = config["extra"]
    out = [
        f"**Version {extra.get('version_in_force')}**, released {extra.get('version_date')}. "
        f"{_stats['guardrails']} guardrails and {_stats['principles']} principles.",
        "",
    ]
    area = None
    for g in _guardrails:
        if g["area"] != area:
            area = g["area"]
            out += [f"## {area}", ""]
        source = posixpath.dirname(g["page"])

        def relink(m, source=source):
            target = posixpath.normpath(posixpath.join(source, m.group(1)))
            return f"]({posixpath.relpath(target, here)})"

        out += [f"### {g['id']} {g['title']} {{#{g['id'].lower()}}}", "", MD_LINK.sub(relink, g["body"]), ""]
        if g["level"] != "principle":
            check = "Manual" if g["automated_check"] == "manual" else g["automated_check"]
            out += [
                f"*Status:* {STATUSES[g['status']]} · *Phases:* {', '.join(PHASES[p] for p in g['phases'])} · "
                f"*Since:* {g['since_version']}  ",
                *(
                    [f"*Evidence in {LIFECYCLE[k].lower()}:* {v}  " for k, v in g["evidence_by_phase"].items()]
                    or [f"*Evidence:* {g['evidence'] or '-'}  "]
                ),
                f"*Automated check:* {check}",
                "",
            ]
    return "\n".join(out) + "\n"


def _musts(page, files) -> str:
    """Every Must guardrail in force, as a table for contracts and statements of work."""
    rows = ["| Guardrail | Requirement | Evidence | Since |", "| --- | --- | --- | --- |"]
    musts = [g for g in _guardrails if g["level"] == "must" and g["status"] != "deprecated"]
    for g in musts:
        rows.append(
            f'| <a href="{_href(g, page, files)}">{g["id"]}</a> {g["title"]} | {g["statement"]} | {g["evidence"]} | '
            f"{g['since_version']} |"
        )
    return f"There are **{len(musts)}** Must guardrails.\n\n" + "\n".join(rows) + "\n"


def _library(page, files) -> str:
    e = html.escape
    areas = sorted({g["area"] for g in _guardrails}, key=lambda a: (a != "Architecture principles", a))
    options = "".join(f'<option value="{e(a)}">{e(a)}</option>' for a in areas)
    phase_options = "".join(f'<option value="{k}">{v}</option>' for k, v in PHASES.items())
    status_options = "".join(f'<option value="{k}">{v}</option>' for k, v in STATUSES.items())
    levels = Counter(g["level"] for g in _guardrails)
    chips = "".join(
        f'<label class="gl-chip"><input type="checkbox" name="gl-level" value="{k}" checked> '
        f'<span class="rfc rfc--{k}">{v}</span> <span class="gl-chip__n">{levels[k]}</span></label>'
        for k, v in LEVELS.items()
    )
    cards = []
    for g in _guardrails:
        search = " ".join([g["id"], g["title"], g["statement"], g["area"], g["evidence"]]).lower()
        details = ""
        if g["level"] != "principle":
            check = "Manual" if g["automated_check"] == "manual" else e(g["automated_check"])
            details = (
                f'<dl class="gl-card__facts"><dt>Evidence</dt><dd>{e(g["evidence"]) or "-"}</dd>'
                f"<dt>Automated check</dt><dd>{check}</dd>"
                f"<dt>Phases</dt><dd>{', '.join(PHASES[p] for p in g['phases'])}</dd></dl>"
            )
        replaced = f' <span class="gl-card__replaced">Replaced by {g["replaced_by"]}</span>' if g["replaced_by"] else ""
        cards.append(
            f'<article class="gl-card" data-level="{g["level"]}" data-area="{e(g["area"])}" '
            f'data-phases="{" ".join(g["phases"])}" data-status="{g["status"]}" data-search="{e(search)}">'
            f'<div class="gl-card__meta"><span class="rfc rfc--{g["level"]}">{LEVELS[g["level"]]}</span>'
            f'<code>{g["id"]}</code><span class="gr-status gr-status--{g["status"]}">{STATUSES[g["status"]]}</span>'
            f'<span class="gl-card__area">{e(g["area"])}</span></div>'
            f'<h3 class="gl-card__title"><a href="{_href(g, page, files)}">{e(g["title"])}</a>{replaced}</h3>'
            f"<p>{e(g['statement'])}</p>{details}</article>"
        )
    return (
        '<div class="gl" data-guardrail-library>\n'
        '<div class="gl-tools" role="search">'
        '<label class="gl-field"><span>Search</span>'
        '<input type="search" id="gl-search" placeholder="e.g. secrets, hosting, GR-API-02" autocomplete="off"></label>'
        '<label class="gl-field"><span>Area</span><select id="gl-area">'
        f'<option value="">All areas</option>{options}</select></label>'
        '<label class="gl-field"><span>Phase</span><select id="gl-phase">'
        f'<option value="">All phases</option>{phase_options}</select></label>'
        '<label class="gl-field"><span>Status</span><select id="gl-status">'
        f'<option value="">Any status</option>{status_options}</select></label>'
        f'<fieldset class="gl-levels"><legend>Level</legend>{chips}</fieldset>'
        "</div>\n"
        f'<p class="gl-count" aria-live="polite">Showing <strong id="gl-shown">{len(_guardrails)}</strong> '
        f"of {len(_guardrails)} guardrails</p>\n"
        f'<div class="gl-grid">{"".join(cards)}</div>\n'
        '<p class="gl-empty" hidden>No guardrails match. Try a different word, or clear the filters.</p>\n'
        "</div>\n"
    )
