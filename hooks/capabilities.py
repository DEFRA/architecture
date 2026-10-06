"""MkDocs hook that renders the Defra capability handrail from YAML.

The business and technology capability models live in ``capabilities/*.yaml``
so they can be reviewed in pull requests, reused by other tools and rendered
consistently. The technology model is aligned to Technology Business
Management (TBM): level 1 areas, each with level 2 capabilities, some of which
list the needs teams commonly have and the options to use first. This hook:

* validates the models when the site builds (unknown or duplicate ids, missing
  guardrail pages and broken references fail the build);
* replaces ``<!-- capabilities:... -->`` markers in pages with generated
  content; and
* publishes the combined model as ``capabilities.json`` alongside the site.

Markers:

    <!-- capabilities:business-map -->         the one-page business capability map
    <!-- capabilities:attributes -->           what makes a good capability
    <!-- capabilities:business-detail -->      level 1 and draft level 2 detail
    <!-- capabilities:technology-summary -->   counts of areas, capabilities and needs
    <!-- capabilities:technology-catalogue --> what to use, by level 1 and level 2
    <!-- capabilities:matrix -->               business x technology heatmap
    <!-- capabilities:stack -->                level 1 and level 2 capability map
"""

from __future__ import annotations

import html
import json
import os
import posixpath

import yaml
from mkdocs.exceptions import PluginError
from mkdocs.utils import get_relative_url

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUSINESS_FILE = os.path.join(ROOT, "capabilities", "business-capabilities.yaml")
TECHNOLOGY_FILE = os.path.join(ROOT, "capabilities", "technology-capabilities.yaml")

BUSINESS_PAGE = "handrail/business-capabilities.md"
TECHNOLOGY_PAGE = "handrail/technology-capabilities.md"

_model: dict = {}


def _load(path: str) -> dict:
    with open(path, encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def technology_ids(technology: dict) -> dict[str, dict]:
    """Every level 1 area and level 2 capability by id, each with its ``area`` (level 1 id)."""
    found: dict[str, dict] = {}
    for area in technology["domains"]:
        found[area["id"]] = {**area, "area": area["id"], "level": 1}
        for l2 in area.get("level2", []):
            found[l2["id"]] = {**l2, "area": area["id"], "level": 2}
    return found


def validate(business: dict, technology: dict, docs_dir: str) -> list[str]:
    """Return a list of problems with the capability models."""
    errors: list[str] = []
    ids = [a["id"] for a in technology["domains"]] + [
        l2["id"] for a in technology["domains"] for l2 in a.get("level2", [])
    ]
    for dup in sorted({i for i in ids if ids.count(i) > 1}):
        errors.append(f"duplicate technology capability id {dup}")
    known = set(ids)

    for cap in technology_ids(technology).values():
        if not cap.get("name"):
            errors.append(f"{cap['id']} has no name")
        targets = list(cap.get("guardrails", []))
        for need in cap.get("needs", []):
            if not need.get("name") or not need.get("description"):
                errors.append(f"{cap['id']} has a need without a name or description")
            targets += [o.get("url") for o in need.get("options", [])]
        for target in targets:
            if target and not target.startswith("http"):
                if not os.path.exists(os.path.join(docs_dir, target.split("#")[0])):
                    errors.append(f"{cap['id']} links to missing page {target}")

    bus_ids = [c["id"] for c in business["capabilities"]]
    for dup in {i for i in bus_ids if bus_ids.count(i) > 1}:
        errors.append(f"duplicate business capability id {dup}")

    for cap in business["capabilities"]:
        if cap.get("type") not in ("core", "supporting"):
            errors.append(f"{cap['id']} has unknown type {cap.get('type')!r}")
        for ref in cap.get("technology", []):
            if ref not in known:
                errors.append(f"{cap['id']} references unknown technology capability {ref}")

    return errors


# --- MkDocs events -----------------------------------------------------------


def on_config(config):
    business = _load(BUSINESS_FILE)
    technology = _load(TECHNOLOGY_FILE)
    errors = validate(business, technology, config["docs_dir"])
    if errors:
        raise PluginError("Capability model is invalid:\n  - " + "\n  - ".join(errors))

    tech_by_id = technology_ids(technology)
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
        "stack": _stack,
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
        "technology_capabilities": _model["technology"]["domains"],
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
    rows = "\n".join(f"| **{a['name']}** | {a['description']} |" for a in _model["business"]["attributes"])
    return "| Attribute | What it means |\n| --- | --- |\n" + rows + "\n"


def _tech_name(ref: str) -> str:
    cap = _model["tech_by_id"][ref]
    if cap["level"] == 1:
        return f"{cap['name']} (all)"
    return f"{cap['name']} ({_model['tech_by_id'][cap['area']]['name']})"


def _business_detail(_url_to, url_to) -> str:
    out = []
    current_type = None
    for cap in _model["business"]["capabilities"]:
        if cap["type"] != current_type:
            current_type = cap["type"]
            out.append(f"## {current_type.capitalize()} capabilities\n")
        # The id is in the heading so searching "BC05" finds this section first.
        out.append(f"### {cap['number']} {cap['name']} ({cap['id']}) {{#{cap['id'].lower()}}}\n")
        out.append(f"{cap['description']}\n")
        out.append('<div class="grid" markdown>\n')
        out.append("<div markdown>\n\n**Outcomes**\n")
        out.extend(f"- {o}" for o in cap.get("outcomes", []))
        out.append("\n**Level 2 capabilities** <small>(draft)</small>\n")
        out.extend(f"- {l2}" for l2 in cap.get("level2", []))
        out.append("\n</div>\n<div markdown>\n\n**Enabled by technology capabilities**\n")
        for ref in cap.get("technology", []):
            out.append(f"- [{_tech_name(ref)}]({url_to(TECHNOLOGY_PAGE, ref)})")
        out.append("\n</div>\n</div>\n")
    return "\n".join(out) + "\n"


def _needs_list(cap: dict) -> str:
    items = "".join(
        f"<li>{e(n['name'])}{'' if n.get('options') else ' <em>(no Defra-wide answer)</em>'}</li>"
        for n in cap.get("needs", [])
    )
    return f'<ul class="tstack__needs">{items}</ul>' if items else ""


def _stack(url_to, md_to=None) -> str:
    """The capability map: one row per level 1 area, with a box per level 2 capability.

    Boxes with Defra guidance list its needs and link to what to use. Areas and
    capabilities are in the order of technology-capabilities.yaml.
    """
    rows = []
    for area in _model["technology"]["domains"]:
        code = f"<span>{e(area['code'])}</span>" if area.get("code") else ""
        across = _needs_list(area)
        boxes = []
        for l2 in area.get("level2", []):
            name = e(l2["name"])
            if l2.get("needs"):
                name = f'<a href="{url_to(TECHNOLOGY_PAGE, l2["id"])}">{name}</a>'
            cls = "tstack__l2 tstack__l2--guided" if l2.get("needs") else "tstack__l2"
            boxes.append(f'<li class="{cls}"><span class="tstack__l2name">{name}</span>{_needs_list(l2)}</li>')
        rows.append(
            f'<div class="tstack__layer"><div class="tstack__label"><strong>'
            f'<a href="{url_to(TECHNOLOGY_PAGE, area["id"])}">{e(area["name"])}</a></strong>{code}</div>'
            f'<div>{across}<ul class="tstack__l2s">{"".join(boxes)}</ul></div></div>'
        )
    return f'<div class="tstack" role="group" aria-label="Defra technology capability map">{"".join(rows)}</div>\n'


def _technology_summary(url_to, md_to=None) -> str:
    caps = list(_model["tech_by_id"].values())
    needs = [n for c in caps for n in c.get("needs", [])]
    counts = [
        (sum(1 for c in caps if c["level"] == 1), "level 1 areas"),
        (sum(1 for c in caps if c["level"] == 2), "level 2 capabilities"),
        (sum(1 for n in needs if n.get("options")), "needs with an option to use first"),
        (sum(1 for n in needs if not n.get("options")), "needs with no Defra-wide answer yet"),
    ]
    cards = "".join(
        f'<div class="cap-count"><span class="cap-count__n">{n}</span>'
        f'<span class="cap-count__label">{label}</span></div>'
        for n, label in counts
    )
    return f'<div class="cap-counts">{cards}</div>\n'


def _technology_catalogue(_url_to, url_to) -> str:
    out = []
    for area in _model["technology"]["domains"]:
        out.append(f"## {area['name']} {{#{area['id']}}}\n")
        if area.get("needs"):
            out.extend(_guidance(area, url_to))
        empty = []
        for l2 in area.get("level2", []):
            if not l2.get("needs"):
                empty.append(l2["name"])
                continue
            out.append(f"### {l2['name']} {{#{l2['id']}}}\n")
            out.extend(_guidance(l2, url_to))
        if empty:
            out.append(
                f"**Other level 2 capabilities in this area:** {', '.join(empty)}. "
                "There is no Defra-specific guidance for these yet.\n"
            )
    return "\n".join(out) + "\n"


def _guidance(cap: dict, url_to) -> list[str]:
    bus = _model["bus_by_id"]
    rows = ["| Need | Use first |", "| --- | --- |"]
    for need in cap["needs"]:
        options = need.get("options", [])
        if options:
            # One block per option, tall enough to be an easy touch target (WCAG 2.2 target size).
            use = "".join(
                f'<span class="cap-option">{f"[{o['name']}]({url_to(o['url'])})" if o.get("url") else o["name"]}</span>'
                for o in options
            )
        else:
            use = (
                "No Defra-wide answer yet. "
                f"[Talk to the Technical Design Authority]({url_to('governance/tda.md')}) so we solve it once."
            )
        rows.append(f"| **{need['name']}**<br>{need['description']} | {use} |")
    out = ["\n".join(rows) + "\n"]
    if cap.get("guardrails"):
        links = ", ".join(f"[{_page_title(g)}]({url_to(g)})" for g in cap["guardrails"])
        out.append(f"**Guardrails:** {links}\n")
    supported = ", ".join(
        f"[{bus[b]['number']} {bus[b]['name']}]({url_to(BUSINESS_PAGE, b.lower())})"
        for b in _model["supports"][cap["id"]]
    )
    if supported:
        out.append(f"**Supports business capabilities:** {supported}\n")
    return out


def _page_title(src_path: str) -> str:
    name = os.path.splitext(os.path.basename(src_path))[0]
    return name.replace("-", " ").capitalize().replace("Apis", "APIs").replace("Ai", "AI")


def _matrix(url_to, md_to=None) -> str:
    """Business capabilities against the technology capabilities they use, grouped by level 1 area."""
    used = {ref for c in _model["business"]["capabilities"] for ref in c.get("technology", [])}
    columns = []
    for area in _model["technology"]["domains"]:
        cols = [area] if area["id"] in used else []
        cols += [l2 for l2 in area.get("level2", []) if l2["id"] in used]
        if cols:
            columns.append((area, cols))
    head_areas = "".join(
        f'<th scope="colgroup" colspan="{len(cols)}" class="cap-matrix__domain">{e(a["name"])}</th>'
        for a, cols in columns
    )
    ordered = [c for _, cols in columns for c in cols]
    areas = {a["id"] for a, _ in columns}

    def label(t: dict) -> str:
        return f"All of {t['name']}" if t["id"] in areas else t["name"]

    head_caps = "".join(
        f'<th scope="col" class="cap-matrix__tech">'
        f'<a href="{url_to(TECHNOLOGY_PAGE, t["id"])}" title="{e(t["name"])}">'
        f"<span>{e(label(t))}</span></a></th>"
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
    reuse = "".join(f'<td class="cap-matrix__total">{len(_model["supports"][t["id"]])}</td>' for t in ordered)
    rows.append(f'<tr class="cap-matrix__totals"><th scope="row">Business capabilities supported</th>{reuse}</tr>')
    return (
        '<div class="cap-matrix-wrapper" tabindex="0" role="region" aria-label="Capability mapping matrix">\n'
        '<table class="cap-matrix">\n'
        f'<thead><tr><td rowspan="2"></td>{head_areas}</tr><tr>{head_caps}</tr></thead>\n'
        f"<tbody>{''.join(rows)}</tbody>\n"
        "</table>\n</div>\n"
    )
