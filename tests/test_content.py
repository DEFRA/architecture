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


# --- Pages ---------------------------------------------------------------------


MERMAID = re.compile(r"```mermaid\n(.*?)```", re.S)


@pytest.mark.parametrize("path", sorted(glob.glob(os.path.join(DOCS, "**", "*.md"), recursive=True)))
def test_diagrams_have_text_alternatives(path):
    with open(path, encoding="utf-8") as handle:
        for diagram in MERMAID.findall(handle.read()):
            assert "accTitle:" in diagram and "accDescr:" in diagram, (
                f"{os.path.relpath(path, ROOT)}: add accTitle and accDescr to every mermaid diagram"
            )
