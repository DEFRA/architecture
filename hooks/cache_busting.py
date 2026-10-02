"""MkDocs hook that stops browsers using stale copies of our CSS and JavaScript.

Material fingerprints its own assets, but files listed in ``extra_css`` and
``extra_javascript`` keep the same URL between releases, so a browser can mix a
cached old stylesheet with new HTML. This hook adds ``?v=<content hash>`` to
those links, so the URL changes whenever the file does.
"""

from __future__ import annotations

import hashlib
import os
import re

_versions: dict[str, str] = {}


def on_config(config):
    _versions.clear()
    for entry in [*config["extra_css"], *config["extra_javascript"]]:
        path = str(entry)
        full = os.path.join(config["docs_dir"], path)
        if os.path.isfile(full):
            with open(full, "rb") as handle:
                _versions[path] = hashlib.sha256(handle.read()).hexdigest()[:10]
    return config


def on_post_page(output, page, config):
    for path, version in _versions.items():
        # Matches the relative or absolute reference MkDocs writes for this file.
        output = re.sub(
            r'((?:href|src)="[^"]*' + re.escape(path) + r')"',
            lambda m, v=version: f'{m.group(1)}?v={v}"',
            output,
        )
    return output
