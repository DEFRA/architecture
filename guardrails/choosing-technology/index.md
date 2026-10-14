<!-- https://defra.github.io/architecture/guardrails/choosing-technology/ | maturity: published | site version 0.3.0 | generated from guardrails/choosing-technology.md -->

# Choosing technology

<p class="lead">How to decide whether to reuse, buy or build - and how to avoid being stuck with the choice.</p>

<div class="da-trace" markdown>

**Doctrine:** [1. Platforms before projects. Built as products](https://defra.github.io/architecture/principles/doctrine/#ddts-01), [2. Standards and guardrails before exceptions](https://defra.github.io/architecture/principles/doctrine/#ddts-02), [3. Reuse before buy](https://defra.github.io/architecture/principles/doctrine/#ddts-03)  
**Principles:** [3. Maximise value, minimise waste](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-03), [1. Delivery-focused architecture](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-01)

</div>


!!! info "Who these guardrails apply to"
    The core department. Whether the choosing technology guardrails also apply to Defra's arm's length bodies is [still to be confirmed](https://defra.github.io/architecture/guardrails/#arms-length-bodies).


## GR-TECH-01 Look for something to reuse first {#gr-tech-01}

<span class="rfc rfc--must">Must</span> Before buying or building, check the [technology capability catalogue](https://defra.github.io/architecture/handrail/technology-capabilities/) and cross-government components for something that already meets the need.

**Why:** Duplicate capabilities multiply cost, security risk and support effort.

**How to meet it:** Record in your ADR which strategic options you considered and why they did or did not fit. If a strategic option is close but not quite right, talk to the owning platform team before building around it.


<details class="gr-meta"><summary>Phases, evidence and status for GR-TECH-01</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Discovery, Alpha</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Discovery:</strong> Existing Defra and cross-government options for the need identified from the technology capability catalogue</li><li><strong>Alpha:</strong> ADR recording the reuse options considered and why they did or did not fit</li><li><strong>Significant change:</strong> ADR showing reuse options considered for any new component</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Use and contribute to open standards, common components and patterns">13</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Share, reuse and collaborate">8</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-TECH-02 Buy commodity, build differentiating {#gr-tech-02}

<span class="rfc rfc--should">Should</span> Buy or use SaaS for commodity needs (email, HR, finance, CRM, document management). Build only where the capability is specific to Defra's mission and no product fits without heavy customisation.

**Why:** Heavily customised products combine the cost of building with the constraints of buying.

**How to meet it:** If you are configuring more than you are using out of the box, stop and reconsider. Prefer configuration over customisation; avoid modifying vendor code.


<details class="gr-meta"><summary>Phases, evidence and status for GR-TECH-02</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Discovery, Alpha</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a>, <a href="../../deliver/roles/product-manager/">Product manager</a></dd><dt>Evidence</dt><dd>Buy or build options appraisal in the ADR or business case</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Choose the right tools and technology">11</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Define your purchasing strategy">11</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-TECH-03 Plan your exit before you enter {#gr-tech-03}

<span class="rfc rfc--should">Should</span> Any new product, platform or significant supplier dependency has a documented exit plan covering data export in open formats, contract terms and an estimate of switching cost.

**Why:** Lock-in is sometimes a sensible trade-off, but it must be a deliberate one.

**How to meet it:** Include an exit section in your ADR or business case. Make sure contracts give Defra ownership of its data and the right to export it.


<details class="gr-meta"><summary>Phases, evidence and status for GR-TECH-03</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a>, <a href="../../deliver/roles/delivery-manager/">Delivery manager</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Draft exit plan for each new product, platform or significant supplier</li><li><strong>Beta:</strong> Exit plan agreed, with contracts giving Defra its data and the right to export it in open formats</li><li><strong>Live:</strong> Exit plan reviewed at contract renewal, with switching cost estimated</li><li><strong>Significant change:</strong> Exit plan updated for any new product or supplier</li><li><strong>Retire:</strong> Exit plan carried out - data exported in open formats and contracts ended</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Define your purchasing strategy">11</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-TECH-04 Assess SaaS before you adopt it {#gr-tech-04}

<span class="rfc rfc--must">Must</span> SaaS and third-party hosted products are assessed for security, data protection, data location, accessibility and integration before contract.

**Why:** Supply chain risk is one of the biggest sources of security incidents in government.

**How to meet it:** Use the [Secure by Design](https://defra.github.io/architecture/security/secure-by-design/) supplier assurance activities, complete a DPIA if personal data is involved and confirm the product supports single sign-on with Microsoft Entra ID for staff ([GR-IAM-02](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-02)).


<details class="gr-meta"><summary>Phases, evidence and status for GR-TECH-04</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Discovery, Alpha</dd><dt>Led by</dt><dd><a href="../../deliver/roles/security-architect/">Security architect</a>, <a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Discovery:</strong> SaaS and third-party products under consideration listed, with the assessments they will need</li><li><strong>Alpha:</strong> Security, data protection, data location, accessibility and single sign-on assessed before contract</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Create a secure service which protects users&#x27; privacy">9</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make things secure">6</abbr>, <abbr title="Make privacy integral">7</abbr>, <abbr title="Define your purchasing strategy">11</abbr>; <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Source secure technology products">2</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-TECH-05 Prefer open standards and portable technology {#gr-tech-05}

<span class="rfc rfc--should">Should</span> Choose products and components that use [open standards](https://www.gov.uk/government/publications/open-standards-principles) and can be run on more than one provider.

**Why:** Portability keeps our options open and our commercial position strong.


<details class="gr-meta"><summary>Phases, evidence and status for GR-TECH-05</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd>ADR noting the open standards used and how portable the choice is</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Use and contribute to open standards, common components and patterns">13</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make use of open standards">4</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-TECH-06 Get spend approval early {#gr-tech-06}

<span class="rfc rfc--must">Must</span> Spend that falls under the [government digital and technology spend control](https://www.gov.uk/service-manual/agile-delivery/spend-controls-check-if-you-need-approval-to-spend-money-on-a-service) is discussed with the architecture team before procurement starts.

**Why:** Architecture questions raised at the end of a procurement are expensive to answer.

<details class="gr-meta"><summary>Phases, evidence and status for GR-TECH-06</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Discovery</dd><dt>Led by</dt><dd><a href="../../deliver/roles/delivery-manager/">Delivery manager</a>, <a href="../../deliver/roles/product-manager/">Product manager</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Discovery:</strong> Architecture team consulted before any procurement under spend control starts</li><li><strong>Significant change:</strong> Architecture team consulted before new procurement for the change</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Define your purchasing strategy">11</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>


