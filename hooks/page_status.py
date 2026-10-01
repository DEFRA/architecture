"""MkDocs hook that flags draft pages.

Add ``status: draft`` to a page's front matter while its content is waiting to
be confirmed by the owning team. The page then shows a banner at the top and a
draft marker in the navigation. Remove the line once the content is agreed.

    ---
    status: draft
    ---

Add ``status_note: ...`` to replace the standard wording of the banner.

Run ``grep -rl "status: draft" docs`` to list every page still in draft.
"""

from __future__ import annotations

DEFAULT_NOTE = (
    "Parts of this page, such as names, timings and thresholds, are still being "
    "confirmed by the architecture team. Use it as a guide, and check with your "
    "solution design authority before relying on the detail."
)


def on_page_markdown(markdown, page, config, files):
    if page.meta.get("status") != "draft":
        return markdown
    note = page.meta.get("status_note", DEFAULT_NOTE)
    banner = f'!!! warning "Draft - to be confirmed"\n    {note}\n\n'
    lines = markdown.split("\n")
    # Place the banner after the lead paragraph, or after the title if there is none.
    anchor = next((i for i, l in enumerate(lines) if l.startswith('<p class="lead">')), None)
    if anchor is None:
        anchor = next((i for i, l in enumerate(lines) if l.startswith("# ")), -1)
    lines.insert(anchor + 1, "\n" + banner)
    return "\n".join(lines)
