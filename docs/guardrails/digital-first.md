---
principles: [GR-PRIN-02]
applicability: tbc
guardrail_defaults:
  status: draft
  owner: Architecture team
  automated_check: manual
  last_reviewed: 2026-10-01
  since_version: 0.2.0
guardrails:
  GR-DIG-01:
    phases: [discovery, alpha]
    lead_roles: [service-designer, user-researcher]
    evidence: Discovery findings showing paper, email and manual steps in the current process and how the new design removes or justifies each one
    service_standard_points: [2]
  GR-DIG-02:
    phases: [discovery, alpha, beta]
    lead_roles: [service-designer]
    evidence: A map of the whole service, including the parts other teams and organisations deliver, and agreed hand-offs between them
    service_standard_points: [2, 3]
  GR-DIG-03:
    phases: [alpha, beta, live]
    lead_roles: [service-designer, user-researcher]
    evidence: Assisted digital and offline routes designed and tested with users who need them
    service_standard_points: [3, 5]
    tcop_points: [2]
---

# Digital first and end-to-end services

<p class="lead">Design whole services around users, digital by default, without leaving behind people who cannot use them online. These draft guardrails describe what that means for architecture.</p>

Applies the DDTS doctrines [outcomes over structures](../principles/doctrine.md#ddts-06) and [digital first](../principles/doctrine.md#ddts-07). See the [Defra Digital Service Manual](https://digital.defra.gov.uk/service-manual) for design and research guidance.

!!! info "Draft guardrails"
    These guardrails are new drafts from the [guardrail backlog](../about/roadmap.md#guardrail-backlog). Comment on them by [opening an issue](https://github.com/DEFRA/architecture/issues).

## GR-DIG-01 Challenge paper and manual processes {#gr-dig-01}

<span class="rfc rfc--should">Should</span> Do not put a paper or email process online as it is. Find out why each step exists, and remove, automate or redesign it.

**Why:** digitising a broken process makes it faster to fail. The biggest gains come from removing steps, not speeding them up.

**How to meet it:** map the current process in discovery, including the parts staff do by hand. For each step, record whether it is needed, and why.

## GR-DIG-02 Design across organisational boundaries {#gr-dig-02}

<span class="rfc rfc--should">Should</span> Design the end-to-end service from the user's point of view, even when parts of it are delivered by other Defra organisations or other parts of government.

**Why:** users do not care which organisation does what. Many Defra users deal with several Defra bodies for one task.

**How to meet it:** identify the whole service your work is part of, talk to the teams delivering the other parts, and agree how users and data move between them.

## GR-DIG-03 Provide assisted digital and offline routes {#gr-dig-03}

<span class="rfc rfc--should">Should</span> Make sure people who cannot use the online service, or cannot use it alone, can still get what they need - with help, by phone or on paper - and that those routes lead to the same outcome and data.

**Why:** some Defra users have limited internet access, skills or confidence, particularly in rural areas. Service Standard point 5 asks that everyone can use the service.

**How to meet it:** design assisted routes in alpha, so staff-assisted applications go through the same system as online ones rather than a separate process.
