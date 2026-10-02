"""MkDocs hook for the approval status, exception register and guardrails health pages.

The data lives in ``registers/approvals.yaml`` and ``registers/exceptions.yaml``.
This hook validates it and replaces:

    <!-- registers:approvals -->    approval status of each section of the site
    <!-- registers:exceptions -->   the published exception register
    <!-- registers:health -->       guardrails health: exceptions per guardrail,
                                    exceptions expiring soon and guardrails to review
    <!-- registers:doctrine-intro -->, <!-- registers:doctrine-lead -->,
    <!-- registers:doctrine-by -->   wording about the DDTS doctrine that says it
                                    is draft until the approvals register records
                                    it as endorsed

It also sets ``doctrine_label`` in page metadata for the home page template.

The health page is rebuilt every time the site is published. The figures are
reviewed each quarter.
"""

from __future__ import annotations

import datetime
import importlib.util
import os
import posixpath
import re
from collections import Counter

import yaml
from mkdocs.exceptions import PluginError

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPROVALS = os.path.join(ROOT, "registers", "approvals.yaml")
EXCEPTIONS = os.path.join(ROOT, "registers", "exceptions.yaml")

STATUSES = {"draft": "Draft", "endorsed": "Endorsed"}
DOCTRINE_PAGE = "principles/doctrine.md"

# How the site describes the doctrine, by its status in registers/approvals.yaml.
DOCTRINE_WORDING = {
    "endorsed": {
        "label": "non-negotiables set by the CDIO",
        "intro": "One line of sight from the CDIO's non-negotiables to the decisions your team makes this week.",
        "lead": "The non-negotiables:",
        "by": "set by the CDIO",
    },
    "draft": {
        "label": "draft non-negotiables, awaiting endorsement",
        "intro": "One line of sight from the draft DDTS doctrine to the decisions your team makes this week.",
        "lead": "The draft non-negotiables, awaiting endorsement:",
        "by": "draft, awaiting endorsement",
    },
}


def doctrine_wording(sections: list[dict]) -> dict:
    """Wording for the doctrine: endorsed only when the approvals register says so."""
    status = next((s.get("status") for s in sections if s.get("pages") == DOCTRINE_PAGE), "draft")
    return DOCTRINE_WORDING["endorsed" if status == "endorsed" else "draft"]


EXCEPTION_ID = re.compile(r"^EX-\d{4}-\d{3}$")
DOCS_LINK = re.compile(r"\]\((?!https?://|#)([^)]+)\)")

# An exception expiring within this many days is "expiring soon".
EXPIRING_DAYS = 90
# A guardrail with this many active exceptions is a candidate to change.
REPEATED = 3
# A guardrail not reviewed for this many days is due a review.
REVIEW_DAYS = 365

_data: dict = {}


def _load_guardrails(docs_dir: str) -> dict[str, dict]:
    path = os.path.join(ROOT, "hooks", "guardrails.py")
    spec = importlib.util.spec_from_file_location("_guardrails_for_registers", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return {g["id"]: g for g in module.parse(docs_dir)}


def _date(value):
    if isinstance(value, datetime.date):
        return value
    return datetime.date.fromisoformat(str(value))


def load(docs_dir: str, approvals: dict, exceptions: dict, guardrails: dict[str, dict]) -> dict:
    """Validate the registers and return them ready to render."""
    errors = []
    sections = approvals.get("sections") or []
    for s in sections:
        where = f"approvals: {s.get('name')}"
        if s.get("status") not in STATUSES:
            errors.append(f"{where}: status must be one of {', '.join(STATUSES)}")
        if not os.path.exists(os.path.join(docs_dir, s.get("pages", ""))):
            errors.append(f"{where}: pages '{s.get('pages')}' does not exist")
        for field in ("board", "date"):
            if not s.get(field):
                errors.append(f"{where}: set '{field}', or 'tbc' if it is not known")
        if s.get("date") not in (None, "tbc"):
            try:
                _date(s["date"])
            except ValueError:
                errors.append(f"{where}: date must be YYYY-MM-DD or tbc")

    items = exceptions.get("exceptions") or []
    ids = [e.get("id") for e in items]
    errors += [f"exceptions: duplicate id {i}" for i in sorted({i for i in ids if ids.count(i) > 1})]
    for e in items:
        where = f"exceptions: {e.get('id')}"
        if not EXCEPTION_ID.match(str(e.get("id", ""))):
            errors.append(f"{where}: id must look like EX-2026-001")
        if e.get("guardrail") not in guardrails:
            errors.append(f"{where}: unknown guardrail {e.get('guardrail')}")
        for field in ("service", "owner", "approved", "expiry"):
            if not e.get(field):
                errors.append(f"{where}: missing '{field}'")
        try:
            if _date(e["expiry"]) <= _date(e["approved"]):
                errors.append(f"{where}: expiry must be after the approval date")
        except (KeyError, ValueError):
            errors.append(f"{where}: approved and expiry must be dates (YYYY-MM-DD)")
    if errors:
        raise PluginError("Registers are invalid:\n  - " + "\n  - ".join(errors))
    return {"sections": sections, "exceptions": items, "guardrails": guardrails}


def on_config(config):
    with open(APPROVALS, encoding="utf-8") as handle:
        approvals = yaml.safe_load(handle)
    with open(EXCEPTIONS, encoding="utf-8") as handle:
        exceptions = yaml.safe_load(handle)
    _data.clear()
    _data.update(load(config["docs_dir"], approvals, exceptions, _load_guardrails(config["docs_dir"])))
    _data["today"] = datetime.date.today()
    return config


def on_page_markdown(markdown, page, config, files):
    wording = doctrine_wording(_data["sections"])
    if page.file.src_uri == "index.md":
        page.meta["doctrine_label"] = wording["label"]
    if "<!-- registers:" not in markdown:
        return markdown
    for key in ("intro", "lead", "by"):
        markdown = markdown.replace(f"<!-- registers:doctrine-{key} -->", wording[key])
    src = page.file.src_uri

    def link(target: str) -> str:
        path, _, anchor = target.partition("#")
        rel = posixpath.relpath(path, posixpath.dirname(src))
        return rel + (f"#{anchor}" if anchor else "")

    renderers = {
        "<!-- registers:approvals -->": lambda: _approvals(link, config["docs_dir"]),
        "<!-- registers:exceptions -->": lambda: _exceptions(link),
        "<!-- registers:health -->": lambda: _health(link),
    }
    for marker, render in renderers.items():
        if marker in markdown:
            markdown = markdown.replace(marker, render())
    return markdown


# --- Renderers ---------------------------------------------------------------


def _tbc(value) -> str:
    return "To be confirmed" if value in (None, "tbc") else str(value)


def _draft_pages(docs_dir: str, pages: str) -> tuple[int, int]:
    """Count the pages in a section, and how many are marked draft."""
    path = os.path.join(docs_dir, pages)
    files = (
        [path]
        if os.path.isfile(path)
        else [os.path.join(d, n) for d, _, names in os.walk(path) for n in names if n.endswith(".md")]
    )
    drafts = 0
    for name in files:
        with open(name, encoding="utf-8") as handle:
            if re.match(r"\A---\n(?:.*\n)*?status: draft\n(?:.*\n)*?---\n", handle.read()):
                drafts += 1
    return len(files), drafts


def _approvals(link, docs_dir: str) -> str:
    rows = ["| Section | Status | Approved by | Date | Draft pages | Notes |", "| --- | --- | --- | --- | ---: | --- |"]
    for s in _data["sections"]:
        target = s.get("link") or s["pages"] + ("index.md" if s["pages"].endswith("/") else "")
        total, drafts = _draft_pages(docs_dir, s["pages"])
        note = DOCS_LINK.sub(lambda m: f"]({link(m.group(1))})", s.get("note", "")) or "-"
        rows.append(
            f"| [{s['name']}]({link(target)}) | {STATUSES[s['status']]} | {_tbc(s['board'])} | "
            f"{_tbc(s['date'])} | {drafts} of {total} | {note} |"
        )
    return "\n".join(rows) + "\n"


def _guardrail_link(gid: str, link) -> str:
    g = _data["guardrails"][gid]
    return f"[{gid}]({link(g['page'] + '#' + gid.lower())})"


def _active(today: datetime.date) -> list[dict]:
    return [e for e in _data["exceptions"] if _date(e["expiry"]) >= today]


def _exceptions(link) -> str:
    items = sorted(_data["exceptions"], key=lambda e: e["id"])
    if not items:
        return "No exceptions have been recorded in the published register yet.\n"
    today = _data["today"]
    rows = [
        "| Id | Guardrail | Service | Approved | Expiry | Owner | State |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for e in items:
        state = "Expired" if _date(e["expiry"]) < today else "Active"
        ident = f"[{e['id']}]({e['decision']})" if e.get("decision") else e["id"]
        rows.append(
            f"| {ident} | {_guardrail_link(e['guardrail'], link)} | {e['service']} | {e['approved']} | "
            f"{e['expiry']} | {e['owner']} | {state} |"
        )
    return "\n".join(rows) + "\n"


def _health(link) -> str:
    today = _data["today"]
    quarter = f"{today.year} Q{(today.month - 1) // 3 + 1}"
    guardrails = [g for g in _data["guardrails"].values() if g["level"] != "principle"]
    active = _active(today)
    per = Counter(e["guardrail"] for e in active)
    statuses = Counter(g["status"] for g in guardrails)

    out = [
        f"Figures for **{quarter}**, built on {today.day} {today:%B %Y}.",
        "",
        "| Measure | Now |",
        "| --- | ---: |",
        f"| Guardrails | {len(guardrails)} |",
        f"| Endorsed | {statuses['endorsed']} |",
        f"| Draft | {statuses['draft']} |",
        f"| Deprecated | {statuses['deprecated']} |",
        f"| Active exceptions | {len(active)} |",
        f"| Guardrails with an active exception | {len(per)} |",
        "",
        "## Exceptions per guardrail",
        "",
    ]
    if per:
        out += ["| Guardrail | Active exceptions |", "| --- | ---: |"]
        out += [f"| {_guardrail_link(gid, link)} | {n} |" for gid, n in per.most_common()]
    else:
        out.append("No active exceptions are recorded in the published register.")
    out += ["", f"## Expiring in the next {EXPIRING_DAYS} days", ""]
    soon = sorted(
        (e for e in active if (_date(e["expiry"]) - today).days <= EXPIRING_DAYS), key=lambda e: _date(e["expiry"])
    )
    if soon:
        out += ["| Id | Guardrail | Service | Expiry | Owner |", "| --- | --- | --- | --- | --- |"]
        out += [
            f"| {e['id']} | {_guardrail_link(e['guardrail'], link)} | {e['service']} | {e['expiry']} | {e['owner']} |"
            for e in soon
        ]
    else:
        out.append("No exceptions expire in this period.")

    out += ["", "## Candidates to change", ""]
    repeated = [gid for gid, n in per.items() if n >= REPEATED]
    stale = sorted(
        g["id"]
        for g in guardrails
        if (today - _date(g["last_reviewed"])).days > REVIEW_DAYS and g["status"] != "deprecated"
    )
    drafts = sorted(g["id"] for g in guardrails if g["status"] == "draft")
    out.append(
        f"- **Repeated exceptions** ({REPEATED} or more active): "
        + (", ".join(_guardrail_link(g, link) for g in sorted(repeated)) or "none")
    )
    out.append("- **Not reviewed for over a year**: " + (", ".join(_guardrail_link(g, link) for g in stale) or "none"))
    out.append(
        f"- **Still in draft**: {len(drafts)} guardrails. Endorsing or changing them is the main work for the "
        "Technical Design Authority and Technology Governance Board - see the "
        f"[approval status]({link('about/approval-status.md')})."
    )
    return "\n".join(out) + "\n"
