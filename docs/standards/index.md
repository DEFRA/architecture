# Standards and links

<p class="lead">The government and Defra standards this site builds on. Our guardrails apply these to Defra's context - they do not replace them.</p>

## Defra

| Resource | What it is |
| --- | --- |
| [Defra Digital Service Manual](https://digital.defra.gov.uk/service-manual) | How Defra designs, builds and runs digital services, including service assessments |
| [Defra software development standards](https://defra.github.io/software-development-standards/) | Detailed engineering practice: languages, coding style, testing, source control, versioning and release |
| [Defra Digital blog](https://defradigital.blog.gov.uk/) | What Defra digital, data and technology teams are working on and learning |
| [Defra on GitHub](https://github.com/DEFRA) | Defra's open source code |
| [Defra Data Services Platform](https://environment.data.gov.uk/) | Defra group open and shared data |

## Government standards

| Standard | Why it matters | Where we apply it |
| --- | --- | --- |
| [Service Standard](https://www.gov.uk/service-manual/service-standard) | The 14 points every government service is assessed against | Throughout, especially [principles](../principles/architecture-principles.md) |
| [Technology Code of Practice](https://www.gov.uk/guidance/the-technology-code-of-practice) | Criteria for designing, building and buying technology, used in spend control | Mapped below |
| [Secure by Design](https://www.security.gov.uk/policy-and-guidance/secure-by-design/) | Government approach to security in digital delivery | [Secure by Design in Defra](../security/secure-by-design.md) |
| [GOV.UK Service Manual](https://www.gov.uk/service-manual) | How to deliver government services | Alongside the Defra Digital Service Manual |
| [GOV.UK Design System](https://design-system.service.gov.uk/) | Styles, components and patterns | [Front end guardrails](../guardrails/front-end-and-accessibility.md) |
| [API technical and data standards](https://www.gov.uk/guidance/gds-api-technical-and-data-standards) | How to build government APIs | [APIs and integration](../guardrails/apis-and-integration.md) |
| [Cloud First policy](https://www.gov.uk/guidance/government-cloud-first-policy) | Default to public cloud | [Hosting and platforms](../guardrails/hosting-and-platforms.md) |
| [AI Playbook for the UK Government](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government) | Safe and effective use of AI | [AI guardrails](../guardrails/ai.md) |
| [Greening Government ICT and Digital Services strategy](https://www.gov.uk/government/publications/greening-government-ict-and-digital-services-strategy-2020-2025) | Sustainable technology | [Sustainability guardrails](../guardrails/sustainability.md) |
| [Government Data Quality Framework](https://www.gov.uk/government/publications/the-government-data-quality-framework) | Managing data quality | [Data guardrails](../guardrails/data.md) |
| [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/cyber-assessment-framework) | Assessing cyber resilience (GovAssure) | [Security](../security/index.md) |

## Technology Code of Practice mapping

How the 13 points of the [Technology Code of Practice](https://www.gov.uk/guidance/the-technology-code-of-practice) map to this site.

| TCoP point | Defra guidance |
| --- | --- |
| 1. Define user needs | [GR-PRIN-02](../principles/architecture-principles.md#gr-prin-02); [Defra Digital Service Manual](https://digital.defra.gov.uk/service-manual) |
| 2. Make things accessible and inclusive | [Front end and accessibility](../guardrails/front-end-and-accessibility.md) |
| 3. Be open and use open source | [Open source and working in the open](../guardrails/open-source.md) |
| 4. Make use of open standards | [GR-TECH-05](../guardrails/choosing-technology.md#gr-tech-05), [data standards](../data/data-standards.md) |
| 5. Use cloud first | [Hosting and platforms](../guardrails/hosting-and-platforms.md) |
| 6. Make things secure | [Security guardrails](../guardrails/security.md), [Secure by Design](../security/secure-by-design.md) |
| 7. Make privacy integral | [GR-DATA-06](../guardrails/data.md#gr-data-06) |
| 8. Share, reuse and collaborate | [Handrail](../handrail/index.md), [GR-TECH-01](../guardrails/choosing-technology.md#gr-tech-01) |
| 9. Integrate and adapt technology | [APIs and integration](../guardrails/apis-and-integration.md) |
| 10. Make better use of data | [Data architecture](../data/index.md) |
| 11. Define your purchasing strategy | [Choosing technology](../guardrails/choosing-technology.md) |
| 12. Make your technology sustainable | [Sustainability](../guardrails/sustainability.md) |
| 13. Meet the Service Standard | [Governance](../governance/index.md); [Defra Digital Service Manual](https://digital.defra.gov.uk/service-manual) |

## Cross-government architecture

Other parts of government publish architecture in the open. We reuse their models and approaches rather than inventing our own.

| Resource | What it is | How it relates to this site |
| --- | --- | --- |
| [Secure by Design artefact library](https://github.com/co-cddo/SbD) | Reusable security patterns, blueprints, checklists and threat models, run in the open on GitHub | Linked from [Secure by Design in Defra](../security/secure-by-design.md) and [threat modelling](../security/threat-modelling.md) |
| [OCTO architecture resources](https://architecture.cddo.cabinetoffice.gov.uk/) | Cross-government enterprise architecture from the Office of the Government CTO: capability model, reference architectures, self-assessment tools and AI enablement | The home of the models below |
| [Digital Technology Capability Model](https://architecture.cddo.cabinetoffice.gov.uk/digital-capability-model/index.html) | A six-level common language for a department's technology landscape | Every [technology capability](../handrail/technology-capabilities.md) is tagged with its level |
| [Citizen Facing Reference Architecture](https://architecture.cddo.cabinetoffice.gov.uk/citizen-architecture/CF.html) | How citizen-facing government services fit together, from channels to infrastructure | Our [transactional service](../handrail/reference-architectures/transactional-service.md) reference architecture is Defra's detailed view of it |
| [Architecture maturity self-assessment](https://architecture.cddo.cabinetoffice.gov.uk/Tools/index.html) | A 10-minute self-assessment of architecture practice across 14 dimensions | Use it to assess an architecture team or SDA; see the [roadmap](../about/roadmap.md) |
| [AI technology enablement](https://architecture.cddo.cabinetoffice.gov.uk/psai-tech/index.html) | AI risk toolkit, assurance questionnaire and governance operating model | Linked from the [AI guardrails](../guardrails/ai.md) |
| [Local Government Architecture Model](https://architecture.cddo.cabinetoffice.gov.uk/gds-local/) | GDS Local's layered model of the technology councils use, from public channels and shared components down to service and corporate systems | Inspired our [technology stack view](../handrail/technology-capabilities.md#the-technology-stack-at-a-glance). Useful where Defra services work with councils, such as planning, waste and environmental health |
| [Government data architecture](https://data-architecture.datamarketplace.gov.uk/) | Cross-government data architecture guidance from the Data Marketplace | Complements our [data architecture](../data/index.md) and [data standards](../data/data-standards.md) |
| [Lightweight architecture for learning at pace](https://technology.blog.gov.uk/2026/08/28/lightweight-architecture-for-learning-at-pace/) | Government Technology blog post on lightweight, trust-based architecture practice | Reflected in our [advice-first governance](../governance/index.md#seek-advice-not-permission) |

## Inspiration

We have learned from other departments working in the open, in particular the [DfE architecture site](https://dfe-digital.github.io/architecture/). Thank you.
