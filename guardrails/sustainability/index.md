<!-- https://defra.github.io/architecture/guardrails/sustainability/ | maturity: published | site version 0.3.0 | generated from guardrails/sustainability.md -->

# Sustainability

<p class="lead">Defra leads the <a href="https://www.gov.uk/government/publications/greening-government-ict-and-digital-services-strategy-2020-2025">Greening Government ICT and Digital Services strategy</a>. Our own services should show what good looks like.</p>

<div class="da-trace" markdown>

**Doctrine:** [1. Platforms before projects. Built as products](https://defra.github.io/architecture/principles/doctrine/#ddts-01), [3. Reuse before buy](https://defra.github.io/architecture/principles/doctrine/#ddts-03)  
**Principles:** [3. Maximise value, minimise waste](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-03)

</div>


!!! info "Who these guardrails apply to"
    The core department. Whether the sustainability guardrails also apply to Defra's arm's length bodies is [still to be confirmed](https://defra.github.io/architecture/guardrails/#arms-length-bodies).


Relates to TCoP point 12.

Defra services must also meet a 15th point of the Service Standard, [deliver a sustainable service](https://digital.defra.gov.uk/sustainability), including a sustainability statement against the [6 objectives in Defra's digital sustainability strategy](https://digital.defra.gov.uk/sustainability/objectives). Use the Defra Digital Service Manual for how to do that. These guardrails cover the architecture decisions that contribute to it.

## GR-SUS-01 Consider sustainability in design decisions {#gr-sus-01}

<span class="rfc rfc--should">Should</span> Include environmental impact as a factor in ADRs for hosting, architecture and technology choices.

**In the Defra Digital Service Manual:** [assess risks and record sustainability actions](https://digital.defra.gov.uk/sustainability/process) - record the decisions in your sustainability statement as well as your ADRs.


<details class="gr-meta"><summary>Phases, evidence and status for GR-SUS-01</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Discovery, Alpha</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd>Environmental impact recorded in ADRs for hosting and technology choices</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make your technology sustainable">12</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-SUS-02 Right-size and switch off {#gr-sus-02}

<span class="rfc rfc--should">Should</span> Use autoscaling, scale non-production environments down out of hours, and delete unused resources.


<details class="gr-meta"><summary>Phases, evidence and status for GR-SUS-02</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd>Autoscaling and out-of-hours schedules for non-production environments</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make your technology sustainable">12</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-SUS-03 Choose lower-carbon regions and services {#gr-sus-03}

<span class="rfc rfc--could">Could</span> Where data rules allow, prefer cloud regions and services with lower carbon intensity, and use providers' carbon reporting.


<details class="gr-meta"><summary>Phases, evidence and status for GR-SUS-03</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd>Region and service choice recorded with its carbon intensity</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make your technology sustainable">12</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-SUS-04 Keep data and pages lean {#gr-sus-04}

<span class="rfc rfc--should">Should</span> Store only the data you need, for as long as you need it, and keep page weight low - which also helps users on slow connections ([GR-FE-05](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-05)).


<details class="gr-meta"><summary>Phases, evidence and status for GR-SUS-04</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a>, <a href="../../deliver/roles/interaction-designer/">Interaction designer</a></dd><dt>Evidence</dt><dd>Data retention settings and page weight measurements</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make your technology sustainable">12</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-SUS-05 Measure and report {#gr-sus-05}

<span class="rfc rfc--could">Could</span> Track the carbon footprint of your service using cloud provider tooling and report it alongside cost.

**In the Defra Digital Service Manual:** the [metrics for each of Defra's six objectives](https://digital.defra.gov.uk/sustainability/metrics).

<details class="gr-meta"><summary>Phases, evidence and status for GR-SUS-05</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/performance-analyst/">Performance analyst</a>, <a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd>Carbon footprint reported alongside cost</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make your technology sustainable">12</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>


