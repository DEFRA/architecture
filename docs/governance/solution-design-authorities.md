# Solution design authorities (SDAs)

<p class="lead">SDAs are where most architecture decisions are assured. They sit close to delivery, within delivery groups or portfolios, with authority delegated from the TDA.</p>

## Why delegate

Central boards cannot know every service well, and every hand-off adds delay. SDAs know the domain, the users and the legacy estate. Delegating to them makes governance faster and better informed - as long as they work to the same guardrails.

## What an SDA can decide

- Designs that stay **inside the guardrails**
- Departures from **Should** guardrails, recorded as ADRs
- Technology choices within the [supported stack](../guardrails/software-development.md#gr-dev-01)
- Architecture readiness for service assessments and phase gates

## What an SDA must escalate to the TDA

- Exceptions to **Must** guardrails
- Novel or cross-cutting work (see [triage](triage.md))
- Anything outside the delegation agreed for that SDA
- Repeated deviations that suggest a guardrail should change

## Setting up an SDA

A delivery group or portfolio can request delegated authority from the TDA. It needs:

1. **A named lead architect** accountable for decisions.
2. **A terms of reference** stating its scope (which services and business capabilities) using the [SDA terms of reference outline](#terms-of-reference-outline) below.
3. **A public ADR log** - or an internal one where publishing is not appropriate - that the TDA can see.
4. **Agreement to report** a short summary of decisions and deviations to the TDA every quarter.

Delegation is reviewed annually. An SDA that works well may have its scope widened.

## Delivery partners and SDAs

Partner architects often present to and contribute to SDAs. The decision, though, sits with the Defra-appointed SDA lead. Partners should expect their designs to be assessed against these guardrails and should record decisions as ADRs in Defra repositories.

## Terms of reference outline

- **Scope:** services, products and business capabilities covered
- **Membership:** lead architect (chair), architects from the group, a security architect, a data architect, platform representative; product and delivery leads as needed
- **Delegated authority:** decisions it may make, with reference to this page
- **Escalation:** to the TDA, following [triage](triage.md)
- **Cadence:** as needed, with a maximum 5-working-day turnaround for decisions
- **Transparency:** ADR log location; quarterly summary to the TDA
