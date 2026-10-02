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
| `docs/principles/` | DDTS doctrine and architecture principles | Chief Architect and CDIO office |
| `docs/guardrails/*.md` | Guardrails. The guardrail library is built from these and the principles. | Architects |
| `capabilities/*.yaml` | Business and technology capability models | Business and enterprise architects |
| `nfrs/*.yaml` | Service tiers and the NFR catalogue | Solution architects |
| `registers/*.yaml` | Approval status of each section and the exception register | Architecture team |
| `CHANGELOG.md` | Releases and their version numbers | Site maintainers |
| `scripts/` | Release PDF, release notes and the redirect generator for moving the site | Site maintainers |
| `delivery/*.yaml` | The delivery lifecycle (artefacts and governance for each phase) and the platforms teams can use | Architects and platform teams |
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

Then add its metadata to the `guardrails:` block in the page's front matter:

```yaml
guardrails:
  GR-HOST-08:
    phases: [alpha, beta, live]
    evidence: What a team shows to prove they meet it
    evidence_by_phase:               # required for a Must, for every phase it applies in
      alpha: The design or plan that shows it
      beta: What was built and tested
      live: How it is operated and reviewed
    automated_check: manual          # or describe the automated check
    service_standard_points: [11]    # only where the link is clear
    tcop_points: [5]
    sbd_principles: []
    since_version: 0.2.0             # the release it first appears in
```

| Field | What it holds |
| --- | --- |
| `status` | `draft`, `endorsed` or `deprecated`. Endorsed means approved by the [Technology Governance Board](../governance/tgb.md). |
| `phases` | When the guardrail applies: any of `discovery`, `alpha`, `beta`, `live` |
| `evidence` | What a team shows to prove they meet it, in general. **Required for every Must** - the build fails without it. Used wherever no phase-specific evidence is given. |
| `evidence_by_phase` | What to show in each phase or lifecycle event: `discovery` (intent or constraint identified), `alpha` (design or plan), `beta` (built and tested), `live` (operated and reviewed), `significant-change` and `retire`. **A Must needs an entry for every phase it applies in**, and for `significant-change` or `retire` if it is listed for them in `delivery/lifecycle.yaml`. Only list a phase in `phases` if a team can do or show something for the guardrail in that phase. |
| `automated_check` | How it can be checked automatically, or `manual` |
| `service_standard_points` | [Service Standard](https://www.gov.uk/service-manual/service-standard) points (1 to 14) it helps meet. Leave out unless the link is clear. |
| `tcop_points` | [Technology Code of Practice](https://www.gov.uk/guidance/the-technology-code-of-practice) points (1 to 13) |
| `sbd_principles` | [Secure by Design principles](https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/) (1 to 10) |
| `doctrine` | DDTS doctrine anchors, such as `ddts-02`. Leave out to use the doctrine the page's principles apply. |
| `owner` | The team that maintains it |
| `last_reviewed` | Date it was last reviewed |
| `since_version` | Site [release](../about/changelog.md) it first appeared in |
| `replaced_by` | For deprecated guardrails, the id that replaces it |

`status`, `owner`, `automated_check`, `last_reviewed` and `since_version` usually come from `guardrail_defaults` at the top of the front matter. Set them on a guardrail only where it differs.

- Use the next unused number for that area, and **never reuse, renumber, rename or delete an id** - ids are cited in contracts. To retire a guardrail, set `status: deprecated` and `replaced_by`.
- The level is `rfc--must`, `rfc--should` or `rfc--could`.
- The guardrail library, home page figures, `guardrails.json` and NFR links update automatically. The build fails if the id and anchor do not match, the badge or metadata is missing, or a Must has no evidence.

### Add or change an NFR or service tier

Edit `nfrs/catalogue.yaml` or `nfrs/service-tiers.yaml`. Comments at the top of each file explain every field. The build checks that ids are unique, that targets use real tiers and that linked guardrails exist.

### Change the delivery lifecycle or platforms

Edit `delivery/lifecycle.yaml` or `delivery/platforms.yaml`. Which guardrails apply in each phase comes from the guardrails' `phases` metadata, not from this file. For a platform detail that is not known yet, write `tbc` - the page then shows "To be confirmed" and adds it to the open questions.

### Change the capability model

Edit `capabilities/business-capabilities.yaml` or `capabilities/technology-capabilities.yaml`. The map, catalogue and mapping matrix are generated from them.

### Change the doctrine or principles

The doctrine is in `docs/principles/doctrine.md` and the principles in `docs/principles/architecture-principles.md`. Keep the heading shapes (`## 1. Title {#ddts-01}` and `## GR-PRIN-01 Title {#gr-prin-01}`) - the tests and home page figures rely on them. Changes need TGB approval.

### Link a guardrail page to the principles

Every guardrail page lists the principles it puts into practice in its front matter, for example `principles: [GR-PRIN-05, GR-PRIN-06]`. Which principles apply each doctrine is set in the `applies:` front matter of `docs/principles/doctrine.md`. The site builds the breadcrumbs and coverage table from these, and the build fails if a page is not linked.

### Release a version

Move the entries under `## [Unreleased]` in `CHANGELOG.md` to a new `## [X.Y.Z] - YYYY-MM-DD` section, choosing the number with the [versioning policy](../partners/contracting.md#versioning-policy), and leave an empty `## [Unreleased]` above it. When the change is merged, the release workflow tags the commit, builds the site and attaches a PDF of every guardrail to a GitHub release. Also update [what's new](../about/changelog.md).

### Record an approval or an exception

Update `registers/approvals.yaml` when a section is endorsed, or add an approved exception to `registers/exceptions.yaml`. The [approval status](../about/approval-status.md), [exception register](../governance/exception-register.md) and [guardrails health](../governance/guardrails-health.md) pages are built from them, and the build checks ids, dates and guardrails.

### Say who guardrails apply to

Every guardrail page has `applicability:` in its front matter - who the guardrails apply to, such as the core department and arm's length bodies. Write `tbc` until it is agreed: the page then shows a "To be confirmed" box.

### Mark a page as draft

Add `status: draft` to the page's front matter. The page shows a "Draft - to be confirmed" banner and a marker in the navigation. Remove the line once the content is agreed. To list draft pages, run `grep -rl "status: draft" docs`.

### Add a pattern

Copy an existing page in `docs/patterns/` and keep its sections: context, solution (with a diagram), guardrails it helps you meet, related Secure by Design artefacts, and when not to use it. Set the front matter:

```yaml
pattern:
  category: integration      # infrastructure, integration, security or data
  status: proposed           # proposed, draft or endorsed
  summary: One sentence saying when to use it.
  guardrails: [GR-API-05, GR-API-06]
  sbd: [stride-template]     # artefact keys listed in hooks/patterns.py
```

Keep the `<!-- patterns:guardrails -->` and `<!-- patterns:sbd -->` markers where those sections go. The build fills them in, adds the pattern to the [catalogue](../patterns/index.md), and fails if a guardrail id is unknown. Add the page to `nav` in `mkdocs.yml`.

### Flag a fact that is not confirmed

Do not guess Defra facts such as names, contacts, URLs, lead times or approvals. Write a visible box instead:

```markdown
!!! warning "To be confirmed"
    **TODO:** who approves access requests, and how long it takes.
```

Every box is listed on the [open questions](../about/open-questions.md) page. Delete the box once the fact is confirmed.

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

Every pull request runs these checks. You can run them locally before you push:

| Check | Command | What it catches |
| --- | --- | --- |
| Lint | `ruff check hooks tests scripts tools`, `ruff format --check hooks tests scripts tools` and `npm run lint` | Python and JavaScript style, following the [Defra software development standards](https://defra.github.io/software-development-standards/) |
| Content | `pytest` | Broken references between doctrine, principles, guardrails, capabilities and NFRs; diagrams without text alternatives |
| Build | `mkdocs build --strict` | Broken links and anchors, invalid data, missing pages |
| Accessibility | `npm ci && npx playwright install chromium && npm test` (after a build) | WCAG 2.2 AA failures on every page in light and dark mode |

Merges to `main` are published to [howellsr.github.io/architecture](https://howellsr.github.io/architecture/) once all checks pass. A separate weekly job checks every external link and opens an issue if any are broken.

## What not to publish

This is a public repository. Do not include:

- secrets, credentials, internal hostnames or IP addresses
- detailed security vulnerabilities or threat model detail for live services
- personal information, other than names of people who have agreed to be named
- commercially sensitive information
