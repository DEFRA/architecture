# Contribute

<p class="lead">This site is built in the open and improves when the people who use it change it. Defra staff and delivery partners are equally welcome to contribute.</p>

## Ways to contribute

- **Spotted a mistake or something unclear?** Select **Edit this page** (the pencil icon at the top of each page) to propose a change on GitHub.
- **Have a question or an idea?** [Open an issue](https://github.com/howellsr/architecture/issues).
- **Want to change a guardrail?** Open a pull request explaining what and why. See [how guardrails change](../guardrails/index.md#how-guardrails-change).
- **Improving the capability model?** Edit the YAML in [`capabilities/`](https://github.com/howellsr/architecture/tree/main/capabilities). The site build checks your change.

## Writing style

We follow the [GOV.UK style guide](https://www.gov.uk/guidance/style-guide). In short:

- plain English, short sentences, active voice
- write for a busy delivery team: lead with what they need to do
- explain *why*, not just *what*
- name capabilities and products consistently with the [handrail](../handrail/index.md)
- avoid acronyms, or explain them the first time

## How the repository is organised

Most changes are to Markdown in `docs/` or to the YAML data files. You rarely need to touch the code.

| Path | What it holds | Who usually edits it |
| --- | --- | --- |
| `docs/` | Every page, in Markdown. The folder structure matches the site sections. | Anyone |
| `docs/guardrails/*.md` | Principles and guardrails. The guardrail library is built from these. | Architects |
| `capabilities/*.yaml` | Business and technology capability models | Business and enterprise architects |
| `nfrs/*.yaml` | Service tiers and the NFR catalogue | Solution architects |
| `mkdocs.yml` | Site settings and the navigation | Site maintainers |
| `hooks/` | Small Python scripts that check the data and build tables from it | Site maintainers |
| `overrides/`, `docs/stylesheets/`, `docs/javascripts/` | Home page hero, theme, decision check and library filter | Site maintainers |
| `tests/` | Content checks (`pytest`) and the accessibility check (`npm test`) | Site maintainers |
| `.github/` | CI workflow, pull request and issue templates | Site maintainers |

## Common tasks

### Edit a page

Select **Edit this page** on the site, or edit the file in `docs/` directly. If you add a page, add it to `nav` in `mkdocs.yml`.

### Add or change a guardrail

Add a section to the right page in `docs/guardrails/` using exactly this shape:

```markdown
## GR-HOST-08 Short, active title {#gr-host-08}

<span class="rfc rfc--should">Should</span> One-sentence statement of what teams do.

**Why:** the reason.

**How to meet it:** practical, ideally self-service, steps.
```

- Use the next unused number for that area, and never reuse or renumber an id.
- The level is `rfc--must`, `rfc--should` or `rfc--could`.
- The guardrail library, home page figures and NFR links update automatically. The build fails if the id and anchor do not match or the badge is missing.

### Add or change an NFR or service tier

Edit `nfrs/catalogue.yaml` or `nfrs/service-tiers.yaml`. Comments at the top of each file explain every field. The build checks that ids are unique, that targets use real tiers and that linked guardrails exist.

### Change the capability model

Edit `capabilities/business-capabilities.yaml` or `capabilities/technology-capabilities.yaml`. The map, catalogue and mapping matrix are generated from them.

### Mark a page as draft

Add `status: draft` to the page's front matter. The page shows a "Draft - to be confirmed" banner and a marker in the navigation. Remove the line once the content is agreed. To list draft pages, run `grep -rl "status: draft" docs`.

### Add a diagram

Use a `mermaid` code block. Every diagram needs an `accTitle` and an `accDescr` line describing what it shows, for people using screen readers. The tests fail without them.

## Running the site locally

You need Python 3.10 or later.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
mkdocs serve
```

Then open <http://127.0.0.1:8000>. Pages reload as you edit.

## Checks

Every pull request runs three checks. You can run them locally before you push:

| Check | Command | What it catches |
| --- | --- | --- |
| Content | `pytest` | Broken references between capabilities, guardrails and NFRs; diagrams without text alternatives |
| Build | `mkdocs build --strict` | Broken links and anchors, invalid data, missing pages |
| Accessibility | `npm ci && npx playwright install chromium && npm test` (after a build) | WCAG 2.2 AA failures on every page in light and dark mode |

Merges to `main` are published to [howellsr.github.io/architecture](https://howellsr.github.io/architecture/) once all three pass.

## What not to publish

This is a public repository. Do not include:

- secrets, credentials, internal hostnames or IP addresses
- detailed security vulnerabilities or threat model detail for live services
- personal information, other than names of people who have agreed to be named
- commercially sensitive information
