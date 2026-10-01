"""MkDocs hook that renders the Defra capability handrail from YAML.

The business and technology capability models live in ``capabilities/*.yaml``
so they can be reviewed in pull requests, reused by other tools and rendered
consistently. This hook:

* validates the models when the site builds (unknown ids, missing guardrail
  pages and orphaned technology capabilities fail the build);
* replaces ``<!-- capabilities:... -->`` markers in pages with generated
  content; and
* publishes the combined model as ``capabilities.json`` alongside the site.

Markers:

    <!-- capabilities:business-map -->         the one-page capability map
    <!-- capabilities:attributes -->           what makes a good capability
    <!-- capabilities:business-detail -->      level 1 and draft level 2 detail
    <!-- capabilities:technology-summary -->   counts by status
    <!-- capabilities:technology-catalogue --> technology catalogue by domain
    <!-- capabilities:matrix -->               business x technology heatmap
"""

from __future__ import annotations

import html
import json
import os
import posixpath
from collections import Counter

import yaml
from mkdocs.exceptions import PluginError
from mkdocs.utils import get_relative_url

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUSINESS_FILE = os.path.join(ROOT, "capabilities", "business-capabilities.yaml")
TECHNOLOGY_FILE = os.path.join(ROOT, "capabilities", "technology-capabilities.yaml")

BUSINESS_PAGE = "handrail/business-capabilities.md"
TECHNOLOGY_PAGE = "handrail/technology-capabilities.md"

STATUS_LABELS = {
    "strategic": "Strategic",
    "emerging": "Emerging",
    "gap": "Gap",
}

_model: dict = {}


def _load(path: str) -> dict:
    with open(path, encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def validate(business: dict, technology: dict, docs_dir: str) -> list[str]:
    """Return a list of problems with the capability models."""
    errors: list[str] = []
    domains = {d["id"] for d in technology["domains"]}

    tech_ids = [c["id"] for c in technology["capabilities"]]
    for dup in {i for i in tech_ids if tech_ids.count(i) > 1}:
        errors.append(f"duplicate technology capability id {dup}")

    for cap in technology["capabilities"]:
        if cap.get("domain") not in domains:
            errors.append(f"{cap['id']} has unknown domain {cap.get('domain')!r}")
        if cap.get("status") not in STATUS_LABELS:
            errors.append(f"{cap['id']} has unknown status {cap.get('status')!r}")
        targets = [cap.get("guardrail")] + [o.get("url") for o in cap.get("options", [])]
        for target in targets:
            if target and not target.startswith("http"):
                if not os.path.exists(os.path.join(docs_dir, target.split("#")[0])):
                    errors.append(f"{cap['id']} links to missing page {target}")

    bus_ids = [c["id"] for c in business["capabilities"]]
    for dup in {i for i in bus_ids if bus_ids.count(i) > 1}:
        errors.append(f"duplicate business capability id {dup}")

    used = set()
    for cap in business["capabilities"]:
        if cap.get("type") not in ("core", "supporting"):
            errors.append(f"{cap['id']} has unknown type {cap.get('type')!r}")
        for ref in cap.get("technology", []):
            if ref not in tech_ids:
                errors.append(f"{cap['id']} references unknown technology capability {ref}")
            used.add(ref)

    for orphan in sorted(set(tech_ids) - used):
        errors.append(f"technology capability {orphan} does not support any business capability")

    return errors


# --- MkDocs events -----------------------------------------------------------


def on_config(config):
    business = _load(BUSINESS_FILE)
    technology = _load(TECHNOLOGY_FILE)
    errors = validate(business, technology, config["docs_dir"])
    if errors:
        raise PluginError("Capability model is invalid:\n  - " + "\n  - ".join(errors))

    tech_by_id = {c["id"]: c for c in technology["capabilities"]}
    supports: dict[str, list[str]] = {i: [] for i in tech_by_id}
    for cap in business["capabilities"]:
        for ref in cap.get("technology", []):
            supports[ref].append(cap["id"])

    _model.clear()
    _model.update(
        business=business,
        technology=technology,
        tech_by_id=tech_by_id,
        bus_by_id={c["id"]: c for c in business["capabilities"]},
        supports=supports,
    )
    return config


def on_page_markdown(markdown, page, config, files):
    if "<!-- capabilities:" not in markdown:
        return markdown

    def url_to(src_path: str, anchor: str = "") -> str:
        if src_path.startswith("http"):
            return src_path
        path, _, existing = src_path.partition("#")
        target = files.get_file_from_path(path)
        if target is None:
            raise PluginError(f"capabilities hook: no page {path}")
        frag = anchor or existing
        return get_relative_url(target.url, page.url) + (f"#{frag}" if frag else "")

    def md_to(src_path: str, anchor: str = "") -> str:
        """Relative .md link, so MkDocs validates it like a hand-written link."""
        if src_path.startswith("http"):
            return src_path
        path, _, existing = src_path.partition("#")
        frag = anchor or existing
        rel = posixpath.relpath(path, posixpath.dirname(page.file.src_uri))
        return rel + (f"#{frag}" if frag else "")

    renderers = {
        "business-map": _business_map,
        "attributes": _attributes,
        "business-detail": _business_detail,
        "technology-summary": _technology_summary,
        "technology-catalogue": _technology_catalogue,
        "matrix": _matrix,
    }
    for name, render in renderers.items():
        marker = f"<!-- capabilities:{name} -->"
        if marker in markdown:
            markdown = markdown.replace(marker, render(url_to, md_to))
    return markdown


def on_post_build(config):
    out = {
        "attributes": _model["business"]["attributes"],
        "business_capabilities": _model["business"]["capabilities"],
        "technology_domains": _model["technology"]["domains"],
        "technology_capabilities": _model["technology"]["capabilities"],
    }
    with open(os.path.join(config["site_dir"], "capabilities.json"), "w", encoding="utf-8") as handle:
        json.dump(out, handle, indent=2)


# --- Renderers ---------------------------------------------------------------

e = html.escape


def _tile(cap, url_to) -> str:
    href = url_to(BUSINESS_PAGE, cap["id"].lower())
    return (
        f'<a class="bcm-tile" href="{href}">'
        f'<span class="bcm-tile__number">{e(cap["number"])}</span>'
        f'<span class="bcm-tile__name">{e(cap["name"])}</span>'
        "</a>"
    )


def _business_map(url_to, md_to=None) -> str:
    caps = _model["business"]["capabilities"]
    core = "".join(_tile(c, url_to) for c in caps if c["type"] == "core")
    supporting = "".join(_tile(c, url_to) for c in caps if c["type"] == "supporting")
    return (
        '<div class="bcm" role="navigation" aria-label="Defra business capability map">\n'
        '<p class="bcm__heading">Core capabilities</p>\n'
        f'<div class="bcm-grid">{core}</div>\n'
        '<p class="bcm__heading bcm__heading--supporting">Supporting capabilities</p>\n'
        f'<div class="bcm-grid bcm-grid--supporting">{supporting}</div>\n'
        "</div>\n"
    )


def _attributes(url_to, md_to=None) -> str:
    rows = "\n".join(
        f"| **{a['name']}** | {a['description']} |" for a in _model["business"]["attributes"]
    )
    return "| Attribute | What it means |\n| --- | --- |\n" + rows + "\n"


def _status_badge(status: str) -> str:
    return f'<span class="cap-status cap-status--{status}">{STATUS_LABELS[status]}</span>'


def _business_detail(_url_to, url_to) -> str:
    tech = _model["tech_by_id"]
    out = []
    current_type = None
    for cap in _model["business"]["capabilities"]:
        if cap["type"] != current_type:
            current_type = cap["type"]
            out.append(f"## {current_type.capitalize()} capabilities\n")
        out.append(f'### {cap["number"]} {cap["name"]} {{#{cap["id"].lower()}}}\n')
        out.append(f'{cap["description"]}\n')
        out.append('<div class="grid" markdown>\n')
        out.append('<div markdown>\n\n**Outcomes**\n')
        out.extend(f"- {o}" for o in cap.get("outcomes", []))
        out.append("\n**Level 2 capabilities** <small>(draft)</small>\n")
        out.extend(f"- {l2}" for l2 in cap.get("level2", []))
        out.append("\n</div>\n<div markdown>\n\n**Enabled by technology capabilities**\n")
        for ref in cap.get("technology", []):
            t = tech[ref]
            out.append(
                f'- [{ref} {t["name"]}]({url_to(TECHNOLOGY_PAGE, ref.lower())}) '
                f'{_status_badge(t["status"])}'
            )
        out.append("\n</div>\n</div>\n")
    return "\n".join(out) + "\n"


def _technology_summary(url_to, md_to=None) -> str:
    counts = Counter(c["status"] for c in _model["technology"]["capabilities"])
    cards = "".join(
        f'<div class="cap-count cap-count--{s}"><span class="cap-count__n">{counts.get(s, 0)}</span>'
        f'<span class="cap-count__label">{label}</span></div>'
        for s, label in STATUS_LABELS.items()
    )
    return f'<div class="cap-counts">{cards}</div>\n'


def _technology_catalogue(_url_to, url_to) -> str:
    bus = _model["bus_by_id"]
    out = []
    for domain in _model["technology"]["domains"]:
        out.append(f'## {domain["name"]}\n\n{domain["description"]}\n')
        for cap in (c for c in _model["technology"]["capabilities"] if c["domain"] == domain["id"]):
            out.append(f'### {cap["id"]} {cap["name"]} {{#{cap["id"].lower()}}}\n')
            out.append(f'{_status_badge(cap["status"])} {cap["description"]}\n')
            options = cap.get("options", [])
            if options:
                out.append("**Use first**\n")
                for opt in options:
                    if opt.get("url"):
                        out.append(f'- [{opt["name"]}]({url_to(opt["url"])})')
                    else:
                        out.append(f'- {opt["name"]}')
                out.append("")
            else:
                out.append(
                    "**No Defra-wide answer yet.** If you need this capability, "
                    f"[talk to the Technical Design Authority]({url_to('governance/tda.md')}) "
                    "so we solve it once.\n"
                )
            if cap.get("guardrail"):
                out.append(f'**Guardrails:** [{_page_title(cap["guardrail"])}]({url_to(cap["guardrail"])})\n')
            supported = ", ".join(
                f'[{bus[b]["number"]} {bus[b]["name"]}]({url_to(BUSINESS_PAGE, b.lower())})'
                for b in _model["supports"][cap["id"]]
            )
            out.append(f"**Supports:** {supported}\n")
    return "\n".join(out) + "\n"


def _page_title(src_path: str) -> str:
    name = os.path.splitext(os.path.basename(src_path))[0]
    return name.replace("-", " ").capitalize().replace("Apis", "APIs").replace("Ai", "AI")


def _matrix(url_to, md_to=None) -> str:
    domains = _model["technology"]["domains"]
    techs = _model["technology"]["capabilities"]
    head_domains = "".join(
        f'<th scope="colgroup" colspan="{sum(1 for t in techs if t["domain"] == d["id"])}" '
        f'class="cap-matrix__domain">{e(d["name"])}</th>'
        for d in domains
    )
    ordered = [t for d in domains for t in techs if t["domain"] == d["id"]]
    head_caps = "".join(
        f'<th scope="col" class="cap-matrix__tech cap-matrix__tech--{t["status"]}">'
        f'<a href="{url_to(TECHNOLOGY_PAGE, t["id"].lower())}" title="{e(t["name"])}">'
        f'<span>{e(t["name"])}</span></a></th>'
        for t in ordered
    )
    rows = []
    for cap in _model["business"]["capabilities"]:
        refs = set(cap.get("technology", []))
        cells = "".join(
            f'<td class="cap-matrix__hit" title="{e(cap["name"])} uses {e(t["name"])}">'
            '<span aria-hidden="true">●</span><span class="visually-hidden">Yes</span></td>'
            if t["id"] in refs
            else '<td><span class="visually-hidden">No</span></td>'
            for t in ordered
        )
        rows.append(
            f'<tr><th scope="row"><a href="{url_to(BUSINESS_PAGE, cap["id"].lower())}">'
            f'<span class="cap-matrix__num">{e(cap["number"])}</span> {e(cap["name"])}</a></th>{cells}</tr>'
        )
    reuse = "".join(
        f'<td class="cap-matrix__total">{len(_model["supports"][t["id"]])}</td>' for t in ordered
    )
    rows.append(f'<tr class="cap-matrix__totals"><th scope="row">Business capabilities supported</th>{reuse}</tr>')
    return (
        '<div class="cap-matrix-wrapper" tabindex="0" role="region" aria-label="Capability mapping matrix">\n'
        '<table class="cap-matrix">\n'
        f'<thead><tr><td rowspan="2"></td>{head_domains}</tr><tr>{head_caps}</tr></thead>\n'
        f'<tbody>{"".join(rows)}</tbody>\n'
        "</table>\n</div>\n"
    )
