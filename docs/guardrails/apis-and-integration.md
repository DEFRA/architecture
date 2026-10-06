---
applicability: tbc
principles: [GR-PRIN-05]
# Metadata for every guardrail on this page. See the contribution guide for the fields.
guardrail_defaults:
  status: draft
  owner: Architecture team
  automated_check: manual
  last_reviewed: 2026-10-01
  since_version: 0.1.0
guardrails:
  GR-API-01:
    phases: [alpha, beta]
    lead_roles: [technical-architect]
    evidence: API specification written before or alongside the user interface
    service_standard_points: [13]
    tcop_points: [9]
  GR-API-02:
    phases: [alpha, beta, live]
    lead_roles: [developer]
    evidence: OpenAPI 3 or AsyncAPI documents in the service repository that match the running API
    evidence_by_phase:
      alpha: Draft OpenAPI 3 or AsyncAPI documents for the interfaces you are prototyping
      beta: OpenAPI 3 or AsyncAPI documents in the repository, checked in the pipeline against the running API
      live: Specifications kept in step with every released change
    automated_check: "Guardrail check (tools/guardrail-check): OpenAPI 3 and AsyncAPI documents present and well formed"
    service_standard_points: [13]
    tcop_points: [4, 9]
  GR-API-03:
    phases: [alpha, beta, live]
    lead_roles: [developer, technical-architect]
    evidence: API design reviewed against the GDS API technical and data standards
    service_standard_points: [13]
    tcop_points: [4]
  GR-API-04:
    phases: [beta, live]
    lead_roles: [technical-architect, product-manager]
    evidence: Published versioning policy, deprecation notices sent to consumers and retirement dates for old versions
    evidence_by_phase:
      beta: Versioning approach published for each API and event
      live: Deprecation notices sent to consumers and retirement dates published for old versions
      significant-change: Consumers told about breaking changes in advance, with a new version and a retirement date for the old one
      retire: Consumers told the retirement date in advance, and moved to a replacement
    tcop_points: [9]
  GR-API-05:
    phases: [alpha, beta, live]
    lead_roles: [technical-architect]
    evidence: Container diagram showing integration only through APIs, events or governed data products
    evidence_by_phase:
      alpha: Container diagram showing integration only through APIs, events or governed data products
      beta: Built integrations match the container diagram, with no access to another service's database
      live: Integrations reviewed when the service or its dependencies change
    tcop_points: [9]
    sbd_principles: [6]
  GR-API-06:
    phases: [alpha, beta]
    lead_roles: [technical-architect, developer]
    evidence: Event and message definitions described in AsyncAPI
  GR-API-07:
    phases: [alpha, beta, live]
    lead_roles: [security-architect, developer]
    evidence: Authentication and authorisation design, rate limits and input validation, covered by security testing
    evidence_by_phase:
      alpha: Authentication, authorisation, input validation and rate limiting designed for each API
      beta: These controls built and covered by security testing
      live: API access reviewed, and controls re-tested after significant change
    service_standard_points: [9]
    tcop_points: [6]
    sbd_principles: [7, 8]
  GR-API-08:
    phases: [beta, live]
    lead_roles: [technical-architect]
    evidence: Entry in the platform API catalogue
    tcop_points: [8]
---

# APIs and integration

<p class="lead">How services talk to each other and to partners. Good integration lets us reuse capabilities and change one part of Defra without breaking another.</p>

Technology capability [Enabling Platforms](../handrail/technology-capabilities.md#enabling-platforms): aPI management and integration.

## GR-API-01 API first {#gr-api-01}

<span class="rfc rfc--should">Should</span> Design the API for a capability before (or with) the user interface, so other services and partners can use it.

## GR-API-02 Describe APIs with open specifications {#gr-api-02}

<span class="rfc rfc--should">Should</span> Synchronous APIs are described with **OpenAPI 3**, and asynchronous/event interfaces with **AsyncAPI**, kept in the same repository as the code.

**Why:** Machine-readable contracts make APIs discoverable, testable and safe to change.

## GR-API-03 Follow government API standards {#gr-api-03}

<span class="rfc rfc--should">Should</span> Follow the [API technical and data standards](https://www.gov.uk/guidance/gds-api-technical-and-data-standards): RESTful resources, JSON, HTTPS only, consistent error formats and standard identifiers from the [data standards](../data/data-standards.md).

## GR-API-04 Version and deprecate deliberately {#gr-api-04}

<span class="rfc rfc--should">Should</span> Breaking changes are versioned, consumers are told in advance, and old versions have a published retirement date.

## GR-API-05 No integration through shared databases {#gr-api-05}

<span class="rfc rfc--should">Should</span> Services do not read or write another service's database directly. Integrate through APIs, events or governed data products.

**Why:** Shared databases tightly couple services and make both impossible to change safely.

## GR-API-06 Use events for change notifications {#gr-api-06}

<span class="rfc rfc--should">Should</span> Use asynchronous messages or events when other services need to react to something that happened (an application submitted, a permit issued), rather than polling.

## GR-API-07 Secure every API {#gr-api-07}

<span class="rfc rfc--must">Must</span> All APIs authenticate callers (OAuth 2.0 / OpenID Connect or mutual TLS), authorise every request, validate input and apply rate limiting. No API is "internal so it's safe".

## GR-API-08 Make APIs discoverable {#gr-api-08}

<span class="rfc rfc--should">Should</span> Register APIs in the platform API catalogue and, where they are useful beyond Defra, the [government API catalogue](https://www.api.gov.uk/).
