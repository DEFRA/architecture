# Guardrails

<p class="lead">Guardrails are opinionated, good-practice defaults for designing, building and running services in Defra. They exist so teams can make good decisions quickly, without waiting for permission.</p>

## Why guardrails

Defra delivers hundreds of services across the core department and its arm's length bodies. Without shared defaults, every team solves the same problems again - hosting, identity, logging, payments - at extra cost and risk. Guardrails:

- **speed teams up** by answering common questions once
- **make governance lighter** - a design that stays inside the guardrails can be self-assured and needs no board
- **make Defra easier to work with** - delivery partners know what we expect before they start
- **reduce risk** by building in security, accessibility, data protection and sustainability from the start

Guardrails are **not** a gate. They are the road with the barriers at the edge: you can drive as fast as you like in the middle.

## How to read a guardrail

Each guardrail has an identifier, a level, a short rationale and a way to show you meet it.

| Level | Means | If you cannot meet it |
| --- | --- | --- |
| <span class="rfc rfc--must">Must</span> | A requirement, usually from law, government policy or a significant Defra risk. | You need an approved [exception](../governance/exceptions.md) from the Technical Design Authority. |
| <span class="rfc rfc--should">Should</span> | The strong default. There may be good reasons to differ. | Record why in an [architecture decision record](../governance/architecture-decision-records.md) and share it with your solution design authority. |
| <span class="rfc rfc--could">Could</span> | Recommended good practice. | No action needed, but we would like to know what worked better. |

Identifiers (for example `GR-HOST-01`) are stable so they can be referenced in decision records, assessments, contracts and statements of work.

## The guardrails

Search them all in the [guardrail library](library.md), or browse by area:

| Area | What it covers |
| --- | --- |
| [Architecture principles](principles.md) | The ten principles every other guardrail derives from |
| [Choosing technology](choosing-technology.md) | Reuse, buy or build; SaaS; avoiding lock-in; exit plans |
| [Hosting and platforms](hosting-and-platforms.md) | Cloud first, the Core Delivery Platform, environments, infrastructure as code |
| [Software development](software-development.md) | Languages, source control, CI/CD, testing, dependencies |
| [APIs and integration](apis-and-integration.md) | API first, open standards, events and messaging |
| [Identity and access](identity-and-access.md) | Customer and staff identity, authorisation, secrets |
| [Data](data.md) | Ownership, authoritative sources, standards, sharing, retention |
| [Security](security.md) | Secure by Design, threat modelling, vulnerability management |
| [Observability and operations](observability-and-operations.md) | Logging, monitoring, alerting, resilience and support |
| [Front end and accessibility](front-end-and-accessibility.md) | GOV.UK design system, WCAG 2.2 AA, progressive enhancement |
| [Open source and working in the open](open-source.md) | Coding in the open, licensing, publishing safely |
| [Artificial intelligence](ai.md) | Safe, lawful and transparent use of AI |
| [Sustainability](sustainability.md) | Greening government ICT and efficient design |

## Self-assure in 10 minutes

Use this checklist at the end of discovery, at each phase gate and before any significant change. If you can tick every box you are **inside the guardrails** and can proceed with your [solution design authority](../governance/solution-design-authorities.md).

- [ ] The service maps to one or more [business capabilities](../handrail/business-capabilities.md) and we have checked the [technology capabilities](../handrail/technology-capabilities.md) for something to reuse
- [ ] We are hosting on a strategic platform (`GR-HOST-01`) or have an agreed exception
- [ ] Code is in a Defra GitHub organisation and public unless there is a recorded reason (`GR-OPEN-01`)
- [ ] We use the strategic identity services for customers and staff (`GR-IAM-01`, `GR-IAM-02`)
- [ ] Our APIs are documented with OpenAPI or AsyncAPI (`GR-API-02`)
- [ ] We know who owns each data set we create or use, and we use authoritative sources (`GR-DATA-01`, `GR-DATA-02`)
- [ ] We have a current threat model (`GR-SEC-02`) and a DPIA where personal data is involved (`GR-DATA-06`)
- [ ] Logs, metrics and alerts flow to the platform's observability tooling (`GR-OPS-01`)
- [ ] The service meets WCAG 2.2 AA and uses the GOV.UK Design System (`GR-FE-01`, `GR-FE-02`)
- [ ] Significant decisions are recorded as ADRs (`GR-PRIN-10`)

Ticked every box? Great - carry on, and record it. Not sure, or found a gap? Use the [decision check](../governance/decision-check.md) to find the right route.

## How guardrails change

Guardrails are owned by the architecture team, reviewed by the [Technical Design Authority](../governance/tda.md) and approved by the [Technology Governance Board](../governance/tgb.md). Anyone can propose a change:

1. Open an issue or pull request in [the repository](https://github.com/howellsr/architecture) describing the change and why.
2. The architecture team triages it within two weeks.
3. Minor clarifications are merged directly. New or changed **Must** guardrails go to the TDA for review and to the TGB for approval.
4. Changes are listed in [what's new](../about/changelog.md).

!!! info "Repeated exceptions are a signal"
    If several teams need the same exception, the guardrail is probably wrong. We review exceptions every quarter and change guardrails when they get in the way.
