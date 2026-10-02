# What's new

<p class="lead">Significant changes to guardrails, capabilities and governance. Minor wording changes are visible in the <a href="https://github.com/howellsr/architecture/commits/main">commit history</a>.</p>

## October 2026

### Aligned with the Defra Digital Service Manual

The [Defra Digital Service Manual](https://digital.defra.gov.uk/) is the place for how to run a service in Defra. This site now links to it rather than repeating or contradicting it, and keeps to architecture.

- **[Deliver a service](../deliver/index.md)** now points to the manual for service assessments, operational service readiness, spend control, governance, and design, research and content.
- **Sign-in ([GR-IAM-01](../guardrails/identity-and-access.md#gr-iam-01))** now names Defra Customer Identity (Defra ID), which uses GOV.UK One Login and Government Gateway, instead of presenting One Login as an alternative.
- **Approved technologies ([GR-DEV-01](../guardrails/software-development.md#gr-dev-01))** now follow the manual's software development standards and the Tools Radar.
- **AI data ([GR-AI-02](../guardrails/ai.md#gr-ai-02))** now follows the AI digital toolkit's rules on using data with AI.
- **[Non-functional requirements](../nfrs/index.md)** point to the service tiers and NFR list owned by business analysis. This site's catalogue is kept for now, with the manual taking precedence.
- **[Architecture patterns](../patterns/index.md)** are now called that, with a pointer to the manual's design patterns. The guardrails page explains that business analysis guardrails are different.
- **[Getting onto Defra platforms](../deliver/platforms.md)** links each platform to the manual, adds the Defra Interactive Map and corrects CDP support and portal links.
- [Working with architects](../deliver/working-with-architects.md) and [the architecture team](team.md) give the Delivery Architecture team's mailbox.

### Fewer Must guardrails

- **There are now 29 Must guardrails, down from 55.** A guardrail is a Must only where law or mandatory government policy requires it, it is a baseline security control, or it puts a [DDTS doctrine](../principles/doctrine.md) non-negotiable into practice. The other 26 are now Shoulds: still the strong default, but you can depart from them with a recorded reason rather than an exception. We will make guardrails Musts again where feedback and real-world experience show they need to be. See [ADR 0004](../adr/0004-musts-only-where-required.md).
- Alpha now has 18 Musts (was 37) and beta 25 (was 50).

### Spend control, investment and technology radars

- [Governance](../governance/index.md#how-this-relates-to-other-assurance) now names the Portfolio Assurance Board (PAB) for spend control and InvestCo for investment approvals.
- The [handrail](../handrail/index.md#technology-radars) links to Defra's tools radar of approved software tools, and to the Emerging Technology Radar 2026 and its four themes. Both need a Defra network connection and sign-in.

### Working with architects

- **New page: [working with architects](../deliver/working-with-architects.md)** for service designers, interaction designers, content designers and user researchers - which design decisions are also architecture decisions, when to involve an architect in each phase, what to bring and what architects do in return. Linked from the home page and Deliver a service.
- [The architecture team](team.md) page now explains the architect's place in a multidisciplinary team.

### Who leads each guardrail

- **Every guardrail now names the roles that lead it**, using DDaT role names - for example content designers lead [Welsh language support](../guardrails/front-end-and-accessibility.md#gr-fe-06), and service designers and user researchers lead [human oversight of AI](../guardrails/ai.md#gr-ai-03).
- **[Guardrails by role](../deliver/roles/index.md):** a page for each role, listing its guardrails phase by phase, the patterns that help and when to work with an architect.
- The [guardrail library](../guardrails/library.md) can now be filtered by role.

### Evidence that matches the phase

- **Every Must guardrail now says what to show in each phase**: in discovery the intent or constraint identified, in alpha the design or plan, in beta what was built and tested, and in live how it is operated and reviewed - plus what to show for a significant change or when retiring a service. The [phase pages](../deliver/index.md) and evidence checklists show the evidence for that phase, so alpha no longer asks for a published accessibility statement or the date of the last recovery test.
- **Fewer, better-placed Musts per phase.** We re-checked when each Must applies. Discovery now lists 11 Musts (was 13) and alpha 37 (was 45). Beta (50) and live (49) are unchanged.

### Automated guardrail checks

- **[Check your repository automatically](../deliver/guardrail-check.md):** a GitHub Action that checks a repository against GR-OPEN-02, GR-DEV-08, GR-API-02, GR-OPEN-03, GR-DEV-03, GR-DEV-06 and GR-DEV-09, and writes a report naming each guardrail. Each of those guardrails now names the check as its automated check.
- **[Decisions about this site](../adr/index.md):** this site now records its own architecture decisions, following GR-DEV-09.

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
