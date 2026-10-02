# Changelog

All notable changes to the Defra architecture site are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the site uses [semantic versioning](https://semver.org/):

- **major** - a new or stricter Must guardrail, or a Must deprecated or relaxed (from 1.0.0; while the site is in alpha these are minor changes)
- **minor** - new Should or Could guardrails, new guidance or new pages
- **patch** - clearer wording that does not change what is required, and fixes

A plain-English summary is on the site's [what's new](https://howellsr.github.io/architecture/about/changelog/) page. See [contracting with this site](https://howellsr.github.io/architecture/partners/contracting/) for how to cite a version.

To release a version, change `## [Unreleased]` to `## [X.Y.Z] - YYYY-MM-DD` and add a new empty `## [Unreleased]` section above it. When that change reaches `main`, the release workflow tags the commit `vX.Y.Z`, builds the site and attaches a PDF of every guardrail to a GitHub release. It does nothing while the `Unreleased` section has entries, because `main` then holds changes that are not in the latest version.

## [Unreleased]

### Added

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
