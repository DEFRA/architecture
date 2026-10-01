"""MkDocs hook for the architecture patterns section.

Each pattern is a page in ``docs/patterns/`` with front matter that says what
kind of pattern it is, which guardrails it helps a team meet, and which
Secure by Design (SbD) artefacts relate to it:

    pattern:
      category: integration          # infrastructure, integration, security or data
      status: draft                  # proposed, draft or endorsed
      summary: One sentence for the catalogue.
      guardrails: [GR-API-05, GR-API-06]
      sbd: [stride-template]         # keys of SBD_ARTEFACTS below

This hook validates that front matter and replaces:

    <!-- patterns:guardrails -->   the guardrails the pattern satisfies
    <!-- patterns:sbd -->          links to the related SbD artefacts
    <!-- patterns:catalogue -->    every pattern, grouped by category
"""

from __future__ import annotations

import importlib.util
import os
import posixpath
import re

import yaml
from mkdocs.exceptions import PluginError

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER = "patterns"
FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
TITLE = re.compile(r"^# (.+)$", re.M)

CATEGORIES = {
    "infrastructure": "Infrastructure",
    "integration": "Integration",
    "security": "Security and identity",
    "data": "Data",
}
STATUSES = {"proposed": "Proposed", "draft": "Draft", "endorsed": "Endorsed"}

# Artefacts in the cross-government Secure by Design artefact library.
SBD_BASE = "https://github.com/co-cddo/SbD"
SBD_ARTEFACTS = {
    "security-patterns": ("Security patterns", "tree/Main/Security%20Architecture%20/Security%20Patterns"),
    "one-login-pattern": (
        "GOV.UK One Login security pattern",
        "tree/Main/Security%20Architecture%20/Security%20Patterns/GOV.UK%20One%20Login",
    ),
    "security-requirements": (
        "Security requirements",
        "tree/Main/Security%20Architecture%20/Security%20Requirements",
    ),
    "access-control": ("Access control and authentication", "tree/Main/Access%20Control%20%26%20Authentication"),
    "stride-template": (
        "STRIDE threat modelling template",
        "blob/Main/Risks%20and%20Threats/Stride%20Threat%20Modelling%20Template%20-%20Secure%20By%20Design%20Artefact%20Library.xlsx",
    ),
    "stride-defra": (
        "STRIDE threat modelling guardrails - Defra",
        "blob/Main/Risks%20and%20Threats/STRIDE%20Threat%20modeling%20Guardrails%20-%20Defra.docx",
    ),
    "dlp-strategy": (
        "Data loss prevention strategy",
        "blob/Main/Security%20Architecture%20/Security%20Documentation/"
        "Data%20Loss%20Prevention%20%28DLP%29%20Strategy%20aligning%20with%20SbD/"
        "Data%20Loss%20Prevention%20%28DLP%29%20Strategy%20-%20Alignment%20with%20SbD.md",
    ),
    "security-event-logs": (
        "Security event logs",
        "tree/Main/Operations/Security%20Monitoring/Security%20Event%20Logs",
    ),
    "secure-pipeline": (
        "Secure software development pipeline",
        "tree/Main/Security%20Architecture%20/Security%20Documentation/"
        "Secure%20Software%20Development%20Pipeline%20%28SSDP%29",
    ),
    "incident-response-plan": (
        "Incident response plan template",
        "tree/Main/Operations/Incident%20Management%20/Incident%20Response%20Plan%20Template",
    ),
}

_patterns: list[dict] = []
_guardrails: dict[str, dict] = {}


def _load_guardrails(docs_dir: str) -> dict[str, dict]:
    path = os.path.join(ROOT, "hooks", "guardrails.py")
    spec = importlib.util.spec_from_file_location("_guardrails_for_patterns", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return {g["id"]: g for g in module.parse(docs_dir)}


def parse(docs_dir: str, guardrails: dict[str, dict]) -> list[dict]:
    """Read and validate every pattern page."""
    found, errors = [], []
    for dirpath, _, names in sorted(os.walk(os.path.join(docs_dir, FOLDER))):
        for name in sorted(names):
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            src = os.path.relpath(path, docs_dir).replace(os.sep, "/")
            with open(path, encoding="utf-8") as handle:
                text = handle.read()
            match = FRONT_MATTER.match(text)
            meta = ((yaml.safe_load(match.group(1)) if match else None) or {}).get("pattern")
            if meta is None:
                continue
            title = TITLE.search(text[match.end() :]).group(1)
            if meta.get("category") not in CATEGORIES:
                errors.append(f"{src}: category must be one of {', '.join(CATEGORIES)}")
            if meta.get("status") not in STATUSES:
                errors.append(f"{src}: status must be one of {', '.join(STATUSES)}")
            if not meta.get("summary"):
                errors.append(f"{src}: add a one-sentence 'summary'")
            if not meta.get("guardrails"):
                errors.append(f"{src}: list the 'guardrails' the pattern helps meet")
            errors += [f"{src}: unknown guardrail {g}" for g in meta.get("guardrails", []) if g not in guardrails]
            errors += [f"{src}: unknown SbD artefact '{a}'" for a in meta.get("sbd", []) if a not in SBD_ARTEFACTS]
            for marker in ("<!-- patterns:guardrails -->", "<!-- patterns:sbd -->"):
                if marker not in text:
                    errors.append(f"{src}: add a {marker} section")
            found.append({"src": src, "title": title, **meta})
    if errors:
        raise PluginError("Patterns are invalid:\n  - " + "\n  - ".join(errors))
    return found


def on_config(config):
    _guardrails.clear()
    _guardrails.update(_load_guardrails(config["docs_dir"]))
    _patterns[:] = parse(config["docs_dir"], _guardrails)
    return config


def on_page_markdown(markdown, page, config, files):
    if "<!-- patterns:" not in markdown:
        return markdown
    src = page.file.src_uri

    def link(target: str) -> str:
        path, _, anchor = target.partition("#")
        return posixpath.relpath(path, posixpath.dirname(src)) + (f"#{anchor}" if anchor else "")

    pattern = next((p for p in _patterns if p["src"] == src), None)
    if pattern:
        rows = ["| Guardrail | Level | What the guardrail asks |", "| --- | --- | --- |"]
        for gid in pattern["guardrails"]:
            g = _guardrails[gid]
            rows.append(
                f"| [{gid}]({link(g['page'] + '#' + gid.lower())}) {g['title']} | "
                f'<span class="rfc rfc--{g["level"]}">{g["level"].title()}</span> | {g["statement"]} |'
            )
        markdown = markdown.replace("<!-- patterns:guardrails -->", "\n".join(rows) + "\n")
        sbd = [f"- [{SBD_ARTEFACTS[a][0]}]({SBD_BASE}/{SBD_ARTEFACTS[a][1]})" for a in pattern.get("sbd", [])]
        sbd.append(f"- The whole [Secure by Design artefact library]({SBD_BASE})")
        markdown = markdown.replace("<!-- patterns:sbd -->", "\n".join(sbd) + "\n")

    if "<!-- patterns:catalogue -->" in markdown:
        markdown = markdown.replace("<!-- patterns:catalogue -->", _catalogue(link))
    return markdown


def _catalogue(link) -> str:
    out = []
    for key, name in CATEGORIES.items():
        items = [p for p in _patterns if p["category"] == key]
        out += [f"## {name} {{#{key}}}", ""]
        if not items:
            out += [
                "No patterns yet. [Propose one](https://github.com/howellsr/architecture/issues) "
                "if your team has solved a problem others will meet.",
                "",
            ]
            continue
        out += ["| Pattern | Use it when | Status | Guardrails |", "| --- | --- | --- | --- |"]
        for p in items:
            ids = ", ".join(f"`{g}`" for g in p["guardrails"])
            out.append(f"| [{p['title']}]({link(p['src'])}) | {p['summary']} | {STATUSES[p['status']]} | {ids} |")
        out.append("")
    return "\n".join(out) + "\n"
