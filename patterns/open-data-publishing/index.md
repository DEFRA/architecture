<!-- https://defra.github.io/architecture/patterns/open-data-publishing/ | maturity: published | site version 0.3.0 | generated from patterns/open-data-publishing.md -->

# Publishing open data with metadata

<p class="lead">Publish data once, in open formats, with metadata that lets people find it, understand it and trust it - and an automated pipeline that keeps it current.</p>

## Context

Defra holds a great deal of data that is useful outside government: environmental monitoring, flood risk, land use, species records. Data published as a one-off spreadsheet with no description is hard to find, quickly out of date and easy to misuse. Data published by hand can also leak information that should not be public.

## Solution

Publish through an automated pipeline from the data's source. The pipeline checks the data against the rules for what can be published, produces open formats, and publishes the data with **metadata**: what it is, who owns it, how it was collected, how good it is and how often it changes.

```mermaid
flowchart LR
    accTitle: Publishing open data with metadata
    accDescr: Source data owned by an information asset owner flows into a publishing pipeline. The pipeline checks the data contains nothing personal or sensitive, validates it against data standards and measures its quality. It produces open formats and metadata in UK GEMINI or DCAT, then publishes them to the Defra Data Services Platform or data.gov.uk under the Open Government Licence. Users and other services download the data or call an API.
    SRC[("Source data<br/>named owner")] --> P["Publishing pipeline"]
    P --> CHK{"Safe to publish?<br/>no personal or<br/>sensitive data"}
    CHK -->|"no"| STOP["Stop and alert<br/>the owner"]
    CHK -->|"yes"| VAL["Validate against data<br/>standards, measure quality"]
    VAL --> OUT["Open formats<br/>and metadata"]
    OUT --> PUB["Defra Data Services Platform<br/>or data.gov.uk"]
    PUB --> USERS(["Users, researchers,<br/>other services"])
```

How it works:

1. Confirm the data set has a named owner and is recorded in the information asset register.
2. Check, automatically and on every run, that nothing personal, commercially sensitive or security-relevant is included. If the check fails, publish nothing and alert the owner.
3. Validate against the [data standards](https://defra.github.io/architecture/data/data-standards/), so the data can be joined with other data sets.
4. Publish in open formats (such as CSV, GeoJSON or GeoPackage) under the [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).
5. Publish metadata in [UK GEMINI](https://www.agi.org.uk/why-uk-gemini/) for geospatial data or DCAT for other data, including quality, lineage, update frequency and contact.
6. Keep stable URLs for each data set and version, so people can cite them.

## What users see

<div id="tbc-1"></div>

!!! warning "To be confirmed"
    **TODO:** what users of the published data see, such as the dataset page, licence and update dates, the content for them, and what to test with users. Write these three sections with a designer and a user researcher.

## Content to design

To be written - see the box above.

## What to test with users

To be written - see the box above.

## Guardrails it helps you meet

| Guardrail | Level | What the guardrail asks |
| --- | --- | --- |
| [GR-DATA-07](https://defra.github.io/architecture/guardrails/data/#gr-data-07) Open by default | <span class="rfc rfc--should">Should</span> | Publish non-personal, non-sensitive data as open data under the Open Government Licence, through the Defra Data Services Platform or data.gov.uk. |
| [GR-DATA-05](https://defra.github.io/architecture/guardrails/data/#gr-data-05) Describe your data | <span class="rfc rfc--should">Should</span> | Publish metadata for data sets so they can be found and understood - UK GEMINI for geospatial data and DCAT for other data sets. |
| [GR-DATA-03](https://defra.github.io/architecture/guardrails/data/#gr-data-03) Use agreed data standards and identifiers | <span class="rfc rfc--should">Should</span> | Use the data standards for dates, addresses, locations, identifiers and code lists, so data can be joined across services. |
| [GR-DATA-08](https://defra.github.io/architecture/guardrails/data/#gr-data-08) Manage data quality | <span class="rfc rfc--should">Should</span> | Define, measure and report data quality using the Government Data Quality Framework, especially for data that feeds payments, regulatory decisions or official statistics. |
| [GR-DATA-01](https://defra.github.io/architecture/guardrails/data/#gr-data-01) Every data set has an owner | <span class="rfc rfc--should">Should</span> | Each data set a service creates or holds has a named business owner (information asset owner) and is recorded in the information asset register. |
| [GR-SEC-03](https://defra.github.io/architecture/guardrails/security/#gr-sec-03) Classify information | <span class="rfc rfc--must">Must</span> | Identify the government security classification and data types the service handles, and design controls to match. |


## Related Secure by Design artefacts

- [Data loss prevention strategy](https://github.com/co-cddo/SbD/blob/Main/Security%20Architecture%20/Security%20Documentation/Data%20Loss%20Prevention%20%28DLP%29%20Strategy%20aligning%20with%20SbD/Data%20Loss%20Prevention%20%28DLP%29%20Strategy%20-%20Alignment%20with%20SbD.md)
- The whole [Secure by Design artefact library](https://github.com/co-cddo/SbD)


## When not to use it

- **The data includes personal data** that cannot be safely aggregated or anonymised. Share it under a data sharing agreement instead ([GR-DATA-04](https://defra.github.io/architecture/guardrails/data/#gr-data-04)).
- **Official statistics.** Follow the Code of Practice for Statistics and your statistics producers' release process, which this pattern does not replace.

## Related

- [Data and analytics](https://defra.github.io/architecture/patterns/service/data-and-analytics/) service pattern
- [Data guardrails](https://defra.github.io/architecture/guardrails/data/)

