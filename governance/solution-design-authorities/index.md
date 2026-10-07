<!-- https://defra.github.io/architecture/governance/solution-design-authorities/ | maturity: draft | site version 0.3.0 | generated from governance/solution-design-authorities.md -->

# Solution design authorities (SDAs)

<p class="lead">SDAs are where most architecture decisions are assured. They sit close to delivery, within delivery groups or portfolios, with authority delegated from the TDA. In an SDA, the principal architect is accountable for decisions.</p>

!!! warning "Draft - to be confirmed"
    Parts of this page, such as names, timings and thresholds, are still being confirmed by the architecture team. Use it as a guide, and check with your solution design authority before relying on the detail.



## Why delegate

Central boards cannot know every service well, and every hand-off adds delay. SDAs know the domain, the users and the legacy estate. Delegating to them makes governance faster and better informed - as long as they work to the same guardrails.

## What an SDA can decide

- Designs that stay **inside the guardrails** and align with a **roadmap agreed at the TDA**
- Departures from **Should** guardrails, recorded as ADRs
- Technology choices within the [supported stack](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-01)
- Architecture readiness for service assessments and phase gates

## What an SDA must escalate to the TDA

- Exceptions to **Must** guardrails
- Novel or cross-cutting work (see [triage](https://defra.github.io/architecture/governance/triage/))
- Anything outside the delegation agreed for that SDA
- Repeated deviations that suggest a guardrail should change

## Setting up an SDA

A delivery group or portfolio can request delegated authority from the TDA. It needs:

1. **A named principal architect** accountable for decisions.
2. **A terms of reference** stating its scope (which services and business capabilities) using the [SDA terms of reference outline](https://defra.github.io/architecture/governance/solution-design-authorities/#terms-of-reference-outline) below.
3. **A public ADR log** - or an internal one where publishing is not appropriate - that the TDA can see.
4. **Agreement to report** a short summary of decisions and deviations to the TDA every quarter.

Delegation is reviewed annually. An SDA that works well may have its scope widened.

## Delivery groups and principal architects

Defra delivery groups have their own [governance model](https://digital.defra.gov.uk/delivery-groups/follow-delivery-governance/governance-model), in which principal architects set the technology guardrails for the group in line with the enterprise architecture principles. The Delivery Architecture team tells each team who the principal architect for their delivery group is - see [architecture](https://digital.defra.gov.uk/architecture) in the Defra Digital Service Manual.

How the three levels fit together:

- **The [Technology Governance Board (TGB)](https://defra.github.io/architecture/governance/tgb/)** agrees strategies.
- **The [Technical Design Authority (TDA)](https://defra.github.io/architecture/governance/tda/)** is the technical decision-making authority. It agrees roadmaps, and grants authority to solution design authorities.
- **In a solution design authority**, the principal architect is accountable for decisions, as long as they align with a roadmap agreed at the TDA, follow the [architecture principles](https://defra.github.io/architecture/principles/architecture-principles/) and work within the [guardrails](https://defra.github.io/architecture/guardrails/).

A decision that would not align with the agreed roadmap, or would go outside the guardrails, goes to the TDA.

## Delivery partners and SDAs

Partner architects often present to and contribute to SDAs. The decision, though, sits with the principal architect accountable for the SDA. Partners should expect their designs to be assessed against these guardrails and should record decisions as ADRs in Defra repositories.

## Terms of reference outline

- **Scope:** services, products and business capabilities covered
- **Membership:** principal architect (chair), architects from the group, a security architect, a data architect, platform representative; product and delivery leads as needed
- **Delegated authority:** decisions it may make, with reference to this page
- **Escalation:** to the TDA, following [triage](https://defra.github.io/architecture/governance/triage/)
- **Cadence:** as needed, with a maximum 5-working-day turnaround for decisions
- **Transparency:** ADR log location; quarterly summary to the TDA

