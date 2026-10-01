# Reference architectures

<p class="lead">Reference architectures are proven starting shapes for common kinds of Defra service, assembled from the technology capabilities in the handrail. Start here rather than from a blank page.</p>

| Reference architecture | Use it for | Main business capabilities |
| --- | --- | --- |
| [Transactional digital service](transactional-service.md) | Any public-facing service where users apply, register, notify or claim | [04](../business-capabilities.md#bc04), [05](../business-capabilities.md#bc05), [07](../business-capabilities.md#bc07) |
| [Regulatory casework](regulatory-casework.md) | Assessing applications, inspecting, investigating and taking enforcement action | [05](../business-capabilities.md#bc05), [06](../business-capabilities.md#bc06) |
| [Data and analytics](data-and-analytics.md) | Collecting, managing, analysing and publishing evidence and environmental data | [01](../business-capabilities.md#bc01), [02](../business-capabilities.md#bc02) |

## How to use a reference architecture

- **It is a default, not a mandate.** Diverge where your users or context need it, and record why in an [ADR](../../governance/architecture-decision-records.md).
- **Following one lightens governance.** A design that follows a reference architecture and stays inside the [guardrails](../../guardrails/index.md) can normally be approved by your [solution design authority](../../governance/solution-design-authorities.md).
- **Diagrams use plain capability names** so they stay true as products change.

## Coming next

We plan to add reference architectures for incident response, grants and scheme management, field inspection with offline mobile working, and public registers. Tell us which you need most by [opening an issue](https://github.com/howellsr/architecture/issues).
