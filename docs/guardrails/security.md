# Security

<p class="lead">Security guardrails for every Defra service. They put the government <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/">Secure by Design</a> approach into practice.</p>

Supports principle [GR-PRIN-06](principles.md#gr-prin-06). See also [enterprise security architecture](../security/index.md).

## GR-SEC-01 Follow Secure by Design {#gr-sec-01}

<span class="rfc rfc--must">Must</span> Every new service and significant change follows the [Secure by Design](../security/secure-by-design.md) activities, with a named risk owner, from discovery onward.

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
