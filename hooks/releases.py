"""MkDocs hook that reads CHANGELOG.md to show which version is in force.

``CHANGELOG.md`` at the root of the repository is the record of releases, in
Keep a Changelog format. This hook:

* checks every release heading looks like ``## [X.Y.Z] - YYYY-MM-DD``, with
  versions in descending order;
* sets ``extra.version_in_force`` and ``extra.version_date`` (the latest
  release) and ``extra.version_unreleased`` (true when there are changes not
  yet released), which the phase banner shows on every page; and
* replaces ``<!-- releases:changelog -->`` with the releases from the file.
"""

from __future__ import annotations

import datetime
import os
import re

from mkdocs.exceptions import PluginError

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHANGELOG = os.path.join(ROOT, "CHANGELOG.md")
SECTION = re.compile(r"^## \[(.+?)\](?: - (\S+))?\s*$", re.M)
VERSION = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")

_releases: list[dict] = []


def parse(text: str) -> list[dict]:
    """Return the sections of the changelog, newest first."""
    sections, errors = [], []
    matches = list(SECTION.finditer(text))
    for i, match in enumerate(matches):
        name, date = match.groups()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[match.end() : end].strip()
        if name == "Unreleased":
            sections.append({"version": None, "date": None, "body": body})
            continue
        if not VERSION.match(name):
            errors.append(f"'{name}' is not a version like 1.2.3")
            continue
        try:
            datetime.date.fromisoformat(date or "")
        except ValueError:
            errors.append(f"version {name} needs a date like '## [{name}] - 2026-10-01'")
        sections.append({"version": name, "date": date, "body": body})
    versions = [tuple(map(int, s["version"].split("."))) for s in sections if s["version"]]
    if versions != sorted(versions, reverse=True) or len(set(versions)) != len(versions):
        errors.append("versions must be unique and listed newest first")
    if not versions:
        errors.append("there are no released versions")
    if errors:
        raise PluginError("CHANGELOG.md is invalid:\n  - " + "\n  - ".join(errors))
    return sections


def latest(sections: list[dict]) -> dict:
    return next(s for s in sections if s["version"])


def on_config(config):
    with open(CHANGELOG, encoding="utf-8") as handle:
        _releases[:] = parse(handle.read())
    current = latest(_releases)
    day = datetime.date.fromisoformat(current["date"])
    unreleased = next((s for s in _releases if s["version"] is None), None)
    config["extra"]["version_in_force"] = current["version"]
    config["extra"]["version_date"] = f"{day.day} {day:%B %Y}"
    config["extra"]["version_unreleased"] = bool(unreleased and unreleased["body"])
    return config


def on_page_markdown(markdown, page, config, files):
    marker = "<!-- releases:changelog -->"
    if marker not in markdown:
        return markdown
    out = []
    for s in _releases:
        if s["version"] is None:
            if s["body"]:
                out += ["## Not yet released", "", "Changes on the site that are not yet part of a release.", ""]
                out += [s["body"], ""]
            continue
        out += [f"## Version {s['version']} {{#v{s['version'].replace('.', '-')}}}", "", f"Released {s['date']}.", ""]
        out += [s["body"], ""]
    return markdown.replace(marker, "\n".join(out))
