<!-- https://defra.github.io/architecture/guardrails/ | maturity: published | site version 0.3.0 | generated from guardrails/index.md -->

# Guardrails

<p class="lead">Guardrails are opinionated, good-practice defaults for designing, building and running services in Defra. They exist so teams can make good decisions quickly, without waiting for permission.</p>

## Why guardrails

Defra delivers hundreds of services across the core department and its arm's length bodies. Without shared defaults, every team solves the same problems again - hosting, identity, logging, payments - at extra cost and risk. Guardrails:

- **speed teams up** by answering common questions once
- **make governance lighter** - a design that stays inside the guardrails can be self-assured and needs no board
- **make Defra easier to work with** - delivery partners know what we expect before they start
- **reduce risk** by building in security, accessibility, data protection and sustainability from the start

Guardrails are **not** a gate.

!!! note "Not the same as business analysis guardrails"
    The [business analysis guardrails](https://digital.defra.gov.uk/business-analysis/guardrails) in the Defra Digital Service Manual are a separate quality framework for business analysis work. The guardrails on this site are architecture guardrails. They are the road with the barriers at the edge: you can drive as fast as you like in the middle.

## What the guardrails apply to

The guardrails apply to digital services and products that Defra builds, buys or runs. Some, such as [GR-IAM-02](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-02), name software as a service explicitly.

<div id="tbc-1"></div>

!!! warning "To be confirmed"
    **TODO:** which guardrails apply to commercial off-the-shelf products and to data and reporting platforms. The [architecture guidance](https://digital.defra.gov.uk/architecture) in the Defra Digital Service Manual says it may not apply to deploying commercial off-the-shelf software or building a data or reporting platform.

### Arm's length bodies {#arms-length-bodies}

<div id="tbc-2"></div>

!!! warning "To be confirmed"
    **TODO:** whether the guardrails apply to Defra's arm's length bodies as well as the core department, and any differences by area. Each area page links here until its applicability is confirmed; record the answer in that page's `applicability` front matter.

## How to read a guardrail

Each guardrail has an identifier, a level, a short rationale and a way to show you meet it.

| Level | Means | If you cannot meet it |
| --- | --- | --- |
| <span class="rfc rfc--must">Must</span> | A requirement from law or mandatory government policy, a baseline security control, or a [DDTS doctrine](https://defra.github.io/architecture/principles/doctrine/) non-negotiable. We keep these few. | You need an approved [exception](https://defra.github.io/architecture/governance/exceptions/) from the Technical Design Authority. |
| <span class="rfc rfc--should">Should</span> | The strong default. There may be good reasons to differ. | Record why in an [architecture decision record](https://defra.github.io/architecture/governance/architecture-decision-records/) and share it with your solution design authority. |
| <span class="rfc rfc--could">Could</span> | Recommended good practice. | No action needed, but we would like to know what worked better. |

Identifiers (for example `GR-HOST-01`) are stable so they can be referenced in decision records, assessments, contracts and statements of work. We never renumber, rename or delete an identifier: a guardrail that is no longer needed is marked deprecated and points to its replacement.

Under each guardrail, **Phases, evidence and status** shows:

- **status** - draft, endorsed by the [Technology Governance Board](https://defra.github.io/architecture/governance/tgb/), or deprecated
- **phases** - when it applies: discovery, alpha, beta or live
- **evidence** - what to show an assessor or your solution design authority to prove you meet it, phase by phase: in discovery the intent or constraint you identified, in alpha the design or plan, in beta what you built and tested, and in live how you operate and review it
- **led by** - the roles that make sure the team meets it, such as content designer or technical architect - see [guardrails by role](https://defra.github.io/architecture/deliver/roles/)
- **automated check** - whether it can be checked by a tool, or needs a person
- the Service Standard, Technology Code of Practice and Secure by Design points it helps you meet, and the DDTS doctrine it applies

The same data is published as <a href="../guardrails.json"><code>guardrails.json</code></a> for tools and dashboards.

## The guardrails

Search them all in the [guardrail library](https://defra.github.io/architecture/guardrails/library/), or browse by area:

| Area | What it covers |
| --- | --- |
| [Architecture principles](https://defra.github.io/architecture/principles/architecture-principles/) | The eight principles every other guardrail derives from |
| [Choosing technology](https://defra.github.io/architecture/guardrails/choosing-technology/) | Reuse, buy or build; SaaS; avoiding lock-in; exit plans |
| [Hosting and platforms](https://defra.github.io/architecture/guardrails/hosting-and-platforms/) | Cloud first, the Core Delivery Platform, environments, infrastructure as code |
| [Software development](https://defra.github.io/architecture/guardrails/software-development/) | Languages, source control, CI/CD, testing, dependencies |
| [APIs and integration](https://defra.github.io/architecture/guardrails/apis-and-integration/) | API first, open standards, events and messaging |
| [Identity and access](https://defra.github.io/architecture/guardrails/identity-and-access/) | Customer and staff identity, authorisation, secrets |
| [Data](https://defra.github.io/architecture/guardrails/data/) | Ownership, authoritative sources, standards, sharing, retention |
| [Security](https://defra.github.io/architecture/guardrails/security/) | Secure by Design, threat modelling, vulnerability management |
| [Observability and operations](https://defra.github.io/architecture/guardrails/observability-and-operations/) | Logging, monitoring, alerting, resilience and support |
| [Front end and accessibility](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/) | GOV.UK design system, WCAG 2.2 AA, progressive enhancement |
| [Open source and working in the open](https://defra.github.io/architecture/guardrails/open-source/) | Coding in the open, licensing, publishing safely |
| [Artificial intelligence](https://defra.github.io/architecture/guardrails/ai/) | Safe, lawful and transparent use of AI, including AI agents and supplier use of AI coding assistants |
| [Sustainability](https://defra.github.io/architecture/guardrails/sustainability/) | Greening government ICT and efficient design |
| [Products and platforms](https://defra.github.io/architecture/guardrails/products-and-platforms/) (draft) | Long-lived product teams, ownership, contributing to platforms, retiring products |
| [Digital first and end-to-end services](https://defra.github.io/architecture/guardrails/digital-first/) (draft) | Challenging paper processes, designing across boundaries, assisted digital |
| [Field working and devices](https://defra.github.io/architecture/guardrails/field-working-and-devices/) (draft) | Devices suited to the job, offline working, device security |

## Self-assure in 10 minutes

Use this checklist at the end of discovery, at each phase gate and before any significant change. If you can tick every box you are **inside the guardrails** and can proceed with your [solution design authority](https://defra.github.io/architecture/governance/solution-design-authorities/).

- The service maps to one or more [business capabilities](https://defra.github.io/architecture/handrail/business-capabilities/) and we have checked the [technology capabilities](https://defra.github.io/architecture/handrail/technology-capabilities/) for something to reuse
- We are hosting on a strategic platform (`GR-HOST-01`) or have an agreed exception
- Code is in a Defra GitHub organisation and public unless there is a recorded reason (`GR-OPEN-01`)
- We use the strategic identity services for customers and staff (`GR-IAM-01`, `GR-IAM-02`)
- Our APIs are documented with OpenAPI or AsyncAPI (`GR-API-02`)
- We know who owns each data set we create or use, and we use authoritative sources (`GR-DATA-01`, `GR-DATA-02`)
- We have a current threat model (`GR-SEC-02`) and a DPIA where personal data is involved (`GR-DATA-06`)
- Logs, metrics and alerts flow to the platform's observability tooling (`GR-OPS-01`)
- The service meets WCAG 2.2 AA and uses the GOV.UK Design System (`GR-FE-01`, `GR-FE-02`)
- Significant decisions are recorded as ADRs (`GR-DEV-09`)

Ticked every box? Great - carry on, and record it. Not sure, or found a gap? Use the [decision check](https://defra.github.io/architecture/governance/decision-check/) to find the right route.

## How guardrails change

Guardrails are owned by the architecture team, reviewed by the [Technical Design Authority](https://defra.github.io/architecture/governance/tda/) and approved by the [Technology Governance Board](https://defra.github.io/architecture/governance/tgb/). Anyone can propose a change:

1. Open an issue or pull request in [the repository](https://github.com/DEFRA/architecture) describing the change and why.
2. The architecture team triages it within two weeks.
3. Minor clarifications are merged directly. New or changed **Must** guardrails go to the TDA for review and to the TGB for approval.
4. Changes are listed in [what's new](https://defra.github.io/architecture/about/changelog/).

!!! info "Repeated exceptions are a signal"
    If several teams need the same exception, the guardrail is probably wrong. We review exceptions every quarter and change guardrails when they get in the way.

