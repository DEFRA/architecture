<!-- https://defra.github.io/architecture/deliver/roles/data-architect/ | maturity: prototype | site version 0.3.0 | generated from deliver/roles/data-architect.md -->

# Data architect

<p class="lead">The guardrails a data architect leads, what to show in each phase, the patterns that help and when to work with an architect.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



You make sure the data the service creates and uses is owned, standard, trustworthy and reusable across Defra.

You lead **10 guardrails**, often with other roles. Leading means making sure the team meets them and can show it, not doing all the work. See them all in the <a href="../../../guardrails/library/#role=data-architect">guardrail library, filtered to your role</a>.

## Your guardrails, phase by phase

### Discovery

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | Must | DPIA screening completed, showing whether personal data is involved |
| [GR-SEC-03](https://defra.github.io/architecture/guardrails/security/#gr-sec-03) Classify information | Must | Security classification and the types of data the service will handle identified |
| [GR-DATA-02](https://defra.github.io/architecture/guardrails/data/#gr-data-02) Use authoritative sources | Should | Shared entities the service needs identified, with their authoritative sources |

More on the [discovery page](https://defra.github.io/architecture/deliver/discovery/).

### Alpha

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | Must | Draft DPIA, with data minimisation and retention designed in |
| [GR-SEC-03](https://defra.github.io/architecture/guardrails/security/#gr-sec-03) Classify information | Must | Controls in the design that match the classification |
| [GR-AI-05](https://defra.github.io/architecture/guardrails/ai/#gr-ai-05) Evaluate, monitor and threat model | Should | Evaluation plan for accuracy, bias and safety, and AI-specific threats in the threat model |
| [GR-DATA-01](https://defra.github.io/architecture/guardrails/data/#gr-data-01) Every data set has an owner | Should | Each data set the service will create or hold identified, with a proposed information asset owner |
| [GR-DATA-02](https://defra.github.io/architecture/guardrails/data/#gr-data-02) Use authoritative sources | Should | Data flow diagram naming the authoritative source for each shared entity, and how any copies are refreshed |
| [GR-DATA-03](https://defra.github.io/architecture/guardrails/data/#gr-data-03) Use agreed data standards and identifiers | Should | Data model using the agreed data standards and identifiers |

More on the [alpha page](https://defra.github.io/architecture/deliver/alpha/).

### Beta

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | Must | Approved DPIA, and retention and deletion built and tested |
| [GR-DATA-09](https://defra.github.io/architecture/guardrails/data/#gr-data-09) Retain and dispose of records properly | Must | Retention schedule identified for each type of record, and disposal built in |
| [GR-AI-05](https://defra.github.io/architecture/guardrails/ai/#gr-ai-05) Evaluate, monitor and threat model | Should | Evaluation results for accuracy, bias and safety before release, and mitigations for AI threats tested |
| [GR-DATA-01](https://defra.github.io/architecture/guardrails/data/#gr-data-01) Every data set has an owner | Should | Information asset register entries with a named owner for each data set |
| [GR-DATA-02](https://defra.github.io/architecture/guardrails/data/#gr-data-02) Use authoritative sources | Should | The service reads from the authoritative sources as designed, tested with the source owners |
| [GR-DATA-03](https://defra.github.io/architecture/guardrails/data/#gr-data-03) Use agreed data standards and identifiers | Should | Data stored and exchanged using the agreed standards, checked in testing |
| [GR-DATA-05](https://defra.github.io/architecture/guardrails/data/#gr-data-05) Describe your data | Should | Published metadata records in UK GEMINI or DCAT |
| [GR-DATA-07](https://defra.github.io/architecture/guardrails/data/#gr-data-07) Open by default | Should | Link to the published open data and its licence |
| [GR-DATA-08](https://defra.github.io/architecture/guardrails/data/#gr-data-08) Manage data quality | Should | Data quality measures and regular reports |

More on the [beta page](https://defra.github.io/architecture/deliver/beta/).

### Live

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | Must | DPIA reviewed when processing changes, and deletion running as designed |
| [GR-DATA-09](https://defra.github.io/architecture/guardrails/data/#gr-data-09) Retain and dispose of records properly | Must | Retention applied and records of permanent value identified for The National Archives |
| [GR-AI-05](https://defra.github.io/architecture/guardrails/ai/#gr-ai-05) Evaluate, monitor and threat model | Should | Monitoring of model performance and drift in live, with evaluation repeated when the model or data changes |
| [GR-DATA-01](https://defra.github.io/architecture/guardrails/data/#gr-data-01) Every data set has an owner | Should | Register entries and owners kept current |
| [GR-DATA-02](https://defra.github.io/architecture/guardrails/data/#gr-data-02) Use authoritative sources | Should | Copies and refresh arrangements reviewed when sources change |
| [GR-DATA-05](https://defra.github.io/architecture/guardrails/data/#gr-data-05) Describe your data | Should | Published metadata records in UK GEMINI or DCAT |
| [GR-DATA-07](https://defra.github.io/architecture/guardrails/data/#gr-data-07) Open by default | Should | Link to the published open data and its licence |
| [GR-DATA-08](https://defra.github.io/architecture/guardrails/data/#gr-data-08) Manage data quality | Should | Data quality measures and regular reports |

More on the [live page](https://defra.github.io/architecture/deliver/live/).

### Significant change

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | Must | DPIA updated for any change in how personal data is processed |

More on the [significant change page](https://defra.github.io/architecture/deliver/significant-change/).

### Retire a service

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-DATA-09](https://defra.github.io/architecture/guardrails/data/#gr-data-09) Retain and dispose of records properly | Must | Records kept, transferred to The National Archives or destroyed, as agreed with the information asset owner |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | Must | Personal data deleted or transferred lawfully, as set out in the DPIA |
| [GR-DATA-01](https://defra.github.io/architecture/guardrails/data/#gr-data-01) Every data set has an owner | Should | Information asset register updated to show what happened to each data set |

More on the [retire a service page](https://defra.github.io/architecture/deliver/retire/).

## Patterns that help

- [Acting on behalf of an organisation or holding](https://defra.github.io/architecture/patterns/acting-on-behalf/) - Users act for a business, a land holding or another person, and the service must check they are allowed to.
- [Reading from an authoritative source](https://defra.github.io/architecture/patterns/authoritative-source/) - A service needs shared data - customers, organisations, holdings, locations or species - that another part of Defra owns.
- [File upload with malware scanning](https://defra.github.io/architecture/patterns/file-upload/) - Users upload documents or images, and the files must be scanned and stored safely before anyone opens them.
- [Publishing open data with metadata](https://defra.github.io/architecture/patterns/open-data-publishing/) - You hold non-personal data that others could use, and want to publish it so it can be found, trusted and reused.

## Working with architects

- Identify authoritative sources in discovery - see [Defra on a page](https://defra.github.io/architecture/data/defra-on-a-page/).
- Review the data model against the [data standards](https://defra.github.io/architecture/data/data-standards/) in alpha.



