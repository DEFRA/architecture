<!-- https://defra.github.io/architecture/deliver/ | maturity: prototype | site version 0.3.0 | generated from deliver/index.md -->

# Deliver a service

<p class="lead">What architecture your team needs at each stage of delivery: the guardrails that apply, the artefacts to produce, who to talk to and the evidence to bring to an assessment.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



This section is for delivery team leads, product managers, architects and delivery partners. It covers the **architecture** evidence only. The [Defra Digital Service Manual](https://digital.defra.gov.uk/service-manual) is the place for how Defra delivers services, and we link to it rather than repeat it:

| For | Use the Defra Digital Service Manual |
| --- | --- |
| When services are assessed (after alpha, private beta and public beta), and how to book | [Service assessments](https://digital.defra.gov.uk/service-assessments) and [book an assessment](https://digital.defra.gov.uk/service-assessments/book-an-assessment) |
| What assessors ask | [Assessment questions](https://digital.defra.gov.uk/service-assessments/assessment-questions) |
| Getting ready to run a live service, including the operational service design review board at the start of beta | [Operational service readiness](https://digital.defra.gov.uk/delivery-groups/follow-delivery-governance/assurance/operational-service-readiness) |
| Recording and approving spend | [Spend control](https://digital.defra.gov.uk/delivery-groups/follow-delivery-governance/assurance/spend-control) |
| Who decides what in a delivery group | [Governance model](https://digital.defra.gov.uk/delivery-groups/follow-delivery-governance/governance-model) |
| Designing, researching and writing content | [Design](https://digital.defra.gov.uk/design), [user research](https://digital.defra.gov.uk/user-research) and [content design](https://digital.defra.gov.uk/content) |
| Building on Defra's common tools and approved technologies | [Architecture](https://digital.defra.gov.uk/architecture) and [software development](https://digital.defra.gov.uk/software-development) |

This site adds what is specific to architecture: the guardrails, the decisions to record and the architecture evidence for each phase.

```mermaid
flowchart LR
    accTitle: The delivery lifecycle
    accDescr: A service moves from discovery to alpha, beta and live. A live service can go through significant change, which loops back through design, and is eventually retired.
    D["Discovery"] --> A["Alpha"] --> B["Beta"] --> L["Live"]
    L -->|"significant change"| C["Significant change"]
    C --> L
    L --> R["Retire"]
```

## Phases and events

| Phase | Guardrails | Must | Key artefacts | Checklist |
| --- | ---: | ---: | --- | --- |
| [Discovery](https://defra.github.io/architecture/deliver/discovery/) | 24 | 9 | Architecture decision record (ADR) log, C4 system context diagram, Service tier, Data protection impact assessment (DPIA) | [Checklist](https://defra.github.io/architecture/deliver/checklists/discovery/) |
| [Alpha](https://defra.github.io/architecture/deliver/alpha/) | 73 | 18 | Architecture decision record (ADR) log, C4 system context diagram, C4 container diagram, Threat model | [Checklist](https://defra.github.io/architecture/deliver/checklists/alpha/) |
| [Beta](https://defra.github.io/architecture/deliver/beta/) | 84 | 25 | Architecture decision record (ADR) log, C4 container diagram, Threat model, Data protection impact assessment (DPIA) | [Checklist](https://defra.github.io/architecture/deliver/checklists/beta/) |
| [Live](https://defra.github.io/architecture/deliver/live/) | 77 | 25 | Architecture decision record (ADR) log, C4 container diagram, Threat model, Runbooks and support model | [Checklist](https://defra.github.io/architecture/deliver/checklists/live/) |
| [Significant change](https://defra.github.io/architecture/deliver/significant-change/) | 12 | 7 | Architecture decision record (ADR) log, C4 container diagram, Threat model, Data protection impact assessment (DPIA) | [Checklist](https://defra.github.io/architecture/deliver/checklists/significant-change/) |
| [Retire a service](https://defra.github.io/architecture/deliver/retire/) | 9 | 5 | Architecture decision record (ADR) log, Exit plan, Runbooks and support model, Data protection impact assessment (DPIA) | [Checklist](https://defra.github.io/architecture/deliver/checklists/retire/) |


Each phase has a printable **assessment evidence checklist**, built from the same guardrail data as the [guardrail library](https://defra.github.io/architecture/guardrails/library/), so they never disagree.

## Before you start

- [Working with architects](https://defra.github.io/architecture/deliver/working-with-architects/): for designers and researchers - when to involve an architect, what to bring and what to expect.
- [Guardrails by role](https://defra.github.io/architecture/deliver/roles/): the guardrails each role leads, phase by phase - for product managers, designers, researchers, developers, architects and analysts.
- [Getting onto Defra platforms](https://defra.github.io/architecture/deliver/platforms/): what the shared platforms give you, and how to get access.
- [Check your repository automatically](https://defra.github.io/architecture/deliver/guardrail-check/) against the guardrails a tool can check.
- [Check a decision](https://defra.github.io/architecture/governance/decision-check/) to find your governance route.
- [Service patterns](https://defra.github.io/architecture/patterns/service/) to start from a known-good shape.
- [Service tiers](https://defra.github.io/architecture/nfrs/service-tiers/) and the [NFR catalogue](https://defra.github.io/architecture/nfrs/catalogue/) to set your quality targets.

## The architecture artefacts

The same small set of artefacts carries through every phase. Start them light and keep them current. Assessors, solution design authorities and security teams all ask for them, so prepare them once.

| Artefact | Why |
| --- | --- |
| [Architecture decision record (ADR) log](https://defra.github.io/architecture/governance/architecture-decision-records/) | Shows what you decided and why ([GR-DEV-09](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-09)) |
| C4 context and container diagrams | Show the service, its users, dependencies and building blocks. See the [C4 model](https://c4model.com/). |
| [Threat model](https://defra.github.io/architecture/security/threat-modelling/) | Shows what can go wrong and what you are doing about it ([GR-SEC-02](https://defra.github.io/architecture/guardrails/security/#gr-sec-02)) |
| Data protection impact assessment (DPIA) | Shows personal data is handled lawfully ([GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06)) |
| [Service tier](https://defra.github.io/architecture/nfrs/service-tiers/) and [NFRs](https://defra.github.io/architecture/nfrs/catalogue/) | Set how reliable, fast and recoverable the service must be |
| Exit plan | Shows how Defra could change product or supplier ([GR-TECH-03](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03)) |
| Runbooks and support model | Show the service can be run by people who did not build it ([GR-OPS-05](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05)) |

