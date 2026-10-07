<!-- https://defra.github.io/architecture/partners/multi-supplier/ | maturity: published | site version 0.3.0 | generated from partners/multi-supplier.md -->

# Working with other suppliers

<p class="lead">Many Defra services are built by more than one team, often from different companies. These rules of the road stop integrations, incidents and environments falling between the gaps.</p>

## Every integration has one owner

Each API, event or data product has **one owning team**, named in its specification and in the service catalogue. The owner:

- publishes the contract as OpenAPI or AsyncAPI, in its repository ([GR-API-02](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-02))
- versions it, and tells consumers about breaking changes in advance with a retirement date for old versions ([GR-API-04](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-04))
- runs consumers' contract tests in its pipeline (see below)
- is the first point of contact when the integration fails

Consumers own their own resilience: timeouts, retries and what users see when a dependency is down ([GR-OPS-04](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-04)).

| Responsibility | Owning team | Consuming team | Defra |
| --- | --- | --- | --- |
| Contract (OpenAPI or AsyncAPI) | Writes and versions | Reviews and agrees | Solution design authority resolves disputes |
| Contract tests | Runs in its pipeline | Writes and maintains | - |
| Availability and performance | Meets agreed targets | Handles failure gracefully | Agrees targets through the service tier |
| Breaking changes | Announces with notice | Migrates before the retirement date | Approves exceptions to the notice period |

## Test contracts, not just code

Use **consumer-driven contract tests**: each consumer writes tests describing exactly what it relies on, and the provider runs them in its pipeline before every release. A change that would break a consumer fails the provider's build, not the consumer's service in production.

- Keep contract tests in the consumer's repository and publish them where the provider's pipeline can fetch them, for example through a contract broker.
- Test against the published OpenAPI or AsyncAPI specification as well, so the specification and the code cannot drift.
- Do not rely on a shared end-to-end environment as the only test of an integration. It is slow, fragile and hard to own.

## Shared incidents

When an incident affects more than one team:

1. **One incident lead** coordinates, normally from the team that owns the failing component or from Defra's live service team. Everyone else supports.
2. **One channel** for the incident, joined by every affected team, whichever company they work for.
3. **Runbooks name the other teams** you depend on and how to reach them out of hours ([GR-OPS-05](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05)).
4. **One blameless post-incident review**, with every team involved, shared openly ([GR-OPS-06](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-06)).

Commercial disputes about who caused an incident are handled separately and later. They must never slow down recovery.

<div id="tbc-1"></div>

!!! warning "To be confirmed"
    **TODO:** Defra's incident management process and tools for digital services, and how suppliers are given access to them.

## Shared environments and repositories

- Agree who owns each shared environment, and how changes to it are made - through code and pipelines, never by hand ([GR-HOST-03](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-03)).
- Work in the open in the Defra GitHub organisation, so every team can see the code it integrates with ([GR-OPEN-01](https://defra.github.io/architecture/guardrails/open-source/#gr-open-01)).
- Record decisions that affect other teams as ADRs, and share them with those teams before they take effect.

