<!-- https://defra.github.io/architecture/deliver/roles/performance-analyst/ | maturity: prototype | site version 0.3.0 | generated from deliver/roles/performance-analyst.md -->

# Performance analyst

<p class="lead">The guardrails a performance analyst leads, what to show in each phase, the patterns that help and when to work with an architect.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



You measure whether the service works for users and for Defra. Service levels, cost, carbon and data quality all need measuring.

You lead **4 guardrails**, often with other roles. Leading means making sure the team meets them and can show it, not doing all the work. See them all in the <a href="../../../guardrails/library/#role=performance-analyst">guardrail library, filtered to your role</a>.

## Your guardrails, phase by phase

### Beta

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-DATA-08](https://defra.github.io/architecture/guardrails/data/#gr-data-08) Manage data quality | Should | Data quality measures and regular reports |
| [GR-OPS-03](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-03) Define and measure service levels | Should | Agreed service level objectives with monitoring and alerts |
| [GR-OPS-07](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-07) Measure performance and cost | Should | Published key performance indicators and cost tags on cloud resources |

More on the [beta page](https://defra.github.io/architecture/deliver/beta/).

### Live

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-DATA-08](https://defra.github.io/architecture/guardrails/data/#gr-data-08) Manage data quality | Should | Data quality measures and regular reports |
| [GR-OPS-03](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-03) Define and measure service levels | Should | Agreed service level objectives with monitoring and alerts |
| [GR-OPS-07](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-07) Measure performance and cost | Should | Published key performance indicators and cost tags on cloud resources |
| [GR-SUS-05](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-05) Measure and report | Could | Carbon footprint reported alongside cost |

More on the [live page](https://defra.github.io/architecture/deliver/live/).

## Patterns that help

- [Publishing open data with metadata](https://defra.github.io/architecture/patterns/open-data-publishing/) - You hold non-personal data that others could use, and want to publish it so it can be found, trusted and reused.

## Working with architects

- Agree what will be measured, and how, with the architect in alpha, so the data exists in beta.



