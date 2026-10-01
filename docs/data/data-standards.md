# Data standards

<p class="lead">The standards that make Defra data consistent, joinable and reusable. Use these by default - see guardrail <a href="../../guardrails/data/#gr-data-03">GR-DATA-03</a>.</p>

We adopt cross-government standards from the [Data Standards Authority](https://www.gov.uk/government/collections/data-standards-for-government) wherever they exist, and add Defra-specific standards only where needed.

## Cross-government standards

| Topic | Standard |
| --- | --- |
| Dates and times | ISO 8601, stored in UTC |
| Property and street identifiers | UPRN and USRN |
| Organisations | Companies House number, Charity Commission number |
| Countries and territories | ISO 3166 / FCDO country register |
| Tabular data | CSV with UTF-8 encoding |
| Character encoding | UTF-8 |
| APIs | [API technical and data standards](https://www.gov.uk/guidance/gds-api-technical-and-data-standards), OpenAPI 3 |
| Metadata | [DCAT](https://www.w3.org/TR/vocab-dcat-3/) for data catalogues |
| Data quality | [Government Data Quality Framework](https://www.gov.uk/government/publications/the-government-data-quality-framework) |
| Data ethics | [Data and AI Ethics Framework](https://www.gov.uk/government/publications/data-ethics-framework) |

## Geospatial standards

Much of Defra's data is about places. Geospatial data should follow these standards so it can be overlaid and analysed together.

| Topic | Standard |
| --- | --- |
| Coordinate reference system (GB) | British National Grid, EPSG:27700, for storage and analysis |
| Coordinate reference system (web) | WGS 84 (EPSG:4326) or Web Mercator (EPSG:3857) for web display and exchange |
| Geospatial metadata | [UK GEMINI](https://www.agi.org.uk/uk-gemini/) |
| Data exchange | OGC API - Features, GeoJSON, GeoPackage; WMS/WMTS for map services |
| Base mapping and addresses | Ordnance Survey data under the [Public Sector Geospatial Agreement](https://www.ordnancesurvey.co.uk/customers/public-sector/public-sector-geospatial-agreement) |

## Defra identifiers

These identifiers are widely used across Defra group. Use them, and validate them, rather than inventing local equivalents.

| Identifier | Identifies | Notes |
| --- | --- | --- |
| **CRN** - Customer Reference Number | A person registered with the Rural Payments service | |
| **SBI** - Single Business Identifier | A business registered with the Rural Payments service | |
| **CPH** - County Parish Holding number | A holding (land or premises) where livestock are kept | Format `NN/NNN/NNNN` |
| Land parcel identifier | A parcel of land on the RPA land register | Sheet reference and parcel number |
| Water body identifier | A water body under the Water Framework Directive classification | |
| Protected site code | A designated site such as an SSSI | |

## Proposing a new standard

If you need a standard that is not listed, check the [Data Standards Authority](https://www.gov.uk/government/collections/data-standards-for-government) first. If there is still a gap, raise an issue in this repository - the data architecture team will review it with the [TDA](../governance/tda.md).
