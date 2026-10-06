# Changelog

All notable changes to the Defra architecture site are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the site uses [semantic versioning](https://semver.org/):

- **major** - a new or stricter Must guardrail, or a Must deprecated or relaxed (from 1.0.0; while the site is in alpha these are minor changes)
- **minor** - new Should or Could guardrails, new guidance or new pages
- **patch** - clearer wording that does not change what is required, and fixes

A plain-English summary is on the site's [what's new](https://defra.github.io/architecture/about/changelog/) page. See [contracting with this site](https://defra.github.io/architecture/partners/contracting/) for how to cite a version.

To release a version, change `## [Unreleased]` to `## [X.Y.Z] - YYYY-MM-DD` and add a new empty `## [Unreleased]` section above it. When that change reaches `main`, the release workflow tags the commit `vX.Y.Z`, builds the site and attaches a PDF of every guardrail to a GitHub release. It does nothing while the `Unreleased` section has entries, because `main` then holds changes that are not in the latest version.

## [Unreleased]

### Added

- A guide for the team on updating the site, linked from the contribute page: how it is built, the rules every change follows, which file to edit and how to fix a failed check.
- `CLAUDE.md` with the repository's ground rules, layout, commands and gotchas for AI assistants, kept under 80 lines by a test.
- Issue forms for a new pattern, answering an open question and feedback by role, and a pull request checklist covering unchanged ids, the changelog, checks and \"To be confirmed\" boxes. Tests keep the feedback roles in step with `delivery/roles.yaml`.
- Site design page for maintainers: hooks, templates, theme tokens, components and interactive tools, with a test that every hook is described.
- Content style page with house rules, how to write a guardrail and a pattern, diagrams and a glossary. A prose job on pull requests reports Vale findings and headings not in sentence case as warnings.
- `MAINTAINERS.md`, `.github/CODEOWNERS` and `.github/labels.yml`, with tests that every label used is defined. CI warns about guardrails whose `last_reviewed` date is more than 12 months old.
- Where things live: the site, repository, Issues, GitHub Project, Discussions and releases, and why the GitHub wiki is not used. A test fails on links to a wiki.
- Draft services and capabilities page, using the definitions from Defra's service taxonomy and showing where the handrail fits.
- Draft guardrails `GR-DATA-10` (research data), `GR-DATA-11` (no real personal data in prototypes) and `GR-FE-07` (tell users what is happening when things fail or are slow), all Shoulds, with evidence for each phase.
- "What users see", "Content to design" and "What to test with users" sections in every pattern and the worked example, with `user_experience` pattern metadata (`written` or `tbc`) checked by the build and shown in the pattern catalogue.

### Changed

- Business capabilities no longer list the technology capabilities that enable them; the page points to capability mapping, the one place that draft mapping is shown. Outcomes and level 2 capabilities now sit side by side.
- Reference architectures are now service patterns, in the Patterns section alongside the solution patterns, and are marked as exploratory early work. Overclaims such as "proven" and lighter governance are removed. Old addresses redirect through a new `redirects.py` hook. The term "reference architecture" is kept for a future layered view.
- Contribute and the decisions about this site are no longer in the top navigation, to keep it simple for users. The pages are still published at their addresses for the team.
- Technology capabilities follow Defra's Technology Business Management (TBM) model: level 1 areas and level 2 capabilities in `capabilities/technology-capabilities.yaml`, shown as a map. TC01 to TC24, their statuses and options are removed pending internal review. Business capabilities, platforms, guardrails, reference architectures and the mapping matrix point to level 2 capabilities. The boxes page is folded in. Tests check ids are unique and platforms name a level 2 capability.
- The accessibility check runs light and dark mode in two parallel jobs, so CI finishes about a minute sooner. Set `A11Y_SCHEMES` to check one scheme locally.
- Only `DEFRA/architecture` deploys the site, makes releases and runs the weekly link check. A fork runs the checks but cannot overwrite its own `gh-pages` branch, which serves redirects to the new address. A test keeps these workflows limited to `DEFRA/architecture`.
- The site moved to the DEFRA GitHub organisation: source at `DEFRA/architecture`, published at https://defra.github.io/architecture/. Every link, the issue forms, the guardrail check and the link-check settings point to the new address. Version 0.2.0 stays at https://github.com/howellsr/architecture/releases/tag/v0.2.0. See ADR 0006.
- Architecture decisions for review are emailed to StrategicEnterpriseArchitecture@defra.gov.uk, replacing the alpha holding address noreply@defra.gov.uk.

### Fixed

- The site publishes from `howellsr/architecture` again until the move to `DEFRA/architecture` is complete. The fork guard had stopped it deploying since 2 October.
- CI could not install its JavaScript tools after Dependabot moved ESLint to version 10, which the neostandard lint rules do not support yet. ESLint is back on version 9, Dependabot no longer proposes a new major version of ESLint, and a test checks the two stay compatible.
- The link check no longer fails on GitHub errors it cannot avoid: Secure by Design library files are checked at their raw address, folders in that library and this repository's own releases page are skipped, and the Defra Digital Service Manual step checks only manual links. Tests keep these settings in place.
- Abbreviation tooltips appeared inside guardrail ids such as GR-API-05, and next to their own expansion, where screen readers could announce it twice. The build now removes them and fails if any are left.
- The open questions page asked whether the guardrails apply to arm's length bodies 15 times, once for each area. It is now one question on the guardrails overview.
- Getting onto Defra platforms links GOV.UK Pay's support page instead of "To be confirmed".

## [0.2.0] - 2026-10-02

The first release with a PDF of every guardrail attached.

### Added

- Where things live page, setting out what belongs on this site and what belongs in the Defra Digital Service Manual, with matching links checked by a test and a link check.
- Developing architecture at Defra page: roles and skills, the Architecture Community and All Architecture meetups.
- Structured metadata for every guardrail: status, phases, evidence, automated check, Service Standard, Technology Code of Practice and Secure by Design mappings, doctrine, owner, last reviewed and version introduced. The build fails if a Must has no evidence.
- Guardrail library filters for phase and status, and `guardrails.json`.
- Open questions page, generated from "To be confirmed" boxes.
- Deliver a service section: phase pages, evidence checklists and getting onto Defra platforms.
- Patterns section, a worked licence example and proposed reference architectures for field inspection, incident response and grants.
- Delivery partners section: contracting, mobilisation, handover and exit, and working with other suppliers.
- Draft guardrails: `GR-DEV-09` (ADRs), `GR-AI-07` (supplier AI coding assistants), `GR-AI-08` to `GR-AI-11` (agentic AI), `GR-PROD-01` to `GR-PROD-04` (products and platforms), `GR-DIG-01` to `GR-DIG-03` (digital first) and `GR-FIELD-01` to `GR-FIELD-04` (field working and devices).
- Links from the handrail to Defra's tools radar and the Emerging Technology Radar 2026.
- Working with architects page for designers and researchers, and the architect's place in a multidisciplinary team on the team page.
- `lead_roles` guardrail metadata naming the DDaT roles that lead each guardrail, a role filter in the library, and a page for each role under Deliver a service.
- `evidence_by_phase` guardrail metadata, with phase-specific evidence for every Must, used on phase pages and checklists.
- A GitHub Action, `tools/guardrail-check`, that checks a repository against GR-OPEN-02, GR-DEV-08, GR-API-02, GR-OPEN-03, GR-DEV-03, GR-DEV-06 and GR-DEV-09.
- Architecture decision records for this site in `docs/adr`.
- Versioned releases with a PDF of every guardrail, a "version in force" banner, approval status, the exception register, guardrails health and applicability notes for each guardrail area.

### Changed

- Guardrails GR-AI-01, GR-AI-02, GR-AI-07 to GR-AI-11, GR-FE-01, GR-FE-02, GR-FE-04, GR-FE-06, GR-SUS-01, GR-SUS-05 and GR-HOST-01 link to the matching pages of the Defra Digital Service Manual. Secure by Design defers to the DDTS Portfolio Hub lifecycle requirements. Getting onto Defra platforms no longer lists GOV.UK One Login separately, because Defra services use it through Defra Customer Identity. The home page describes the DDTS doctrine as draft until the approvals register records it as endorsed.
- TDA and TGB decisions are recorded in an architecture decision register on the Defra architecture SharePoint site, raised by email, instead of in this repository. Team ADRs stay in service repositories. See ADR 0005.
- Aligned with the Defra Digital Service Manual: `GR-IAM-01` names Defra Customer Identity (Defra ID); `GR-DEV-01` follows the manual's approved technologies; `GR-AI-02` follows the AI digital toolkit's data rules; Deliver a service, governance, platforms, NFRs, patterns and the security, accessibility and sustainability guardrail pages link to the manual instead of repeating it. Platforms now include the Defra Interactive Map.
- Fewer Must guardrails: 26 Musts became Shoulds, leaving 29 Musts. A guardrail is now a Must only where law or mandatory government policy requires it, it is a baseline security control, or it puts a DDTS doctrine non-negotiable into practice. The new Shoulds are `GR-AI-05`, `GR-AI-06`, `GR-AI-08` to `GR-AI-11`, `GR-API-02`, `GR-API-04`, `GR-API-05`, `GR-TECH-03`, `GR-DATA-01` to `GR-DATA-03`, `GR-FIELD-03`, `GR-HOST-02`, `GR-HOST-03`, `GR-HOST-06`, `GR-HOST-07`, `GR-OPS-01`, `GR-OPS-02`, `GR-OPEN-02`, `GR-OPEN-03`, `GR-SEC-08`, `GR-DEV-03`, `GR-DEV-04` and `GR-DEV-06`.
- Governance names the Portfolio Assurance Board (PAB) for spend control and InvestCo for investment approvals.
- When Must guardrails apply: `GR-DATA-02` now also applies in discovery; `GR-HOST-02`, `GR-OPEN-01` and `GR-SEC-09` no longer apply in discovery; `GR-HOST-03`, `GR-IAM-02`, `GR-IAM-03`, `GR-OPS-02`, `GR-SEC-04`, `GR-SEC-05`, `GR-DEV-04` and `GR-DEV-06` no longer apply in alpha.

### Fixed

- The open questions page listed the example "To be confirmed" box from the contribution guide as a real question.
- Applicability notes lower-cased acronyms in area names, such as "apis and integration".
- The guardrails page described ten architecture principles; there are eight.
- The self-assurance checklist mapped ADRs to a principle rather than a guardrail.

## [0.1.0] - 2026-10-01

Baseline: the site as first published in alpha, up to and including commit `93279cc`. This version has no archived PDF; the first release with one is 0.2.0.

### Added

- DDTS doctrine, Defra's eight architecture principles and 82 guardrails across 12 areas, with stable ids.
- Non-functional requirements: service tiers and the NFR catalogue.
- The handrail: business and technology capability models, capability mapping and three reference architectures.
- Governance (TGB, TDA and solution design authorities), the decision check, ADR guidance, exceptions and templates.
- Enterprise data and security architecture.
- Traceability from doctrine to principles to guardrails, the guardrail backlog and roadmap.
