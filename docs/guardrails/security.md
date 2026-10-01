---
principles: [GR-PRIN-06]
# Metadata for every guardrail on this page. See the contribution guide for the fields.
guardrail_defaults:
  status: draft
  owner: Enterprise security architecture
  automated_check: manual
  last_reviewed: 2026-10-01
  since_version: 0.1.0
guardrails:
  GR-SEC-01:
    phases: [discovery, alpha, beta, live]
    evidence: Named risk owner and the Secure by Design activities completed for the phase
    service_standard_points: [9]
    tcop_points: [6]
    sbd_principles: [1, 3]
  GR-SEC-02:
    phases: [alpha, beta, live]
    evidence: Current, dated threat model, reviewed at the last significant change and at least annually
    service_standard_points: [9]
    tcop_points: [6]
    sbd_principles: [3]
  GR-SEC-03:
    phases: [discovery, alpha]
    evidence: Security classification and data types recorded with the controls that match them
    tcop_points: [6]
    sbd_principles: [3]
  GR-SEC-04:
    phases: [alpha, beta, live]
    evidence: TLS configuration and encryption at rest settings for every data store
    tcop_points: [6]
    sbd_principles: [8]
  GR-SEC-05:
    phases: [alpha, beta, live]
    evidence: Pipeline scanning results and the time taken to fix critical and high vulnerabilities
    automated_check: Static analysis, dependency, container and infrastructure scanning in the pipeline
    tcop_points: [6]
    sbd_principles: [9]
  GR-SEC-06:
    phases: [beta, live]
    evidence: IT health check report and remediation tracker
    service_standard_points: [9]
    sbd_principles: [9]
  GR-SEC-07:
    phases: [beta, live]
    evidence: Security-relevant events reaching the security operations centre
    sbd_principles: [5]
  GR-SEC-08:
    phases: [alpha, beta, live]
    evidence: Supplier security assessments, pinned dependencies and a software bill of materials
    automated_check: Dependency review and software bill of materials generation in the pipeline
    tcop_points: [6]
    sbd_principles: [2]
  GR-SEC-09:
    phases: [discovery, alpha, beta, live]
    evidence: Risk register entries with an owner and an expiry date for every accepted risk
    sbd_principles: [1, 3]
---

# Security

<p class="lead">Security guardrails for every Defra service. They put the government <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/">Secure by Design</a> approach into practice.</p>

See also [enterprise security architecture](../security/index.md).

## GR-SEC-01 Follow Secure by Design {#gr-sec-01}

<span class="rfc rfc--must">Must</span> Every new service and significant change follows the [Secure by Design](../security/secure-by-design.md) activities, with a named risk owner, from discovery onward.

**How to meet it:** start from the patterns and checklists in the [Secure by Design artefact library](https://github.com/co-cddo/SbD) rather than designing controls from scratch.

## GR-SEC-02 Keep a current threat model {#gr-sec-02}

<span class="rfc rfc--must">Must</span> Each service has a [threat model](../security/threat-modelling.md), created by the team in alpha and revisited at every significant change and at least annually.

## GR-SEC-03 Classify information {#gr-sec-03}

<span class="rfc rfc--must">Must</span> Identify the [government security classification](https://www.gov.uk/government/publications/government-security-classifications) and data types the service handles, and design controls to match.

## GR-SEC-04 Encrypt in transit and at rest {#gr-sec-04}

<span class="rfc rfc--must">Must</span> Use TLS 1.2 or higher for all traffic, internal and external, and encrypt data at rest using platform-managed or customer-managed keys.

## GR-SEC-05 Scan continuously and fix quickly {#gr-sec-05}

<span class="rfc rfc--must">Must</span> Run static analysis, dependency, container and infrastructure scanning in the pipeline. Fix critical vulnerabilities within 14 days and high within 30 days, or record a risk decision.

## GR-SEC-06 Test before go-live and after major change {#gr-sec-06}

<span class="rfc rfc--must">Must</span> Commission an independent IT health check (penetration test) proportionate to risk before go-live and after significant change, and track remediation.

## GR-SEC-07 Log for detection and response {#gr-sec-07}

<span class="rfc rfc--must">Must</span> Send security-relevant events (authentication, authorisation failures, administrative actions, data exports) to the security operations centre. See [GR-OPS-01](observability-and-operations.md#gr-ops-01).

## GR-SEC-08 Protect the supply chain {#gr-sec-08}

<span class="rfc rfc--must">Must</span> Assess suppliers and third-party products for security before use, pin and verify dependencies, and know what is in your software (keep a software bill of materials).

## GR-SEC-09 Manage risk explicitly {#gr-sec-09}

<span class="rfc rfc--must">Must</span> Where a control cannot be met, record the risk and get it accepted by the right owner through the [security exception process](../security/managing-exceptions.md). Accepted risks are time-limited.
