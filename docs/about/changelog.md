# What's new

<p class="lead">Significant changes to guardrails, capabilities and governance. Minor wording changes are visible in the <a href="https://github.com/howellsr/architecture/commits/main">commit history</a>.</p>

## October 2026

### For the CDIO: versions, approvals and health

- **Versioned releases.** The site now has [releases](releases.md) with semantic version numbers, recorded in `CHANGELOG.md`. Each release is tagged and has a PDF of every guardrail attached, to cite in contracts. The banner on every page shows the version in force.
- **[Approval status](approval-status.md)** of each section of the site, and who approved it.
- **[Exception register](../governance/exception-register.md)** and **[guardrails health](../governance/guardrails-health.md)**: exceptions per guardrail, exceptions expiring soon and guardrails that are candidates to change, reviewed every quarter.
- **Who guardrails apply to:** each guardrail area now says whether it applies to arm's length bodies as well as the core department. These are still to be confirmed.
- **New draft guardrails** from the high-priority backlog: [products and platforms](../guardrails/products-and-platforms.md), [digital first and end-to-end services](../guardrails/digital-first.md), [field working and devices](../guardrails/field-working-and-devices.md) and [agentic AI](../guardrails/ai.md#gr-ai-08).
- **[Moving this site to a Defra GitHub organisation](moving-to-defra.md):** the plan, including redirects so links in contracts keep working.

### Delivery partners

- **[Delivery partners](delivery-partners.md) is now a section**, with new pages on [contracting with this site](../partners/contracting.md) (versioning policy, how to cite a version, model clauses and an annex of every Must), a [mobilisation checklist](../partners/mobilisation.md), [handover and exit](../partners/handover-and-exit.md) and [working with other suppliers](../partners/multi-supplier.md).
- **New draft guardrail [GR-AI-07](../guardrails/ai.md#gr-ai-07):** suppliers use AI coding assistants openly and safely, in line with GR-AI-02. Comments welcome.

### Patterns and a worked example

- **New [Patterns](../patterns/index.md) section**, modelled on the Department for Education's: asynchronous submission with an outbox, acting on behalf of an organisation or holding, file upload with malware scanning, reading from an authoritative source, and publishing open data with metadata. Each lists the guardrails it helps you meet and related Secure by Design artefacts.
- **[Worked example: apply for a licence](../patterns/worked-example/index.md):** a fictional service taken through the transactional reference architecture, with C4 context and container diagrams, [three sample ADRs](../patterns/worked-example/adrs.md) and a [threat model excerpt](../patterns/worked-example/threat-model.md).
- **Proposed reference architectures** for capabilities Defra does not yet have a strategic solution for: [field inspection](../handrail/reference-architectures/field-inspection.md), [incident response](../handrail/reference-architectures/incident-response.md) and [grants and schemes](../handrail/reference-architectures/grants.md).

### Deliver a service

- **New [Deliver a service](../deliver/index.md) section:** one page for each phase - discovery, alpha, beta and live - and for significant change and retiring a service. Each lists the guardrails that apply, the architecture artefacts to produce, the governance touchpoints and the evidence pack to bring to an assessment.
- **Printable evidence checklists** for each phase, built from the guardrail metadata so they always match the guardrail library.
- **[Getting onto Defra platforms](../deliver/platforms.md):** what the Core Delivery Platform, Defra ID, GOV.UK One Login, Defra Forms, GOV.UK Notify, GOV.UK Pay, the data platform and the API gateway give you, and how to get access. Details we have not confirmed yet are listed on the [open questions](open-questions.md) page.
- The home page has two new routes: deliver a service, and get onto Defra platforms.

### Guardrail metadata

- **Every guardrail now has structured metadata:** status (draft, endorsed or deprecated), the phases it applies in, the evidence that shows you meet it, whether it can be checked automatically, the Service Standard, Technology Code of Practice and Secure by Design points it supports, the DDTS doctrine it applies, its owner and when it was last reviewed. Open **Phases, evidence and status** under any guardrail to see it.
- The [guardrail library](../guardrails/library.md) can now be filtered by phase and status, and each card shows the evidence and automated check.
- Guardrail metadata is published as `guardrails.json` for tools and dashboards.
- New guardrail [GR-DEV-09 Record significant decisions as ADRs](../guardrails/software-development.md#gr-dev-09). The self-assurance checklist now points to it instead of a principle.
- New [open questions](open-questions.md) page listing facts that are still to be confirmed.
- Fixed the guardrails page describing "ten" architecture principles - there are eight.

### Traceability, guardrail backlog and standards

- **Doctrine to guardrails:** every guardrail page now shows the doctrine and principles it applies, and the [Principles](../principles/index.md#how-the-doctrine-principles-and-guardrails-line-up) page shows coverage, including where guardrails are thin.
- **[Guardrail backlog](roadmap.md#guardrail-backlog):** guardrails we know we are missing, including the agreed Defra on a page.
- Fixed broken links to the Data Standards Authority, UK GEMINI and the Public Sector Geospatial Agreement. Links are now checked weekly.
- The repository now follows the [Defra software development standards](https://defra.github.io/software-development-standards/): pinned GitHub Actions, dependency review, grouped Dependabot updates, exact dependency versions, Ruff and neostandard linting.

### Alpha and roadmap

- The site is now marked as **alpha**, with a phase banner on every page.
- New [roadmap](roadmap.md): now, next and later, including an AI architecture facilitator agent (next), AI tools and architecture review automation (later).
- Technology capabilities are now aligned with the cross-government [Digital Technology Capability Model](https://architecture.cddo.cabinetoffice.gov.uk/digital-capability-model/index.html), with links to OCTO's citizen-facing reference architecture, self-assessment and AI enablement tools.
- Search now treats ids such as `GR-HOST-01` and `NFR-AVL-01` as single terms, so searching an id finds it first.

### DDTS doctrine

- **[DDTS doctrine](../principles/doctrine.md):** the CDIO's seven non-negotiables now sit above the architecture principles, with links to the principles and guardrails that apply them.
- **[Principles](../principles/index.md)** have their own section, showing how doctrine, principles and guardrails fit together.
- [GR-AI-01](../guardrails/ai.md#gr-ai-01) now asks teams to consider AI first, in line with the doctrine.
- Fixed the home page figures displaying incorrectly when the browser had cached an older stylesheet.
- **[Technology stack view](../handrail/technology-capabilities.md#the-technology-stack-at-a-glance):** technology capabilities shown as layers, inspired by the Local Government Architecture Model.
- **[Seek advice, not permission](../governance/index.md#seek-advice-not-permission):** the advice process is now explicit in governance, and ADRs record the advice sought.
- Links to the cross-government [Secure by Design artefact library](https://github.com/co-cddo/SbD), the Local Government Architecture Model and government data architecture guidance.

### Principles, NFRs and accessibility

- **[Architecture principles](../principles/architecture-principles.md)** now use Defra's eight agreed Strategic Architecture Principles, each linked to the guardrails that put it into practice.
- **[Non-functional requirements](../nfrs/index.md):** new section with service tiers, an NFR catalogue and guidance on writing good NFRs. Targets are draft until confirmed.
- **Accessibility:** every page is now checked against WCAG 2.2 AA in light and dark mode on each change. Fixed colour contrast, keyboard access to the home page search, touch target sizes and diagram text alternatives.
- **Draft markers:** pages awaiting confirmation now show a "Draft - to be confirmed" banner.

### Front door and tools

- **New home page** with search, "What do you need to do?" routes, the governance flow, the capability map and links to detailed guidance.
- **[Check a decision](../governance/decision-check.md):** an interactive check that suggests a governance route and drafts a decision record.
- **[Guardrail library](../guardrails/library.md):** search and filter every guardrail and principle, built automatically from the guardrail pages.
- Links to the [Defra software development standards](https://defra.github.io/software-development-standards/) for detailed coding practice.

### First release

- **New site.** First version of the Defra architecture site, published in the open.
- **Guardrails:** first set of guardrails across 13 areas, with stable ids and Must/Should/Could levels, and a 10-minute self-assurance checklist.
- **Handrail:** Defra business capability model (9 core and 2 supporting capabilities) with draft level 2 capabilities, a technology capability catalogue of 24 capabilities, a capability mapping matrix and three reference architectures. The model is published as machine-readable YAML and JSON.
- **Governance:** the three-tier model (TGB, TDA and solution design authorities), triage, ADR guidance, exception process and templates.
- **Data:** Defra on a page and data standards.
- **Security:** Secure by Design in Defra, threat modelling and managing security exceptions.
