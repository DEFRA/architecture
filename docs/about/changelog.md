# What's new

<p class="lead">Significant changes to guardrails, capabilities and governance. Minor wording changes are visible in the <a href="https://github.com/howellsr/architecture/commits/main">commit history</a>.</p>

## October 2026

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
