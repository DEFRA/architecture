<!-- https://defra.github.io/architecture/guardrails/hosting-and-platforms/ | maturity: published | site version 0.3.0 | generated from guardrails/hosting-and-platforms.md -->

# Hosting and platforms

<p class="lead">Where and how services run. Use the paved road so your team can focus on users rather than infrastructure.</p>

<div class="da-trace" markdown>

**Doctrine:** [1. Platforms before projects. Built as products](https://defra.github.io/architecture/principles/doctrine/#ddts-01), [2. Standards and guardrails before exceptions](https://defra.github.io/architecture/principles/doctrine/#ddts-02), [3. Reuse before buy](https://defra.github.io/architecture/principles/doctrine/#ddts-03)  
**Principles:** [3. Maximise value, minimise waste](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-03), [1. Delivery-focused architecture](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-01)

</div>


!!! info "Who these guardrails apply to"
    The core department. Whether the hosting and platforms guardrails also apply to Defra's arm's length bodies is [still to be confirmed](https://defra.github.io/architecture/guardrails/#arms-length-bodies).


Technology capability [Enabling Platforms](https://defra.github.io/architecture/handrail/technology-capabilities/#enabling-platforms): application hosting and delivery platform.

## GR-HOST-01 Use Defra's strategic delivery platform by default {#gr-host-01}

<span class="rfc rfc--must">Must</span> New digital services are hosted on the **Defra Core Delivery Platform (CDP)** unless an exception has been agreed.

**Why:** CDP provides secure-by-default hosting, CI/CD, observability, secrets management and protective monitoring once, for everyone. Each team that builds its own platform recreates this at its own cost and risk.

**How to meet it:** In discovery or alpha, work with the Delivery Architecture team to decide whether CDP is right for your service - the expectation is that it will be - and engage the platform team. If CDP cannot meet a requirement (for example specialist compute, a SaaS product or a legacy migration), raise an [exception](https://defra.github.io/architecture/governance/exceptions/) early and tell the platform team - the gap may be something they should solve for everyone.

**In the Defra Digital Service Manual:** [Core Delivery Platform](https://digital.defra.gov.uk/architecture-and-software-development/core-delivery-platform). The manual says a service not on CDP is managed as an exception through the Delivery Architecture team's governance process; how that relates to exceptions on this site is [still being agreed](https://defra.github.io/architecture/governance/exceptions/#exceptions-to-the-software-development-standards).


<details class="gr-meta"><summary>Phases, evidence and status for GR-HOST-01</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Discovery, Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Discovery:</strong> Platform team engaged, and any hosting needs the Core Delivery Platform might not meet identified</li><li><strong>Alpha:</strong> The design runs on the Core Delivery Platform, or an exception has been requested</li><li><strong>Beta:</strong> The service runs on the Core Delivery Platform, or under an approved exception</li><li><strong>Live:</strong> The service still runs on the platform, and any exception is reviewed before it expires</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Choose the right tools and technology">11</abbr>; <a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Use cloud first">5</abbr>, <abbr title="Share, reuse and collaborate">8</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-HOST-02 Public cloud first {#gr-host-02}

<span class="rfc rfc--should">Should</span> Where a service cannot use a strategic platform, it is hosted in a Defra-managed public cloud tenancy. New on-premises hosting is not permitted.

**Why:** Government [Cloud First policy](https://www.gov.uk/guidance/government-cloud-first-policy) and Defra's data centre exit.


<details class="gr-meta"><summary>Phases, evidence and status for GR-HOST-02</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Where the platform cannot be used, the hosting design uses a Defra-managed public cloud tenancy</li><li><strong>Beta:</strong> The service runs in a Defra-managed public cloud tenancy</li><li><strong>Live:</strong> No on-premises hosting introduced</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Use cloud first">5</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-HOST-03 Everything as code {#gr-host-03}

<span class="rfc rfc--should">Should</span> Infrastructure, configuration, pipelines and policies are defined as code, version-controlled and deployed through automated pipelines. No manual changes to production.

**Why:** Repeatable, reviewable, recoverable environments. Manual changes cause drift and incidents.

**How to meet it:** Use the platform's provided templates. Where you manage your own infrastructure, use a declarative tool such as Terraform and run drift detection.


<details class="gr-meta"><summary>Phases, evidence and status for GR-HOST-03</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Beta:</strong> Infrastructure, configuration and pipelines defined as code in the repository, with no manual changes to production</li><li><strong>Live:</strong> Drift detection running, and no manual changes to production in the change history</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Operate a reliable service">14</abbr>; <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Make changes securely">10</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-HOST-04 Use managed services before self-managed {#gr-host-04}

<span class="rfc rfc--should">Should</span> Prefer managed cloud services (databases, queues, storage) over running your own on virtual machines.

**Why:** Managed services remove patching and much operational toil.


<details class="gr-meta"><summary>Phases, evidence and status for GR-HOST-04</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a>, <a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd>Hosting design listing the managed services used</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Use cloud first">5</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-HOST-05 Consistent, disposable environments {#gr-host-05}

<span class="rfc rfc--should">Should</span> Have at least development, test and production environments, created from the same code, with production data never copied to lower environments unless anonymised.


<details class="gr-meta"><summary>Phases, evidence and status for GR-HOST-05</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd>Environments created from the same code, and how lower environments avoid real personal data</dd><dt>Automated check</dt><dd>Manual</dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-HOST-06 Host data in the UK {#gr-host-06}

<span class="rfc rfc--should">Should</span> Data classified OFFICIAL is held in UK regions unless an assessed and approved exception exists.

**Why:** Data protection, sovereignty and Defra's information risk appetite.


<details class="gr-meta"><summary>Phases, evidence and status for GR-HOST-06</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a>, <a href="../../deliver/roles/security-architect/">Security architect</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Hosting design places every data store and backup in UK regions</li><li><strong>Beta:</strong> Data location confirmed for every data store and backup as built</li><li><strong>Live:</strong> Data location checked when new stores or services are added</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>

## GR-HOST-07 Design for the resilience the service needs {#gr-host-07}

<span class="rfc rfc--should">Should</span> Agree recovery time and recovery point objectives with the service owner, design to them across availability zones, and test recovery at least once a year.

**Why:** Some Defra services, such as flood warnings and disease control, are critical during emergencies - exactly when infrastructure is under stress.

<details class="gr-meta"><summary>Phases, evidence and status for GR-HOST-07</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/technical-architect/">Technical architect</a>, <a href="../../deliver/roles/product-manager/">Product manager</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Recovery time and recovery point objectives agreed with the service owner, and a design that meets them</li><li><strong>Beta:</strong> Multi-zone design built, and recovery tested before go-live</li><li><strong>Live:</strong> Recovery tested at least once a year, with the date of the last test</li><li><strong>Significant change:</strong> Recovery objectives and design checked for the change</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Operate a reliable service">14</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-01">1</a>, <a href="../../principles/doctrine/#ddts-02">2</a>, <a href="../../principles/doctrine/#ddts-03">3</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.1.0</dd></dl></details>


