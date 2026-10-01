# Changelog

All notable changes to the Defra architecture site are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the site uses [semantic versioning](https://semver.org/):

- **major** - a new or stricter Must guardrail, or a Must deprecated or relaxed (from 1.0.0; while the site is in alpha these are minor changes)
- **minor** - new Should or Could guardrails, new guidance or new pages
- **patch** - clearer wording that does not change what is required, and fixes

A plain-English summary is on the site's [what's new](https://howellsr.github.io/architecture/about/changelog/) page. See [contracting with this site](https://howellsr.github.io/architecture/partners/contracting/) for how to cite a version.

To release a version, change `## [Unreleased]` to `## [X.Y.Z] - YYYY-MM-DD` and add a new empty `## [Unreleased]` section above it. When that change reaches `main`, the release workflow tags the commit `vX.Y.Z`, builds the site and attaches a PDF of every guardrail to a GitHub release. It does nothing while the `Unreleased` section has entries, because `main` then holds changes that are not in the latest version.

## [Unreleased]

### Added

- Structured metadata for every guardrail: status, phases, evidence, automated check, Service Standard, Technology Code of Practice and Secure by Design mappings, doctrine, owner, last reviewed and version introduced. The build fails if a Must has no evidence.
- Guardrail library filters for phase and status, and `guardrails.json`.
- Open questions page, generated from "To be confirmed" boxes.
- Deliver a service section: phase pages, evidence checklists and getting onto Defra platforms.
- Patterns section, a worked licence example and proposed reference architectures for field inspection, incident response and grants.
- Delivery partners section: contracting, mobilisation, handover and exit, and working with other suppliers.
- Draft guardrails: `GR-DEV-09` (ADRs), `GR-AI-07` (supplier AI coding assistants), `GR-AI-08` to `GR-AI-11` (agentic AI), `GR-PROD-01` to `GR-PROD-04` (products and platforms), `GR-DIG-01` to `GR-DIG-03` (digital first) and `GR-FIELD-01` to `GR-FIELD-04` (field working and devices).
- New Must guardrails, all in draft: `GR-AI-08`, `GR-AI-09`, `GR-AI-10`, `GR-AI-11` and `GR-FIELD-03`.
- Versioned releases with a PDF of every guardrail, a "version in force" banner, approval status, the exception register, guardrails health and applicability notes for each guardrail area.

### Fixed

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
