<!-- https://defra.github.io/architecture/guardrails/security/ | maturity: published | site version 0.3.0 | generated from guardrails/security.md -->

# Security

<p class="lead">Security guardrails for every Defra service. They put the government <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/">Secure by Design</a> approach into practice.</p>

<div class="da-trace" markdown>

**Doctrine:** [2. Standards and guardrails before exceptions](https://defra.github.io/architecture/principles/doctrine/#ddts-02)  
**Principles:** [6. Secure today, safe tomorrow](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-06)

</div>


!!! info "Who these guardrails apply to"
    The core department. Whether the security guardrails also apply to Defra's arm's length bodies is [still to be confirmed](https://defra.github.io/architecture/guardrails/#arms-length-bodies).


See also [enterprise security architecture](https://defra.github.io/architecture/security/), and [create a secure service](https://digital.defra.gov.uk/security) in the Defra Digital Service Manual, which links to the Defra Group Security policies you must follow.

## GR-SEC-01 Follow Secure by Design {#gr-sec-01}

<span class="rfc rfc--must">Must</span> Every new service and significant change follows the [Secure by Design](https://defra.github.io/architecture/security/secure-by-design/) activities, with a named risk owner, from discovery onward.

**How to meet it:** start from the patterns and checklists in the [Secure by Design artefact library](https://github.com/co-cddo/SbD) rather than designing controls from scratch.


<details class="gr-meta"><summary>Phases, evidence and status for GR-SEC-01</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Discovery, Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/security-architect/">Security architect</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Discovery:</strong> Named risk owner, and the information and threats the service is likely to face identified</li><li><strong>Alpha:</strong> Secure by Design activities for alpha completed, including security requirements in the backlog</li><li><strong>Beta:</strong> Secure by Design activities for beta completed, including controls built and tested</li><li><strong>Live:</strong> Secure by Design activities for live continuing, including monitoring and review</li><li><strong>Significant change:</strong> Secure by Design activities repeated for the change, with the risk owner involved</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Create a secure service which protects users&#x27; privacy">9</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make things secure">6</abbr>; <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Create responsibility for cyber security risk">1</abbr>, <abbr title="Adopt a risk-driven approach">3</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-02">2</a></dd><dt>Owner</dt><dd>Enterprise security architecture, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-SEC-02 Keep a current threat model {#gr-sec-02}

<span class="rfc rfc--must">Must</span> Each service has a [threat model](https://defra.github.io/architecture/security/threat-modelling/), created by the team in alpha and revisited at every significant change and at least annually.


<details class="gr-meta"><summary>Phases, evidence and status for GR-SEC-02</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/security-architect/">Security architect</a>, <a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> First threat model, created by the team</li><li><strong>Beta:</strong> Threat model updated as controls are built and tested</li><li><strong>Live:</strong> Threat model reviewed at least once a year, with the date of the last review</li><li><strong>Significant change:</strong> Threat model revisited for the change before it is built</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Create a secure service which protects users&#x27; privacy">9</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make things secure">6</abbr>; <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Adopt a risk-driven approach">3</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-02">2</a></dd><dt>Owner</dt><dd>Enterprise security architecture, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-SEC-03 Classify information {#gr-sec-03}

<span class="rfc rfc--must">Must</span> Identify the [government security classification](https://www.gov.uk/government/publications/government-security-classifications) and data types the service handles, and design controls to match.


<details class="gr-meta"><summary>Phases, evidence and status for GR-SEC-03</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Discovery, Alpha</dd><dt>Led by</dt><dd><a href="../../deliver/roles/security-architect/">Security architect</a>, <a href="../../deliver/roles/data-architect/">Data architect</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Discovery:</strong> Security classification and the types of data the service will handle identified</li><li><strong>Alpha:</strong> Controls in the design that match the classification</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make things secure">6</abbr>; <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Adopt a risk-driven approach">3</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-02">2</a></dd><dt>Owner</dt><dd>Enterprise security architecture, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-SEC-04 Encrypt in transit and at rest {#gr-sec-04}

<span class="rfc rfc--must">Must</span> Use TLS 1.2 or higher for all traffic, internal and external, and encrypt data at rest using platform-managed or customer-managed keys.


<details class="gr-meta"><summary>Phases, evidence and status for GR-SEC-04</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a>, <a href="../../deliver/roles/security-architect/">Security architect</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Beta:</strong> TLS 1.2 or higher for all traffic and encryption at rest for every data store, confirmed as built</li><li><strong>Live:</strong> Encryption settings checked when new stores or connections are added</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make things secure">6</abbr>; <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Defend in depth">8</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-02">2</a></dd><dt>Owner</dt><dd>Enterprise security architecture, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-SEC-05 Scan continuously and fix quickly {#gr-sec-05}

<span class="rfc rfc--must">Must</span> Run static analysis, dependency, container and infrastructure scanning in the pipeline. Fix critical vulnerabilities within 14 days and high within 30 days, or record a risk decision.


<details class="gr-meta"><summary>Phases, evidence and status for GR-SEC-05</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Beta:</strong> Static analysis, dependency, container and infrastructure scanning running in the pipeline</li><li><strong>Live:</strong> Time taken to fix critical and high vulnerabilities, within 14 and 30 days, or a recorded risk decision</li></ul></dd><dt>Automated check</dt><dd>Static analysis, dependency, container and infrastructure scanning in the pipeline</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make things secure">6</abbr>; <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Embed continuous assurance">9</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-02">2</a></dd><dt>Owner</dt><dd>Enterprise security architecture, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-SEC-06 Test before go-live and after major change {#gr-sec-06}

<span class="rfc rfc--must">Must</span> Commission an independent IT health check (penetration test) proportionate to risk before go-live and after significant change, and track remediation.


<details class="gr-meta"><summary>Phases, evidence and status for GR-SEC-06</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/security-architect/">Security architect</a>, <a href="../../deliver/roles/delivery-manager/">Delivery manager</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Beta:</strong> IT health check before go-live, and a remediation tracker</li><li><strong>Live:</strong> IT health check after significant change, with remediation tracked</li><li><strong>Significant change:</strong> IT health check scoped and booked for the change where it is significant</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Create a secure service which protects users&#x27; privacy">9</abbr>; <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Embed continuous assurance">9</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-02">2</a></dd><dt>Owner</dt><dd>Enterprise security architecture, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-SEC-07 Log for detection and response {#gr-sec-07}

<span class="rfc rfc--must">Must</span> Send security-relevant events (authentication, authorisation failures, administrative actions, data exports) to the security operations centre. See [GR-OPS-01](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-01).


<details class="gr-meta"><summary>Phases, evidence and status for GR-SEC-07</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a>, <a href="../../deliver/roles/security-architect/">Security architect</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Beta:</strong> Authentication, authorisation failures, administrative actions and data exports sent to the security operations centre, and tested</li><li><strong>Live:</strong> Security events reviewed and alerts acted on</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Build in detect and respond security">5</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-02">2</a></dd><dt>Owner</dt><dd>Enterprise security architecture, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-SEC-08 Protect the supply chain {#gr-sec-08}

<span class="rfc rfc--should">Should</span> Assess suppliers and third-party products for security before use, pin and verify dependencies, and know what is in your software (keep a software bill of materials).


<details class="gr-meta"><summary>Phases, evidence and status for GR-SEC-08</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/security-architect/">Security architect</a>, <a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Security assessment of suppliers and third-party products in the design</li><li><strong>Beta:</strong> Dependencies pinned and verified, and a software bill of materials produced in the pipeline</li><li><strong>Live:</strong> Software bill of materials kept current, and supplier assessments reviewed at renewal</li></ul></dd><dt>Automated check</dt><dd>Dependency review and software bill of materials generation in the pipeline</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make things secure">6</abbr>; <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Source secure technology products">2</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-02">2</a></dd><dt>Owner</dt><dd>Enterprise security architecture, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-SEC-09 Manage risk explicitly {#gr-sec-09}

<span class="rfc rfc--must">Must</span> Where a control cannot be met, record the risk and get it accepted by the right owner through the [security exception process](https://defra.github.io/architecture/security/managing-exceptions/). Accepted risks are time-limited.

<details class="gr-meta"><summary>Phases, evidence and status for GR-SEC-09</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/security-architect/">Security architect</a>, <a href="../../deliver/roles/product-manager/">Product manager</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Risks from controls that cannot be met recorded, with an owner</li><li><strong>Beta:</strong> Residual risks accepted by the right owner through the security exception process, each with an expiry date</li><li><strong>Live:</strong> Accepted risks reviewed before they expire</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Create responsibility for cyber security risk">1</abbr>, <abbr title="Adopt a risk-driven approach">3</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-02">2</a></dd><dt>Owner</dt><dd>Enterprise security architecture, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>


