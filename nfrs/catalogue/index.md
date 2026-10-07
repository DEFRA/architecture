<!-- https://defra.github.io/architecture/nfrs/catalogue/ | maturity: draft | site version 0.3.0 | generated from nfrs/catalogue.md -->

# NFR catalogue

<p class="lead">Defra's standard non-functional requirements. Start from these rather than writing your own, so services are consistent and assessors know what good looks like.</p>

!!! warning "Draft - to be confirmed"
    Parts of this page, such as names, timings and thresholds, are still being confirmed by the architecture team. Use it as a guide, and check with your solution design authority before relying on the detail.



**How to use it:** pick your [service tier](https://defra.github.io/architecture/nfrs/service-tiers/), copy the requirements that apply into your backlog with the target for your tier, and add any service-specific NFRs using the guidance on [writing good NFRs](https://defra.github.io/architecture/nfrs/writing-nfrs/). Ids such as `NFR-AVL-01` are stable, so you can reference them in stories, test reports and contracts.

## Availability and resilience {#nfr-avl}

The service is there when users need it and recovers quickly when it fails.

| ID | Requirement | How to show it is met | Target by tier | Related guardrails |
| --- | --- | --- | --- | --- |
| `NFR-AVL-01` | **Availability**<br>The service is available to users for the target percentage of its supported hours, measured monthly, excluding planned maintenance announced 5 working days ahead. | Synthetic monitoring of the main user journey; monthly availability report. | **T1:** 99.9%<br>**T2:** 99.5%<br>**T3:** 99%<br>**T4:** Best effort | [`GR-OPS-03`](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-03) |
| `NFR-AVL-02` | **Recovery time objective**<br>After a major failure, the service is restored within the recovery time objective. | Disaster recovery test with a timed restore. | **T1:** 4 hours<br>**T2:** 24 hours<br>**T3:** 3 working days<br>**T4:** 5 working days | [`GR-HOST-07`](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-07) |
| `NFR-AVL-03` | **Recovery point objective**<br>No more data is lost in a failure than the recovery point objective allows. | Backup configuration review and point-in-time restore test. | **T1:** 15 minutes<br>**T2:** 1 hour<br>**T3:** 24 hours<br>**T4:** 24 hours | [`GR-HOST-07`](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-07) |
| `NFR-AVL-04` | **No single point of failure**<br>The service runs across at least two availability zones, with no single component whose failure stops the service. | Architecture review and a zone failure test. | **T1:** Required<br>**T2:** Required<br>**T3:** Recommended<br>**T4:** Not required | - |
| `NFR-AVL-05` | **Graceful degradation**<br>When a dependency fails, users are told what has happened and do not lose information they have entered. | Dependency failure tests in the pipeline. | All tiers | [`GR-OPS-04`](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-04) |

## Performance and capacity {#nfr-prf}

The service is fast enough for users and copes with expected peaks.

| ID | Requirement | How to show it is met | Target by tier | Related guardrails |
| --- | --- | --- | --- | --- |
| `NFR-PRF-01` | **Page response time**<br>95% of page requests complete within 2 seconds, measured at the server, at expected peak load. | Load test at peak volume before go-live and after significant change. | All tiers | - |
| `NFR-PRF-02` | **API response time**<br>95% of synchronous API calls complete within 500 milliseconds at expected peak load. | Load test and production monitoring of latency percentiles. | All tiers | [`GR-API-02`](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-02) |
| `NFR-PRF-03` | **Peak capacity**<br>The service handles twice the highest expected peak (for example a scheme deadline or flood event) without failing. | Load test at 2x forecast peak; autoscaling configuration review. | **T1:** 2x peak<br>**T2:** 2x peak<br>**T3:** 1.5x peak<br>**T4:** Expected peak | - |
| `NFR-PRF-04` | **Low bandwidth**<br>Core journeys are usable on a 3G connection, with page weight under 500KB excluding cached assets. | Lighthouse or WebPageTest on a throttled connection. | All tiers | [`GR-FE-05`](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-05) |

## Security {#nfr-sec}

The service protects its users, data and Defra.

| ID | Requirement | How to show it is met | Target by tier | Related guardrails |
| --- | --- | --- | --- | --- |
| `NFR-SEC-01` | **Threat model**<br>A current threat model exists and is reviewed at every significant change and at least annually. | Threat model in the repository or linked from it, with a review date. | All tiers | [`GR-SEC-02`](https://defra.github.io/architecture/guardrails/security/#gr-sec-02) |
| `NFR-SEC-02` | **Vulnerability remediation**<br>Critical vulnerabilities are fixed within 14 days and high within 30 days, or a risk decision is recorded. | Scanner reports and the risk register. | All tiers | [`GR-SEC-05`](https://defra.github.io/architecture/guardrails/security/#gr-sec-05) |
| `NFR-SEC-03` | **Independent security testing**<br>An IT health check proportionate to risk is completed before go-live and after significant change. | Health check report and remediation plan. | **T1:** Required<br>**T2:** Required<br>**T3:** Required<br>**T4:** Risk based | [`GR-SEC-06`](https://defra.github.io/architecture/guardrails/security/#gr-sec-06) |
| `NFR-SEC-04` | **Encryption**<br>All data is encrypted in transit with TLS 1.2 or higher and encrypted at rest. | Configuration review and automated TLS checks. | All tiers | [`GR-SEC-04`](https://defra.github.io/architecture/guardrails/security/#gr-sec-04) |
| `NFR-SEC-05` | **Access control**<br>Users and services have only the permissions they need, granted by role, and access is reviewed at least every 6 months. | Role model documentation and access review records. | All tiers | [`GR-IAM-03`](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-03) |

## Accessibility and usability {#nfr-acc}

Everyone who needs the service can use it.

| ID | Requirement | How to show it is met | Target by tier | Related guardrails |
| --- | --- | --- | --- | --- |
| `NFR-ACC-01` | **WCAG 2.2 AA**<br>The service meets WCAG 2.2 level AA and publishes an accessibility statement. | Automated checks in the pipeline, manual testing with assistive technology and an accessibility audit before public beta. | All tiers | [`GR-FE-01`](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-01) |
| `NFR-ACC-02` | **Design system**<br>Public-facing pages use GOV.UK Frontend components and patterns. | Code review and service assessment. | All tiers | [`GR-FE-02`](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-02) |
| `NFR-ACC-03` | **Works without JavaScript**<br>Core journeys can be completed with JavaScript unavailable. | End-to-end tests run with JavaScript disabled. | All tiers | [`GR-FE-03`](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-03) |
| `NFR-ACC-04` | **Supported browsers and devices**<br>The service works on the browsers and assistive technologies in the GOV.UK Service Manual's supported list. | Cross-browser test results. | All tiers | - |

## Observability and supportability {#nfr-ops}

The service can be monitored, supported and fixed by people who did not build it.

| ID | Requirement | How to show it is met | Target by tier | Related guardrails |
| --- | --- | --- | --- | --- |
| `NFR-OPS-01` | **Logging and tracing**<br>Structured logs, metrics and traces with correlation ids are sent to the platform observability tooling. | Dashboard and a traced request across service boundaries. | All tiers | [`GR-OPS-01`](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-01), [`GR-OPS-02`](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-02) |
| `NFR-OPS-02` | **Alerting**<br>Alerts on user-facing symptoms reach the support team within 5 minutes of a breach. | Alert test during operational readiness review. | **T1:** 24/7 on-call<br>**T2:** Extended hours<br>**T3:** Business hours<br>**T4:** Business hours | [`GR-OPS-03`](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-03) |
| `NFR-OPS-03` | **Runbooks**<br>Runbooks cover deployment, rollback, restart, common failures and contacts. | Runbook walkthrough with the support team before public beta. | All tiers | [`GR-OPS-05`](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05) |

## Maintainability and testability {#nfr-mnt}

The service is cheap and safe to change.

| ID | Requirement | How to show it is met | Target by tier | Related guardrails |
| --- | --- | --- | --- | --- |
| `NFR-MNT-01` | **Automated deployment**<br>Every change reaches production through an automated pipeline, and any release can be rolled back. | Pipeline configuration and a rollback demonstration. | All tiers | [`GR-DEV-04`](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-04), [`GR-HOST-03`](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-03) |
| `NFR-MNT-02` | **Automated tests**<br>Unit, integration and journey tests run on every change, and the main branch is always releasable. | Pipeline results and coverage of critical journeys. | All tiers | [`GR-DEV-05`](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-05) |
| `NFR-MNT-03` | **Supported runtimes and dependencies**<br>Languages, frameworks and dependencies are on supported versions, with automated update pull requests. | Dependency report. | All tiers | [`GR-DEV-06`](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-06) |
| `NFR-MNT-04` | **Documentation**<br>The repository explains how to run, test and deploy the service and links to its decision records. | README and ADR log review. | All tiers | [`GR-DEV-08`](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-08) |

## Interoperability {#nfr-int}

The service works with the rest of Defra and its partners.

| ID | Requirement | How to show it is met | Target by tier | Related guardrails |
| --- | --- | --- | --- | --- |
| `NFR-INT-01` | **Documented APIs**<br>APIs are described with OpenAPI or AsyncAPI and published to the API catalogue. | Specification in the repository; catalogue entry. | All tiers | [`GR-API-02`](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-02), [`GR-API-08`](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-08) |
| `NFR-INT-02` | **Standard identifiers**<br>Shared entities use the identifiers in Defra's data standards (such as SBI, CRN, CPH and UPRN). | Data model review. | All tiers | [`GR-DATA-03`](https://defra.github.io/architecture/guardrails/data/#gr-data-03) |

## Data and compliance {#nfr-dat}

Data is accurate, protected and kept for the right length of time.

| ID | Requirement | How to show it is met | Target by tier | Related guardrails |
| --- | --- | --- | --- | --- |
| `NFR-DAT-01` | **Data protection**<br>A DPIA is completed before personal data is processed, and personal data is minimised. | Approved DPIA. | All tiers | [`GR-DATA-06`](https://defra.github.io/architecture/guardrails/data/#gr-data-06) |
| `NFR-DAT-02` | **Retention and disposal**<br>Data is retained and deleted automatically in line with Defra retention schedules. | Retention configuration and a disposal test. | All tiers | [`GR-DATA-09`](https://defra.github.io/architecture/guardrails/data/#gr-data-09) |
| `NFR-DAT-03` | **Data location**<br>OFFICIAL data is stored in UK regions. | Infrastructure configuration review. | All tiers | [`GR-HOST-06`](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-06) |
| `NFR-DAT-04` | **Data quality**<br>Data quality rules are defined for data that feeds payments, regulatory decisions or statistics, and are measured. | Data quality dashboard. | All tiers | [`GR-DATA-08`](https://defra.github.io/architecture/guardrails/data/#gr-data-08) |

## Sustainability {#nfr-sus}

The service uses no more energy and resources than it needs.

| ID | Requirement | How to show it is met | Target by tier | Related guardrails |
| --- | --- | --- | --- | --- |
| `NFR-SUS-01` | **Right-sized and switched off**<br>Non-production environments scale down out of hours, and production scales with demand. | Scaling configuration and monthly cost and carbon report. | All tiers | [`GR-SUS-02`](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-02) |
| `NFR-SUS-02` | **Carbon reporting**<br>The service's cloud carbon footprint is reported alongside its cost. | Cloud provider carbon report. | All tiers | [`GR-SUS-05`](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-05) |



