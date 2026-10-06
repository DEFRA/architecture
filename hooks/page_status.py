"""MkDocs hook that flags draft pages.

Add ``status: draft`` to a page's front matter while its content is waiting to
be confirmed by the owning team. The page then shows a banner at the top and a
draft marker in the navigation. Remove the line once the content is agreed.

    ---
    status: draft
    ---

Add ``status_note: ...`` to replace the standard wording of the banner.

A whole section can be marked as a prototype in ``mkdocs.yml``. Every page whose
source path starts with ``section`` then shows a prototype banner instead:

    extra:
      prototype:
        - section: deliver/
          note: This section is an early prototype that we are testing with users.

Run ``grep -rl "status: draft" docs`` to list every page still in draft.
"""

from __future__ import annotations

DEFAULT_NOTE = (
    "Parts of this page, such as names, timings and thresholds, are still being "
    "confirmed by the architecture team. Use it as a guide, and check with your "
    "solution design authority before relying on the detail."
)


def prototype_note(src_path: str, config) -> str | None:
    """The prototype note for a page's section, if its section is marked as a prototype."""
    for entry in (config.get("extra") or {}).get("prototype") or []:
        if src_path.startswith(entry["section"]):
            return entry["note"]
    return None


def on_page_markdown(markdown, page, config, files):
    prototype = prototype_note(page.file.src_uri, config)
    if prototype:
        banner = f'!!! warning "Prototype - testing with users"\n    {prototype}\n\n'
    elif page.meta.get("status") == "draft":
        note = page.meta.get("status_note", DEFAULT_NOTE)
        banner = f'!!! warning "Draft - to be confirmed"\n    {note}\n\n'
    else:
        return markdown
    lines = markdown.split("\n")
    # Place the banner after the lead paragraph, or after the title if there is none.
    anchor = next((i for i, line in enumerate(lines) if line.startswith('<p class="lead">')), None)
    if anchor is None:
        anchor = next((i for i, line in enumerate(lines) if line.startswith("# ")), -1)
    lines.insert(anchor + 1, "\n" + banner)
    return "\n".join(lines)
