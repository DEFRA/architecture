# Defra architecture

[![ci](https://github.com/howellsr/architecture/actions/workflows/ci.yml/badge.svg)](https://github.com/howellsr/architecture/actions/workflows/ci.yml)
[![links](https://github.com/howellsr/architecture/actions/workflows/links.yml/badge.svg)](https://github.com/howellsr/architecture/actions/workflows/links.yml)
[![Accessibility: WCAG 2.2 AA tested](https://img.shields.io/badge/accessibility-WCAG%202.2%20AA%20tested-00703c)](tests/accessibility.js)
[![Status: alpha](https://img.shields.io/badge/status-alpha-bbd4ea)](https://howellsr.github.io/architecture/about/roadmap/)
[![Licence: OGL v3](https://img.shields.io/badge/licence-OGL%20v3-12324a)](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
[![Built with Material for MkDocs](https://img.shields.io/badge/built%20with-Material%20for%20MkDocs-526cfe)](https://squidfunk.github.io/mkdocs-material/)

Source for the Defra architecture site at **<https://howellsr.github.io/architecture/>**: the DDTS doctrine, architecture principles, guardrails, non-functional requirements, the business-to-technology capability handrail, governance, and enterprise data and security architecture. It is written for Defra product and platform teams and the delivery partners who work with us.

The site is a static site built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). It is in **alpha** - see the [roadmap](https://howellsr.github.io/architecture/about/roadmap/).

## How it fits together

| Path | Contents |
| --- | --- |
| `docs/` | Site content in Markdown, one folder per section |
| `capabilities/` | Business and technology capability models (YAML) |
| `nfrs/` | Service tiers and the non-functional requirements catalogue (YAML) |
| `delivery/` | The delivery lifecycle and Defra platforms, used to build the "Deliver a service" pages (YAML) |
| `docs/patterns/` | Architecture patterns. Front matter lists each pattern's guardrails and Secure by Design artefacts, validated at build time |
| `hooks/` | Build-time scripts that validate the content and generate the capability map, guardrail library and metadata (`guardrails.json`), NFR tables, doctrine-to-guardrail traceability, draft banners and the open questions page |
| `overrides/`, `docs/stylesheets/`, `docs/javascripts/` | Home page hero, alpha banner, theme, decision check and library filter |
| `tests/` | Content checks (`pytest`) and the WCAG 2.2 AA accessibility check (`npm test`) |
| `.github/` | CI and link-check workflows, pull request and issue templates, Dependabot |

The [contribution guide](https://howellsr.github.io/architecture/contribute/) explains how to add a guardrail, NFR or capability, and how the content is validated.

## Prerequisites

- [Python](https://www.python.org/) 3.12
- [Node.js](https://nodejs.org/) - the Active LTS version in `.nvmrc` - for linting and the accessibility check only

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
npm ci
```

## Running in development

```bash
mkdocs serve
```

Open <http://127.0.0.1:8000>. Pages reload as you edit.

## Running tests

Run the same checks as CI before you raise a pull request:

| Check | Command |
| --- | --- |
| Python lint and format (Ruff) | `ruff check hooks tests && ruff format --check hooks tests` |
| JavaScript lint (neostandard) | `npm run lint` |
| Content checks | `pytest` |
| Build, links and anchors | `mkdocs build --strict` |
| Accessibility, WCAG 2.2 AA, light and dark mode (after a build) | `npx playwright install chromium && npm test` |

External links are checked weekly, and on pull requests, by the `links` workflow.

## Branching policy

We use [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow): branch from `main`, open a pull request, and merge once checks pass and the change is reviewed. `main` is always releasable. Every merge to `main` is published.

## Publishing

The site is published with GitHub Pages at <https://howellsr.github.io/architecture/>.

- Every push to `main` runs `.github/workflows/ci.yml`: lint, content tests, a strict build and an accessibility check. If all pass, `mkdocs gh-deploy` pushes the built site to the `gh-pages` branch.
- GitHub Pages serves the `gh-pages` branch. One-off setup (repository admin): **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `gh-pages` / `(root)` → Save**.
- If the site shows this README instead of the home page, Pages is serving `main`. Change the branch to `gh-pages` as above.
- To republish without a code change, run the **ci** workflow manually from the **Actions** tab.

## Contributing to this project

Issues and pull requests are welcome from Defra staff and delivery partners. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

This repository follows the [Defra software development standards](https://defra.github.io/software-development-standards/), including pinned GitHub Actions, Dependabot and dependency review.

## Licence

THIS INFORMATION IS LICENSED UNDER THE CONDITIONS OF THE OPEN GOVERNMENT LICENCE found at:

<http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3>

The following attribution statement MUST be cited in your products and applications when using this information.

> Contains public sector information licensed under the Open Government license v3

### About the licence

The Open Government Licence (OGL) was developed by the Controller of Her Majesty's Stationery Office (HMSO) to enable information providers in the public sector to license the use and re-use of their information under a common open licence.

It is designed to encourage use and re-use of information freely and flexibly, with only a few conditions.
