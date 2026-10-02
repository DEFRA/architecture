---
applicability: tbc
principles: [GR-PRIN-01]
# Metadata for every guardrail on this page. See the contribution guide for the fields.
guardrail_defaults:
  status: draft
  owner: Architecture team
  automated_check: manual
  last_reviewed: 2026-10-01
  since_version: 0.1.0
guardrails:
  GR-OPS-01:
    phases: [beta, live]
    evidence: Dashboards and alerts in the platform's observability tooling and security events reaching the security operations centre
    evidence_by_phase:
      beta: Logs, metrics and traces reaching the platform's observability tooling, and security events reaching the security operations centre
      live: Dashboards and alerts in use by the team that runs the service
    service_standard_points: [14]
    sbd_principles: [5]
  GR-OPS-02:
    phases: [beta, live]
    evidence: Sample logs showing structured fields and correlation identifiers and no secrets
    evidence_by_phase:
      beta: Structured logs with correlation identifiers, tested to show no secrets or unnecessary personal data are logged
      live: Logging reviewed when new data or features are added
    sbd_principles: [5]
  GR-OPS-03:
    phases: [beta, live]
    evidence: Agreed service level objectives with monitoring and alerts
    service_standard_points: [14]
  GR-OPS-04:
    phases: [beta, live]
    evidence: Health endpoints, timeout and retry settings, and a design for when dependencies fail
    service_standard_points: [14]
  GR-OPS-05:
    phases: [beta, live]
    evidence: Support model, on-call arrangements, runbooks, incident process, named live owner and service catalogue entry
    evidence_by_phase:
      beta: Before public beta, the support model, on-call arrangements, runbooks, incident process and live owner agreed, and the service catalogue entry made
      live: Runbooks and support arrangements tested and kept current
      significant-change: Runbooks and support arrangements updated before the change goes live
    service_standard_points: [14]
  GR-OPS-06:
    phases: [live]
    evidence: Post-incident reviews and the actions taken
    service_standard_points: [14]
  GR-OPS-07:
    phases: [beta, live]
    evidence: Published key performance indicators and cost tags on cloud resources
    service_standard_points: [10]
---

# Observability and operations

<p class="lead">Services live for years. These guardrails make sure they can be run, supported and improved by people who did not build them.</p>

Technology capability [TC23 Observability and security monitoring](../handrail/technology-capabilities.md#tc23).

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
