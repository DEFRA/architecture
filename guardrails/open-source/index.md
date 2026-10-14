<!-- https://defra.github.io/architecture/guardrails/open-source/ | maturity: published | site version 0.3.0 | generated from guardrails/open-source.md -->

# Open source and working in the open

<p class="lead">We code in the open and share what we learn. It improves quality, makes reuse easy and lets partners see how we work before they work with us.</p>

<div class="da-trace" markdown>

**Doctrine:** [1. Platforms before projects. Built as products](https://defra.github.io/architecture/principles/doctrine/#ddts-01), [3. Reuse before buy](https://defra.github.io/architecture/principles/doctrine/#ddts-03), [5. Assume AI until proven otherwise](https://defra.github.io/architecture/principles/doctrine/#ddts-05)  
**Principles:** [3. Maximise value, minimise waste](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-03), [7. Empower to innovate](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-07)

</div>


!!! info "Who these guardrails apply to"
    The core department. Whether the open source and working in the open guardrails also apply to Defra's arm's length bodies is [still to be confirmed](https://defra.github.io/architecture/guardrails/#arms-length-bodies).


Relates to Service Standard point 12 and TCoP point 3.

## GR-OPEN-01 Code in the open {#gr-open-01}

<span class="rfc rfc--must">Must</span> New source code is public from the start, in a Defra GitHub organisation, unless there is a recorded reason to keep a specific repository private (for example fraud rules or unannounced policy).

**Why:** [Service Standard point 12](https://www.gov.uk/service-manual/service-standard/point-12-make-new-source-code-open). Openness also makes teams more careful about secrets and quality.


<details class="gr-meta"><summary>Phases, evidence and status for GR-OPEN-01</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a>, <a href="../../deliver/roles/delivery-manager/">Delivery manager</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Code public in a Defra GitHub organisation from the first commit, or a recorded reason for keeping a repository private</li><li><strong>Beta:</strong> Repositories public, or the reasons for keeping them private reviewed</li><li><strong>Live:</strong> Repositories still public, or private for a recorded reason</li><li><strong>Retire:</strong> Repositories archived, not deleted, so the code and decisions stay available</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Make new source code open">12</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Be open and use open source">3</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-03">3</a>, <a href="../../principles/doctrine/#ddts-05">5</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-OPEN-02 Licence clearly {#gr-open-02}

<span class="rfc rfc--should">Should</span> Code is released under the [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) or the MIT licence, with a LICENCE file in every repository.


<details class="gr-meta"><summary>Phases, evidence and status for GR-OPEN-02</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> LICENCE file in every repository from the start</li><li><strong>Beta:</strong> LICENCE file with the Open Government Licence or MIT licence in every repository</li><li><strong>Live:</strong> LICENCE file in every new repository</li></ul></dd><dt>Automated check</dt><dd>Guardrail check (tools/guardrail-check): LICENCE file with the Open Government Licence or MIT</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Make new source code open">12</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Be open and use open source">3</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-03">3</a>, <a href="../../principles/doctrine/#ddts-05">5</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-OPEN-03 Publish safely {#gr-open-03}

<span class="rfc rfc--should">Should</span> Enable secret scanning and push protection on every repository. Keep secrets, credentials and sensitive configuration out of code.


<details class="gr-meta"><summary>Phases, evidence and status for GR-OPEN-03</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a>, <a href="../../deliver/roles/security-architect/">Security architect</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Secret scanning and push protection on for every repository from the first commit</li><li><strong>Beta:</strong> Secret scanning and push protection on for every repository</li><li><strong>Live:</strong> Secret scanning alerts dealt with promptly</li></ul></dd><dt>Automated check</dt><dd>Guardrail check (tools/guardrail-check): secret scanning and push protection turned on, with a token that can read security settings</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Make new source code open">12</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Be open and use open source">3</abbr>, <abbr title="Make things secure">6</abbr>; <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Minimise the attack surface">7</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-03">3</a>, <a href="../../principles/doctrine/#ddts-05">5</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-OPEN-04 Reuse and contribute back {#gr-open-04}

<span class="rfc rfc--should">Should</span> Use and improve existing open source and Defra components rather than forking or rewriting. Contribute fixes back upstream.


<details class="gr-meta"><summary>Phases, evidence and status for GR-OPEN-04</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd>Reuse and upstream contributions noted in ADRs and pull requests</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Use and contribute to open standards, common components and patterns">13</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Be open and use open source">3</abbr>, <abbr title="Share, reuse and collaborate">8</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-03">3</a>, <a href="../../principles/doctrine/#ddts-05">5</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-OPEN-05 Blog and show the thing {#gr-open-05}

<span class="rfc rfc--could">Could</span> Share what you learn on the [Defra Digital blog](https://defradigital.blog.gov.uk/), at show and tells, and in this repository.

<details class="gr-meta"><summary>Phases, evidence and status for GR-OPEN-05</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Discovery, Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/delivery-manager/">Delivery manager</a></dd><dt>Evidence</dt><dd>Blog posts, show and tells or contributions to this site</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Share, reuse and collaborate">8</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-03">3</a>, <a href="../../principles/doctrine/#ddts-05">5</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>


