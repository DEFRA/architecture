<!-- https://defra.github.io/architecture/patterns/service/regulatory-casework/ | maturity: draft | site version 0.3.0 | generated from patterns/service/regulatory-casework.md -->

# Regulatory casework

<p class="lead">An exploratory starting shape for assessing applications, inspecting, investigating and taking enforcement action - the heart of how Defra regulates.</p>

!!! warning "Draft - to be confirmed"
    Exploratory, early work. Service patterns are starting points for discussion, not agreed designs, and have not been reviewed by the Technical Design Authority. Talk to the architecture team before building on one.



**Typical business capabilities:** [05 Issue licences and permits](https://defra.github.io/architecture/handrail/business-capabilities/#bc05), [06 Enforce compliance](https://defra.github.io/architecture/handrail/business-capabilities/#bc06).

## Context

Across Defra group, staff assess permit and licence applications, plan and carry out inspections, investigate incidents and take enforcement action. Historically each regime has had its own system. This service pattern separates what is common to all regulatory regimes from what is specific to each, so new regimes can be added by configuration rather than new systems.

## Architecture

```mermaid
flowchart TB
    accTitle: Regulatory casework service pattern
    accDescr: Intake from transactional services and intelligence feeds case and workflow management, which uses rules and risk scoring and documents and records, sends inspection tasks to field work, uses shared reference and geospatial data, publishes public registers and sends decisions to the data platform, which improves risk models.
    subgraph Intake["Intake"]
        TS["Transactional services<br/>(see transactional service pattern)"]
        INT["Intelligence, reports<br/>and referrals"]
    end

    subgraph Core["Regulatory core"]
        CASE["Case and workflow"]
        RULES["Rules and risk scoring"]
        DOCS["Documents and records"]
    end

    subgraph Field["Field"]
        INSP["Field work and inspection<br/>(no Defra-wide answer)"]
    end

    subgraph Shared["Shared data"]
        REF["Customers, organisations,<br/>sites and holdings"]
        GEO["Geospatial"]
        REG["Public registers"]
    end

    TS -->|"application events"| CASE
    INT --> CASE
    CASE <--> RULES
    CASE <--> DOCS
    CASE -->|"inspection tasks"| INSP
    INSP -->|"findings, evidence"| CASE
    CASE <--> REF
    CASE <--> GEO
    CASE -->|"permits issued,<br/>enforcement published"| REG
    CASE -->|"decisions, events"| DP[("Data platform")]
    DP -->|"risk models,<br/>compliance insight"| RULES
```

## Principles for this architecture

1. **One customer, many regimes.** A farmer may hold a water abstraction licence, a waste exemption and an animal movement record. Use shared reference data so staff and users see the whole picture.
2. **Rules are data.** Eligibility, conditions and risk scores are versioned and testable, separate from workflow.
3. **Risk-based regulation needs data.** Decisions and inspection findings flow to the data platform so risk models improve over time.
4. **Field first.** Inspectors often have no signal. Field tools must work offline and synchronise safely.
5. **Registers are outputs, not separate systems.** Public registers are generated from case decisions and published as open data where the law allows.

## Building blocks

| Concern | Default | Notes |
| --- | --- | --- |
| Case and workflow | Strategic case management capability ([Manufacturing & Delivery](https://defra.github.io/architecture/handrail/technology-capabilities/#manufacturing-and-delivery)) | Configure per regime; avoid new bespoke case systems |
| Rules | Rules as code, versioned with the service ([Manufacturing & Delivery](https://defra.github.io/architecture/handrail/technology-capabilities/#manufacturing-and-delivery)) | Emerging - talk to the architecture team |
| Documents | Records management with retention labels ([Communication & Collaboration](https://defra.github.io/architecture/handrail/technology-capabilities/#communication-and-collaboration)) | Apply retention schedules automatically |
| Field inspection | No strategic answer yet ([Manufacturing & Delivery](https://defra.github.io/architecture/handrail/technology-capabilities/#manufacturing-and-delivery)) | Raise with the TDA - a cross-Defra need |
| Staff access | Microsoft Entra ID with role-based access | [GR-IAM-02](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-02) |

## Key decisions to record

- Which regimes share a case model and which need their own.
- Where the authoritative record of a permit or licence lives.
- How enforcement data is shared with other regulators and published.
- How AI or automated risk scoring is overseen ([GR-AI-03](https://defra.github.io/architecture/guardrails/ai/#gr-ai-03)).

