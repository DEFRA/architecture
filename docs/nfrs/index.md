# Non-functional requirements

Non-functional requirements (NFRs) describe **how well** a system should work, rather than **what** it should do.

They set expectations for quality, performance, reliability, security and user experience. Functional requirements describe the service's features. NFRs describe the qualities those features must demonstrate.

## Start with the authoritative DDTS catalogue

Defra colleagues should use the internal DDTS NFR page for the current service tiers, catalogue, ownership, assurance route and supporting guidance:

[Use the internal DDTS non-functional requirements catalogue](https://defra.sharepoint.com/teams/Team3221/SitePages/Non-Functional-Requirements.aspx){ .govuk-button }

The internal page is available only to authorised Defra Group users. Delivery partners who cannot access it should work with their Defra service owner, business analyst or delivery architect to agree the applicable requirements and evidence.

This public site explains how architecture uses NFRs and provides reusable guidance. If public examples or placeholders differ from the internal DDTS catalogue, use the internal catalogue.

## What to do

1. **Assess business criticality and service tier.** Do this as early as possible so the tier can inform the required characteristics of the service.
2. **Define the solution requirements.** Use the internal DDTS catalogue as the baseline, then add service-specific functional and non-functional requirements where needed.
3. **Build a coherent set of requirements.** Remove duplication, identify owners and make each requirement clear, measurable and testable.
4. **Use the requirements in procurement or build decisions.** Include applicable NFRs in supplier, platform and engineering decisions.
5. **Test and assure the service.** Put requirements and acceptance criteria in the backlog, gather evidence and validate them at the appropriate delivery and assurance points.
6. **Use the evidence for service transition and go-live.** Record unmet mandatory requirements and follow the agreed exception and risk route.
7. **Monitor and improve in live.** Measure performance against the agreed targets and revisit requirements when the service, its users or its criticality changes.

NFRs are not a document written once. They shape design, build, testing, service transition and live operation.

## Start here

- **[Service tiers](service-tiers.md)**  
  Understand how service criticality informs availability, recovery and support targets. Confirm the applicable tier using the internal DDTS page.

- **[NFR catalogue](catalogue.md)**  
  Browse the public, reusable view of NFRs and their evidence. Confirm the current requirement and tier target in the internal DDTS catalogue before adoption.

- **[Writing good NFRs](writing-nfrs.md)**  
  Draft requirements that are specific, measurable, testable and focused on outcomes rather than solutions.

## Apply NFRs throughout delivery

| Delivery point | What to do |
| --- | --- |
| **Discovery** | Understand the impact of failure and agree a provisional service tier with the service owner. |
| **Alpha** | Select applicable NFRs from the internal catalogue, add service-specific requirements and use them to shape the architecture. |
| **Beta** | Put NFRs and acceptance criteria in the backlog. Build, test and retain evidence for each requirement. |
| **Service transition** | Confirm operational readiness, evidence, ownership and monitoring. Record any unmet mandatory requirements through the agreed exception and risk route. |
| **Live** | Monitor targets, report performance and revisit the tier and requirements after material change. |

## Requirement types and ownership

The internal DDTS catalogue distinguishes between:

- **Design requirements**, considered early and led primarily through delivery architecture
- **Operational delivery requirements**, demonstrated as the service moves through readiness, transition and live operation

Ownership does not replace collaboration. Product, delivery, architecture, engineering, security, commercial, service management and operations should agree how each requirement will be met, tested and evidenced.

## NFR categories

The categories below provide a public navigation view. The internal DDTS catalogue remains the source for the current category structure, requirement wording and tier applicability.

| Category | What it covers |
| --- | --- |
| [Availability and resilience](catalogue.md#nfr-avl) | The service is available when users need it and can recover from failure. |
| [Performance and capacity](catalogue.md#nfr-prf) | The service responds in time and can handle expected demand and peaks. |
| [Security](catalogue.md#nfr-sec) | The service protects its users, data and Defra. |
| [Accessibility and usability](catalogue.md#nfr-acc) | People who need the service can use it. |
| [Observability and supportability](catalogue.md#nfr-ops) | The service can be monitored, supported and restored by the teams responsible for it. |
| [Maintainability and testability](catalogue.md#nfr-mnt) | The service can be changed and verified safely. |
| [Interoperability](catalogue.md#nfr-int) | The service works with other Defra services and relevant partners. |
| [Data and compliance](catalogue.md#nfr-dat) | Data is managed, protected and retained appropriately. |
| [Sustainability](catalogue.md#nfr-sus) | The service uses energy and resources responsibly. |

## Write requirements that can be evidenced

Use this form:

> The service shall **[measurable outcome]** under **[defined conditions]**.

Good NFRs are:

- specific and unambiguous
- written in plain English
- measurable where possible
- focused on the required outcome rather than an assumed technical solution
- testable or otherwise verifiable

Avoid words such as "fast", "secure", "easy to use" or "reliable" unless you define how they will be measured.

Before accepting a requirement, ask:

- Is it clear?
- Is it measurable?
- Can it be tested or verified?
- Does it describe an outcome rather than a solution?
- Would different readers interpret it consistently?

See [writing good NFRs](writing-nfrs.md) for examples.

## When a requirement will not be met

Treat an unmet NFR as a service risk, not as missing paperwork. Record:

- the requirement that will not be met
- the affected tier or service outcome
- the evidence and reason
- the impact and risk owner
- the mitigation or improvement action
- the review point

Follow the current exception, waiver and assurance route described on the [internal DDTS non-functional requirements page](https://defra.sharepoint.com/teams/Team3221/SitePages/Non-Functional-Requirements.aspx).

## How NFRs relate to guardrails

[Guardrails](../guardrails/index.md) describe approved boundaries and approaches for building services. NFRs describe the outcomes and qualities a service must achieve. Use both: guardrails help teams make consistent design choices, while NFR evidence shows whether the required service outcome has been achieved.

## Machine-readable catalogue

The public site publishes service-tier and catalogue data from YAML in `nfrs/`. Teams can use the generated JSON in backlog and assurance tooling, but should check current requirements and tier applicability against the internal DDTS catalogue before using them as an assurance baseline.
