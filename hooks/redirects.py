"""MkDocs hook that keeps moved pages' old addresses working.

When a page moves, add its old and new source paths to MOVED. After the build,
this hook writes a small page at each old address that sends the reader to the
new one, keeping any #anchor, and says so in plain text for anyone whose
browser does not follow the redirect. The build fails if a new path is not a
page in the site.
"""

from __future__ import annotations

import html
import json
import os

from mkdocs.exceptions import PluginError

# Old source path: new source path. Both relative to docs/.
MOVED = {
    "handrail/reference-architectures/index.md": "patterns/service/index.md",
    "handrail/reference-architectures/transactional-service.md": "patterns/service/transactional-service.md",
    "handrail/reference-architectures/regulatory-casework.md": "patterns/service/regulatory-casework.md",
    "handrail/reference-architectures/data-and-analytics.md": "patterns/service/data-and-analytics.md",
    "handrail/reference-architectures/field-inspection.md": "patterns/service/field-inspection.md",
    "handrail/reference-architectures/incident-response.md": "patterns/service/incident-response.md",
    "handrail/reference-architectures/grants.md": "patterns/service/grants.md",
}

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>This page has moved</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<script>window.location.replace({url_js} + window.location.hash)</script>
<meta http-equiv="refresh" content="0; url={url}">
</head>
<body>
<main>
<h1>This page has moved</h1>
<p>This page is now at <a href="{url}">{text}</a>.</p>
</main>
</body>
</html>
"""


def _directory(src_path: str) -> str:
    """The folder a page is built into, for example patterns/service/grants.md -> patterns/service/grants/."""
    stem = src_path[: -len(".md")]
    return stem[: -len("index")] if stem.endswith("index") else stem + "/"


def on_files(files, config):
    missing = [new for new in MOVED.values() if files.get_file_from_path(new) is None]
    if missing:
        raise PluginError("redirects: these new pages do not exist: " + ", ".join(missing))
    return files


def on_post_build(config):
    for old, new in MOVED.items():
        old_dir, new_dir = _directory(old), _directory(new)
        depth = old_dir.count("/")
        url = "../" * depth + new_dir
        page = PAGE.format(url=html.escape(url), url_js=json.dumps(url), text=html.escape(new_dir))
        path = os.path.join(config["site_dir"], old_dir, "index.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(page)
