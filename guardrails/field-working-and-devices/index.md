<!-- https://defra.github.io/architecture/guardrails/field-working-and-devices/ | maturity: published | site version 0.3.0 | generated from guardrails/field-working-and-devices.md -->

# Field working and devices

<p class="lead">Many Defra staff and partners work on farms, at ports, on rivers and at sea. These draft guardrails make sure the tools they use work where they work, and keep Defra data safe on the move.</p>

<div class="da-trace" markdown>

**Doctrine:** [7. Digital first where appropriate](https://defra.github.io/architecture/principles/doctrine/#ddts-07)  
**Principles:** [8. Right tools, right place](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-08)

</div>


!!! info "Who these guardrails apply to"
    The core department. Whether the field working and devices guardrails also apply to Defra's arm's length bodies is [still to be confirmed](https://defra.github.io/architecture/guardrails/#arms-length-bodies).


Puts architecture principle [8. Right tools, right place](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-08) into practice. See also the proposed [field inspection](https://defra.github.io/architecture/patterns/service/field-inspection/) service pattern.

!!! info "Draft guardrails"
    These guardrails are new drafts from the [guardrail backlog](https://defra.github.io/architecture/about/roadmap/#guardrail-backlog). Comment on them by [opening an issue](https://github.com/DEFRA/architecture/issues).

## GR-FIELD-01 Choose devices that suit the job {#gr-field-01}

<span class="rfc rfc--should">Should</span> Choose devices for field work from research into where and how people work - outdoors, in bad weather, wearing gloves, in the dark - not from what is already on the desk.

**Why:** a tool that cannot be used in the rain or with gloves on will not be used, and staff fall back to paper.

**How to meet it:** observe field work in discovery, and record the device choice and the reasons in an ADR.


<details class="gr-meta"><summary>Phases, evidence and status for GR-FIELD-01</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Discovery, Alpha</dd><dt>Led by</dt><dd><a href="../../deliver/roles/user-researcher/">User researcher</a>, <a href="../../deliver/roles/service-designer/">Service designer</a></dd><dt>Evidence</dt><dd>User research on the working environment, and the device choice recorded in an ADR</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Understand users and their needs">1</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-07">7</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.2.0</dd></dl></details>

## GR-FIELD-02 Design field tools to work offline {#gr-field-02}

<span class="rfc rfc--should">Should</span> Field tools work without a connection: they download what is needed before a visit, save work on the device, and sync safely when back in signal.

**Why:** much of rural England and the sea has poor or no mobile coverage. Losing work because the signal dropped destroys trust in digital tools.

**How to meet it:** test every field journey in flight mode, and decide in an ADR how conflicts are resolved when two people change the same record offline.


<details class="gr-meta"><summary>Phases, evidence and status for GR-FIELD-02</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/interaction-designer/">Interaction designer</a>, <a href="../../deliver/roles/developer/">Developer</a></dd><dt>Evidence</dt><dd>Field journeys tested with no connection, including sync after reconnecting and conflict handling</dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/service-manual/service-standard">Service Standard</a> <abbr title="Make sure everyone can use the service">5</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-07">7</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.2.0</dd></dl></details>

## GR-FIELD-03 Manage and secure every device {#gr-field-03}

<span class="rfc rfc--should">Should</span> Devices that hold or access Defra data are enrolled in Defra device management, encrypted, kept patched, protected by a screen lock and able to be wiped remotely if lost.

**Why:** field devices are lost and stolen more often than office equipment, and may hold personal and sensitive data.

**How to meet it:** use Defra-managed devices. If a supplier or partner device is needed, agree how it meets the same controls before it is used.


<details class="gr-meta"><summary>Phases, evidence and status for GR-FIELD-03</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Alpha, Beta, Live</dd><dt>Led by</dt><dd><a href="../../deliver/roles/security-architect/">Security architect</a></dd><dt>Evidence</dt><dd><ul class="gr-meta__phases"><li><strong>Alpha:</strong> Device management approach agreed for the devices the service will use</li><li><strong>Beta:</strong> Devices enrolled in Defra device management, with encryption, patching, screen lock and remote wipe confirmed</li><li><strong>Live:</strong> Device compliance monitored, and lost devices wiped</li></ul></dd><dt>Automated check</dt><dd>Manual</dd><dt>Maps to</dt><dd><a href="https://www.gov.uk/guidance/the-technology-code-of-practice">Technology Code of Practice</a> <abbr title="Make things secure">6</abbr>; <a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/principles/">Secure by Design principles</a> <abbr title="Minimise the attack surface">7</abbr>, <abbr title="Defend in depth">8</abbr></dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-07">7</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.2.0</dd></dl></details>

## GR-FIELD-04 Check connectivity before you design {#gr-field-04}

<span class="rfc rfc--could">Could</span> Check the mobile and broadband coverage where the service will be used before choosing an approach, rather than assuming it.

**Why:** coverage maps and real-world signal often differ, especially inside farm buildings and in valleys.

**How to meet it:** use public coverage data and ask users, and plan for the worst case.

<details class="gr-meta"><summary>Phases, evidence and status for GR-FIELD-04</summary><dl><dt>Status</dt><dd><span class="gr-status gr-status--draft">Draft</span></dd><dt>Phases</dt><dd>Discovery, Alpha</dd><dt>Led by</dt><dd><a href="../../deliver/roles/user-researcher/">User researcher</a>, <a href="../../deliver/roles/technical-architect/">Technical architect</a></dd><dt>Evidence</dt><dd>Connectivity in the places the service will be used checked, and the approach recorded</dd><dt>Automated check</dt><dd>Manual</dd><dt>DDTS doctrine</dt><dd><a href="../../principles/doctrine/#ddts-07">7</a></dd><dt>Owner</dt><dd>Architecture team, last reviewed 2026-10-01, since v0.2.0</dd></dl></details>


