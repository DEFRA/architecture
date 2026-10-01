# Contracting with this site

<p class="lead">How to reference the guardrails in a statement of requirements or statement of work, so buyers and suppliers share one clear, stable baseline.</p>

This page is for Defra commercial teams, delivery leads writing requirements, and suppliers bidding for or delivering Defra work.

!!! warning "To be confirmed"
    **TODO:** confirm with Defra commercial and legal teams that the model clauses on this page can be used in Defra contracts, and in which frameworks.

## Cite a fixed version

The site changes often. A contract should point to a **fixed version**, so both sides know exactly what applied when the contract was signed.

Each release of the site is:

- numbered using [semantic versioning](https://semver.org/), for example `0.2.0`
- tagged in the [repository](https://github.com/howellsr/architecture/tags) as `v0.2.0`
- published as a [GitHub release](https://github.com/howellsr/architecture/releases) with a PDF of every guardrail attached, as an archived copy
- listed in [what's new](../about/changelog.md)

Cite it like this:

> Defra architecture guardrails, version 0.2.0, as published at https://github.com/howellsr/architecture/releases/tag/v0.2.0, including the archived PDF attached to that release.

Guardrail ids, such as `GR-HOST-01`, never change meaning and are never reused. A guardrail that is no longer needed is marked **deprecated** and points to its replacement, so a reference in an older contract can always be traced.

## Versioning policy

| Change | Example | Version change |
| --- | --- | --- |
| A new Must, a Should raised to a Must, or a Must made stricter | Adding a Must for supplier AI use | **Major** (from 1.0.0 onwards); minor while the site is in alpha (0.x) |
| A Must deprecated or relaxed | Removing a requirement that no longer applies | Major (from 1.0.0); minor in alpha |
| A new Should or Could, new guidance or a new page | A new pattern | Minor |
| Clearer wording that does not change what is required, fixed links | Typo fixes | Patch |

While the site is in **alpha** (versions `0.x`), anything may change between releases. Contracts should cite the version in force at signature, and agree how later versions are adopted.

## Notice period for new Musts

New or stricter Must guardrails do not apply to existing contracts automatically. They apply from the version a contract cites, or from a later version both parties agree to adopt.

!!! warning "To be confirmed"
    **TODO:** the notice period Defra gives before a new Must applies to new work, and how it is communicated to suppliers.

## Model clauses

Use or adapt these in a statement of requirements or statement of work. Text in square brackets is for you to complete.

### 1. Guardrails

> The Supplier shall meet every Must guardrail in the Defra architecture guardrails, version [X.Y.Z] (Annex A), unless the Authority has approved an exception through the published [exception process](../governance/exceptions.md). Where the Supplier departs from a Should guardrail, it shall record the reason in an architecture decision record and share it with the Authority's solution design authority.

### 2. Non-functional requirements for the service tier

> The Service is service tier [T1 / T2 / T3 / T4], as defined in the Defra [service tiers](../nfrs/service-tiers.md), version [X.Y.Z]. The Supplier shall meet the targets for that tier in the Defra [NFR catalogue](../nfrs/catalogue.md), version [X.Y.Z], and evidence them through automated testing before each release to production.

### 3. Code and repositories

> All source code, infrastructure code, pipeline definitions and documentation shall be held in a Defra-owned GitHub organisation from the first commit ([GR-DEV-02](../guardrails/software-development.md#gr-dev-02)), public unless the Authority agrees a recorded reason ([GR-OPEN-01](../guardrails/open-source.md#gr-open-01)), and licensed as required by [GR-OPEN-02](../guardrails/open-source.md#gr-open-02). The Authority owns all code and intellectual property created under this contract.

### 4. Architecture decision records

> The Supplier shall record significant architecture decisions as architecture decision records in the service repository ([GR-DEV-09](../guardrails/software-development.md#gr-dev-09)), using the Authority's [ADR template](../governance/templates/adr.md), from the start of the engagement.

### 5. Secure by Design

> The Supplier shall carry out the [Secure by Design](../security/secure-by-design.md) activities for each phase, and provide and keep current the threat model ([GR-SEC-02](../guardrails/security.md#gr-sec-02)), security risk records ([GR-SEC-09](../guardrails/security.md#gr-sec-09)) and IT health check remediation ([GR-SEC-06](../guardrails/security.md#gr-sec-06)). The Supplier shall support the Authority's named risk owner.

### 6. AI coding assistants

> The Supplier shall use AI coding assistants on the Authority's work only as set out in [GR-AI-07](../guardrails/ai.md#gr-ai-07), and only tools that meet [GR-AI-02](../guardrails/ai.md#gr-ai-02).

### 7. Exit and handover

> The Supplier shall maintain an exit plan ([GR-TECH-03](../guardrails/choosing-technology.md#gr-tech-03)) and, at the end of the contract or on request, hand over the Service so that it meets the Authority's [handover definition of done](handover-and-exit.md). The Supplier shall co-operate with any incoming supplier during transition.

## Annex A: Must guardrails

Generated from the guardrails on this site. For a contract, use the PDF attached to the release you cite rather than this live list.

<!-- guardrails:musts -->
