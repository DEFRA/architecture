<!-- https://defra.github.io/architecture/guardrails/front-end-and-accessibility/ | maturity: published | site version 0.3.0 | generated from guardrails/front-end-and-accessibility.md -->

# Front end and accessibility

<p class="lead">Defra services should look like government, work for everyone and work on any device.</p>

<div class="da-trace" markdown>

**Doctrine:** [6. Outcomes and services over organisational structures](https://defra.github.io/architecture/principles/doctrine/#ddts-06), [7. Digital first where appropriate](https://defra.github.io/architecture/principles/doctrine/#ddts-07)  
**Principles:** [2. Design for users](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-02), [8. Right tools, right place](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-08)

</div>


!!! info "Who these guardrails apply to"
    The core department. Whether the front end and accessibility guardrails also apply to Defra's arm's length bodies is [still to be confirmed](https://defra.github.io/architecture/guardrails/#arms-length-bodies).


See the Defra Digital Service Manual for how to do this: [make sure everyone can use the service](https://digital.defra.gov.uk/accessibility), [components and patterns](https://digital.defra.gov.uk/design/components-and-patterns), [content design](https://digital.defra.gov.uk/content) and [Welsh language translation](https://digital.defra.gov.uk/content/welsh-language-translation). These guardrails cover the architecture choices that make it possible.

## GR-FE-01 Meet WCAG 2.2 AA {#gr-fe-01}

<span class="rfc rfc--must">Must</span> Public and staff-facing services meet [WCAG 2.2 level AA](https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps), are tested with assistive technology and publish an accessibility statement.

**Why:** It is the law (Public Sector Bodies Accessibility Regulations 2018) and Service Standard point 5.

**In the Defra Digital Service Manual:** [make sure everyone can use the service](https://digital.defra.gov.uk/accessibility), including the assistive technologies Defra staff use and when exemptions apply, [manage accessibility in your project](https://digital.defra.gov.uk/accessibility/manage-accessibility) and [test for accessibility](https://digital.defra.gov.uk/accessibility/test-for-accessibility).


<details class="gr-meta"><summary>Phases, evidence and status for GR-FE-01</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/interaction-designer/">Interaction designer</a>, <a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Prototypes built with accessible components, and a plan for an accessibility audit and assistive technology testing</li><li><strong>Beta:</strong> Accessibility audit and assistive technology testing completed, issues fixed, and an accessibility statement published</li><li><strong>Live:</strong> Accessibility statement kept current, and accessibility re-tested after significant change</li></ul></dd><dt>Automated check</dt><dd>Automated accessibility tests such as axe in the pipeline. These find some issues only; manual testing is still needed.</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Make sure everyone can use the service">5</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make things accessible and inclusive">2</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-06">6</a>, <a href="../../principles/doctrine/#ddts-07">7</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-FE-02 Use the GOV.UK Design System {#gr-fe-02}

<span class="rfc rfc--must">Must</span> Public-facing services use [GOV.UK Frontend](https://design-system.service.gov.uk/) and patterns. Staff-facing services should use them too.

**In the Defra Digital Service Manual:** [components and patterns](https://digital.defra.gov.uk/design/components-and-patterns).


<details class="gr-meta"><summary>Phases, evidence and status for GR-FE-02</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/interaction-designer/">Interaction designer</a>, <a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Prototypes built with the GOV.UK Design System, with departures recorded and researched</li><li><strong>Beta:</strong> The service uses GOV.UK Frontend, with design decisions recording any departures</li><li><strong>Live:</strong> GOV.UK Frontend kept up to date</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Make the service simple to use">4</abbr>, <abbr title="Use and contribute to open standards, common components and patterns">13</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make things accessible and inclusive">2</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-06">6</a>, <a href="../../principles/doctrine/#ddts-07">7</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-FE-03 Progressive enhancement {#gr-fe-03}

<span class="rfc rfc--should">Should</span> Core journeys work without JavaScript, and are server-rendered. Use JavaScript to enhance, not to make things work.


<details class="gr-meta"><summary>Phases, evidence and status for GR-FE-03</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a>, <a href="../../deliver/roles/interaction-designer/">Interaction designer</a></dd><dt>Evidence</dt><dd>Core journeys tested with JavaScript turned off</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Make sure everyone can use the service">5</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-06">6</a>, <a href="../../principles/doctrine/#ddts-07">7</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-FE-04 Consider forms platforms first {#gr-fe-04}

<span class="rfc rfc--should">Should</span> For form-based services, consider the forms options under [Customer Service](https://defra.github.io/architecture/handrail/technology-capabilities/#customer-service) before building a bespoke front end.

**In the Defra Digital Service Manual:** [Defra Forms](https://digital.defra.gov.uk/architecture-and-software-development/defra-forms).


<details class="gr-meta"><summary>Phases, evidence and status for GR-FE-04</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Discovery, Alpha</dd><dt>Led by</dt><dd><a href="../../deliver/roles/service-designer/">Service designer</a>, <a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd>ADR noting whether the forms capability was considered</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Share, reuse and collaborate">8</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-06">6</a>, <a href="../../principles/doctrine/#ddts-07">7</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-FE-05 Design for low bandwidth and rural users {#gr-fe-05}

<span class="rfc rfc--should">Should</span> Many Defra users - farmers, land managers, field staff - work in places with poor connectivity. Keep pages light, support saving progress, and consider offline working for field tools.


<details class="gr-meta"><summary>Phases, evidence and status for GR-FE-05</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta</dd><dt>Led by</dt><dd><a href="../../deliver/roles/service-designer/">Service designer</a>, <a href="../../deliver/roles/user-researcher/">User researcher</a></dd><dt>Evidence</dt><dd>Page weight budget, save-progress design and testing on slow connections</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Make sure everyone can use the service">5</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-06">6</a>, <a href="../../principles/doctrine/#ddts-07">7</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-FE-06 Support Welsh where required {#gr-fe-06}

<span class="rfc rfc--must">Must</span> Services used in Wales meet the Welsh Language Standards where they apply. Design for translation from the start.

**In the Defra Digital Service Manual:** [Welsh language translation](https://digital.defra.gov.uk/content/welsh-language-translation).


<details class="gr-meta"><summary>Phases, evidence and status for GR-FE-06</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/content-designer/">Content designer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Whether the Welsh Language Standards apply decided, and the service designed for translation</li><li><strong>Beta:</strong> Welsh content and journeys built and tested where the standards apply</li><li><strong>Live:</strong> Welsh content kept in step with English content</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Make sure everyone can use the service">5</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-06">6</a>, <a href="../../principles/doctrine/#ddts-07">7</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-FE-07 Tell users what is happening when things fail or are slow {#gr-fe-07}

<span class="rfc rfc--should">Should</span> When a service is slow, a dependency fails or something is still being processed, users see a clear message saying what has happened, whether their work is saved, and what to do next - not a generic error or a page that seems to hang.

**Why:** Defra services depend on platforms and back-office systems that will sometimes be slow or unavailable. Users who are not told what is happening give up, try again and create duplicates, or phone for help.

**How to meet it:**

- With the developers, list each dependency that can fail or be slow, and decide what users see for each. This is the user-facing side of [GR-OPS-04](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-04), which designs the service to degrade gracefully.
- Use the GOV.UK Design System [problem with the service pages](https://design-system.service.gov.uk/patterns/problem-with-the-service-pages/) and [service unavailable pages](https://design-system.service.gov.uk/patterns/service-unavailable-pages/), and say whether the user's answers are saved.
- For work that is processed later, show a status and a realistic time, as in the [asynchronous submission](https://defra.github.io/architecture/patterns/async-submission/#content-to-design) pattern.
- Test these messages with users in alpha, and test the real failures in beta by switching dependencies off.

This guardrail is a **draft** proposal. Comment on it by [opening an issue](https://github.com/DEFRA/architecture/issues).

<details class="gr-meta"><summary>Phases, evidence and status for GR-FE-07</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/content-designer/">Content designer</a>, <a href="../../deliver/roles/developer/">Developer</a>, <a href="../../deliver/roles/interaction-designer/">Interaction designer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Each dependency that can fail or be slow identified with the developers, and what users see in each case designed and tested in the prototype</li><li><strong>Beta:</strong> The front end shows the designed content when a dependency fails or is slow, tested by switching dependencies off</li><li><strong>Live:</strong> Failure and delay content kept accurate as dependencies and processing times change</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Make sure everyone can use the service">5</abbr>, <abbr title="Operate a reliable service">14</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-06">6</a>, <a href="../../principles/doctrine/#ddts-07">7</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.3.0</dd></dl></details>


