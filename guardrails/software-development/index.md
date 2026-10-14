<!-- https://defra.github.io/architecture/guardrails/software-development/ | maturity: published | site version 0.3.0 | generated from guardrails/software-development.md -->

# Software development

<p class="lead">How we write, test and ship code so that any Defra team, or any partner, can pick it up and run with it.</p>

<div class="da-trace" markdown>

**Doctrine:** [1. Platforms before projects. Built as products](https://defra.github.io/architecture/principles/doctrine/#ddts-01), [2. Standards and guardrails before exceptions](https://defra.github.io/architecture/principles/doctrine/#ddts-02), [3. Reuse before buy](https://defra.github.io/architecture/principles/doctrine/#ddts-03)  
**Principles:** [1. Delivery-focused architecture](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-01), [3. Maximise value, minimise waste](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-03)

</div>


!!! info "Who these guardrails apply to"
    The core department. Whether the software development guardrails also apply to Defra's arm's length bodies is [still to be confirmed](https://defra.github.io/architecture/guardrails/#arms-length-bodies).


!!! tip "Looking for detailed coding guidance?"
    These guardrails set the boundaries. The [Defra software development standards](https://defra.github.io/software-development-standards/) are the detailed, practical guide to languages, coding style, testing, source control, versioning and release - follow them for day-to-day engineering.

## GR-DEV-01 Use the supported languages and frameworks {#gr-dev-01}

<span class="rfc rfc--should">Should</span> Use Defra's approved technologies and languages for new services so that skills, libraries and support are shared.

The list, and the reasons for each choice, are in [approved technologies and languages](https://digital.defra.gov.uk/software-development#approved-technologies-and-languages) in the Defra Digital Service Manual and in the [Defra software development standards](https://defra.github.io/software-development-standards/). In short: Node.js with hapi for front-end and back-end services, GOV.UK Frontend Nunjucks templates, .NET or Python only where Node.js is not suitable, and no other front-end frameworks. Review approved technologies, and request new ones, on the [Defra Tools Radar](https://eaflood.atlassian.net/jira/software/projects/TR/boards/630), which needs a Defra network and sign-in.

**Why:** A small, well-supported set of technologies makes it easier to move people between teams, share components and support services for the long term.

**How to meet it:** If you need something else, request it through the Tools Radar and record the reason in an ADR, including how the service will be supported after the team moves on. The Delivery Architecture team handles exceptions to the software development standards.


<details class="gr-meta"><summary>Phases, evidence and status for GR-DEV-01</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a>, <a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd>ADR recording the reason wherever the service uses a different stack</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Choose the right tools and technology">11</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-DEV-02 All code in Defra source control {#gr-dev-02}

<span class="rfc rfc--must">Must</span> All source code, including infrastructure and pipeline code written by suppliers, lives in a Defra-owned GitHub organisation from day one.

**Why:** Defra owns what it pays for and must be able to change supplier without losing code or history.


<details class="gr-meta"><summary>Phases, evidence and status for GR-DEV-02</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a>, <a href="../../deliver/roles/delivery-manager/">Delivery manager</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> All code, including prototypes and infrastructure code written by suppliers, in a Defra-owned GitHub organisation from the first commit</li><li><strong>Beta:</strong> All source, infrastructure and pipeline code in the Defra GitHub organisation, with nothing held only by a supplier</li><li><strong>Live:</strong> All changes made in the Defra GitHub organisation</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Make new source code open">12</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-DEV-03 Protect the main branch {#gr-dev-03}

<span class="rfc rfc--should">Should</span> Main branches are protected: changes arrive through pull requests with at least one review and passing automated checks.


<details class="gr-meta"><summary>Phases, evidence and status for GR-DEV-03</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Main branch protected from the start, with changes through reviewed pull requests</li><li><strong>Beta:</strong> Branch protection requiring at least one review and passing checks</li><li><strong>Live:</strong> Branch protection still in place on every repository</li></ul></dd><dt>Automated check</dt><dd>Guardrail check (tools/guardrail-check): default branch protected by branch protection or a ruleset</dd><dt>Maps to</dt><dd><a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Make changes securely">10</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-DEV-04 Continuous integration and delivery {#gr-dev-04}

<span class="rfc rfc--should">Should</span> Every change is built, tested, scanned and deployed by an automated pipeline. Releases to production are small, frequent and reversible.


<details class="gr-meta"><summary>Phases, evidence and status for GR-DEV-04</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Beta:</strong> Every change built, tested, scanned and deployed by an automated pipeline, with rollback tested</li><li><strong>Live:</strong> Deployment history showing small, frequent, reversible releases</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Operate a reliable service">14</abbr>; <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Make changes securely">10</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-DEV-05 Automated testing at the right levels {#gr-dev-05}

<span class="rfc rfc--should">Should</span> Use a balanced set of automated tests - unit, integration/contract, end-to-end journey, accessibility, performance and security - run in the pipeline.


<details class="gr-meta"><summary>Phases, evidence and status for GR-DEV-05</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd>Test results from the pipeline at each level</dd><dt>Automated check</dt><dd>Manual</dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-DEV-06 Manage dependencies actively {#gr-dev-06}

<span class="rfc rfc--should">Should</span> Use automated dependency updates and software composition analysis, and keep runtimes on supported versions.

**Why:** Unpatched dependencies are one of the most common ways services are compromised.


<details class="gr-meta"><summary>Phases, evidence and status for GR-DEV-06</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Beta:</strong> Dependabot or Renovate configured, software composition analysis in the pipeline, and runtimes on supported versions</li><li><strong>Live:</strong> Dependency updates merged promptly and runtimes upgraded before they go out of support</li></ul></dd><dt>Automated check</dt><dd>Guardrail check (tools/guardrail-check): Dependabot or Renovate configured</dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-DEV-07 Follow shared coding standards {#gr-dev-07}

<span class="rfc rfc--should">Should</span> Use automated linting and formatting, and follow the [Defra software development standards](https://defra.github.io/software-development-standards/), so code looks and behaves consistently across teams.


<details class="gr-meta"><summary>Phases, evidence and status for GR-DEV-07</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd>Linting and formatting checks in the pipeline</dd><dt>Automated check</dt><dd>Lint and format checks in the pipeline</dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-DEV-08 Document as you go {#gr-dev-08}

<span class="rfc rfc--should">Should</span> Each repository has a README explaining what it does, how to run it locally, how to test it and how to deploy it, and links to its ADRs.


<details class="gr-meta"><summary>Phases, evidence and status for GR-DEV-08</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd>README explaining what the service does and how to run, test and deploy it, with links to its ADRs</dd><dt>Automated check</dt><dd>Guardrail check (tools/guardrail-check): README sections on running, testing and deploying, and a link to ADRs</dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-DEV-09 Record significant decisions as ADRs {#gr-dev-09}

<span class="rfc rfc--should">Should</span> Record significant architecture decisions as [architecture decision records](https://defra.github.io/architecture/governance/architecture-decision-records/) (ADRs), kept with the code or linked from the repository's README.

**Why:** the reasons behind a design are lost when people move on. ADRs let the next team, an assessor or a partner taking over the service understand what was decided and why, and change it safely.

**How to meet it:** keep ADRs in a `docs/adr` folder in the service repository, using the [ADR template](https://defra.github.io/architecture/governance/templates/adr/). Write one when you make a decision that is hard to reverse, departs from a guardrail, or that someone will later ask "why did we do this?".

<details class="gr-meta"><summary>Phases, evidence and status for GR-DEV-09</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Discovery, Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd>ADR log in the repository or linked from its README</dd><dt>Automated check</dt><dd>Guardrail check (tools/guardrail-check): ADRs in docs/adr</dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.2.0</dd></dl></details>


