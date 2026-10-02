"""Content checks that run before the site is built.

These catch mistakes a reviewer could miss: broken references between the
capability, guardrail and NFR data, and diagrams without text alternatives.
Run with:  pytest
"""

import glob
import importlib.util
import os
import re

import pytest
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")


def load_hook(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, "hooks", f"{name}.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_yaml(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as handle:
        return yaml.safe_load(handle)


capabilities = load_hook("capabilities")
guardrails = load_hook("guardrails")
nfrs = load_hook("nfrs")
traceability = load_hook("traceability")
delivery = load_hook("delivery")
patterns = load_hook("patterns")
releases = load_hook("releases")
open_questions = load_hook("open_questions")
registers = load_hook("registers")


# --- Capability model --------------------------------------------------------


def test_capability_model_is_valid():
    business = load_yaml("capabilities", "business-capabilities.yaml")
    technology = load_yaml("capabilities", "technology-capabilities.yaml")
    assert capabilities.validate(business, technology, DOCS) == []


def test_capability_model_catches_unknown_reference():
    business = load_yaml("capabilities", "business-capabilities.yaml")
    technology = load_yaml("capabilities", "technology-capabilities.yaml")
    business["capabilities"][0]["technology"].append("TC99")
    assert any("TC99" in e for e in capabilities.validate(business, technology, DOCS))


def test_every_technology_capability_has_a_government_model_level():
    technology = load_yaml("capabilities", "technology-capabilities.yaml")
    del technology["capabilities"][0]["government_model"]
    business = load_yaml("capabilities", "business-capabilities.yaml")
    assert any("government_model" in e for e in capabilities.validate(business, technology, DOCS))


# --- Guardrails ----------------------------------------------------------------


def test_guardrails_parse():
    found = guardrails.parse(DOCS)
    levels = {g["level"] for g in found}
    assert levels == {"principle", "must", "should", "could"}
    assert len([g for g in found if g["level"] == "principle"]) == 8


def test_principles_live_in_the_principles_section():
    pages = {g["page"] for g in guardrails.parse(DOCS) if g["level"] == "principle"}
    assert pages == {"principles/architecture-principles.md"}


def test_doctrine_has_seven_non_negotiables():
    with open(os.path.join(DOCS, "principles", "doctrine.md"), encoding="utf-8") as handle:
        assert len(re.findall(r"^## \d+\. .+\{#ddts-0\d\}$", handle.read(), re.M)) == 7


def test_every_guardrail_has_metadata():
    for g in guardrails.parse(DOCS):
        assert g["status"] in guardrails.STATUSES, g["id"]
        assert g["phases"] and set(g["phases"]) <= set(guardrails.PHASES), g["id"]
        assert g["owner"] and g["automated_check"] and g["last_reviewed"], g["id"]
        if g["level"] == "must":
            assert g["evidence"], g["id"]


def test_guardrails_apply_doctrine():
    for g in guardrails.parse(DOCS):
        assert g["doctrine"], f"{g['id']} does not trace to the DDTS doctrine"


def test_adrs_have_their_own_guardrail():
    with open(os.path.join(DOCS, "guardrails", "index.md"), encoding="utf-8") as handle:
        text = handle.read()
    assert "recorded as ADRs (`GR-DEV-09`)" in text
    assert "ten principles" not in text


def test_supplier_ai_guardrail_is_a_draft_should():
    g = next(g for g in guardrails.parse(DOCS) if g["id"] == "GR-AI-07")
    assert (g["level"], g["status"], g["since_version"]) == ("should", "draft", "0.2.0")


def test_musts_are_kept_few():
    """ADR 0004: Musts only where law, policy, baseline security or doctrine require them."""
    found = [g for g in guardrails.parse(DOCS) if g["level"] != "principle"]
    musts = [g for g in found if g["level"] == "must"]
    assert len(musts) <= 30, f"{len(musts)} Musts - see docs/adr/0004-musts-only-where-required.md"


GOOD_PAGE = """---
applicability: tbc
guardrail_defaults:
  lead_roles: [developer]
  status: draft
  owner: Architecture team
  automated_check: manual
  last_reviewed: 2026-10-01
  since_version: 0.1.0
guardrails:
  GR-EXM-01: {{{meta}}}
---
# Example

## GR-EXM-01 Example {{#gr-exm-01}}

<span class="rfc rfc--must">Must</span> Text.
"""


def _example(tmp_path, meta):
    folder = tmp_path / "guardrails"
    folder.mkdir()
    (folder / "example.md").write_text(GOOD_PAGE.format(meta=meta))
    return guardrails.parse(str(tmp_path))


def test_valid_guardrail_metadata_parses(tmp_path):
    meta = "phases: [alpha], evidence: A thing, evidence_by_phase: {alpha: Designed}, tcop_points: [5]"
    [g] = _example(tmp_path, meta)
    assert g["phases"] == ["alpha"] and g["tcop_points"] == [5] and g["status"] == "draft"


def test_must_without_evidence_fails(tmp_path):
    with pytest.raises(Exception, match="is a Must but has no 'evidence'"):
        _example(tmp_path, "phases: [alpha]")


def test_unknown_phase_status_and_points_fail(tmp_path):
    with pytest.raises(Exception) as err:
        _example(tmp_path, "phases: [gamma], evidence: x, status: agreed, service_standard_points: [15]")
    assert "unknown phase 'gamma'" in str(err.value)
    assert "status 'agreed'" in str(err.value)
    assert "Service Standard point 15" in str(err.value)


def test_must_needs_evidence_for_each_of_its_phases(tmp_path):
    with pytest.raises(Exception, match="is a Must in beta but has no evidence_by_phase for beta"):
        _example(tmp_path, "phases: [alpha, beta], evidence: x, evidence_by_phase: {alpha: y}")


def test_evidence_by_phase_checks_its_phases(tmp_path):
    with pytest.raises(Exception) as err:
        _example(tmp_path, "phases: [alpha], evidence: x, evidence_by_phase: {alpha: y, gamma: z, live: w}")
    assert "unknown phase 'gamma'" in str(err.value)
    assert "has evidence for live but does not apply in live" in str(err.value)


def test_evidence_by_phase_parses_and_falls_back(tmp_path):
    meta = "phases: [alpha], evidence: general, evidence_by_phase: {alpha: designed, retire: removed}"
    [g] = _example(tmp_path, meta)
    assert g["evidence_by_phase"] == {"alpha": "designed", "retire": "removed"}
    assert guardrails.evidence_for(g, "alpha") == "designed"
    assert guardrails.evidence_for(g, "significant-change") == "general"


def test_lead_roles_must_be_known_roles(tmp_path):
    with pytest.raises(Exception, match="unknown lead role 'architect'"):
        _example(tmp_path, "phases: [alpha], evidence: x, evidence_by_phase: {alpha: y}, lead_roles: [architect]")


def test_every_guardrail_has_lead_roles():
    for g in guardrails.parse(DOCS):
        if g["level"] != "principle":
            assert g["lead_roles"], g["id"]
            assert set(g["lead_roles"]) <= set(guardrails.ROLES), g["id"]


@pytest.mark.parametrize(
    "gid, roles",
    [
        ("GR-FE-06", {"content-designer"}),
        ("GR-AI-04", {"content-designer", "interaction-designer"}),
        ("GR-DATA-04", {"service-designer"}),
        ("GR-FE-05", {"service-designer", "user-researcher"}),
        ("GR-AI-03", {"service-designer", "user-researcher"}),
    ],
)
def test_lead_roles_for_user_facing_guardrails(gid, roles):
    g = next(g for g in guardrails.parse(DOCS) if g["id"] == gid)
    assert set(g["lead_roles"]) == roles


def test_every_role_has_a_page_and_leads_something():
    data = delivery.load(DOCS)
    assert [r["id"] for r in data["roles"]] == list(guardrails.ROLES)
    for r in data["roles"]:
        assert any(r["id"] in g["lead_roles"] for g in data["guardrails"].values()), r["id"]


def test_deprecated_needs_a_replacement(tmp_path):
    with pytest.raises(Exception, match="deprecated but has no 'replaced_by'"):
        _example(tmp_path, "phases: [alpha], evidence: x, status: deprecated")


def test_guardrail_without_metadata_fails(tmp_path):
    folder = tmp_path / "guardrails"
    folder.mkdir()
    (folder / "example.md").write_text(
        '# Example\n\n## GR-EXM-01 Example {#gr-exm-01}\n\n<span class="rfc rfc--should">Should</span> Text.\n'
    )
    with pytest.raises(Exception, match="has no metadata"):
        guardrails.parse(str(tmp_path))


def test_guardrail_without_badge_fails(tmp_path):
    folder = tmp_path / "guardrails"
    folder.mkdir()
    (folder / "example.md").write_text("# Example\n\n## GR-EXM-01 No badge {#gr-exm-01}\n\nText.\n")
    with pytest.raises(Exception, match="no Principle/Must/Should/Could badge"):
        guardrails.parse(str(tmp_path))


def test_guardrail_ids_match_anchors(tmp_path):
    folder = tmp_path / "guardrails"
    folder.mkdir()
    (folder / "example.md").write_text(
        '# Example\n\n## GR-EXM-01 Wrong anchor {#gr-exm-02}\n\n<span class="rfc rfc--must">Must</span> Text.\n'
    )
    with pytest.raises(Exception, match="expected #gr-exm-01"):
        guardrails.parse(str(tmp_path))


# --- Doctrine -> principles -> guardrails ------------------------------------


def test_every_doctrine_and_guardrail_page_is_in_the_chain():
    chain = traceability.build(DOCS)
    assert len(chain["doctrines"]) == 7
    assert all(d["principles"] for d in chain["doctrines"])
    assert all(a["principles"] for a in chain["areas"])


def test_every_principle_applies_a_doctrine():
    chain = traceability.build(DOCS)
    assert all(chain["doctrines_for"][pid] for pid in chain["principles"])


def test_guardrail_page_without_principles_fails(tmp_path):
    import shutil

    shutil.copytree(DOCS, tmp_path / "docs")
    page = tmp_path / "docs" / "guardrails" / "data.md"
    page.write_text(re.sub(r"\A---\n.*?\n---\n", "", page.read_text(), flags=re.S))
    with pytest.raises(Exception, match="guardrails/data.md: add 'principles"):
        traceability.build(str(tmp_path / "docs"))


# --- NFRs ----------------------------------------------------------------------


def test_nfrs_are_valid():
    tiers = load_yaml("nfrs", "service-tiers.yaml")
    catalogue = load_yaml("nfrs", "catalogue.yaml")
    assert nfrs.validate(tiers, catalogue, nfrs.guardrail_pages(DOCS)) == []


def test_nfr_with_unknown_tier_and_guardrail_fails():
    tiers = load_yaml("nfrs", "service-tiers.yaml")
    catalogue = load_yaml("nfrs", "catalogue.yaml")
    req = catalogue["categories"][0]["requirements"][0]
    req["targets"]["T9"] = "x"
    req["guardrails"].append("GR-NOPE-01")
    errors = nfrs.validate(tiers, catalogue, nfrs.guardrail_pages(DOCS))
    assert any("unknown tier T9" in e for e in errors)
    assert any("GR-NOPE-01" in e for e in errors)


# --- Deliver a service ---------------------------------------------------------


def test_delivery_lifecycle_is_valid():
    data = delivery.load(DOCS)
    phases = {p["id"]: p for p in data["phases"]}
    assert list(phases) == ["discovery", "alpha", "beta", "live", "significant-change", "retire"]
    for pid in ("discovery", "alpha", "beta", "live"):
        assert phases[pid]["guardrails"], f"no guardrails apply in {pid}"
    for p in data["phases"]:
        assert os.path.exists(os.path.join(DOCS, "deliver", "checklists", f"{p['id']}.md")), p["id"]


def test_phase_guardrails_come_from_metadata():
    alpha = next(p for p in delivery.load(DOCS)["phases"] if p["id"] == "alpha")
    expected = [g["id"] for g in guardrails.parse(DOCS) if g["level"] != "principle" and "alpha" in g["phases"]]
    assert alpha["guardrails"] == expected


def test_delivery_with_unknown_guardrail_fails(tmp_path, monkeypatch):
    lifecycle = load_yaml("delivery", "lifecycle.yaml")
    lifecycle["phases"][-1]["guardrails"].append("GR-NOPE-01")
    path = tmp_path / "lifecycle.yaml"
    path.write_text(yaml.safe_dump(lifecycle))
    monkeypatch.setattr(delivery, "LIFECYCLE", str(path))
    with pytest.raises(Exception, match="unknown guardrail GR-NOPE-01"):
        delivery.load(DOCS)


def test_every_must_shown_in_a_phase_has_evidence_for_that_phase():
    """Phase pages and checklists show phase-specific evidence, so every Must needs it."""
    missing = []
    data = delivery.load(DOCS)
    for phase in data["phases"]:
        for gid in phase["guardrails"]:
            g = data["guardrails"][gid]
            if g["level"] == "must" and not g["evidence_by_phase"].get(phase["id"]):
                missing.append(f"{gid} in {phase['id']}")
    assert not missing, "Musts with no evidence for a phase they appear in: " + ", ".join(missing)


def test_every_platform_says_what_is_unknown():
    for platform in load_yaml("delivery", "platforms.yaml")["platforms"]:
        for field in ("gives", "request", "lead_time", "support", "docs"):
            assert platform.get(field), f"{platform['id']}: set {field}, or 'tbc' if it is not known"


def test_platform_service_manual_links_point_to_the_manual():
    """Platforms link to the Defra Digital Service Manual rather than repeat it."""
    for platform in load_yaml("delivery", "platforms.yaml")["platforms"]:
        url = platform.get("service_manual")
        if url:
            assert url.startswith("https://digital.defra.gov.uk/"), f"{platform['id']}: link a manual page"
        if platform.get("docs_note"):
            assert str(platform["docs"]).startswith("https://"), f"{platform['id']}: docs_note needs a docs link"


# --- Patterns ------------------------------------------------------------------


def test_patterns_are_valid():
    found = patterns.parse(DOCS, {g["id"]: g for g in guardrails.parse(DOCS)})
    assert len(found) >= 5
    assert {p["category"] for p in found} <= set(patterns.CATEGORIES)


def test_pattern_with_unknown_guardrail_fails(tmp_path):
    folder = tmp_path / "patterns"
    folder.mkdir()
    (folder / "bad.md").write_text(
        "---\npattern:\n  category: data\n  status: draft\n  summary: x\n  guardrails: [GR-NOPE-01]\n---\n"
        "# Bad\n\n<!-- patterns:guardrails -->\n<!-- patterns:sbd -->\n"
    )
    with pytest.raises(Exception, match="unknown guardrail GR-NOPE-01"):
        patterns.parse(str(tmp_path), {})


# --- Releases and registers -----------------------------------------------------


def test_changelog_is_valid():
    with open(os.path.join(ROOT, "CHANGELOG.md"), encoding="utf-8") as handle:
        sections = releases.parse(handle.read())
    assert releases.latest(sections)["version"]


def test_changelog_versions_must_be_newest_first():
    text = "## [Unreleased]\n\n## [0.1.0] - 2026-01-01\n\n## [0.2.0] - 2026-02-01\n"
    with pytest.raises(Exception, match="newest first"):
        releases.parse(text)


def test_registers_are_valid():
    found = {g["id"]: g for g in guardrails.parse(DOCS)}
    approvals = load_yaml("registers", "approvals.yaml")
    data = registers.load(DOCS, approvals, load_yaml("registers", "exceptions.yaml"), found)
    assert data["sections"]


def test_exception_needs_known_guardrail_and_expiry_after_approval():
    found = {g["id"]: g for g in guardrails.parse(DOCS)}
    bad = {
        "exceptions": [
            {
                "id": "EX-2026-001",
                "guardrail": "GR-NOPE-01",
                "service": "x",
                "owner": "y",
                "approved": "2026-06-01",
                "expiry": "2026-01-01",
            }
        ]
    }
    with pytest.raises(Exception) as err:
        registers.load(DOCS, {"sections": []}, bad, found)
    assert "unknown guardrail GR-NOPE-01" in str(err.value)
    assert "expiry must be after" in str(err.value)


def test_every_guardrail_page_says_who_it_applies_to():
    folder = os.path.join(DOCS, "guardrails")
    for name in os.listdir(folder):
        if name.endswith(".md") and name not in ("index.md", "library.md"):
            with open(os.path.join(folder, name), encoding="utf-8") as handle:
                assert "\napplicability:" in handle.read().split("\n---\n")[0], name


def test_open_questions_ignore_examples_in_code_blocks():
    class Page:
        class file:
            src_uri = "example.md"

    open_questions.on_config({})
    text = (
        '```markdown\n!!! warning "To be confirmed"\n    **TODO:** an example.\n```\n\n'
        '!!! warning "To be confirmed"\n    **TODO:** a real question.\n'
    )
    open_questions.on_page_markdown(text, Page, {}, None)
    found = [q["text"] for q in open_questions._found["example.md"]["questions"]]
    assert found == ["a real question."]


def test_area_names_keep_acronyms_mid_sentence():
    assert guardrails._sentence_case("APIs and integration") == "APIs and integration"
    assert guardrails._sentence_case("Data") == "data"


# --- Pages ---------------------------------------------------------------------


def test_working_with_architects_is_linked_from_home_and_deliver():
    assert os.path.exists(os.path.join(DOCS, "deliver", "working-with-architects.md"))
    with open(os.path.join(DOCS, "index.md"), encoding="utf-8") as handle:
        assert 'href="deliver/working-with-architects/"' in handle.read()
    with open(os.path.join(DOCS, "deliver", "index.md"), encoding="utf-8") as handle:
        assert "(working-with-architects.md)" in handle.read()


REPO_LINK = re.compile(r"https://github\.com/howellsr/architecture/(?:blob|tree)/main/([^)\s\"'#>]+)")


def test_links_to_files_in_this_repository_exist():
    """The link checker skips these links, because they 404 until a pull request is merged."""
    missing = []
    for path in glob.glob(os.path.join(DOCS, "**", "*.md"), recursive=True) + [os.path.join(ROOT, "README.md")]:
        with open(path, encoding="utf-8") as handle:
            for target in REPO_LINK.findall(handle.read()):
                if not os.path.exists(os.path.join(ROOT, target.rstrip("/"))):
                    missing.append(f"{os.path.relpath(path, ROOT)} -> {target}")
    assert not missing, "Links to files that do not exist: " + ", ".join(missing)


MERMAID = re.compile(r"```mermaid\n(.*?)```", re.S)


@pytest.mark.parametrize("path", sorted(glob.glob(os.path.join(DOCS, "**", "*.md"), recursive=True)))
def test_diagrams_have_text_alternatives(path):
    with open(path, encoding="utf-8") as handle:
        for diagram in MERMAID.findall(handle.read()):
            assert "accTitle:" in diagram and "accDescr:" in diagram, (
                f"{os.path.relpath(path, ROOT)}: add accTitle and accDescr to every mermaid diagram"
            )


# --- Contacts ------------------------------------------------------------------

# Email addresses confirmed by Defra. Add one here only with a source; anything
# not yet known goes in a "To be confirmed" box instead.
KNOWN_EMAILS = {
    "delivery.architecture@defra.gov.uk",  # Defra Digital Service Manual, architecture page
    "noreply@defra.gov.uk",  # holding address for alpha, agreed by the site owner
}
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}")


def test_only_known_email_addresses_are_published():
    found = set()
    for folder in ("docs", "delivery", "capabilities", "overrides"):
        for path in glob.glob(os.path.join(ROOT, folder, "**", "*.*"), recursive=True):
            if path.endswith((".md", ".yaml", ".yml", ".html")):
                with open(path, encoding="utf-8") as handle:
                    found |= {(m, os.path.relpath(path, ROOT)) for m in EMAIL.findall(handle.read())}
    unknown = sorted(f"{email} in {path}" for email, path in found if email.lower() not in KNOWN_EMAILS)
    assert not unknown, "Unconfirmed email addresses - use a 'To be confirmed' box: " + ", ".join(unknown)


# --- Defra Digital Service Manual ------------------------------------------------

# Pages generated from data: the manual link lives in the data, not the page.
GENERATED_FROM = {
    "deliver/platforms.md": os.path.join("delivery", "platforms.yaml"),
    "handrail/technology-capabilities.md": os.path.join("capabilities", "technology-capabilities.yaml"),
}
MATCHING_ROW = re.compile(
    r"^\| [^|]+ \| \[[^]]+\]\(\.\./([^)#]+)(?:#[^)]*)?\) \| \[[^]]+\]\((https://digital\.defra\.gov\.uk/[^)]*)\) \|$"
)


def test_where_things_live_links_match_both_ways():
    """Every matching link on where-things-live is also on the page it names."""
    with open(os.path.join(DOCS, "contribute", "where-things-live.md"), encoding="utf-8") as handle:
        rows = [MATCHING_ROW.match(line) for line in handle.read().splitlines()]
    rows = [r for r in rows if r]
    assert len(rows) >= 10, "the matching links table on where-things-live.md was not found"
    missing = []
    for row in rows:
        page, url = row.groups()
        path = os.path.join(ROOT, GENERATED_FROM.get(page, os.path.join("docs", page)))
        assert os.path.exists(path), f"where-things-live.md links to {page}, which does not exist"
        with open(path, encoding="utf-8") as handle:
            if url not in handle.read():
                missing.append(f"{page} does not link to {url}")
    assert not missing, "Add the manual link at the matching point: " + "; ".join(missing)


def test_service_manual_links_have_no_tracking_parameters():
    found = []
    for path in glob.glob(os.path.join(ROOT, "**", "*.*"), recursive=True):
        if "node_modules" in path or f"{os.sep}site{os.sep}" in path or not path.endswith((".md", ".yaml", ".py")):
            continue
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
            for url in re.findall(r"https://(?:digital\.defra\.gov\.uk|defra\.sharepoint\.com)[^\s)\"']*", text):
                if re.search(r"[?&](xsdata|sdata|clickparams|csf|web|e|OR|CT)=", url):
                    found.append(f"{os.path.relpath(path, ROOT)}: {url[:80]}")
    assert not found, "Remove tracking parameters from links: " + "; ".join(found)


# --- Doctrine status -------------------------------------------------------------


def test_doctrine_wording_follows_the_approvals_register():
    hook = registers
    draft = hook.doctrine_wording([{"pages": hook.DOCTRINE_PAGE, "status": "draft"}])
    endorsed = hook.doctrine_wording([{"pages": hook.DOCTRINE_PAGE, "status": "endorsed"}])
    assert "draft" in draft["label"] and "CDIO" not in draft["label"]
    assert endorsed["label"] == "non-negotiables set by the CDIO"
    assert hook.doctrine_wording([]) == draft, "an unlisted doctrine must read as draft"


def test_home_page_does_not_hard_code_doctrine_status():
    """The home page and principles overview get doctrine wording from registers/approvals.yaml."""
    for path in ("docs/index.md", "docs/principles/index.md", "overrides/home.html"):
        with open(os.path.join(ROOT, path), encoding="utf-8") as handle:
            assert "set by the CDIO" not in handle.read(), f"{path}: use the registers:doctrine markers"


def test_unconfirmed_applicability_is_one_open_question():
    """Area pages link to the single arm's length bodies question rather than each raising their own."""
    out = guardrails._add_applicability('# Area\n\n<p class="lead">Lead.</p>\n', "tbc", "Security")
    assert "To be confirmed" not in out and "index.md#arms-length-bodies" in out
    with open(os.path.join(DOCS, "guardrails", "index.md"), encoding="utf-8") as handle:
        assert "{#arms-length-bodies}" in handle.read()


# --- Pattern user experience sections ---------------------------------------------

UX_BODY = (
    "## Context\n\nText.\n\n## What users see\n\n{a}\n\n"
    "## Content to design\n\n{b}\n\n## What to test with users\n\n{c}\n"
)
TBC = '!!! warning "To be confirmed"\n    **TODO:** something.'


def test_every_pattern_states_its_user_experience():
    found = patterns.parse(DOCS, {g["id"]: g for g in guardrails.parse(DOCS)})
    assert all(p["user_experience"] in patterns.UX_STATES for p in found)
    written = {p["src"] for p in found if p["user_experience"] == "written"}
    assert {"patterns/async-submission.md", "patterns/file-upload.md", "patterns/acting-on-behalf.md"} <= written


def test_ux_sections_must_be_present_and_in_order():
    assert patterns.ux_problems("## Context\n\nText.\n", "written")
    swapped = (
        UX_BODY.format(a="a", b="b", c="c")
        .replace("## Content to design", "## X")
        .replace("## What users see", "## Content to design")
        .replace("## X", "## What users see")
    )
    assert any("order" in p for p in patterns.ux_problems(swapped, "written"))


def test_ux_state_must_match_the_sections():
    written = UX_BODY.format(a="Users see a page.", b="Messages.", c="Questions.")
    assert patterns.ux_problems(written, "written") == []
    assert patterns.ux_problems(written, "tbc"), "tbc needs a To be confirmed box"
    unfinished = UX_BODY.format(a=TBC, b="See above.", c="See above.")
    assert patterns.ux_problems(unfinished, "tbc") == []
    assert patterns.ux_problems(unfinished, "written"), "written must not keep a To be confirmed box"
    empty = UX_BODY.format(a="Users see a page.", b="", c="Questions.")
    assert any("Content to design" in p for p in patterns.ux_problems(empty, "written"))


def test_worked_example_has_the_ux_sections():
    with open(os.path.join(DOCS, "patterns", "worked-example", "index.md"), encoding="utf-8") as handle:
        assert patterns.ux_problems(handle.read(), "written") == []
