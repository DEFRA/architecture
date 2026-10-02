"""MkDocs hook that builds the "Deliver a service" pages.

The lifecycle lives in ``delivery/lifecycle.yaml`` and the platforms in
``delivery/platforms.yaml``. Which guardrails apply in discovery, alpha, beta
and live comes from each guardrail's ``phases`` metadata, so the phase pages,
the checklists and the guardrail library always agree. This hook:

* validates the data - unique ids, known artefacts, guardrail ids that exist
  and pages that exist;
* replaces these markers with generated content:

      <!-- deliver:phase alpha -->       guardrails, artefacts, governance and evidence pack
      <!-- deliver:checklist alpha -->   printable assessment evidence checklist
      <!-- deliver:journey -->           overview of every phase
      <!-- deliver:platforms -->         getting onto Defra platforms

* writes a "To be confirmed" box for every platform fact still marked ``tbc``,
  so it is listed on the open questions page.
"""

from __future__ import annotations

import html
import importlib.util
import os
import posixpath
import re

import yaml
from mkdocs.exceptions import PluginError
from mkdocs.utils import get_relative_url

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIFECYCLE = os.path.join(ROOT, "delivery", "lifecycle.yaml")
PLATFORMS = os.path.join(ROOT, "delivery", "platforms.yaml")
ROLES = os.path.join(ROOT, "delivery", "roles.yaml")

MARKER = re.compile(r"<!-- deliver:(phase|checklist|journey|platforms|roles|role)(?: ([a-z-]+))? -->")
DOCS_LINK = re.compile(r"\]\((?!https?://|#)([^)]+)\)")
PHASES = ("discovery", "alpha", "beta", "live")
LEVEL_ORDER = ("must", "should", "could")
LEVEL_NAMES = {"must": "Must", "should": "Should", "could": "Could"}
PLATFORM_FIELDS = {
    "request": "How to request access",
    "lead_time": "Lead time",
    "support": "Support",
    "docs": "Documentation",
}

_data: dict = {}


def _load_guardrails_hook():
    path = os.path.join(ROOT, "hooks", "guardrails.py")
    spec = importlib.util.spec_from_file_location("_guardrails_for_delivery", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _load_patterns(docs_dir: str, by_id: dict) -> list[dict]:
    path = os.path.join(ROOT, "hooks", "patterns.py")
    spec = importlib.util.spec_from_file_location("_patterns_for_delivery", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.parse(docs_dir, by_id)


def load(docs_dir: str) -> dict:
    """Read and validate the lifecycle, platforms and guardrails."""
    with open(LIFECYCLE, encoding="utf-8") as handle:
        lifecycle = yaml.safe_load(handle)
    with open(PLATFORMS, encoding="utf-8") as handle:
        platforms = yaml.safe_load(handle)["platforms"]
    with open(ROLES, encoding="utf-8") as handle:
        roles = yaml.safe_load(handle)["roles"]
    hook = _load_guardrails_hook()
    guardrails = [g for g in hook.parse(docs_dir) if g["level"] != "principle"]
    by_id = {g["id"]: g for g in guardrails}
    artefacts = {a["id"]: a for a in lifecycle["artefacts"]}

    errors: list[str] = []

    def check_page(where: str, target: str):
        if target and not target.startswith("http") and target != "tbc":
            if not os.path.exists(os.path.join(docs_dir, target.split("#")[0])):
                errors.append(f"{where} links to missing page {target}")

    for a in lifecycle["artefacts"]:
        check_page(f"artefact {a['id']}", a.get("guide"))
        check_page(f"artefact {a['id']}", a.get("template"))
        for gid in a.get("guardrails", []):
            if gid not in by_id:
                errors.append(f"artefact {a['id']} refers to unknown guardrail {gid}")

    ids = [p["id"] for p in lifecycle["phases"]]
    errors += [f"duplicate phase id {i}" for i in sorted({i for i in ids if ids.count(i) > 1})]
    for p in lifecycle["phases"]:
        check_page(f"phase {p['id']}", p["page"])
        for aid in p.get("artefacts", {}):
            if aid not in artefacts:
                errors.append(f"phase {p['id']} refers to unknown artefact {aid}")
        if p["id"] in PHASES:
            if "guardrails" in p:
                errors.append(f"phase {p['id']}: set guardrails through each guardrail's 'phases' metadata instead")
            p["guardrails"] = [g["id"] for g in guardrails if p["id"] in g["phases"]]
        else:
            for gid in p.get("guardrails", []):
                if gid not in by_id:
                    errors.append(f"phase {p['id']} refers to unknown guardrail {gid}")
        for line in p.get("governance", []):
            for target in DOCS_LINK.findall(line):
                check_page(f"phase {p['id']}", target)

    platform_ids = [p["id"] for p in platforms]
    errors += [f"duplicate platform id {i}" for i in sorted({i for i in platform_ids if platform_ids.count(i) > 1})]
    for p in platforms:
        for field in ("name", "gives", *PLATFORM_FIELDS):
            if not p.get(field):
                errors.append(f"platform {p['id']} is missing '{field}' - use 'tbc' if it is not known")
        for target in DOCS_LINK.findall(" ".join(str(p.get(f, "")) for f in ("gives", "request", "support"))):
            check_page(f"platform {p['id']}", target)

    role_ids = [r["id"] for r in roles]
    errors += [f"duplicate role id {i}" for i in sorted({i for i in role_ids if role_ids.count(i) > 1})]
    for r in roles:
        for field in ("name", "summary", "touchpoints"):
            if not r.get(field):
                errors.append(f"role {r['id']} is missing '{field}'")
        if not os.path.exists(os.path.join(docs_dir, "deliver", "roles", f"{r['id']}.md")):
            errors.append(f"role {r['id']} has no page at deliver/roles/{r['id']}.md")
        for line in r.get("touchpoints", []):
            for target in DOCS_LINK.findall(line):
                check_page(f"role {r['id']}", target)

    if errors:
        raise PluginError("Delivery lifecycle data is invalid:\n  - " + "\n  - ".join(errors))
    return {
        "phases": lifecycle["phases"],
        "artefacts": artefacts,
        "platforms": platforms,
        "guardrails": by_id,
        "evidence_for": hook.evidence_for,
        "roles": roles,
        "patterns": _load_patterns(docs_dir, {g["id"]: g for g in hook.parse(docs_dir)}),
    }


# --- MkDocs events -----------------------------------------------------------


def on_config(config):
    _data.clear()
    _data.update(load(config["docs_dir"]))
    return config


def on_page_markdown(markdown, page, config, files):
    if "<!-- deliver:" not in markdown:
        return markdown
    src = page.file.src_uri

    def link(target: str) -> str:
        if target.startswith("http"):
            return target
        path, _, anchor = target.partition("#")
        rel = posixpath.relpath(path, posixpath.dirname(src))
        return rel + (f"#{anchor}" if anchor else "")

    def url(target: str) -> str:
        """The built URL of a docs page, for links inside raw HTML."""
        path, _, anchor = target.partition("#")
        file = files.get_file_from_path(path)
        return get_relative_url(file.url, page.url) + (f"#{anchor}" if anchor else "")

    def relink(text: str) -> str:
        return DOCS_LINK.sub(lambda m: f"]({link(m.group(1))})", text)

    def render(match: re.Match) -> str:
        kind, arg = match.groups()
        if kind in ("phase", "checklist"):
            phase = next((p for p in _data["phases"] if p["id"] == arg), None)
            if not phase:
                raise PluginError(f"{src}: unknown phase '{arg}' in {match.group(0)}")
            if kind == "phase":
                return _phase(phase, link, relink)
            return _checklist(phase, link, url)
        if kind == "journey":
            return _journey(link)
        if kind == "roles":
            return _roles(link)
        if kind == "role":
            role = next((r for r in _data["roles"] if r["id"] == arg), None)
            if not role:
                raise PluginError(f"{src}: unknown role '{arg}' in {match.group(0)}")
            return _role(role, link, relink, url)
        return _platforms(link, relink)

    return MARKER.sub(render, markdown)


# --- Renderers ---------------------------------------------------------------


def _guardrail_link(g: dict, link) -> str:
    return f"[{g['id']}]({link(g['page'] + '#' + g['id'].lower())})"


def _by_level(phase: dict) -> dict[str, list[dict]]:
    found = [_data["guardrails"][gid] for gid in phase["guardrails"]]
    return {level: [g for g in found if g["level"] == level] for level in LEVEL_ORDER}


def _artefact_link(a: dict, link) -> str:
    return f"[{a['name']}]({link(a['guide'])})" if a.get("guide") else a["name"]


def _phase(phase: dict, link, relink) -> str:
    groups = _by_level(phase)
    out = ["## Guardrails that apply", ""]
    if phase["id"] in PHASES:
        out.append(
            f"These guardrails apply in {phase['name'].lower()}, taken from each guardrail's metadata. "
            "Meet every Must, or have an approved [exception]"
            f"({link('governance/exceptions.md')}). Depart from a Should only with a recorded reason."
        )
    else:
        out.append(
            f"These guardrails need particular attention when you {phase['name'][0].lower() + phase['name'][1:]}. "
            "The guardrails for the phase the service is in still apply."
        )
    out.append("")
    for level in LEVEL_ORDER:
        items = groups[level]
        if not items:
            continue
        rows = ["| Guardrail | What to show |", "| --- | --- |"]
        rows += [
            f"| {_guardrail_link(g, link)} {g['title']} | {_data['evidence_for'](g, phase['id']) or '-'} |"
            for g in items
        ]
        if level == "must":
            out += [f"### {LEVEL_NAMES[level]} ({len(items)})", "", *rows, ""]
        else:
            out += [f'??? note "{LEVEL_NAMES[level]} ({len(items)})"', ""]
            out += ["    " + r for r in rows] + [""]

    out += ["## Architecture artefacts", "", "| Artefact | What to do in this phase |", "| --- | --- |"]
    for aid, action in phase.get("artefacts", {}).items():
        a = _data["artefacts"][aid]
        template = f" ([template]({link(a['template'])}))" if a.get("template") else ""
        out.append(f"| {_artefact_link(a, link)}{template} | {action} |")
    out.append("")

    out += ["## Governance touchpoints", ""]
    out += [f"- {relink(line)}" for line in phase.get("governance", [])]
    out.append("")

    out += ["## Evidence pack", ""]
    out.append(
        "Bring these together once and reuse them for your solution design authority, service assessment, "
        "spend control and security assurance:"
    )
    out.append("")
    out += [f"- {_data['artefacts'][aid]['name']}" for aid in phase.get("artefacts", {})]
    out.append(f"- evidence for each Must guardrail above ({len(groups['must'])})")
    out.append("")
    out.append(
        f"Use the [{phase['name'].lower()} evidence checklist]({link('deliver/checklists/' + phase['id'] + '.md')}) "
        "to gather and print it."
    )
    if phase.get("service_manual"):
        out += [
            "",
            f"For how the phase works and what assessors look for, see the GOV.UK Service Manual on "
            f"[{phase['name'].lower()}]({phase['service_manual']}) and the "
            f"[Defra Digital Service Manual](https://digital.defra.gov.uk/service-manual). "
            "This site covers the architecture evidence only.",
        ]
    return "\n".join(out) + "\n"


def _checklist(phase: dict, link, url) -> str:
    """A printable checklist with real, labelled checkboxes."""
    e = html.escape
    groups = _by_level(phase)
    counter = iter(range(1, 1000))

    def item(text: str) -> str:
        n = next(counter)
        return f'<li><input type="checkbox" id="ck-{n}"><label for="ck-{n}">{text}</label></li>'

    out = [
        '<p class="dl-print"><button type="button" class="md-button" data-print>Print this checklist</button></p>',
        "",
        "## Artefacts",
        "",
        '<ul class="dl-checklist">',
    ]
    for aid, action in phase.get("artefacts", {}).items():
        out.append(item(f"<strong>{e(_data['artefacts'][aid]['name'])}</strong> - {e(action)}"))
    out += ["</ul>", ""]
    for level in LEVEL_ORDER:
        if not groups[level]:
            continue
        out += [f"## {LEVEL_NAMES[level]} guardrails", "", '<ul class="dl-checklist">']
        for g in groups[level]:
            text = _data["evidence_for"](g, phase["id"])
            evidence = f" - {e(text)}" if text else ""
            href = url(g["page"] + "#" + g["id"].lower())
            out.append(item(f'<a href="{href}">{g["id"]}</a> <strong>{e(g["title"])}</strong>{evidence}'))
        out += ["</ul>", ""]
    out += [
        "## Sign-off",
        "",
        "| Detail | Answer |",
        "| --- | --- |",
        "| Service | |",
        "| Completed by | |",
        "| Date | |",
        "| Solution design authority | |",
        "| Exceptions or departures (guardrail ids) | |",
        "",
        f"Read more on the [{phase['name'].lower()} page]({link(phase['page'])}).",
    ]
    return "\n".join(out) + "\n"


def _journey(link) -> str:
    rows = ["| Phase | Guardrails | Must | Key artefacts | Checklist |", "| --- | ---: | ---: | --- | --- |"]
    for p in _data["phases"]:
        groups = _by_level(p)
        artefacts = ", ".join(_data["artefacts"][a]["name"] for a in list(p.get("artefacts", {}))[:4])
        rows.append(
            f"| [{p['name']}]({link(p['page'])}) | {len(p['guardrails'])} | {len(groups['must'])} | {artefacts} | "
            f"[Checklist]({link('deliver/checklists/' + p['id'] + '.md')}) |"
        )
    return "\n".join(rows) + "\n"


def _platforms(link, relink) -> str:
    out = []
    for p in _data["platforms"]:
        out += [f"## {p['name']} {{#{p['id']}}}", "", relink(p["gives"]), ""]
        rows = ["| Detail | What we know |", "| --- | --- |"]
        unknown = []
        for field, label in PLATFORM_FIELDS.items():
            value = str(p[field])
            if value == "tbc":
                unknown.append(label.lower())
                value = "To be confirmed"
            elif field == "docs":
                value = f"[{value}]({value})" + (f" - {p['docs_note']}" if p.get("docs_note") else "")
            else:
                value = relink(value)
            rows.append(f"| **{label}** | {value} |")
        if p.get("service_manual"):
            rows.append(f"| **Defra Digital Service Manual** | [{p['name']}]({p['service_manual']}) |")
        cap = p.get("capability")
        if cap:
            rows.append(
                f"| **Technology capability** | [{cap}]({link('handrail/technology-capabilities.md#' + cap.lower())}) |"
            )
        out += rows + [""]
        if unknown:
            listed = ", ".join(unknown[:-1]) + (" and " if len(unknown) > 1 else "") + unknown[-1]
            out += ['!!! warning "To be confirmed"', f"    **TODO:** {p['name']}: {listed}.", ""]
    return "\n".join(out) + "\n"


def _roles(link) -> str:
    rows = ["| Role | Guardrails you lead | Must |", "| --- | ---: | ---: |"]
    for r in _data["roles"]:
        led = [g for g in _data["guardrails"].values() if r["id"] in g["lead_roles"]]
        musts = sum(1 for g in led if g["level"] == "must")
        rows.append(f"| [{r['name']}]({link('deliver/roles/' + r['id'] + '.md')}) | {len(led)} | {musts} |")
    return "\n".join(rows) + "\n"


def _role(role: dict, link, relink, url) -> str:
    led = {gid: g for gid, g in _data["guardrails"].items() if role["id"] in g["lead_roles"]}
    library = url("guardrails/library.md").split("#")[0] + "#role=" + role["id"]
    out = [
        relink(role["summary"]),
        "",
        f"You lead **{len(led)} guardrails**, often with other roles. Leading means making sure the team meets them "
        "and can show it, not doing all the work. "
        f'See them all in the <a href="{library}">guardrail library, filtered to your role</a>.',
        "",
        "## Your guardrails, phase by phase",
        "",
    ]
    for phase in _data["phases"]:
        mine = [led[gid] for gid in phase["guardrails"] if gid in led]
        if not mine:
            continue
        out += [f"### {phase['name']}", ""]
        out += ["| Guardrail | Level | What to show |", "| --- | --- | --- |"]
        for level in LEVEL_ORDER:
            for g in (g for g in mine if g["level"] == level):
                shown = _data["evidence_for"](g, phase["id"]) or "-"
                out.append(f"| {_guardrail_link(g, link)} {g['title']} | {LEVEL_NAMES[level]} | {shown} |")
        out += ["", f"More on the [{phase['name'].lower()} page]({link(phase['page'])}).", ""]

    patterns = [p for p in _data["patterns"] if set(p["guardrails"]) & set(led)]
    out += ["## Patterns that help", ""]
    if patterns:
        out += [f"- [{p['title']}]({link(p['src'])}) - {p['summary']}" for p in patterns]
    else:
        out.append("No patterns yet. See the [patterns](" + link("patterns/index.md") + ") section.")
    out += ["", "## Working with architects", ""]
    out += [f"- {relink(line)}" for line in role["touchpoints"]]
    out.append("")
    return "\n".join(out) + "\n"
