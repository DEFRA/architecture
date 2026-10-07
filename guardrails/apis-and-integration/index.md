<!-- https://defra.github.io/architecture/guardrails/apis-and-integration/ | maturity: published | site version 0.3.0 | generated from guardrails/apis-and-integration.md -->

# APIs and integration

<p class="lead">How services talk to each other and to partners. Good integration lets us reuse capabilities and change one part of Defra without breaking another.</p>

<div class="da-trace" markdown>

**Doctrine:** [4. Data is an enterprise asset](https://defra.github.io/architecture/principles/doctrine/#ddts-04), [6. Outcomes and services over organisational structures](https://defra.github.io/architecture/principles/doctrine/#ddts-06)  
**Principles:** [5. Connect and collaborate](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-05)

</div>


!!! info "Who these guardrails apply to"
    The core department. Whether the APIs and integration guardrails also apply to Defra's arm's length bodies is [still to be confirmed](https://defra.github.io/architecture/guardrails/#arms-length-bodies).


Technology capability [Enabling Platforms](https://defra.github.io/architecture/handrail/technology-capabilities/#enabling-platforms): aPI management and integration.

## GR-API-01 API first {#gr-api-01}

<span class="rfc rfc--should">Should</span> Design the API for a capability before (or with) the user interface, so other services and partners can use it.


<details class="gr-meta"><summary>Phases, evidence and status for GR-API-01</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd>API specification written before or alongside the user interface</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Use and contribute to open standards, common components and patterns">13</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Integrate and adapt technology">9</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-04">4</a>, <a href="../../principles/doctrine/#ddts-06">6</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-API-02 Describe APIs with open specifications {#gr-api-02}

<span class="rfc rfc--should">Should</span> Synchronous APIs are described with **OpenAPI 3**, and asynchronous/event interfaces with **AsyncAPI**, kept in the same repository as the code.

**Why:** Machine-readable contracts make APIs discoverable, testable and safe to change.


<details class="gr-meta"><summary>Phases, evidence and status for GR-API-02</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Draft OpenAPI 3 or AsyncAPI documents for the interfaces you are prototyping</li><li><strong>Beta:</strong> OpenAPI 3 or AsyncAPI documents in the repository, checked in the pipeline against the running API</li><li><strong>Live:</strong> Specifications kept in step with every released change</li></ul></dd><dt>Automated check</dt><dd>Guardrail check (tools/guardrail-check): OpenAPI 3 and AsyncAPI documents present and well formed</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Use and contribute to open standards, common components and patterns">13</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make use of open standards">4</abbr>, <abbr title="Integrate and adapt technology">9</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-04">4</a>, <a href="../../principles/doctrine/#ddts-06">6</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-API-03 Follow government API standards {#gr-api-03}

<span class="rfc rfc--should">Should</span> Follow the [API technical and data standards](https://www.gov.uk/guidance/gds-api-technical-and-data-standards): RESTful resources, JSON, HTTPS only, consistent error formats and standard identifiers from the [data standards](https://defra.github.io/architecture/data/data-standards/).


<details class="gr-meta"><summary>Phases, evidence and status for GR-API-03</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a>, <a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd>API design reviewed against the GDS API technical and data standards</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Use and contribute to open standards, common components and patterns">13</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make use of open standards">4</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-04">4</a>, <a href="../../principles/doctrine/#ddts-06">6</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-API-04 Version and deprecate deliberately {#gr-api-04}

<span class="rfc rfc--should">Should</span> Breaking changes are versioned, consumers are told in advance, and old versions have a published retirement date.


<details class="gr-meta"><summary>Phases, evidence and status for GR-API-04</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a>, <a href="../../deliver/roles/product-manager/">Product manager</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Beta:</strong> Versioning approach published for each API and event</li><li><strong>Live:</strong> Deprecation notices sent to consumers and retirement dates published for old versions</li><li><strong>Significant change:</strong> Consumers told about breaking changes in advance, with a new version and a retirement date for the old one</li><li><strong>Retire:</strong> Consumers told the retirement date in advance, and moved to a replacement</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Integrate and adapt technology">9</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-04">4</a>, <a href="../../principles/doctrine/#ddts-06">6</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-API-05 No integration through shared databases {#gr-api-05}

<span class="rfc rfc--should">Should</span> Services do not read or write another service's database directly. Integrate through APIs, events or governed data products.

**Why:** Shared databases tightly couple services and make both impossible to change safely.


<details class="gr-meta"><summary>Phases, evidence and status for GR-API-05</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Container diagram showing integration only through APIs, events or governed data products</li><li><strong>Beta:</strong> Built integrations match the container diagram, with no access to another service&#x27;s database</li><li><strong>Live:</strong> Integrations reviewed when the service or its dependencies change</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Integrate and adapt technology">9</abbr>; <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Design flexible architectures">6</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-04">4</a>, <a href="../../principles/doctrine/#ddts-06">6</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-API-06 Use events for change notifications {#gr-api-06}

<span class="rfc rfc--should">Should</span> Use asynchronous messages or events when other services need to react to something that happened (an application submitted, a permit issued), rather than polling.


<details class="gr-meta"><summary>Phases, evidence and status for GR-API-06</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a>, <a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd>Event and message definitions described in AsyncAPI</dd><dt>Automated check</dt><dd>Manual</dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-04">4</a>, <a href="../../principles/doctrine/#ddts-06">6</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-API-07 Secure every API {#gr-api-07}

<span class="rfc rfc--must">Must</span> All APIs authenticate callers (OAuth 2.0 / OpenID Connect or mutual TLS), authorise every request, validate input and apply rate limiting. No API is "internal so it's safe".


<details class="gr-meta"><summary>Phases, evidence and status for GR-API-07</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/security-architect/">Security architect</a>, <a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Authentication, authorisation, input validation and rate limiting designed for each API</li><li><strong>Beta:</strong> These controls built and covered by security testing</li><li><strong>Live:</strong> API access reviewed, and controls re-tested after significant change</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Create a secure service which protects users&#x27; privacy">9</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make things secure">6</abbr>; <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Minimise the attack surface">7</abbr>, <abbr title="Defend in depth">8</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-04">4</a>, <a href="../../principles/doctrine/#ddts-06">6</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-API-08 Make APIs discoverable {#gr-api-08}

<span class="rfc rfc--should">Should</span> Register APIs in the platform API catalogue and, where they are useful beyond Defra, the [government API catalogue](https://www.api.gov.uk/).

<details class="gr-meta"><summary>Phases, evidence and status for GR-API-08</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd>Entry in the platform API catalogue</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Share, reuse and collaborate">8</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-04">4</a>, <a href="../../principles/doctrine/#ddts-06">6</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>


