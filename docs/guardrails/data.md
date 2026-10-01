# Data

<p class="lead">Defra's science, regulation and payments all depend on trusted data. These guardrails make sure the data each service creates is an asset for the whole department.</p>

Supports principle [GR-PRIN-05](principles.md#gr-prin-05). See also [enterprise data architecture](../data/index.md).

## GR-DATA-01 Every data set has an owner {#gr-data-01}

<span class="rfc rfc--must">Must</span> Each data set a service creates or holds has a named business owner (information asset owner) and is recorded in the information asset register.

**Why:** Data without an owner is not maintained, not trusted and not deleted when it should be.

## GR-DATA-02 Use authoritative sources {#gr-data-02}

<span class="rfc rfc--must">Must</span> Use the authoritative source for shared entities - customers, organisations, land parcels, holdings, locations, species - rather than creating local copies that drift. See [Defra on a page](../data/defra-on-a-page.md).

**How to meet it:** If you must cache or replicate, record the source, refresh frequency and how you handle changes.

## GR-DATA-03 Use agreed data standards and identifiers {#gr-data-03}

<span class="rfc rfc--must">Must</span> Use the [data standards](../data/data-standards.md) for dates, addresses, locations, identifiers and code lists, so data can be joined across services.

## GR-DATA-04 Collect once, share safely {#gr-data-04}

<span class="rfc rfc--should">Should</span> Do not ask users for information Defra already holds. Share data between services through APIs or governed data products, with data sharing agreements where required.

## GR-DATA-05 Describe your data {#gr-data-05}

<span class="rfc rfc--should">Should</span> Publish metadata for data sets so they can be found and understood - [UK GEMINI](https://www.agi.org.uk/uk-gemini/) for geospatial data and DCAT for other data sets.

## GR-DATA-06 Protect personal data by design {#gr-data-06}

<span class="rfc rfc--must">Must</span> Complete a data protection impact assessment (DPIA) before processing personal data, minimise what you collect, and apply retention and deletion automatically.

**Why:** UK GDPR and the Data Protection Act 2018; TCoP point 7.

## GR-DATA-07 Open by default {#gr-data-07}

<span class="rfc rfc--should">Should</span> Publish non-personal, non-sensitive data as open data under the Open Government Licence, through the [Defra Data Services Platform](https://environment.data.gov.uk/) or [data.gov.uk](https://www.data.gov.uk/).

## GR-DATA-08 Manage data quality {#gr-data-08}

<span class="rfc rfc--should">Should</span> Define, measure and report data quality using the [Government Data Quality Framework](https://www.gov.uk/government/publications/the-government-data-quality-framework), especially for data that feeds payments, regulatory decisions or official statistics.

## GR-DATA-09 Retain and dispose of records properly {#gr-data-09}

<span class="rfc rfc--must">Must</span> Apply Defra's retention schedules. Records of permanent value are identified for transfer to The National Archives.
