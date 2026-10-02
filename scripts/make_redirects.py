"""Build a site of redirects from this site's old address to its new one.

When the site moves - for example from howellsr.github.io/architecture to a
DEFRA GitHub organisation - publish the output of this script at the old
address, so links in contracts, decision records and other sites keep working.

    mkdocs build --strict
    python scripts/make_redirects.py site redirects https://defra.github.io/architecture/

For every page in the built site it writes a page at the same path that sends
the reader to the same path at the new address, keeping any #anchor such as
#gr-host-01, and says so in plain text for
anyone whose browser does not follow the redirect. A 404 page sends any other
address to the same path on the new site. Machine-readable files such as
guardrails.json are copied as they are, because they cannot redirect.
"""

from __future__ import annotations

import html
import os
import shutil
import sys

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>This page has moved</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<link rel="canonical" href="{url}">
<script>window.location.replace({url_js} + window.location.hash)</script>
<meta http-equiv="refresh" content="1; url={url}">
</head>
<body>
<h1>This page has moved</h1>
<p>The Defra architecture site has moved. This page is now at <a href="{url}">{text}</a>.</p>
</body>
</html>
"""

NOT_FOUND = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>This site has moved</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<script>
  (function () {{
    var old = {old_path};
    var path = window.location.pathname;
    if (path.indexOf(old) === 0) path = path.slice(old.length);
    window.location.replace({new_base} + path.replace(/^\\//, '') + window.location.search + window.location.hash);
  }})()
</script>
</head>
<body>
<h1>This site has moved</h1>
<p>The Defra architecture site is now at <a href="{new_base_text}">{new_base_text}</a>.</p>
</body>
</html>
"""

COPY_AS_IS = (".json", ".pdf")


def build(site: str, out: str, new_base: str, old_path: str) -> int:
    if not new_base.endswith("/"):
        new_base += "/"
    count = 0
    for folder, _, names in os.walk(site):
        rel_folder = os.path.relpath(folder, site)
        for name in names:
            rel = os.path.normpath(os.path.join(rel_folder, name)).replace(os.sep, "/")
            target = os.path.join(out, rel)
            if name.endswith(COPY_AS_IS):
                os.makedirs(os.path.dirname(target), exist_ok=True)
                shutil.copyfile(os.path.join(folder, name), target)
            elif name == "index.html" or (name.endswith(".html") and name != "404.html"):
                path = rel[: -len("index.html")] if name == "index.html" else rel
                url = html.escape(new_base + path, quote=True)
                os.makedirs(os.path.dirname(target), exist_ok=True)
                with open(target, "w", encoding="utf-8") as handle:
                    handle.write(PAGE.format(url=url, text=url, url_js=repr(new_base + path)))
                count += 1
    with open(os.path.join(out, "404.html"), "w", encoding="utf-8") as handle:
        handle.write(
            NOT_FOUND.format(
                old_path=repr(old_path),
                new_base=repr(new_base),
                new_base_text=html.escape(new_base),
            )
        )
    return count


def main() -> None:
    if len(sys.argv) < 4:
        sys.exit("Usage: python scripts/make_redirects.py <built site> <output folder> <new base URL> [old path]")
    site, out, new_base = sys.argv[1:4]
    old_path = sys.argv[4] if len(sys.argv) > 4 else "/architecture/"
    count = build(site, out, new_base, old_path)
    print(f"Wrote {count} redirect pages to {out}")


if __name__ == "__main__":
    main()
