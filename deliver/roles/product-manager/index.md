<!-- https://defra.github.io/architecture/deliver/roles/product-manager/ | maturity: prototype | site version 0.3.0 | generated from deliver/roles/product-manager.md -->

# Product manager

<p class="lead">The guardrails a product manager leads, what to show in each phase, the patterns that help and when to work with an architect.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



You decide what the team builds and in what order. Many guardrails are trade-offs you prioritise - reuse, exit plans, service levels and the end of a product's life.

You lead **16 guardrails**, often with other roles. Leading means making sure the team meets them and can show it, not doing all the work. See them all in the <a href="../../../guardrails/library/#role=product-manager">guardrail library, filtered to your role</a>.

## Your guardrails, phase by phase

### Discovery

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-TECH-06](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-06) Get spend approval early | Must | Architecture team consulted before any procurement under spend control starts |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | Must | DPIA screening completed, showing whether personal data is involved |
| [GR-AI-01](https://defra.github.io/architecture/guardrails/ai/#gr-ai-01) Consider AI first | Should | ADR recording the AI options considered and why they were or were not used |
| [GR-TECH-02](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-02) Buy commodity, build differentiating | Should | Buy or build options appraisal in the ADR or business case |
| [GR-PROD-02](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-02) Name the product owner and service owner | Should | Named product owner and service owner, recorded in the service catalogue |

More on the [discovery page](https://defra.github.io/architecture/deliver/discovery/).

### Alpha

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | Must | Draft DPIA, with data minimisation and retention designed in |
| [GR-SEC-09](https://defra.github.io/architecture/guardrails/security/#gr-sec-09) Manage risk explicitly | Must | Risks from controls that cannot be met recorded, with an owner |
| [GR-AI-01](https://defra.github.io/architecture/guardrails/ai/#gr-ai-01) Consider AI first | Should | ADR recording the AI options considered and why they were or were not used |
| [GR-TECH-02](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-02) Buy commodity, build differentiating | Should | Buy or build options appraisal in the ADR or business case |
| [GR-DATA-01](https://defra.github.io/architecture/guardrails/data/#gr-data-01) Every data set has an owner | Should | Each data set the service will create or hold identified, with a proposed information asset owner |
| [GR-HOST-07](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-07) Design for the resilience the service needs | Should | Recovery time and recovery point objectives agreed with the service owner, and a design that meets them |
| [GR-PROD-01](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-01) Fund and run products, not projects | Should | A named, long-lived team responsible for the product, with a roadmap beyond the current funding period |
| [GR-PROD-02](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-02) Name the product owner and service owner | Should | Named product owner and service owner, recorded in the service catalogue |
| [GR-PROD-03](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-03) Contribute to platforms rather than working around them | Should | Requests and contributions raised with platform teams, and ADRs where the team worked around a platform |

More on the [alpha page](https://defra.github.io/architecture/deliver/alpha/).

### Beta

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | Must | Approved DPIA, and retention and deletion built and tested |
| [GR-OPS-05](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05) Be ready for live before you go live | Must | Before public beta, the support model, on-call arrangements, runbooks, incident process and live owner agreed, and the service catalogue entry made |
| [GR-SEC-09](https://defra.github.io/architecture/guardrails/security/#gr-sec-09) Manage risk explicitly | Must | Residual risks accepted by the right owner through the security exception process, each with an expiry date |
| [GR-API-04](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-04) Version and deprecate deliberately | Should | Versioning approach published for each API and event |
| [GR-DATA-01](https://defra.github.io/architecture/guardrails/data/#gr-data-01) Every data set has an owner | Should | Information asset register entries with a named owner for each data set |
| [GR-DATA-07](https://defra.github.io/architecture/guardrails/data/#gr-data-07) Open by default | Should | Link to the published open data and its licence |
| [GR-HOST-07](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-07) Design for the resilience the service needs | Should | Multi-zone design built, and recovery tested before go-live |
| [GR-OPS-03](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-03) Define and measure service levels | Should | Agreed service level objectives with monitoring and alerts |
| [GR-OPS-07](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-07) Measure performance and cost | Should | Published key performance indicators and cost tags on cloud resources |
| [GR-PROD-01](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-01) Fund and run products, not projects | Should | A named, long-lived team responsible for the product, with a roadmap beyond the current funding period |
| [GR-PROD-02](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-02) Name the product owner and service owner | Should | Named product owner and service owner, recorded in the service catalogue |
| [GR-PROD-03](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-03) Contribute to platforms rather than working around them | Should | Requests and contributions raised with platform teams, and ADRs where the team worked around a platform |

More on the [beta page](https://defra.github.io/architecture/deliver/beta/).

### Live

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | Must | DPIA reviewed when processing changes, and deletion running as designed |
| [GR-OPS-05](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05) Be ready for live before you go live | Must | Runbooks and support arrangements tested and kept current |
| [GR-SEC-09](https://defra.github.io/architecture/guardrails/security/#gr-sec-09) Manage risk explicitly | Must | Accepted risks reviewed before they expire |
| [GR-API-04](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-04) Version and deprecate deliberately | Should | Deprecation notices sent to consumers and retirement dates published for old versions |
| [GR-DATA-01](https://defra.github.io/architecture/guardrails/data/#gr-data-01) Every data set has an owner | Should | Register entries and owners kept current |
| [GR-DATA-07](https://defra.github.io/architecture/guardrails/data/#gr-data-07) Open by default | Should | Link to the published open data and its licence |
| [GR-HOST-07](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-07) Design for the resilience the service needs | Should | Recovery tested at least once a year, with the date of the last test |
| [GR-OPS-03](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-03) Define and measure service levels | Should | Agreed service level objectives with monitoring and alerts |
| [GR-OPS-07](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-07) Measure performance and cost | Should | Published key performance indicators and cost tags on cloud resources |
| [GR-PROD-01](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-01) Fund and run products, not projects | Should | A named, long-lived team responsible for the product, with a roadmap beyond the current funding period |
| [GR-PROD-02](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-02) Name the product owner and service owner | Should | Named product owner and service owner, recorded in the service catalogue |
| [GR-PROD-03](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-03) Contribute to platforms rather than working around them | Should | Requests and contributions raised with platform teams, and ADRs where the team worked around a platform |
| [GR-PROD-04](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-04) Plan for the end of a product's life | Should | Product lifecycle stage recorded, with a retirement plan for products being replaced |

More on the [live page](https://defra.github.io/architecture/deliver/live/).

### Significant change

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | Must | DPIA updated for any change in how personal data is processed |
| [GR-TECH-06](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-06) Get spend approval early | Must | Architecture team consulted before new procurement for the change |
| [GR-OPS-05](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05) Be ready for live before you go live | Must | Runbooks and support arrangements updated before the change goes live |
| [GR-API-04](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-04) Version and deprecate deliberately | Should | Consumers told about breaking changes in advance, with a new version and a retirement date for the old one |
| [GR-HOST-07](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-07) Design for the resilience the service needs | Should | Recovery objectives and design checked for the change |

More on the [significant change page](https://defra.github.io/architecture/deliver/significant-change/).

### Retire a service

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | Must | Personal data deleted or transferred lawfully, as set out in the DPIA |
| [GR-DATA-01](https://defra.github.io/architecture/guardrails/data/#gr-data-01) Every data set has an owner | Should | Information asset register updated to show what happened to each data set |
| [GR-API-04](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-04) Version and deprecate deliberately | Should | Consumers told the retirement date in advance, and moved to a replacement |

More on the [retire a service page](https://defra.github.io/architecture/deliver/retire/).

## Patterns that help

- [File upload with malware scanning](https://defra.github.io/architecture/patterns/file-upload/) - Users upload documents or images, and the files must be scanned and stored safely before anyone opens them.
- [Publishing open data with metadata](https://defra.github.io/architecture/patterns/open-data-publishing/) - You hold non-personal data that others could use, and want to publish it so it can be found, trusted and reused.

## Working with architects

- In discovery, agree with an architect what already exists that you could reuse, before you commit to building or buying.
- Before any procurement, talk to the architecture team ([GR-TECH-06](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-06)).
- Agree the service tier and the non-functional requirements that come with it in alpha - see [service tiers](https://defra.github.io/architecture/nfrs/service-tiers/).
- Bring decisions that are hard to reverse to your solution design authority, with an ADR.



