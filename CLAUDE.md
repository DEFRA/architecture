# CLAUDE.md

Guidance for AI assistants working in this repository: the Defra architecture site (MkDocs Material, published to GitHub Pages). Read `CONTRIBUTING.md` and `MAINTAINERS.md` too.

## Ground rules

- **Guardrail ids are stable and may be cited in contracts.** Never renumber, rename, reuse or delete an id. Deprecate with `status: deprecated` and `replaced_by`. New guardrails take the next free id in their area and start as `status: draft`.
- **Never invent Defra facts** - names, contacts, email addresses, URLs, lead times, approvals, boards or product names. Write a `!!! warning "To be confirmed"` box with a `**TODO:**` line instead. Email addresses must be in the allowlist in `tests/test_content.py`.
- **Link, do not repeat.** How to do the job and who to contact belong in the Defra Digital Service Manual; this site holds rules, decisions and evidence. See `docs/contribute/where-things-live.md`.
- **All guidance lives in this repository**, never in the GitHub wiki.
- **Musts only where required** (law or mandatory policy, a baseline security control, or a doctrine non-negotiable) - see ADR 0004. A test caps the number of Musts.
- **Every rule that can be tested gets a test** in `tests/test_content.py`.
- **GOV.UK style:** plain English, sentence case, active voice, expand abbreviations on first use. See `docs/contribute/content-style.md`.
- **Accessible:** WCAG 2.2 AA in light and dark mode. Every Mermaid diagram needs `accTitle` and `accDescr`.
- **Small pull requests, one piece of work each.** Record significant changes in `CHANGELOG.md` (under `Unreleased`) and `docs/about/changelog.md`.

## Where things are

| Path | What |
| --- | --- |
| `docs/` | Every page, in Markdown. Guardrail metadata is in each guardrail page's front matter. |
| `capabilities/`, `nfrs/`, `delivery/`, `registers/` | YAML data the pages are generated from |
| `hooks/` | Validate the data and replace markers such as `<!-- guardrails:library -->`. Listed in `mkdocs.yml`; described in `docs/contribute/site-design.md`. |
| `includes/abbreviations.md` | Abbreviation tooltips, appended to every page |
| `overrides/`, `docs/stylesheets/`, `docs/javascripts/` | Templates, theme and interactive tools |
| `tests/` | `test_content.py` (pytest) and `accessibility.js` (axe, run by `npm test`) |
| `scripts/` | Release notes and PDF, review-due and heading-case warnings, redirects |

## Commands

```bash
pip install -r requirements-dev.txt && npm ci
ruff check . && ruff format --check .   # Python lint
npm run lint                            # JavaScript lint
pytest                                  # content rules
mkdocs build --strict                   # fails on broken links, anchors and invalid data
npm test                                # accessibility, after a build
```

Run all of them before pushing. `vale docs` and `python scripts/heading_case.py` give prose warnings.

## Gotchas

- `mkdocs.yml` uses Python tags, so read it with a regular expression, not `yaml.safe_load`.
- Generated tables come from markers; edit the YAML or front matter, not the rendered output.
- Code fences are skipped when collecting "To be confirmed" boxes, so examples are safe there.
- Links to this repository's `blob/main` files are checked by a test, not by the link checker.
- Never force-push or rewrite history on a shared branch; merge `main` into a branch with a merge commit.
- Do not add model names or session links to page content.
