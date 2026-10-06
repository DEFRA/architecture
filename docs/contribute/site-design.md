---
status: draft
---

# Site design

<p class="lead">How this site is built and why it looks and behaves the way it does - for maintainers changing the theme, a template or a generated page. To change the words, see <a href="../content-style/">content style</a> instead.</p>

## Principles

- **GOV.UK look and feel, not a GOV.UK service.** The site follows GOV.UK conventions - Arial, a yellow focus state, a phase banner, sentence case - so it feels familiar to Defra teams. It is not on GOV.UK and does not use the crown or GOV.UK branding.
- **Accessible by default.** Every page must meet WCAG 2.2 AA in light and dark mode. The accessibility check runs on every page in CI.
- **Data first.** Guardrails, capabilities, NFRs, platforms and registers are data. Pages are generated from it, so a fact is written once and every list stays in step.
- **Static and simple.** No server, database or tracking. The site is plain HTML published to GitHub Pages, and works without JavaScript except for the interactive tools.

## How a page is built

The site uses [MkDocs](https://www.mkdocs.org/) with the [Material](https://squidfunk.github.io/mkdocs-material/) theme - see [ADR 0001](../adr/0001-mkdocs-material-with-hooks.md). When a page is built:

1. Markdown in `docs/` is read, with `includes/abbreviations.md` appended so abbreviations get tooltips.
2. **Hooks** in `hooks/` load and validate the data, then replace markers such as `<!-- guardrails:library -->` with generated content. The build fails if the data is invalid.
3. The page is rendered through the Material theme and the templates in `overrides/`.
4. After the build, hooks write `guardrails.json` and check the output, for example for abbreviation tooltips in the wrong place.

| Hook | What it does |
| --- | --- |
| `capabilities.py` | Business and technology capability models |
| `guardrails.py` | Guardrail metadata, the library, Must lists, the print page and home page figures |
| `traceability.py` | Doctrine to principles to guardrails |
| `nfrs.py` | Service tiers and the NFR catalogue |
| `delivery.py` | Phase pages, checklists, platforms and role pages |
| `patterns.py` | The pattern catalogue and each pattern's guardrails and Secure by Design artefacts |
| `registers.py` | Approval status, the exception register, guardrails health and doctrine wording |
| `page_status.py` | The draft banner and navigation marker for `status: draft` pages, and the prototype banner for sections listed under `extra.prototype` in `mkdocs.yml` |
| `cache_busting.py` | Adds a content hash to the site's CSS and JavaScript addresses |
| `site_info.py` | The last updated date |
| `releases.py` | Release history and the version in force, from `CHANGELOG.md` |
| `open_questions.py` | The open questions page, from every "To be confirmed" box |
| `abbreviations.py` | Removes tooltips inside guardrail ids and next to their own expansion |
| `machine.py` | `llms.txt`, `pages.json` and a Markdown copy of every page, for tools and AI. Keep it last in `mkdocs.yml` |
| `redirects.py` | Keeps the old addresses of moved pages working - add a page to its `MOVED` list when you move it |

## Templates

- **`overrides/main.html`** adds the phase banner to every page: alpha status, the last updated date and the version in force.
- **`overrides/home.html`** is the home page: the hero, the headline figures and the routes into the site. The figures and the doctrine wording come from the hooks, not the template.

Keep logic in hooks rather than templates, so it can be tested.

## Theme

`docs/stylesheets/defra.css` holds every style. Colours are set once as custom properties at the top and reused everywhere:

| Token | Use |
| --- | --- |
| `--da-navy`, `--da-deep`, `--da-ink` | Header, headings and body text |
| `--da-green` | Links, accents and the primary action colour |
| `--da-blue`, `--da-amber`, `--da-red` | Route cards and status, never as the only way to show meaning |
| `--da-paper`, `--da-line`, `--da-card` | Backgrounds, borders and cards |

Dark mode redefines the same tokens. When you add a colour, add it as a token, check its contrast in both modes, and run the accessibility check.

Other conventions the stylesheet keeps:

- a GOV.UK-style yellow focus state on every interactive element
- links and controls at least 24 by 24 pixels (WCAG 2.2 target size)
- secondary text and code highlighting at 4.5:1 contrast or more
- guardrail ids never break across lines

## Components

| Component | Where | How to use it |
| --- | --- | --- |
| **Must, Should and Could badges** | Guardrails | `<span class="rfc rfc--must">Must</span>`. The build checks each guardrail has one. |
| **Status tags** | Guardrails and patterns | Generated from `status` metadata: draft, endorsed or deprecated |
| **"To be confirmed" box** | Any page | `!!! warning "To be confirmed"` with a `**TODO:**` line. Listed on the open questions page. |
| **Information and notes** | Any page | `!!! info` for who something applies to or where to go instead, `!!! note` for context. Keep them short. |
| **Lead paragraph** | Top of every page | `<p class="lead">` - one or two sentences saying what the page is for |
| **Route cards and cascade** | Home page | Defined in `docs/index.md`. The whole card is clickable through its heading link. |
| **Diagrams** | Any page | Mermaid, with `accTitle` and `accDescr` - see [content style](content-style.md#diagrams) |

## Interactive tools

`docs/javascripts/site.js` runs the guardrail library filters and the decision check. Each tool:

- starts from Material's page-change event, because instant navigation swaps pages without a full reload
- checks its own markup is on the page before doing anything
- works with a keyboard and labels every control
- leaves the content readable without JavaScript

## Publishing

Merges to `main` are built and published to GitHub Pages once every check passes. CSS and JavaScript addresses include a hash of their content, so browsers never mix an old stylesheet with new pages. Releases are tagged and get a PDF of every guardrail - see [releases and versions](../about/releases.md).
