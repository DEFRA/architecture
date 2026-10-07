<!-- https://defra.github.io/architecture/patterns/service/field-inspection/ | maturity: draft | site version 0.3.0 | generated from patterns/service/field-inspection.md -->

# Field inspection (proposed)

<p class="lead">A proposed starting shape for services where staff plan, carry out and record inspections, surveys and sampling in the field - often with no mobile signal.</p>

!!! warning "Draft - to be confirmed"
    Exploratory, early work. Service patterns are starting points for discussion, not agreed designs, and have not been reviewed by the Technical Design Authority. Talk to the architecture team before building on one.



**Technology capability:** field work and inspection, under [Manufacturing & Delivery](https://defra.github.io/architecture/handrail/technology-capabilities/#manufacturing-and-delivery). Defra has **no Defra-wide answer yet**. **Typical business capabilities:** [05 Issue licences and permits](https://defra.github.io/architecture/handrail/business-capabilities/#bc05), [06 Enforce compliance](https://defra.github.io/architecture/handrail/business-capabilities/#bc06), [01 Act as a custodian of the environment](https://defra.github.io/architecture/handrail/business-capabilities/#bc01).

## Context

Inspectors, scientists and field officers work on farms, riverbanks, ports and coasts. They need the case history before they go, must record findings and evidence (photos, samples, locations) where they are, and often have no signal. Today many teams use paper, spreadsheets or one-off apps, so the same problem is solved many times.

## Proposed shape

```mermaid
flowchart LR
    accTitle: Proposed field inspection service pattern
    accDescr: Inspections are planned and scheduled from case management. A field app on a managed device downloads the work and reference data before the visit, works offline to capture findings, photos, samples and locations, and stores them encrypted on the device. When back in signal it syncs to a field service API on the Core Delivery Platform, which stores evidence, updates the case through events and feeds the data platform.
    CASE["Case and workflow"] -->|"inspections due"| PLAN["Planning and scheduling"]
    PLAN --> API
    subgraph DEV["Managed mobile device"]
        APP["Field app<br/>works offline"]
        LOCAL[("Encrypted local store")]
        APP --- LOCAL
    end
    API["Field service API<br/>on CDP"] -->|"download work and<br/>reference data"| APP
    APP -->|"sync when in signal"| API
    API --> EV[("Evidence store")]
    API -->|"inspection-completed event"| MSG["Messaging"]
    MSG --> CASE
    MSG --> DP["Data platform"]
    GEO["Geospatial services"] --> APP
```

## Questions to answer

<div id="tbc-1"></div>

!!! warning "To be confirmed"
    **TODO:** whether Defra intends to buy a field inspection product or build shared components, and which team owns the capability.

- Which device management, offline storage and sync approach is supported on Defra devices?
- How should conflicts be resolved when two people update the same record offline?
- What evidence standards apply to photos and samples used in enforcement?

## Guardrails to pay attention to

- [GR-FE-05 Design for low bandwidth and rural users](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-05)
- [GR-SEC-04 Encrypt in transit and at rest](https://defra.github.io/architecture/guardrails/security/#gr-sec-04), including on the device
- [GR-API-06 Use events for change notifications](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-06)
- [GR-TECH-01 Look for something to reuse first](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-01) - other government departments run field inspection services

