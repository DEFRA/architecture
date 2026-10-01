# APIs and integration

<p class="lead">How services talk to each other and to partners. Good integration lets us reuse capabilities and change one part of Defra without breaking another.</p>

Supports principle [GR-PRIN-05](../principles/architecture-principles.md#gr-prin-05). Technology capability [TC22 API management and integration](../handrail/technology-capabilities.md#tc22).

## GR-API-01 API first {#gr-api-01}

<span class="rfc rfc--should">Should</span> Design the API for a capability before (or with) the user interface, so other services and partners can use it.

## GR-API-02 Describe APIs with open specifications {#gr-api-02}

<span class="rfc rfc--must">Must</span> Synchronous APIs are described with **OpenAPI 3**, and asynchronous/event interfaces with **AsyncAPI**, kept in the same repository as the code.

**Why:** Machine-readable contracts make APIs discoverable, testable and safe to change.

## GR-API-03 Follow government API standards {#gr-api-03}

<span class="rfc rfc--should">Should</span> Follow the [API technical and data standards](https://www.gov.uk/guidance/gds-api-technical-and-data-standards): RESTful resources, JSON, HTTPS only, consistent error formats and standard identifiers from the [data standards](../data/data-standards.md).

## GR-API-04 Version and deprecate deliberately {#gr-api-04}

<span class="rfc rfc--must">Must</span> Breaking changes are versioned, consumers are told in advance, and old versions have a published retirement date.

## GR-API-05 No integration through shared databases {#gr-api-05}

<span class="rfc rfc--must">Must</span> Services do not read or write another service's database directly. Integrate through APIs, events or governed data products.

**Why:** Shared databases tightly couple services and make both impossible to change safely.

## GR-API-06 Use events for change notifications {#gr-api-06}

<span class="rfc rfc--should">Should</span> Use asynchronous messages or events when other services need to react to something that happened (an application submitted, a permit issued), rather than polling.

## GR-API-07 Secure every API {#gr-api-07}

<span class="rfc rfc--must">Must</span> All APIs authenticate callers (OAuth 2.0 / OpenID Connect or mutual TLS), authorise every request, validate input and apply rate limiting. No API is "internal so it's safe".

## GR-API-08 Make APIs discoverable {#gr-api-08}

<span class="rfc rfc--should">Should</span> Register APIs in the platform API catalogue and, where they are useful beyond Defra, the [government API catalogue](https://www.api.gov.uk/).
