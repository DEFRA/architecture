# Threat model excerpt: apply for a licence

<p class="lead">Part of the alpha threat model for the fictional apply for a licence service, written with the <a href="../../../governance/templates/threat-model/">threat model template</a> and the STRIDE method.</p>

!!! info "Fictional and partial"
    This is an excerpt from an invented service's threat model, published to show the format and level of detail. Do not publish real threat models for live services in full - see [what not to publish](../../contribute/index.md#what-not-to-publish).

## Scope

| Aspect | In this example |
| --- | --- |
| Version and date | 0.3, 2026-05-28 (alpha) |
| Participants | Tech lead, developers, product manager, solution architect, security architect |
| Risk owner | Service owner |
| Classification | OFFICIAL, including personal data |
| In scope | Front end, application API, file upload and scanning, outbox and events |
| Out of scope | Case management (has its own threat model), Defra ID, GOV.UK Pay |

## What can go wrong?

| ID | Element | STRIDE | Threat | Existing or planned controls |
| --- | --- | --- | --- | --- |
| T1 | Application API | Elevation of privilege | An agent changes the organisation id in a request to see another landowner's applications | Server-side authorisation on every request ([ADR 0003](adrs.md#adr-0003)); tests for each role |
| T2 | File upload | Tampering | A malicious file is uploaded and opened by an assessing officer | Quarantine, type and size checks, malware scanning; staff read only clean files ([pattern](../file-upload.md)) |
| T3 | File upload | Denial of service | Very large or many files exhaust storage or scanning | Size limits, number limits per application, rate limiting |
| T4 | Events | Spoofing | Something other than the service publishes fake `application-submitted` events | Only the relay's workload identity can publish; consumers check the event source |
| T5 | Events and logs | Information disclosure | Personal data copied into events or logs is exposed to more people than needed | Events carry references not personal data; structured logging with redaction ([GR-OPS-02](../../guardrails/observability-and-operations.md#gr-ops-02)) |
| T6 | Front end | Repudiation | An applicant says they did not submit an application | Audit record of submission with user, organisation, time and content hash |

## What are we going to do about it?

| Threat | Response | Action | Owner |
| --- | --- | --- | --- |
| T1 | Mitigate | Build the authorisation module before the first agent journey; include in the IT health check scope | Tech lead |
| T2 | Mitigate | Confirm scanning service with the platform team | Solution architect |
| T3 | Mitigate | Set limits; load test uploads in beta | Developers |
| T4 | Mitigate | Configure publish permissions through infrastructure as code | Developers |
| T5 | Mitigate | Review event schema and log fields with the security architect | Tech lead |
| T6 | Accept for alpha | Revisit in beta with the case management team | Service owner |

## Did we do a good enough job?

- **Assumption:** Defra ID and GOV.UK Pay are covered by their own threat models.
- **Next review:** before private beta, and at every significant change ([GR-SEC-02](../../guardrails/security.md#gr-sec-02)).
