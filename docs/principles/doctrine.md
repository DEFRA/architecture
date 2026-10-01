---
title: DDTS doctrine
status: draft
# Which architecture principles apply each doctrine. The site uses this to
# link doctrine -> principles -> guardrails; see hooks/traceability.py.
applies:
  ddts-01: [GR-PRIN-01, GR-PRIN-03]
  ddts-02: [GR-PRIN-01, GR-PRIN-06]
  ddts-03: [GR-PRIN-03]
  ddts-04: [GR-PRIN-04, GR-PRIN-05]
  ddts-05: [GR-PRIN-07, GR-PRIN-04]
  ddts-06: [GR-PRIN-02, GR-PRIN-05]
  ddts-07: [GR-PRIN-02, GR-PRIN-08]
status_note: This is the CDIO's initial draft. It will be refined, challenged and improved with colleagues across DDTS over the coming months.
---

# DDTS doctrine: our non-negotiables

<p class="lead">Seven non-negotiables set by the Chief Digital and Information Officer for Defra's Digital, Data and Technology Services (DDTS). They give everyone a common way of thinking and a consistent basis for decisions, so people can decide well without escalating every choice.</p>

!!! quote "Why doctrine, not principles"
    Principles are often interpreted as advisory; a doctrine is different. It provides a common way of thinking and a consistent basis for decision-making. It helps people make good decisions without needing to escalate every choice, while ensuring we move in the same direction as a function.

The doctrine sits above the [architecture principles](architecture-principles.md) and the [guardrails](../guardrails/index.md). The principles explain how architecture applies the doctrine; the guardrails make it practical for delivery teams. See [how they fit together](index.md).

| # | Doctrine |
| --- | --- |
| 1 | [Platforms before projects. Built as products.](#ddts-01) |
| 2 | [Standards and guardrails before exceptions.](#ddts-02) |
| 3 | [Reuse before buy.](#ddts-03) |
| 4 | [Data is an enterprise asset.](#ddts-04) |
| 5 | [Assume AI until proven otherwise.](#ddts-05) |
| 6 | [Outcomes and services over organisational structures.](#ddts-06) |
| 7 | [Digital first where appropriate.](#ddts-07) |

## 1. Platforms before projects. Built as products. {#ddts-01}

We will increasingly invest in reusable platforms and long-lived products rather than creating one-off solutions for individual programmes. This will let us scale delivery, reduce duplication and improve consistency across Defra.

**For example:** instead of every programme commissioning its own technology solution, we build reusable capabilities on the Core Delivery Platform that can be used many times.

**Where this shows up:** [GR-PRIN-01 Delivery-focused architecture](architecture-principles.md#gr-prin-01), [GR-PRIN-03 Maximise value, minimise waste](architecture-principles.md#gr-prin-03), [GR-HOST-01 Use Defra's strategic delivery platform](../guardrails/hosting-and-platforms.md#gr-host-01), [technology capabilities](../handrail/technology-capabilities.md).

## 2. Standards and guardrails before exceptions. {#ddts-02}

Standards exist to help us move faster, reduce risk and improve interoperability. Exceptions will always be possible where justified, but they should be the exception rather than the starting point.

**For example:** teams use Defra's approved identity, security and hosting patterns by default, and only seek exceptions where there is a clear business need.

**Where this shows up:** the [guardrails](../guardrails/index.md), [exceptions to guardrails](../governance/exceptions.md), [GR-IAM-01](../guardrails/identity-and-access.md#gr-iam-01), [GR-SEC-01](../guardrails/security.md#gr-sec-01), [GR-HOST-01](../guardrails/hosting-and-platforms.md#gr-host-01).

## 3. Reuse before buy. {#ddts-03}

Before procuring new technology, we first ask whether an existing capability, platform or service can meet the need. This reduces complexity, improves value for money and creates a more coherent technology landscape.

**For example:** before buying a new workflow tool, we first ask whether an existing platform already provides that capability.

**Where this shows up:** [GR-PRIN-03 Maximise value, minimise waste](architecture-principles.md#gr-prin-03), [GR-TECH-01 Look for something to reuse first](../guardrails/choosing-technology.md#gr-tech-01), [technology capabilities](../handrail/technology-capabilities.md).

## 4. Data is an enterprise asset. {#ddts-04}

Data belongs to the organisation, not to individual systems, teams or programmes. We manage data as a strategic asset that can be reused securely to improve services, decisions and outcomes.

**For example:** we do not ask colleagues or citizens for the same information more than once if we already hold it and can use it appropriately and lawfully.

**Where this shows up:** [GR-PRIN-04 Clean data, clear decisions](architecture-principles.md#gr-prin-04), [GR-DATA-01 Every data set has an owner](../guardrails/data.md#gr-data-01), [GR-DATA-04 Collect once, share safely](../guardrails/data.md#gr-data-04), [Defra on a page](../data/defra-on-a-page.md).

## 5. Assume AI until proven otherwise. {#ddts-05}

When tackling a problem or designing a service, we actively consider whether AI can improve quality, productivity, user experience or outcomes. This does not mean using AI everywhere. It means being deliberate about exploring the opportunity before dismissing it.

**For example:** when designing a new process, we first consider whether AI could automate repetitive tasks, improve decision-making or enhance the user experience, before defaulting to a traditional approach.

**Where this shows up:** [GR-PRIN-07 Empower to innovate](architecture-principles.md#gr-prin-07), [GR-AI-01 Consider AI first](../guardrails/ai.md#gr-ai-01), [artificial intelligence guardrails](../guardrails/ai.md).

## 6. Outcomes and services over organisational structures. {#ddts-06}

Citizens and colleagues experience services, not organisational charts. We organise our thinking around outcomes, user needs and end-to-end services rather than internal boundaries.

**For example:** when improving a service, we focus on the end-to-end experience for the user, even if that needs several teams to work across organisational boundaries.

**Where this shows up:** [GR-PRIN-02 Design for users](architecture-principles.md#gr-prin-02), [business capabilities](../handrail/business-capabilities.md), which are deliberately independent of organisation structure.

## 7. Digital first where appropriate. {#ddts-07}

We challenge manual and paper-based processes by default, and design digital services that are simpler, faster and easier to use.

**For example:** when redesigning a process, we start by asking how it could work digitally, rather than replicating existing manual steps online.

**Where this shows up:** [GR-PRIN-02 Design for users](architecture-principles.md#gr-prin-02), [front end and accessibility](../guardrails/front-end-and-accessibility.md), the [Defra Digital Service Manual](https://digital.defra.gov.uk/service-manual).

## Help shape the doctrine

The doctrine is not being developed behind closed doors. Over the coming months it will be refined, challenged and improved with colleagues from across DDTS, and it will evolve as we learn. Tell us how it works in practice by [opening an issue](https://github.com/howellsr/architecture/issues) or talking to your head of profession.
