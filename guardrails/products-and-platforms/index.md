<!-- https://defra.github.io/architecture/guardrails/products-and-platforms/ | maturity: published | site version 0.3.0 | generated from guardrails/products-and-platforms.md -->

# Products and platforms

<p class="lead">Defra builds and runs technology as long-lived products on shared platforms, not as one-off projects. These draft guardrails describe what that means for teams.</p>

<div class="da-trace" markdown>

**Doctrine:** [1. Platforms before projects. Built as products](https://defra.github.io/architecture/principles/doctrine/#ddts-01), [2. Standards and guardrails before exceptions](https://defra.github.io/architecture/principles/doctrine/#ddts-02), [3. Reuse before buy](https://defra.github.io/architecture/principles/doctrine/#ddts-03)  
**Principles:** [1. Delivery-focused architecture](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-01), [3. Maximise value, minimise waste](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-03)

</div>


!!! info "Who these guardrails apply to"
    The core department. Whether the products and platforms guardrails also apply to Defra's arm's length bodies is [still to be confirmed](https://defra.github.io/architecture/guardrails/#arms-length-bodies).


Applies the DDTS doctrine [platforms before projects](https://defra.github.io/architecture/principles/doctrine/#ddts-01).

!!! info "Draft guardrails"
    These guardrails are new drafts from the [guardrail backlog](https://defra.github.io/architecture/about/roadmap/#guardrail-backlog). Comment on them by [opening an issue](https://github.com/DEFRA/architecture/issues).

## GR-PROD-01 Fund and run products, not projects {#gr-prod-01}

<span class="rfc rfc--should">Should</span> Build and run digital services as products, owned by a long-lived team that keeps improving them, rather than as projects that end at go-live.

**Why:** services are used for years. When the team that built a service disbands at launch, knowledge is lost, technical debt grows and the service slowly fails its users.

**How to meet it:** plan funding and team continuity beyond go-live from the start. If a project model is unavoidable, agree before go-live which product team will own the service in live ([GR-OPS-05](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05)).


<details class="gr-meta"><summary>Phases, evidence and status for GR-PROD-01</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/product-manager/">Product manager</a></dd><dt>Evidence</dt><dd>A named, long-lived team responsible for the product, with a roadmap beyond the current funding period</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Have a multidisciplinary team">6</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.2.0</dd></dl></details>

## GR-PROD-02 Name the product owner and service owner {#gr-prod-02}

<span class="rfc rfc--should">Should</span> Every product has a named product owner, and every service a named service owner, who are accountable for it throughout its life.

**Why:** decisions about priorities, risk and retirement need someone with the authority to make them.

**How to meet it:** record both in the service catalogue and in the repository README, and keep them current when people move on.


<details class="gr-meta"><summary>Phases, evidence and status for GR-PROD-02</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Discovery, Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/product-manager/">Product manager</a>, <a href="../../deliver/roles/delivery-manager/">Delivery manager</a></dd><dt>Evidence</dt><dd>Named product owner and service owner, recorded in the service catalogue</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Have a multidisciplinary team">6</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.2.0</dd></dl></details>

## GR-PROD-03 Contribute to platforms rather than working around them {#gr-prod-03}

<span class="rfc rfc--should">Should</span> When a shared platform does not meet a need, raise it with the platform team and contribute to fixing it, rather than building a local workaround.

**Why:** every workaround becomes something else to secure, support and eventually remove, and other teams have the same need.

**How to meet it:** talk to the platform team first. If you must work around a gap to meet a deadline, record it in an ADR with a plan to move back on to the platform.


<details class="gr-meta"><summary>Phases, evidence and status for GR-PROD-03</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a>, <a href="../../deliver/roles/product-manager/">Product manager</a></dd><dt>Evidence</dt><dd>Requests and contributions raised with platform teams, and ADRs where the team worked around a platform</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Use and contribute to open standards, common components and patterns">13</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Share, reuse and collaborate">8</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.2.0</dd></dl></details>

## GR-PROD-04 Plan for the end of a product's life {#gr-prod-04}

<span class="rfc rfc--should">Should</span> Know where each product is in its lifecycle - growing, stable, being replaced or retiring - and plan its retirement as deliberately as its launch.

**Why:** products that linger after they are replaced keep costing money and carrying risk.

**How to meet it:** record the lifecycle stage in the service catalogue, and follow [retire a service](https://defra.github.io/architecture/deliver/retire/) when the time comes.

<details class="gr-meta"><summary>Phases, evidence and status for GR-PROD-04</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/product-manager/">Product manager</a></dd><dt>Evidence</dt><dd>Product lifecycle stage recorded, with a retirement plan for products being replaced</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Define your purchasing strategy">11</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.2.0</dd></dl></details>


