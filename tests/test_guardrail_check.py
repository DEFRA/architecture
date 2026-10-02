"""Tests for tools/guardrail-check/check.py."""

import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("check", os.path.join(ROOT, "tools", "guardrail-check", "check.py"))
check = importlib.util.module_from_spec(spec)
sys.modules["check"] = check  # dataclasses look the module up by name
spec.loader.exec_module(check)

GOOD_README = """# My service

What it does.

## Running locally
## Running tests
## Deployment

Decisions are recorded as ADRs in docs/adr.
"""


def make_repo(tmp_path, files):
    for name, text in files.items():
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    return str(tmp_path)


def no_api(path, token):
    return 404, None


def by_guardrail(results):
    return {r.guardrail: r.status for r in results}


def test_a_well_set_up_repository_passes(tmp_path):
    root = make_repo(
        tmp_path,
        {
            "LICENCE": "Open Government Licence v3.0",
            "README.md": GOOD_README,
            "openapi.yaml": "openapi: 3.0.3\ninfo:\n  title: X\n  version: 1.0.0\npaths:\n  /x: {}\n",
            ".github/dependabot.yml": "version: 2\n",
            "docs/adr/0001-first.md": "# 0001. First\n",
        },
    )
    results = by_guardrail(check.run(root, None, None, api=no_api))
    for gid in ("GR-OPEN-02", "GR-DEV-08", "GR-API-02", "GR-DEV-06", "GR-DEV-09"):
        assert results[gid] == check.PASS, gid
    assert results["GR-OPEN-03"] == check.UNKNOWN
    assert results["GR-DEV-03"] == check.UNKNOWN


def test_an_empty_repository_fails_the_file_checks(tmp_path):
    results = by_guardrail(check.run(str(tmp_path), None, None, api=no_api))
    for gid in ("GR-OPEN-02", "GR-DEV-08", "GR-DEV-06", "GR-DEV-09"):
        assert results[gid] == check.FAIL, gid
    assert results["GR-API-02"] == check.UNKNOWN


def test_wrong_licence_fails(tmp_path):
    root = make_repo(tmp_path, {"LICENSE": "Apache License, Version 2.0"})
    assert check.check_licence(root).status == check.FAIL


def test_readme_without_adr_link_fails(tmp_path):
    root = make_repo(tmp_path, {"README.md": GOOD_README.replace("Decisions are recorded as ADRs in docs/adr.", "")})
    result = check.check_readme(root)
    assert result.status == check.FAIL
    assert "architecture decision records" in result.detail


def test_swagger_2_and_broken_specs_fail(tmp_path):
    root = make_repo(
        tmp_path,
        {
            "api/old.yaml": "openapi: 2.0\ninfo:\n  title: X\n  version: 1\npaths: {}\n",
            "api/broken.json": '{"openapi": "3.1.0", ',
        },
    )
    result = check.check_api_specs(root)
    assert result.status == check.FAIL
    assert "not 3.x" in result.detail and "cannot be parsed" in result.detail


def test_asyncapi_passes(tmp_path):
    root = make_repo(
        tmp_path,
        {"asyncapi.yaml": "asyncapi: 3.0.0\ninfo:\n  title: Events\n  version: 1.0.0\nchannels:\n  submitted: {}\n"},
    )
    assert check.check_api_specs(root).status == check.PASS


def test_settings_checks_use_the_api():
    def api(path, token):
        if path == "/repos/o/r":
            return 200, {
                "default_branch": "main",
                "security_and_analysis": {
                    "secret_scanning": {"status": "enabled"},
                    "secret_scanning_push_protection": {"status": "disabled"},
                },
            }
        if path == "/repos/o/r/branches/main":
            return 200, {"protected": True}
        return 404, None

    assert check.check_secret_scanning("o/r", "t", api).status == check.FAIL
    assert check.check_branch_protection("o/r", "t", None, api).status == check.PASS


def test_report_names_each_guardrail(tmp_path):
    text = check.report(check.run(str(tmp_path), None, None, api=no_api), "o/r")
    for gid in ("GR-OPEN-02", "GR-DEV-08", "GR-API-02", "GR-OPEN-03", "GR-DEV-03", "GR-DEV-06", "GR-DEV-09"):
        assert f"[{gid}]" in text
    assert text.startswith("## Guardrail check for o/r")


def test_checked_guardrails_say_so_in_their_metadata():
    hooks = importlib.util.spec_from_file_location("g", os.path.join(ROOT, "hooks", "guardrails.py"))
    guardrails = importlib.util.module_from_spec(hooks)
    hooks.loader.exec_module(guardrails)
    found = {g["id"]: g for g in guardrails.parse(os.path.join(ROOT, "docs"))}
    for gid in ("GR-OPEN-02", "GR-DEV-08", "GR-API-02", "GR-OPEN-03", "GR-DEV-03", "GR-DEV-06", "GR-DEV-09"):
        assert "tools/guardrail-check" in found[gid]["automated_check"], gid
