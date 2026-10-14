<!-- https://defra.github.io/architecture/guardrails/observability-and-operations/ | maturity: published | site version 0.3.0 | generated from guardrails/observability-and-operations.md -->

# Observability and operations

<p class="lead">Services live for years. These guardrails make sure they can be run, supported and improved by people who did not build them.</p>

<div class="da-trace" markdown>

**Doctrine:** [1. Platforms before projects. Built as products](https://defra.github.io/architecture/principles/doctrine/#ddts-01), [2. Standards and guardrails before exceptions](https://defra.github.io/architecture/principles/doctrine/#ddts-02)  
**Principles:** [1. Delivery-focused architecture](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-01)

</div>


!!! info "Who these guardrails apply to"
    The core department. Whether the observability and operations guardrails also apply to Defra's arm's length bodies is [still to be confirmed](https://defra.github.io/architecture/guardrails/#arms-length-bodies).


Technology capability [Operations](https://defra.github.io/architecture/handrail/technology-capabilities/#operations): observability and security monitoring.

## GR-OPS-01 Use the platform's observability tooling {#gr-ops-01}

<span class="rfc rfc--should">Should</span> Send structured logs, metrics and traces to the platform's observability tooling, and security events to the security operations centre.


<details class="gr-meta"><summary>Phases, evidence and status for GR-OPS-01</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Beta:</strong> Logs, metrics and traces reaching the platform&#x27;s observability tooling, and security events reaching the security operations centre</li><li><strong>Live:</strong> Dashboards and alerts in use by the team that runs the service</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Operate a reliable service">14</abbr>; <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Build in detect and respond security">5</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-OPS-02 Log in a structured, safe way {#gr-ops-02}

<span class="rfc rfc--should">Should</span> Use structured (JSON) logs with correlation identifiers across service boundaries. Never log secrets, tokens or unnecessary personal data.


<details class="gr-meta"><summary>Phases, evidence and status for GR-OPS-02</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Beta:</strong> Structured logs with correlation identifiers, tested to show no secrets or unnecessary personal data are logged</li><li><strong>Live:</strong> Logging reviewed when new data or features are added</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Build in detect and respond security">5</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-OPS-03 Define and measure service levels {#gr-ops-03}

<span class="rfc rfc--should">Should</span> Agree service level objectives for availability, latency and correctness with the service owner, monitor them, and alert on what matters to users rather than on every metric.


<details class="gr-meta"><summary>Phases, evidence and status for GR-OPS-03</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/product-manager/">Product manager</a>, <a href="../../deliver/roles/performance-analyst/">Performance analyst</a>, <a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd>Agreed service level objectives with monitoring and alerts</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Operate a reliable service">14</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-OPS-04 Health checks and graceful degradation {#gr-ops-04}

<span class="rfc rfc--should">Should</span> Expose health endpoints, set timeouts and retries on dependencies, and degrade gracefully (for example save progress and tell the user) when a dependency fails.


<details class="gr-meta"><summary>Phases, evidence and status for GR-OPS-04</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a>, <a href="../../deliver/roles/interaction-designer/">Interaction designer</a></dd><dt>Evidence</dt><dd>Health endpoints, timeout and retry settings, and a design for when dependencies fail</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Operate a reliable service">14</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-OPS-05 Be ready for live before you go live {#gr-ops-05}

<span class="rfc rfc--must">Must</span> Before public beta, agree the support model, on-call arrangements, runbooks, incident process and who owns the service in live. Register the service in the service catalogue.


<details class="gr-meta"><summary>Phases, evidence and status for GR-OPS-05</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/delivery-manager/">Delivery manager</a>, <a href="../../deliver/roles/product-manager/">Product manager</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Beta:</strong> Before public beta, the support model, on-call arrangements, runbooks, incident process and live owner agreed, and the service catalogue entry made</li><li><strong>Live:</strong> Runbooks and support arrangements tested and kept current</li><li><strong>Significant change:</strong> Runbooks and support arrangements updated before the change goes live</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Operate a reliable service">14</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-OPS-06 Learn from incidents {#gr-ops-06}

<span class="rfc rfc--should">Should</span> Hold blameless post-incident reviews for significant incidents and share the lessons in the open where appropriate.


<details class="gr-meta"><summary>Phases, evidence and status for GR-OPS-06</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/delivery-manager/">Delivery manager</a></dd><dt>Evidence</dt><dd>Post-incident reviews and the actions taken</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Operate a reliable service">14</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-OPS-07 Measure performance and cost {#gr-ops-07}

<span class="rfc rfc--should">Should</span> Publish the [mandatory key performance indicators](https://www.gov.uk/service-manual/measuring-success) and tag cloud resources so cost can be attributed to the service and business capability.

<details class="gr-meta"><summary>Phases, evidence and status for GR-OPS-07</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/performance-analyst/">Performance analyst</a>, <a href="../../deliver/roles/product-manager/">Product manager</a></dd><dt>Evidence</dt><dd>Published key performance indicators and cost tags on cloud resources</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Define what success looks like and publish performance data">10</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>


