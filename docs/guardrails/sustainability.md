---
applicability: tbc
principles: [GR-PRIN-03]
# Metadata for every guardrail on this page. See the contribution guide for the fields.
guardrail_defaults:
  status: draft
  owner: Architecture team
  automated_check: manual
  last_reviewed: 2026-10-01
  since_version: 0.1.0
guardrails:
  GR-SUS-01:
    phases: [discovery, alpha]
    lead_roles: [technical-architect]
    evidence: Environmental impact recorded in ADRs for hosting and technology choices
    tcop_points: [12]
  GR-SUS-02:
    phases: [beta, live]
    lead_roles: [developer]
    evidence: Autoscaling and out-of-hours schedules for non-production environments
    tcop_points: [12]
  GR-SUS-03:
    phases: [alpha]
    lead_roles: [technical-architect]
    evidence: Region and service choice recorded with its carbon intensity
    tcop_points: [12]
  GR-SUS-04:
    phases: [alpha, beta, live]
    lead_roles: [developer, interaction-designer]
    evidence: Data retention settings and page weight measurements
    tcop_points: [12]
  GR-SUS-05:
    phases: [live]
    lead_roles: [performance-analyst, technical-architect]
    evidence: Carbon footprint reported alongside cost
    tcop_points: [12]
---

# Sustainability

<p class="lead">Defra leads the <a href="https://www.gov.uk/government/publications/greening-government-ict-and-digital-services-strategy-2020-2025">Greening Government ICT and Digital Services strategy</a>. Our own services should show what good looks like.</p>

Relates to TCoP point 12.

Defra services must also meet a 15th point of the Service Standard, [deliver a sustainable service](https://digital.defra.gov.uk/sustainability), including a sustainability statement against the [6 objectives in Defra's digital sustainability strategy](https://digital.defra.gov.uk/sustainability/objectives). Use the Defra Digital Service Manual for how to do that. These guardrails cover the architecture decisions that contribute to it.

## GR-SUS-01 Consider sustainability in design decisions {#gr-sus-01}

<span class="rfc rfc--should">Should</span> Include environmental impact as a factor in ADRs for hosting, architecture and technology choices.

## GR-SUS-02 Right-size and switch off {#gr-sus-02}

<span class="rfc rfc--should">Should</span> Use autoscaling, scale non-production environments down out of hours, and delete unused resources.

## GR-SUS-03 Choose lower-carbon regions and services {#gr-sus-03}

<span class="rfc rfc--could">Could</span> Where data rules allow, prefer cloud regions and services with lower carbon intensity, and use providers' carbon reporting.

## GR-SUS-04 Keep data and pages lean {#gr-sus-04}

<span class="rfc rfc--should">Should</span> Store only the data you need, for as long as you need it, and keep page weight low - which also helps users on slow connections ([GR-FE-05](front-end-and-accessibility.md#gr-fe-05)).

## GR-SUS-05 Measure and report {#gr-sus-05}

<span class="rfc rfc--could">Could</span> Track the carbon footprint of your service using cloud provider tooling and report it alongside cost.
