<!-- https://defra.github.io/architecture/patterns/service/ | maturity: draft | site version 0.3.0 | generated from patterns/service/index.md -->

# Service patterns

<p class="lead">Service patterns are early, exploratory starting shapes for common kinds of Defra service. Each shows the main building blocks of a whole service and how they connect.</p>

!!! warning "Draft - to be confirmed"
    Exploratory, early work. Service patterns are starting points for discussion, not agreed designs, and have not been reviewed by the Technical Design Authority. Talk to the architecture team before building on one.



A **service pattern** shows the shape of a whole kind of service, such as a transactional service or regulatory casework. A **[solution pattern](https://defra.github.io/architecture/patterns/#solution-patterns)** solves one recurring problem inside a service, such as accepting file uploads or acting on behalf of someone. A service pattern usually uses several solution patterns.

| Service pattern | Use it for | Main business capabilities |
| --- | --- | --- |
| [Transactional digital service](https://defra.github.io/architecture/patterns/service/transactional-service/) | Any public-facing service where users apply, register, notify or claim | [04](https://defra.github.io/architecture/handrail/business-capabilities/#bc04), [05](https://defra.github.io/architecture/handrail/business-capabilities/#bc05), [07](https://defra.github.io/architecture/handrail/business-capabilities/#bc07) |
| [Regulatory casework](https://defra.github.io/architecture/patterns/service/regulatory-casework/) | Assessing applications, inspecting, investigating and taking enforcement action | [05](https://defra.github.io/architecture/handrail/business-capabilities/#bc05), [06](https://defra.github.io/architecture/handrail/business-capabilities/#bc06) |
| [Data and analytics](https://defra.github.io/architecture/patterns/service/data-and-analytics/) | Collecting, managing, analysing and publishing evidence and environmental data | [01](https://defra.github.io/architecture/handrail/business-capabilities/#bc01), [02](https://defra.github.io/architecture/handrail/business-capabilities/#bc02) |
| [Field inspection](https://defra.github.io/architecture/patterns/service/field-inspection/) (proposed) | Planning, carrying out and recording inspections and sampling, including offline | [05](https://defra.github.io/architecture/handrail/business-capabilities/#bc05), [06](https://defra.github.io/architecture/handrail/business-capabilities/#bc06) |
| [Incident response](https://defra.github.io/architecture/patterns/service/incident-response/) (proposed) | Detecting, coordinating and reporting on outbreaks, floods and pollution | [08](https://defra.github.io/architecture/handrail/business-capabilities/#bc08) |
| [Grants and schemes](https://defra.github.io/architecture/patterns/service/grants/) (proposed) | Configuring schemes, applications, agreements, claims and payments | [07](https://defra.github.io/architecture/handrail/business-capabilities/#bc07) |

## How to use a service pattern

- **Use it to start a conversation, not as a design to copy.** Check it with the architecture team and your solution design authority.
- **Diverge where your users or context need it**, and record why in an [ADR](https://defra.github.io/architecture/governance/architecture-decision-records/).
- **Diagrams use plain capability names** so they stay true as products change.

Proposed service patterns cover needs where Defra has no Defra-wide answer yet.

## Coming next

We plan to add a service pattern for public registers, and a layered reference architecture view of Defra's technology. Tell us which you need most by [opening an issue](https://github.com/DEFRA/architecture/issues).

