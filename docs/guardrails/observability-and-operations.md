# Observability and operations

<p class="lead">Services live for years. These guardrails make sure they can be run, supported and improved by people who did not build them.</p>

Supports principle [GR-PRIN-01](principles.md#gr-prin-01). Technology capability [TC23 Observability and security monitoring](../handrail/technology-capabilities.md#tc23).

## GR-OPS-01 Use the platform's observability tooling {#gr-ops-01}

<span class="rfc rfc--must">Must</span> Send structured logs, metrics and traces to the platform's observability tooling, and security events to the security operations centre.

## GR-OPS-02 Log in a structured, safe way {#gr-ops-02}

<span class="rfc rfc--must">Must</span> Use structured (JSON) logs with correlation identifiers across service boundaries. Never log secrets, tokens or unnecessary personal data.

## GR-OPS-03 Define and measure service levels {#gr-ops-03}

<span class="rfc rfc--should">Should</span> Agree service level objectives for availability, latency and correctness with the service owner, monitor them, and alert on what matters to users rather than on every metric.

## GR-OPS-04 Health checks and graceful degradation {#gr-ops-04}

<span class="rfc rfc--should">Should</span> Expose health endpoints, set timeouts and retries on dependencies, and degrade gracefully (for example save progress and tell the user) when a dependency fails.

## GR-OPS-05 Be ready for live before you go live {#gr-ops-05}

<span class="rfc rfc--must">Must</span> Before public beta, agree the support model, on-call arrangements, runbooks, incident process and who owns the service in live. Register the service in the service catalogue.

## GR-OPS-06 Learn from incidents {#gr-ops-06}

<span class="rfc rfc--should">Should</span> Hold blameless post-incident reviews for significant incidents and share the lessons in the open where appropriate.

## GR-OPS-07 Measure performance and cost {#gr-ops-07}

<span class="rfc rfc--should">Should</span> Publish the [mandatory key performance indicators](https://www.gov.uk/service-manual/measuring-success) and tag cloud resources so cost can be attributed to the service and business capability.
