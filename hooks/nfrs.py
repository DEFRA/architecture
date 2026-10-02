"""MkDocs hook that renders the non-functional requirements (NFR) pages.

The service tiers and the NFR catalogue live in ``nfrs/*.yaml`` so they can be
reviewed in pull requests and reused by other tools. This hook:

* validates them when the site builds - unique ids, ids that match their
  category, targets only for tiers that exist, and guardrail ids that exist;
* replaces ``<!-- nfrs:... -->`` markers in pages with generated content; and
* publishes the combined data as ``nfrs.json`` alongside the site.

Markers:

    <!-- nfrs:status -->           draft banner, shown while status is "draft"
    <!-- nfrs:tiers -->            service tier comparison table
    <!-- nfrs:tier-questions -->   questions for choosing a tier
    <!-- nfrs:categories -->       list of categories with counts
    <!-- nfrs:catalogue -->        every requirement, grouped by category
"""

from __future__ import annotations

import json
import os
import posixpath
import re

import yaml
from mkdocs.exceptions import PluginError

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TIERS_FILE = os.path.join(ROOT, "nfrs", "service-tiers.yaml")
CATALOGUE_FILE = os.path.join(ROOT, "nfrs", "catalogue.yaml")

CATALOGUE_PAGE = "nfrs/catalogue.md"
TIERS_PAGE = "nfrs/service-tiers.md"
GUARDRAIL_HEADING = re.compile(r"^## (GR-[A-Z]+-\d{2}) ", re.M)

TIER_ROWS = [
    ("summary", "When to use it"),
    ("examples", "Examples"),
    ("availability", "Availability"),
    ("support_hours", "Support hours"),
    ("rto", "Recovery time objective (RTO)"),
    ("rpo", "Recovery point objective (RPO)"),
    ("dr_test", "Disaster recovery test"),
]

_data: dict = {}


def _load(path: str) -> dict:
    with open(path, encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def guardrail_pages(docs_dir: str) -> dict[str, str]:
    """Map each guardrail id to the docs-relative page that defines it."""
    found = {}
    for section in ("principles", "guardrails"):
        folder = os.path.join(docs_dir, section)
        for name in sorted(os.listdir(folder)):
            if name.endswith(".md"):
                with open(os.path.join(folder, name), encoding="utf-8") as handle:
                    for gid in GUARDRAIL_HEADING.findall(handle.read()):
                        found[gid] = f"{section}/{name}"
    return found


def validate(tiers: dict, catalogue: dict, guardrails: dict[str, str]) -> list[str]:
    errors: list[str] = []
    tier_ids = [t["id"] for t in tiers["tiers"]]
    for tier in tiers["tiers"]:
        missing = [key for key, _ in TIER_ROWS if not tier.get(key)]
        if missing:
            errors.append(f"tier {tier['id']} is missing {', '.join(missing)}")

    seen: set[str] = set()
    for category in catalogue["categories"]:
        for req in category["requirements"]:
            rid = req.get("id", "?")
            if rid in seen:
                errors.append(f"duplicate NFR id {rid}")
            seen.add(rid)
            if not rid.startswith(f"NFR-{category['id']}-"):
                errors.append(f"{rid} is in category {category['id']} but its id does not start NFR-{category['id']}-")
            for field in ("title", "requirement", "verify"):
                if not req.get(field):
                    errors.append(f"{rid} has no {field}")
            for tier in req.get("targets") or {}:
                if tier not in tier_ids:
                    errors.append(f"{rid} has a target for unknown tier {tier}")
            for gid in req.get("guardrails", []):
                if gid not in guardrails:
                    errors.append(f"{rid} refers to unknown guardrail {gid}")
    return errors


# --- MkDocs events -----------------------------------------------------------


def on_config(config):
    tiers = _load(TIERS_FILE)
    catalogue = _load(CATALOGUE_FILE)
    guardrails = guardrail_pages(config["docs_dir"])
    errors = validate(tiers, catalogue, guardrails)
    if errors:
        raise PluginError("NFRs are invalid:\n  - " + "\n  - ".join(errors))
    _data.clear()
    _data.update(tiers=tiers, catalogue=catalogue, guardrails=guardrails)
    return config


def on_page_markdown(markdown, page, config, files):
    if "<!-- nfrs:" not in markdown:
        return markdown

    def link(target: str) -> str:
        path, _, frag = target.partition("#")
        rel = posixpath.relpath(path, posixpath.dirname(page.file.src_uri))
        return rel + (f"#{frag}" if frag else "")

    renderers = {
        "status": _status,
        "tiers": _tiers,
        "tier-questions": _tier_questions,
        "categories": _categories,
        "catalogue": _catalogue,
    }
    for name, render in renderers.items():
        marker = f"<!-- nfrs:{name} -->"
        if marker in markdown:
            markdown = markdown.replace(marker, render(link))
    return markdown


def on_post_build(config):
    out = {"service_tiers": _data["tiers"], "catalogue": _data["catalogue"]}
    with open(os.path.join(config["site_dir"], "nfrs.json"), "w", encoding="utf-8") as handle:
        json.dump(out, handle, indent=2)


# --- Renderers ---------------------------------------------------------------


def _cell(text) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


SERVICE_MANUAL_NFRS = "https://digital.defra.gov.uk/business-analysis/non-functional-requirements"


def _status(link) -> str:
    if _data["tiers"].get("status") != "draft" and _data["catalogue"].get("status") != "draft":
        return ""
    return (
        '!!! warning "Use the DDTS service tiers and NFR list"\n'
        "    The authoritative service tiers, list of non-functional requirements and the Business Criticality "
        "and Service Tier Assessment are maintained by the business analysis community - see "
        f"[non-functional requirements]({SERVICE_MANUAL_NFRS}) in the Defra Digital Service Manual. "
        "The tiers and targets on this site are placeholders that show how architecture uses them. "
        "Where they differ, the DDTS lists apply.\n"
    )


def _tiers(link) -> str:
    tiers = _data["tiers"]["tiers"]
    head = "| | " + " | ".join(f"**{t['id']} {t['name']}**" for t in tiers) + " |"
    sep = "| --- |" + " --- |" * len(tiers)
    rows = [f"| **{label}** | " + " | ".join(_cell(t[key]) for t in tiers) + " |" for key, label in TIER_ROWS]
    return "\n".join([head, sep, *rows]) + "\n"


def _tier_questions(link) -> str:
    return "\n".join(f"1. {q}" for q in _data["tiers"]["questions"]) + "\n"


def _categories(link) -> str:
    rows = ["| Category | What it covers | Requirements |", "| --- | --- | --- |"]
    for c in _data["catalogue"]["categories"]:
        anchor = "nfr-" + c["id"].lower()
        name = f"[{c['name']}]({link(CATALOGUE_PAGE + '#' + anchor)})"
        rows.append(f"| {name} | {_cell(c['description'])} | {len(c['requirements'])} |")
    return "\n".join(rows) + "\n"


def _catalogue(link) -> str:
    tier_ids = [t["id"] for t in _data["tiers"]["tiers"]]
    guardrails = _data["guardrails"]
    out = []
    for c in _data["catalogue"]["categories"]:
        out.append(f"## {c['name']} {{#nfr-{c['id'].lower()}}}\n\n{c['description']}\n")
        out.append("| ID | Requirement | How to show it is met | Target by tier | Related guardrails |")
        out.append("| --- | --- | --- | --- | --- |")
        for r in c["requirements"]:
            targets = r.get("targets")
            target = (
                "<br>".join(f"**{t}:** {_cell(targets[t])}" for t in tier_ids if t in targets)
                if targets
                else "All tiers"
            )
            related = (
                ", ".join(f"[`{g}`]({link(guardrails[g] + '#' + g.lower())})" for g in r.get("guardrails", [])) or "-"
            )
            out.append(
                f"| `{r['id']}` | **{_cell(r['title'])}**<br>{_cell(r['requirement'])} | "
                f"{_cell(r['verify'])} | {target} | {related} |"
            )
        out.append("")
    return "\n".join(out) + "\n"
