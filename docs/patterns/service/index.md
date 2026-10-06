---
status: draft
status_note: "Exploratory, early work. Service patterns are starting points for discussion, not agreed designs, and have not been reviewed by the Technical Design Authority. Talk to the architecture team before building on one."
---

# Service patterns

<p class="lead">Service patterns are early, exploratory starting shapes for common kinds of Defra service. Each shows the main building blocks of a whole service and how they connect.</p>

A **service pattern** shows the shape of a whole kind of service, such as a transactional service or regulatory casework. A **[solution pattern](../index.md#solution-patterns)** solves one recurring problem inside a service, such as accepting file uploads or acting on behalf of someone. A service pattern usually uses several solution patterns.

| Service pattern | Use it for | Main business capabilities |
| --- | --- | --- |
| [Transactional digital service](transactional-service.md) | Any public-facing service where users apply, register, notify or claim | [04](../../handrail/business-capabilities.md#bc04), [05](../../handrail/business-capabilities.md#bc05), [07](../../handrail/business-capabilities.md#bc07) |
| [Regulatory casework](regulatory-casework.md) | Assessing applications, inspecting, investigating and taking enforcement action | [05](../../handrail/business-capabilities.md#bc05), [06](../../handrail/business-capabilities.md#bc06) |
| [Data and analytics](data-and-analytics.md) | Collecting, managing, analysing and publishing evidence and environmental data | [01](../../handrail/business-capabilities.md#bc01), [02](../../handrail/business-capabilities.md#bc02) |
| [Field inspection](field-inspection.md) (proposed) | Planning, carrying out and recording inspections and sampling, including offline | [05](../../handrail/business-capabilities.md#bc05), [06](../../handrail/business-capabilities.md#bc06) |
| [Incident response](incident-response.md) (proposed) | Detecting, coordinating and reporting on outbreaks, floods and pollution | [08](../../handrail/business-capabilities.md#bc08) |
| [Grants and schemes](grants.md) (proposed) | Configuring schemes, applications, agreements, claims and payments | [07](../../handrail/business-capabilities.md#bc07) |

## How to use a service pattern

- **Use it to start a conversation, not as a design to copy.** Check it with the architecture team and your solution design authority.
- **Diverge where your users or context need it**, and record why in an [ADR](../../governance/architecture-decision-records.md).
- **Diagrams use plain capability names** so they stay true as products change.

Proposed service patterns cover needs where Defra has no Defra-wide answer yet.

## Coming next

We plan to add a service pattern for public registers, and a layered reference architecture view of Defra's technology. Tell us which you need most by [opening an issue](https://github.com/DEFRA/architecture/issues).
