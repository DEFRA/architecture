# Architecture principles

<p class="lead">Ten principles that guide every architecture decision in Defra. Each guardrail traces back to at least one of them, and each builds on the <a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> and the <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a>.</p>

Principles help when the guardrails do not give a direct answer. When in doubt, ask: *which option best fits these principles?*

## GR-PRIN-01 Start with user and business outcomes {#gr-prin-01}

Design around the needs of users and the [business capability](../handrail/business-capabilities.md) being delivered, not around existing systems or organisational boundaries.

- **Rationale:** Services that follow organisational structure are harder to use and harder to change.
- **Implications:** Every service can say which business capabilities it supports and what outcome it improves.
- **Relates to:** Service Standard points 1-4, TCoP point 1.

## GR-PRIN-02 Reuse, then buy, then build {#gr-prin-02}

Use what Defra or government already has. If nothing fits, buy commodity products. Build only what makes Defra different.

- **Rationale:** Every bespoke component is something we must secure, patch and pay for for years.
- **Implications:** Check the [technology capabilities](../handrail/technology-capabilities.md) and cross-government components such as GOV.UK Notify, Pay and One Login first. See [choosing technology](choosing-technology.md).
- **Relates to:** TCoP points 8 and 11.

## GR-PRIN-03 Cloud and platform first {#gr-prin-03}

Use public cloud, and use Defra's strategic delivery platforms so teams spend their time on user value rather than infrastructure.

- **Rationale:** Platforms give us security, resilience and observability once, for everyone.
- **Implications:** See [hosting and platforms](hosting-and-platforms.md).
- **Relates to:** TCoP point 5, the government Cloud First policy.

## GR-PRIN-04 API first and open standards {#gr-prin-04}

Expose capabilities through well-documented APIs and events built on open standards, so they can be reused and replaced independently.

- **Rationale:** Point-to-point and database-level integration makes change slow and risky.
- **Implications:** See [APIs and integration](apis-and-integration.md).
- **Relates to:** TCoP points 4 and 9.

## GR-PRIN-05 Data is a shared asset {#gr-prin-05}

Collect data once, from the right source, and make it findable, accessible, interoperable and reusable, with clear ownership and protection.

- **Rationale:** Defra's evidence, regulation and payments all depend on trusted data.
- **Implications:** See the [data guardrails](data.md) and [Defra on a page](../data/defra-on-a-page.md).
- **Relates to:** TCoP point 10, the Government Data Quality Framework.

## GR-PRIN-06 Secure by design {#gr-prin-06}

Treat security as a continuous part of delivery, proportionate to risk and owned by the service team.

- **Rationale:** Security added late is expensive and often ineffective.
- **Implications:** See [Secure by Design in Defra](../security/secure-by-design.md) and the [security guardrails](security.md).
- **Relates to:** TCoP points 6 and 7, Service Standard point 9.

## GR-PRIN-07 Design for change {#gr-prin-07}

Prefer small, loosely coupled components with clear boundaries, automated tests and automated deployment, so they can evolve as policy and needs change.

- **Rationale:** Policy changes often. Systems that cannot keep up become legacy quickly.
- **Implications:** Make it cheap to change and cheap to replace. Avoid lock-in that is not a deliberate, recorded choice.

## GR-PRIN-08 Operable and observable by default {#gr-prin-08}

Build services that tell you how they are doing, recover from failure and can be supported by someone who did not build them.

- **Rationale:** Most cost and risk sits in the years of running a service, not in building it.
- **Implications:** See [observability and operations](observability-and-operations.md).
- **Relates to:** Service Standard points 10 and 14.

## GR-PRIN-09 Open and sustainable by default {#gr-prin-09}

Work in the open, share what we learn, and design for the lowest environmental impact that meets user need.

- **Rationale:** Openness improves quality and reuse. Defra leads government's [Greening Government ICT](https://www.gov.uk/government/publications/greening-government-ict-and-digital-services-strategy-2020-2025) strategy and should model it.
- **Implications:** See [open source](open-source.md) and [sustainability](sustainability.md).
- **Relates to:** TCoP points 3 and 12, Service Standard points 12 and 13.

## GR-PRIN-10 Proportionate, transparent decisions {#gr-prin-10}

Make decisions at the lowest sensible level, proportionate to risk, and record significant ones as [architecture decision records](../governance/architecture-decision-records.md).

- **Rationale:** Decisions that are written down can be reviewed, reused and revisited. Decisions made close to the work are faster and better informed.
- **Implications:** See [governance](../governance/index.md).
