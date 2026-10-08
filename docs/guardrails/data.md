---
applicability: tbc
principles: [GR-PRIN-04]
# Metadata for every guardrail on this page. See the contribution guide for the fields.
guardrail_defaults:
  status: draft
  owner: Enterprise data architecture
  automated_check: manual
  last_reviewed: 2026-10-01
  since_version: 0.1.0
guardrails:
  GR-DATA-12:
    phases: [discovery, alpha, beta, live]
    lead_roles: [data-architect]
    evidence: Data model which complies with the data modelling standards
  GR-DATA-01:
    phases: [alpha, beta, live]
    lead_roles: [data-architect, product-manager]
    evidence: Information asset register entries with a named owner for each data set
    evidence_by_phase:
      alpha: Each data set the service will create or hold identified, with a proposed information asset owner
      beta: Information asset register entries with a named owner for each data set
      live: Register entries and owners kept current
      retire: Information asset register updated to show what happened to each data set
    tcop_points: [10]
  GR-DATA-02:
    phases: [discovery, alpha, beta, live]
    lead_roles: [data-architect]
    evidence: Data flow diagram naming the authoritative source for each shared entity, with refresh arrangements for any copies
    evidence_by_phase:
      discovery: Shared entities the service needs identified, with their authoritative sources
      alpha: Data flow diagram naming the authoritative source for each shared entity, and how any copies are refreshed
      beta: The service reads from the authoritative sources as designed, tested with the source owners
      live: Copies and refresh arrangements reviewed when sources change
    tcop_points: [10]
  GR-DATA-10:
    phases: [discovery, alpha, beta, live]
    lead_roles: [user-researcher]
    evidence: "Research plan showing consent, where recordings and notes are stored, when they are deleted, the approved tools used and DPIA screening"
    evidence_by_phase:
      discovery: Consent forms and privacy notice in use, recordings and notes stored only in approved places, and a deletion date set
      alpha: The same for alpha research, with DPIA screening done for the research and any new research tool assessed
      beta: Research data from earlier phases deleted on schedule, and the same controls for beta research
      live: Research data handled the same way for ongoing research, and deletion checked
    since_version: 0.3.0
  GR-DATA-04:
    phases: [alpha, beta]
    lead_roles: [service-designer]
    evidence: Journey design showing users are not asked for information Defra already holds, and data sharing agreements where required
    tcop_points: [8, 10]
  GR-DATA-06:
    phases: [discovery, alpha, beta, live]
    lead_roles: [data-architect, product-manager]
    evidence: Approved DPIA, and retention and deletion built into the service
    evidence_by_phase:
      discovery: DPIA screening completed, showing whether personal data is involved
      alpha: Draft DPIA, with data minimisation and retention designed in
      beta: Approved DPIA, and retention and deletion built and tested
      live: DPIA reviewed when processing changes, and deletion running as designed
      significant-change: DPIA updated for any change in how personal data is processed
      retire: Personal data deleted or transferred lawfully, as set out in the DPIA
    service_standard_points: [9]
    tcop_points: [7]
  GR-DATA-03:
    phases: [alpha, beta]
    lead_roles: [data-architect]
    evidence: Data model that uses the agreed data standards and identifiers
    evidence_by_phase:
      alpha: Data model using the agreed data standards and identifiers
      beta: Data stored and exchanged using the agreed standards, checked in testing
    service_standard_points: [13]
    tcop_points: [4, 10]
  GR-DATA-07:
    phases: [beta, live]
    lead_roles: [data-architect, product-manager]
    evidence: Link to the published open data and its licence
    tcop_points: [10]
  GR-DATA-05:
    phases: [beta, live]
    lead_roles: [data-architect]
    evidence: Published metadata records in UK GEMINI or DCAT
    tcop_points: [10]
  GR-DATA-08:
    phases: [beta, live]
    lead_roles: [data-architect, performance-analyst]
    evidence: Data quality measures and regular reports
    tcop_points: [10]
  GR-DATA-13:
    phases: [alpha, beta, live]
    lead_roles: [data-architect]
    evidence: Lineage records showing the source data, transformations and versions behind each decision the service makes or supports
    evidence_by_phase:
      alpha: Decisions the service makes or supports identified, with the data each one depends on and its authoritative source
      beta: Lineage captured automatically from source to decision, including transformations, rules and model versions
      live: Lineage kept current when sources, rules or models change, and used to explain or reproduce past decisions
    tcop_points: [10]
    since_version: 0.4.0
  GR-DATA-09:
    phases: [beta, live]
    lead_roles: [data-architect]
    evidence: Retention schedule applied and records of permanent value identified
    evidence_by_phase:
      beta: Retention schedule identified for each type of record, and disposal built in
      live: Retention applied and records of permanent value identified for The National Archives
      retire: Records kept, transferred to The National Archives or destroyed, as agreed with the information asset owner
  GR-DATA-11:
    phases: [discovery, alpha, beta]
    lead_roles: [interaction-designer, user-researcher, developer]
    evidence: Prototypes and test environments use made-up or anonymised data, never real personal data
    evidence_by_phase:
      discovery: Any prototype uses made-up data
      alpha: Prototypes and research materials use made-up data, including data a participant types in during a session
      beta: Test and research environments use synthetic or anonymised data; any exception agreed through a DPIA
    since_version: 0.3.0
---

# Data

<p class="lead">Defra's science, regulation and payments all depend on trusted data. These guardrails make sure that the data each service creates is an asset for the whole of Defra group, and any other appropriate data users.</p>

See also [enterprise data architecture](../data/index.md).

<hr>

## Narrative

Data architecture begins with a [DESIGN](#gr-data-12) phase, and with agreeing [OWNERSHIP](#gr-data-01) of the proposed data assets.

Bring data into the solution architecture through [RE-USE](#gr-data-02) of authoritative data sources (customers, organisations, land parcels, etc) and ensure [COMPLIANCE](#gr-data-10) in the acquisition of any new data. Seek to [SHARE](#gr-data-04) data wherever it is appropriate to do so, but to classify and [PROTECT](#gr-data-06) all sensitive data.

Create data assets that comply with agreed [STANDARDS](#gr-data-03), so that you can [PUBLISH](#gr-data-07) and [DESCRIBE](#gr-data-05) datasets of known [QUALITY](#gr-data-08). Be open about the [LINEAGE](#gr-data-13) of your data, and ensure [DISPOSAL](#gr-data-09) of it in line with regulation, policy and guidance.

Protect [ANONYMITY](#gr-data-11) by avoiding the use of real personal data in any non-production systems.

<hr>

## How to read a guardrail

Each guardrail has an identifier, a level, a short rationale and a way to show you meet it.

| Level | Means | If you cannot meet it |
| --- | --- | --- |
| <span class="rfc rfc--must">Must</span> | A requirement from law or mandatory government policy, a baseline security control, or a [DDTS doctrine](../principles/doctrine.md) non-negotiable. We keep these few. | You need an approved [exception](../governance/exceptions.md) from the Technical Design Authority. |
| <span class="rfc rfc--should">Should</span> | The strong default. There may be good reasons to differ. | Record why in an [architecture decision record](../governance/architecture-decision-records.md) and share it with your solution design authority. |
| <span class="rfc rfc--could">Could</span> | Recommended good practice. | No action needed, but we would like to know what worked better. |

## GR-DATA-12 DESIGN: Align with the enterprise data model {#gr-data-12}

<span class="rfc rfc--should">Should</span> Design should begin with the enterprise data model, to ensure that an enterprise view of stakeholders, IT systems, and data designs is taken into sufficient consideration.

**Why:** All of the data guardrails apply to the enterprise context, and the enterprise data model ensures a written record of that can be used in common across Defra.

## GR-DATA-01 OWNERSHIP: Assign an accountable owner to your data assets {#gr-data-01}

<span class="rfc rfc--should">Should</span> Each data set a service creates or holds has a named business owner (information asset owner) and is recorded in the information asset register.

**Why:** Data without an owner is not maintained, not trusted and not deleted when it should be.

## GR-DATA-02 DATA RE-USE: Use authoritative data sources {#gr-data-02}

<span class="rfc rfc--should">Should</span> Use the authoritative source for shared entities - customers, organisations, land parcels, holdings, locations, species - rather than creating local copies that drift. See [Defra on a page](../data/defra-on-a-page.md).

**How to meet it:** If you must cache or replicate, record the source, refresh frequency and how you handle changes.

## GR-DATA-10 COMPLIANCE: Acquire new data safely {#gr-data-10}

<span class="rfc rfc--should">Should</span> User research often collects personal data: recordings, notes, contact details and what participants type into prototypes. How to do this is set out in the user research [standards and guidance](https://digital.defra.gov.uk/user-research/standards-and-guidance) (consent, participant data handling, and storage and retention) and [tools](https://digital.defra.gov.uk/user-research/tools) in the Defra Digital Service Manual. These guardrails cover the architecture side. Collect research data only with informed consent, store recordings and notes only in Defra-approved places, delete them when they are no longer needed, use only Defra-approved research tools, and screen research for a DPIA.

**Why:** Research recordings and notes are personal data about real people. Keeping them in personal accounts, unapproved tools or for longer than needed puts participants at risk and breaks data protection law.

**How to meet it:**

- Get informed consent before each session, using the templates in the manual's [standards and guidance](https://digital.defra.gov.uk/user-research/standards-and-guidance).
- Store recordings and notes only where the manual's participant data storage and retention guidance says, and set a deletion date when you collect them.
- Use only the manual's [approved research tools](https://digital.defra.gov.uk/user-research/tools), and check a tool can hold the data you plan to collect. Assess any new tool before using it ([GR-TECH-04](choosing-technology.md#gr-tech-04)).
- Screen the research for a DPIA ([GR-DATA-06](#gr-data-06)), especially for new tools, sensitive topics or recordings of people's homes or farms.
- Do not put recordings or transcripts into AI tools except as the [AI digital toolkit](https://digital.defra.gov.uk/ai-toolkit/guidance/keeping-data-safe) allows.

This guardrail is a **draft** proposal. Comment on it by [opening an issue](https://github.com/DEFRA/architecture/issues).

## GR-DATA-04 SHARE: Collect once, share safely {#gr-data-04}

<span class="rfc rfc--should">Should</span> Do not ask users for information Defra already holds. Share data between services through APIs or governed data products, with data sharing agreements where required.

## GR-DATA-06 PROTECT: Protect sensitive data by design {#gr-data-06}

<span class="rfc rfc--must">Must</span> Complete a data protection impact assessment (DPIA) before processing personal data, minimise what you collect, and apply retention and deletion automatically.

**Why:** UK GDPR and the Data Protection Act 2018; TCoP point 7.

##

## GR-DATA-03 STANDARDS: Use data standards identifiers {#gr-data-03}

<span class="rfc rfc--should">Should</span> Use the [data standards](../data/data-standards.md) for dates, addresses, locations, identifiers and code lists, so data can be joined across services.

## GR-DATA-07 PUBLISH: Make your data open by default {#gr-data-07}

<span class="rfc rfc--should">Should</span> Publish non-personal, non-sensitive data as open data under the Open Government Licence, through the [Defra Data Services Platform](https://environment.data.gov.uk/) or [data.gov.uk](https://www.data.gov.uk/).

## GR-DATA-05 DESCRIBE: Explain your data to users {#gr-data-05}

<span class="rfc rfc--should">Should</span> Publish metadata for data sets so they can be found and understood - [UK GEMINI](https://www.agi.org.uk/why-uk-gemini/) for geospatial data and [DCAT](https://www.w3.org/TR/vocab-dcat-3/) for other data sets.

## GR-DATA-08 QUALITY: Define, measure & manage data quality {#gr-data-08}

<span class="rfc rfc--should">Should</span> Define, measure and report data quality using the [Government Data Quality Framework](https://www.gov.uk/government/publications/the-government-data-quality-framework), especially for data that feeds payments, regulatory decisions or official statistics.

## GR-DATA-13 LINEAGE: Trace decisions to trusted data {#gr-data-13}

<span class="rfc rfc--should">Should</span> Record where the data behind each decision comes from, how it was transformed and which rules or models were applied, so any decision can be traced back to trusted sources.

**Why:** Payments, regulatory decisions and official statistics must be explainable and open to challenge. Without lineage you cannot show why a decision was made, correct it when a source turns out to be wrong, or reproduce it later.

**How to meet it:**

- Identify the decisions the service makes or supports, and the data each one depends on.
- Take that data from authoritative sources ([GR-DATA-02](#gr-data-02)) and record the version or time of each extract.
- Capture lineage automatically in pipelines rather than in documents written by hand.
- Record the rule or model version used for each decision, alongside the data quality measures for its inputs ([GR-DATA-08](#gr-data-08)).
- Keep lineage records for as long as the decision records they support ([GR-DATA-09](#gr-data-09)).

## GR-DATA-09 DISPOSAL: Retain and dispose of records properly {#gr-data-09}

<span class="rfc rfc--must">Must</span> Apply Defra's retention schedules. Records of permanent value are identified for transfer to The National Archives.

## GR-DATA-11 ANONYMITY: No real personal data in prototypes {#gr-data-11}

<span class="rfc rfc--should">Should</span> Prototypes, research materials and test environments use made-up or anonymised data, never real personal data copied from a live service or spreadsheet.

**Why:** Prototypes are shared widely, hosted on less protected platforms and shown to participants. Real data in them can be seen by people who should not see it.

**How to meet it:** make up realistic names, addresses, holdings and reference numbers. Tell participants not to enter their own real details into a prototype unless the research plan allows it and the data is handled under [GR-DATA-10](#gr-data-10). If a test genuinely needs real data, agree it through a DPIA first.

This guardrail is a **draft** proposal. Comment on it by [opening an issue](https://github.com/DEFRA/architecture/issues).
