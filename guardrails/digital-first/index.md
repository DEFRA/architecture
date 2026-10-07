<!-- https://defra.github.io/architecture/guardrails/digital-first/ | maturity: published | site version 0.3.0 | generated from guardrails/digital-first.md -->

# Digital first and end-to-end services

<p class="lead">Design whole services around users, digital by default, without leaving behind people who cannot use them online. These draft guardrails describe what that means for architecture.</p>

<div class="da-trace" markdown>

**Doctrine:** [6. Outcomes and services over organisational structures](https://defra.github.io/architecture/principles/doctrine/#ddts-06), [7. Digital first where appropriate](https://defra.github.io/architecture/principles/doctrine/#ddts-07)  
**Principles:** [2. Design for users](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-02)

</div>


!!! info "Who these guardrails apply to"
    The core department. Whether the digital first and end-to-end services guardrails also apply to Defra's arm's length bodies is [still to be confirmed](https://defra.github.io/architecture/guardrails/#arms-length-bodies).


Applies the DDTS doctrines [outcomes over structures](https://defra.github.io/architecture/principles/doctrine/#ddts-06) and [digital first](https://defra.github.io/architecture/principles/doctrine/#ddts-07). See the [Defra Digital Service Manual](https://digital.defra.gov.uk/service-manual) for design and research guidance.

!!! info "Draft guardrails"
    These guardrails are new drafts from the [guardrail backlog](https://defra.github.io/architecture/about/roadmap/#guardrail-backlog). Comment on them by [opening an issue](https://github.com/DEFRA/architecture/issues).

## GR-DIG-01 Challenge paper and manual processes {#gr-dig-01}

<span class="rfc rfc--should">Should</span> Do not put a paper or email process online as it is. Find out why each step exists, and remove, automate or redesign it.

**Why:** digitising a broken process makes it faster to fail. The biggest gains come from removing steps, not speeding them up.

**How to meet it:** map the current process in discovery, including the parts staff do by hand. For each step, record whether it is needed, and why.


<details class="gr-meta"><summary>Phases, evidence and status for GR-DIG-01</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Discovery, Alpha</dd><dt>Led by</dt><dd><a href="../../deliver/roles/service-designer/">Service designer</a>, <a href="../../deliver/roles/user-researcher/">User researcher</a></dd><dt>Evidence</dt><dd>Discovery findings showing paper, email and manual steps in the current process and how the new design removes or justifies each one</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Solve a whole problem for users">2</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-06">6</a>, <a href="../../principles/doctrine/#ddts-07">7</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.2.0</dd></dl></details>

## GR-DIG-02 Design across organisational boundaries {#gr-dig-02}

<span class="rfc rfc--should">Should</span> Design the end-to-end service from the user's point of view, even when parts of it are delivered by other Defra organisations or other parts of government.

**Why:** users do not care which organisation does what. Many Defra users deal with several Defra bodies for one task.

**How to meet it:** identify the whole service your work is part of, talk to the teams delivering the other parts, and agree how users and data move between them.


<details class="gr-meta"><summary>Phases, evidence and status for GR-DIG-02</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Discovery, Alpha, Beta</dd><dt>Led by</dt><dd><a href="../../deliver/roles/service-designer/">Service designer</a></dd><dt>Evidence</dt><dd>A map of the whole service, including the parts other teams and organisations deliver, and agreed hand-offs between them</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Solve a whole problem for users">2</abbr>, <abbr title="Provide a joined-up experience across all channels">3</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-06">6</a>, <a href="../../principles/doctrine/#ddts-07">7</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.2.0</dd></dl></details>

## GR-DIG-03 Provide assisted digital and offline routes {#gr-dig-03}

<span class="rfc rfc--should">Should</span> Make sure people who cannot use the online service, or cannot use it alone, can still get what they need - with help, by phone or on paper - and that those routes lead to the same outcome and data.

**Why:** some Defra users have limited internet access, skills or confidence, particularly in rural areas. Service Standard point 5 asks that everyone can use the service.

**How to meet it:** design assisted routes in alpha, so staff-assisted applications go through the same system as online ones rather than a separate process.

<details class="gr-meta"><summary>Phases, evidence and status for GR-DIG-03</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/service-designer/">Service designer</a>, <a href="../../deliver/roles/user-researcher/">User researcher</a></dd><dt>Evidence</dt><dd>Assisted digital and offline routes designed and tested with users who need them</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Provide a joined-up experience across all channels">3</abbr>, <abbr title="Make sure everyone can use the service">5</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make things accessible and inclusive">2</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-06">6</a>, <a href="../../principles/doctrine/#ddts-07">7</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.2.0</dd></dl></details>


