"""Check a repository against the Defra architecture guardrails that can be automated.

Runs a small set of checks and writes a Markdown report that names the
guardrail each check comes from. Each check passes, fails or is unknown
(for example when the token cannot see a repository setting). Only failures
make the command exit non-zero.

    python tools/guardrail-check/check.py --path . --repo owner/name --report report.md

Set GITHUB_TOKEN (or GH_TOKEN) to check repository settings through the
GitHub API. Without a token those checks are reported as unknown.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass

import yaml

SITE = "https://howellsr.github.io/architecture/guardrails/"
PASS, FAIL, UNKNOWN = "pass", "fail", "unknown"
SYMBOLS = {PASS: "Pass", FAIL: "Fail", UNKNOWN: "Unknown"}

LICENCE_FILES = ("LICENCE", "LICENSE", "LICENCE.md", "LICENSE.md", "LICENCE.txt", "LICENSE.txt")
DEPENDENCY_UPDATE_FILES = (
    ".github/dependabot.yml",
    ".github/dependabot.yaml",
    "renovate.json",
    "renovate.json5",
    ".github/renovate.json",
    ".github/renovate.json5",
    ".renovaterc",
    ".renovaterc.json",
)
README_FILES = ("README.md", "readme.md", "README.rst", "README")
# What GR-DEV-08 asks a README to explain, and headings that show it does.
README_SECTIONS = {
    "how to run it locally": r"run|setup|set up|getting started|install|local development",
    "how to test it": r"test",
    "how to deploy it": r"deploy|release|publish",
}
README_MISSING_ADRS = "links to its architecture decision records"
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "site", "dist", "build", "vendor", "__pycache__"}
SPEC_EXTENSIONS = (".yaml", ".yml", ".json")
NO_REPO = "No repository given, so settings were not checked."


@dataclass
class Result:
    guardrail: str
    anchor_page: str
    check: str
    status: str
    detail: str


def _exists(root: str, names) -> str | None:
    return next((n for n in names if os.path.isfile(os.path.join(root, n))), None)


def check_licence(root: str) -> Result:
    """GR-OPEN-02: a LICENCE file with the Open Government Licence or MIT."""
    name = _exists(root, LICENCE_FILES)
    check = "LICENCE file with the Open Government Licence or MIT licence"
    if not name:
        return Result("GR-OPEN-02", "open-source", check, FAIL, "No LICENCE or LICENSE file in the repository root.")
    with open(os.path.join(root, name), encoding="utf-8", errors="replace") as handle:
        text = handle.read()
    if re.search(r"open government licen[cs]e", text, re.I) or re.search(r"\bMIT License\b|\bMIT Licence\b", text):
        return Result("GR-OPEN-02", "open-source", check, PASS, f"`{name}` found.")
    return Result("GR-OPEN-02", "open-source", check, FAIL, f"`{name}` is not the Open Government Licence or MIT.")


def check_readme(root: str) -> Result:
    """GR-DEV-08: README explains how to run, test and deploy, and links to ADRs."""
    check = "README explains how to run, test and deploy, and links to its ADRs"
    name = _exists(root, README_FILES)
    if not name:
        return Result("GR-DEV-08", "software-development", check, FAIL, "No README in the repository root.")
    with open(os.path.join(root, name), encoding="utf-8", errors="replace") as handle:
        text = handle.read()
    headings = "\n".join(re.findall(r"^#{1,6}\s+(.+)$", text, re.M)).lower()
    missing = [what for what, pattern in README_SECTIONS.items() if not re.search(pattern, headings)]
    if not re.search(r"\badrs?\b|decision record", text, re.I):
        missing.append(README_MISSING_ADRS)
    if missing:
        detail = "README does not cover " + "; ".join(missing) + "."
        return Result("GR-DEV-08", "software-development", check, FAIL, detail)
    return Result("GR-DEV-08", "software-development", check, PASS, f"`{name}` covers each topic.")


def _spec_files(root: str):
    for folder, dirs, names in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in names:
            if name.endswith(SPEC_EXTENSIONS):
                yield os.path.join(folder, name)


def _load(path: str):
    with open(path, encoding="utf-8", errors="replace") as handle:
        text = handle.read(200_000)
    if path.endswith(".json"):
        if not re.search(r'"(openapi|asyncapi)"\s*:', text[:5000]):
            return None
    elif not re.search(r"""^\s*["']?(openapi|asyncapi)["']?\s*:""", text, re.M):
        return None
    try:
        return json.loads(text) if path.endswith(".json") else yaml.safe_load(text)
    except (ValueError, yaml.YAMLError):
        return "invalid"


def check_api_specs(root: str) -> Result:
    """GR-API-02: OpenAPI 3 or AsyncAPI specifications in the repository, and valid."""
    check = "APIs described with OpenAPI 3 or AsyncAPI, kept with the code"
    found, problems = [], []
    for path in _spec_files(root):
        doc = _load(path)
        if doc is None:
            continue
        rel = os.path.relpath(path, root)
        if doc == "invalid" or not isinstance(doc, dict):
            problems.append(f"`{rel}` cannot be parsed")
            continue
        if "openapi" in doc:
            if not str(doc["openapi"]).startswith("3."):
                problems.append(f"`{rel}` is OpenAPI {doc['openapi']}, not 3.x")
            elif not (doc.get("info", {}).get("title") and doc.get("info", {}).get("version")):
                problems.append(f"`{rel}` has no info.title or info.version")
            elif not (doc.get("paths") or doc.get("webhooks") or doc.get("components")):
                problems.append(f"`{rel}` has no paths, webhooks or components")
            else:
                found.append(rel)
        elif "asyncapi" in doc:
            if not (doc.get("info", {}).get("title") and doc.get("info", {}).get("version")):
                problems.append(f"`{rel}` has no info.title or info.version")
            elif not (doc.get("channels") or doc.get("operations") or doc.get("components")):
                problems.append(f"`{rel}` has no channels, operations or components")
            else:
                found.append(rel)
    if problems:
        return Result("GR-API-02", "apis-and-integration", check, FAIL, "; ".join(problems) + ".")
    if found:
        detail = "Found " + ", ".join(f"`{f}`" for f in found) + "."
        return Result("GR-API-02", "apis-and-integration", check, PASS, detail)
    return Result(
        "GR-API-02",
        "apis-and-integration",
        check,
        UNKNOWN,
        "No OpenAPI or AsyncAPI document found. If this repository provides an API or events, add one.",
    )


def check_dependency_updates(root: str) -> Result:
    """GR-DEV-06: automated dependency updates with Dependabot or Renovate."""
    check = "Automated dependency updates with Dependabot or Renovate"
    name = _exists(root, DEPENDENCY_UPDATE_FILES)
    if name:
        return Result("GR-DEV-06", "software-development", check, PASS, f"`{name}` found.")
    return Result("GR-DEV-06", "software-development", check, FAIL, "No Dependabot or Renovate configuration found.")


def check_adr_folder(root: str) -> Result:
    """GR-DEV-09: architecture decision records in docs/adr."""
    check = "Architecture decision records in `docs/adr`"
    folder = os.path.join(root, "docs", "adr")
    if not os.path.isdir(folder):
        return Result("GR-DEV-09", "software-development", check, FAIL, "No `docs/adr` folder.")
    records = [n for n in os.listdir(folder) if n.endswith(".md") and n.lower() not in ("readme.md", "index.md")]
    if not records:
        return Result("GR-DEV-09", "software-development", check, FAIL, "`docs/adr` has no decision records yet.")
    return Result("GR-DEV-09", "software-development", check, PASS, f"{len(records)} decision records in `docs/adr`.")


def _api(path: str, token: str | None):
    """Call the GitHub API. Returns (status code, JSON body or None)."""
    request = urllib.request.Request(
        "https://api.github.com" + path,
        headers={"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"},
    )
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as err:
        return err.code, None
    except (urllib.error.URLError, TimeoutError, ValueError):
        return 0, None


def check_secret_scanning(repo: str | None, token: str | None, api=_api) -> Result:
    """GR-OPEN-03: secret scanning and push protection turned on."""
    check = "Secret scanning and push protection turned on"
    if not repo:
        return Result("GR-OPEN-03", "open-source", check, UNKNOWN, NO_REPO)
    status, body = api(f"/repos/{repo}", token)
    settings = (body or {}).get("security_and_analysis")
    if status != 200 or not settings:
        return Result(
            "GR-OPEN-03",
            "open-source",
            check,
            UNKNOWN,
            "The token cannot read the repository's security settings. Check them in Settings > Code security, "
            "or run with a token that has administration read access.",
        )
    scanning = settings.get("secret_scanning", {}).get("status")
    push = settings.get("secret_scanning_push_protection", {}).get("status")
    if scanning == "enabled" and push == "enabled":
        return Result("GR-OPEN-03", "open-source", check, PASS, "Secret scanning and push protection are on.")
    return Result(
        "GR-OPEN-03",
        "open-source",
        check,
        FAIL,
        f"Secret scanning is {scanning or 'off'} and push protection is {push or 'off'}.",
    )


def check_branch_protection(repo: str | None, token: str | None, branch: str | None, api=_api) -> Result:
    """GR-DEV-03: the main branch is protected."""
    check = "Main branch protected"
    if not repo:
        return Result("GR-DEV-03", "software-development", check, UNKNOWN, NO_REPO)
    if not branch:
        status, body = api(f"/repos/{repo}", token)
        branch = (body or {}).get("default_branch")
        if not branch:
            detail = "Could not read the repository's default branch."
            return Result("GR-DEV-03", "software-development", check, UNKNOWN, detail)
    status, body = api(f"/repos/{repo}/branches/{branch}", token)
    if status != 200 or body is None:
        return Result("GR-DEV-03", "software-development", check, UNKNOWN, f"Could not read branch `{branch}`.")
    status, rules = api(f"/repos/{repo}/rules/branches/{branch}", token)
    ruleset = status == 200 and any(r.get("type") == "pull_request" for r in rules or [])
    if body.get("protected") or ruleset:
        return Result(
            "GR-DEV-03",
            "software-development",
            check,
            PASS,
            f"`{branch}` is protected. Check that it requires a review and passing checks.",
        )
    return Result("GR-DEV-03", "software-development", check, FAIL, f"`{branch}` is not protected.")


def run(root: str, repo: str | None, token: str | None, branch: str | None = None, api=_api) -> list[Result]:
    return [
        check_licence(root),
        check_readme(root),
        check_api_specs(root),
        check_secret_scanning(repo, token, api),
        check_branch_protection(repo, token, branch, api),
        check_dependency_updates(root),
        check_adr_folder(root),
    ]


def report(results: list[Result], repo: str | None = None) -> str:
    counts = {s: sum(1 for r in results if r.status == s) for s in SYMBOLS}
    title = f"Guardrail check for {repo}" if repo else "Guardrail check"
    lines = [
        f"## {title}",
        "",
        f"{counts[PASS]} passed, {counts[FAIL]} failed, {counts[UNKNOWN]} unknown. "
        f"These are the guardrails that can be checked automatically; the rest need a person. "
        f"See the [guardrail library]({SITE}library/).",
        "",
        "| Guardrail | Check | Result | Detail |",
        "| --- | --- | --- | --- |",
    ]
    for r in results:
        link = f"[{r.guardrail}]({SITE}{r.anchor_page}/#{r.guardrail.lower()})"
        lines.append(f"| {link} | {r.check} | {SYMBOLS[r.status]} | {r.detail.replace('|', '/')} |")
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--path", default=".", help="repository folder to check (default: current folder)")
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY"), help="owner/name, for settings checks")
    parser.add_argument("--branch", help="branch to check for protection (default: the default branch)")
    parser.add_argument("--report", help="also write the Markdown report to this file")
    parser.add_argument("--no-fail", action="store_true", help="exit 0 even when checks fail")
    args = parser.parse_args(argv)

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    results = run(os.path.abspath(args.path), args.repo, token, args.branch)
    text = report(results, args.repo)
    print(text)
    for target in filter(None, (args.report, os.environ.get("GITHUB_STEP_SUMMARY"))):
        with open(target, "a", encoding="utf-8") as handle:
            handle.write(text)
    failed = any(r.status == FAIL for r in results)
    return 1 if failed and not args.no_fail else 0


if __name__ == "__main__":
    sys.exit(main())
