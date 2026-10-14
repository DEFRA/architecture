<!-- https://defra.github.io/architecture/guardrails/identity-and-access/ | maturity: published | site version 0.3.0 | generated from guardrails/identity-and-access.md -->

# Identity and access

<p class="lead">Who users are and what they are allowed to do. Getting this right once, centrally, is safer and simpler for everyone.</p>

<div class="da-trace" markdown>

**Doctrine:** [2. Standards and guardrails before exceptions](https://defra.github.io/architecture/principles/doctrine/#ddts-02), [4. Data is an enterprise asset](https://defra.github.io/architecture/principles/doctrine/#ddts-04), [6. Outcomes and services over organisational structures](https://defra.github.io/architecture/principles/doctrine/#ddts-06)  
**Principles:** [5. Connect and collaborate](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-05), [6. Secure today, safe tomorrow](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-06)

</div>


!!! info "Who these guardrails apply to"
    The core department. Whether the identity and access guardrails also apply to Defra's arm's length bodies is [still to be confirmed](https://defra.github.io/architecture/guardrails/#arms-length-bodies).


Technology capability [Security & Compliance](https://defra.github.io/architecture/handrail/technology-capabilities/#security-and-compliance): customer identity and access, and staff identity and access.

## GR-IAM-01 Use the strategic customer identity services {#gr-iam-01}

<span class="rfc rfc--must">Must</span> Services for citizens, farmers and businesses use **Defra Customer Identity (Defra ID)**, which uses GOV.UK One Login and Government Gateway as identity providers, for authentication. Services do not build their own sign-in. See [Defra Customer Identity](https://digital.defra.gov.uk/architecture-and-software-development/defra-customer-identity) in the Defra Digital Service Manual.

**Why:** Users get one account across Defra services, we manage relationships between people and organisations (including agents) once, and we avoid storing credentials.

**How to meet it:** Talk to the Customer Identity team in discovery about the level of identity assurance you need and how the service will represent organisations and agents.


<details class="gr-meta"><summary>Phases, evidence and status for GR-IAM-01</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Discovery, Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a>, <a href="../../deliver/roles/service-designer/">Service designer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Discovery:</strong> Identity team engaged about the level of identity assurance needed and how users act for organisations</li><li><strong>Alpha:</strong> Sign-in designed with Defra Customer Identity, and tested with users</li><li><strong>Beta:</strong> Integration with Defra Customer Identity built and tested</li><li><strong>Live:</strong> No other sign-in introduced</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Create a secure service which protects users&#x27; privacy">9</abbr>, <abbr title="Use and contribute to open standards, common components and patterns">13</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Share, reuse and collaborate">8</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-04">4</a>, <a href="../../principles/doctrine/#ddts-06">6</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-IAM-02 Staff sign in with Microsoft Entra ID {#gr-iam-02}

<span class="rfc rfc--must">Must</span> Staff-facing services and products, including SaaS, use single sign-on through Microsoft Entra ID with multi-factor authentication. No local staff accounts.

**Why:** Joiners, movers and leavers are handled in one place, and conditional access protects every product.


<details class="gr-meta"><summary>Phases, evidence and status for GR-IAM-02</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Beta:</strong> Staff sign in through Microsoft Entra ID with multi-factor authentication, and there are no local staff accounts</li><li><strong>Live:</strong> Staff access reviewed regularly through Entra ID groups</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Create a secure service which protects users&#x27; privacy">9</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make things secure">6</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-04">4</a>, <a href="../../principles/doctrine/#ddts-06">6</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-IAM-03 Authorise on least privilege {#gr-iam-03}

<span class="rfc rfc--must">Must</span> Users, services and pipelines get only the permissions they need, granted through roles or groups, and reviewed regularly.


<details class="gr-meta"><summary>Phases, evidence and status for GR-IAM-03</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/security-architect/">Security architect</a>, <a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Beta:</strong> Role and group model built, with users, services and pipelines given only the permissions they need</li><li><strong>Live:</strong> Record of regular access reviews</li><li><strong>Retire:</strong> All access to the service&#x27;s systems and data removed</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make things secure">6</abbr>; <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Minimise the attack surface">7</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-04">4</a>, <a href="../../principles/doctrine/#ddts-06">6</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-IAM-04 Separate authentication from authorisation {#gr-iam-04}

<span class="rfc rfc--should">Should</span> Use the identity provider to establish who someone is; keep business authorisation rules (for example "can act for this holding") explicit, testable and in the right service.


<details class="gr-meta"><summary>Phases, evidence and status for GR-IAM-04</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a>, <a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd>Authorisation rules written down and covered by automated tests</dd><dt>Automated check</dt><dd>Manual</dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-04">4</a>, <a href="../../principles/doctrine/#ddts-06">6</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-IAM-05 No secrets in code {#gr-iam-05}

<span class="rfc rfc--must">Must</span> Secrets, keys and credentials are held in a managed secrets store, rotated, and never committed to source control. Use workload identity in preference to long-lived keys.

**How to meet it:** Enable secret scanning on every repository ([GR-OPEN-03](https://defra.github.io/architecture/guardrails/open-source/#gr-open-03)).


<details class="gr-meta"><summary>Phases, evidence and status for GR-IAM-05</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Secret scanning on from the first commit, and secrets held in a managed store from the start</li><li><strong>Beta:</strong> All secrets in a managed store with rotation, using workload identity where possible</li><li><strong>Live:</strong> Secrets rotated, and secret scanning alerts dealt with</li><li><strong>Retire:</strong> Secrets, keys and credentials revoked</li></ul></dd><dt>Automated check</dt><dd>GitHub secret scanning with push protection</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make things secure">6</abbr>; <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Minimise the attack surface">7</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-04">4</a>, <a href="../../principles/doctrine/#ddts-06">6</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-IAM-06 Privileged access is controlled and audited {#gr-iam-06}

<span class="rfc rfc--must">Must</span> Production and administrative access is just-in-time, uses phishing-resistant MFA, and is logged to the security operations centre.

<details class="gr-meta"><summary>Phases, evidence and status for GR-IAM-06</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/security-architect/">Security architect</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Beta:</strong> Just-in-time privileged access with phishing-resistant MFA configured, and logged to the security operations centre</li><li><strong>Live:</strong> Privileged access reviewed regularly</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Build in detect and respond security">5</abbr>, <abbr title="Defend in depth">8</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-04">4</a>, <a href="../../principles/doctrine/#ddts-06">6</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>


