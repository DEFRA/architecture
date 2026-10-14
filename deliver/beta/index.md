<!-- https://defra.github.io/architecture/deliver/beta/ | maturity: prototype | site version 0.3.0 | generated from deliver/beta.md -->

# Beta

<p class="lead">Beta is where you build the real service and prove it is secure, reliable and ready to run. The architecture job is to keep the design and the evidence in step with what you build.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



## What it means for architecture

- Build on the platforms you chose in alpha and keep the ADR log current as the design changes.
- Test against your NFRs, including performance, recovery and accessibility.
- Build and test security controls and commission an IT health check before going live.
- Agree how the service will be supported in live before public beta.

## Guardrails that apply

These guardrails apply in beta, taken from each guardrail's metadata. Meet every Must, or have an approved [exception](https://defra.github.io/architecture/governance/exceptions/). Depart from a Should only with a recorded reason.

### Must (25)

| Guardrail | What to show |
| --- | --- |
| [GR-AI-02](https://defra.github.io/architecture/guardrails/ai/#gr-ai-02) Use approved AI services and tenancies | The AI services in the built service run only in approved tenancies, shown in the hosting design and configuration |
| [GR-AI-03](https://defra.github.io/architecture/guardrails/ai/#gr-ai-03) Keep a human accountable | Human review and challenge built into the service and tested with users and staff |
| [GR-AI-04](https://defra.github.io/architecture/guardrails/ai/#gr-ai-04) Be transparent | Draft Algorithmic Transparency Recording Standard record, and the notice telling users about AI tested with them |
| [GR-API-07](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-07) Secure every API | These controls built and covered by security testing |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | Approved DPIA, and retention and deletion built and tested |
| [GR-DATA-09](https://defra.github.io/architecture/guardrails/data/#gr-data-09) Retain and dispose of records properly | Retention schedule identified for each type of record, and disposal built in |
| [GR-FE-01](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-01) Meet WCAG 2.2 AA | Accessibility audit and assistive technology testing completed, issues fixed, and an accessibility statement published |
| [GR-FE-02](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-02) Use the GOV.UK Design System | The service uses GOV.UK Frontend, with design decisions recording any departures |
| [GR-FE-06](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-06) Support Welsh where required | Welsh content and journeys built and tested where the standards apply |
| [GR-HOST-01](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-01) Use Defra's strategic delivery platform by default | The service runs on the Core Delivery Platform, or under an approved exception |
| [GR-IAM-01](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-01) Use the strategic customer identity services | Integration with Defra Customer Identity built and tested |
| [GR-IAM-02](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-02) Staff sign in with Microsoft Entra ID | Staff sign in through Microsoft Entra ID with multi-factor authentication, and there are no local staff accounts |
| [GR-IAM-03](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-03) Authorise on least privilege | Role and group model built, with users, services and pipelines given only the permissions they need |
| [GR-IAM-05](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-05) No secrets in code | All secrets in a managed store with rotation, using workload identity where possible |
| [GR-IAM-06](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-06) Privileged access is controlled and audited | Just-in-time privileged access with phishing-resistant MFA configured, and logged to the security operations centre |
| [GR-OPS-05](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05) Be ready for live before you go live | Before public beta, the support model, on-call arrangements, runbooks, incident process and live owner agreed, and the service catalogue entry made |
| [GR-OPEN-01](https://defra.github.io/architecture/guardrails/open-source/#gr-open-01) Code in the open | Repositories public, or the reasons for keeping them private reviewed |
| [GR-SEC-01](https://defra.github.io/architecture/guardrails/security/#gr-sec-01) Follow Secure by Design | Secure by Design activities for beta completed, including controls built and tested |
| [GR-SEC-02](https://defra.github.io/architecture/guardrails/security/#gr-sec-02) Keep a current threat model | Threat model updated as controls are built and tested |
| [GR-SEC-04](https://defra.github.io/architecture/guardrails/security/#gr-sec-04) Encrypt in transit and at rest | TLS 1.2 or higher for all traffic and encryption at rest for every data store, confirmed as built |
| [GR-SEC-05](https://defra.github.io/architecture/guardrails/security/#gr-sec-05) Scan continuously and fix quickly | Static analysis, dependency, container and infrastructure scanning running in the pipeline |
| [GR-SEC-06](https://defra.github.io/architecture/guardrails/security/#gr-sec-06) Test before go-live and after major change | IT health check before go-live, and a remediation tracker |
| [GR-SEC-07](https://defra.github.io/architecture/guardrails/security/#gr-sec-07) Log for detection and response | Authentication, authorisation failures, administrative actions and data exports sent to the security operations centre, and tested |
| [GR-SEC-09](https://defra.github.io/architecture/guardrails/security/#gr-sec-09) Manage risk explicitly | Residual risks accepted by the right owner through the security exception process, each with an expiry date |
| [GR-DEV-02](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-02) All code in Defra source control | All source, infrastructure and pipeline code in the Defra GitHub organisation, with nothing held only by a supplier |

??? note "Should (58)"

    | Guardrail | What to show |
    | --- | --- |
    | [GR-AI-05](https://defra.github.io/architecture/guardrails/ai/#gr-ai-05) Evaluate, monitor and threat model | Evaluation results for accuracy, bias and safety before release, and mitigations for AI threats tested |
    | [GR-AI-07](https://defra.github.io/architecture/guardrails/ai/#gr-ai-07) Suppliers use AI coding assistants openly and safely | Supplier's agreed list of AI coding assistants and how each runs within Defra-approved terms, the review process for generated code, and disclosure in pull requests or delivery reports |
    | [GR-AI-08](https://defra.github.io/architecture/guardrails/ai/#gr-ai-08) Give agents the least privilege they need | Agent permissions configured as designed and tested, including that the agent cannot reach tools it should not |
    | [GR-AI-09](https://defra.github.io/architecture/guardrails/ai/#gr-ai-09) Get human approval for consequential actions | Approval enforced in the tool layer, with tests showing the agent cannot act without it |
    | [GR-AI-10](https://defra.github.io/architecture/guardrails/ai/#gr-ai-10) Keep an audit trail of what agents do | Audit records of agent inputs, tool calls, approvals and outcomes produced and sent to security monitoring |
    | [GR-AI-11](https://defra.github.io/architecture/guardrails/ai/#gr-ai-11) Defend agents against prompt injection | Prompt injection mitigations tested, including attempts to misuse tools and leak data |
    | [GR-API-01](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-01) API first | API specification written before or alongside the user interface |
    | [GR-API-02](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-02) Describe APIs with open specifications | OpenAPI 3 or AsyncAPI documents in the repository, checked in the pipeline against the running API |
    | [GR-API-03](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-03) Follow government API standards | API design reviewed against the GDS API technical and data standards |
    | [GR-API-04](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-04) Version and deprecate deliberately | Versioning approach published for each API and event |
    | [GR-API-05](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-05) No integration through shared databases | Built integrations match the container diagram, with no access to another service's database |
    | [GR-API-06](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-06) Use events for change notifications | Event and message definitions described in AsyncAPI |
    | [GR-API-08](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-08) Make APIs discoverable | Entry in the platform API catalogue |
    | [GR-TECH-03](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) Plan your exit before you enter | Exit plan agreed, with contracts giving Defra its data and the right to export it in open formats |
    | [GR-DATA-01](https://defra.github.io/architecture/guardrails/data/#gr-data-01) Every data set has an owner | Information asset register entries with a named owner for each data set |
    | [GR-DATA-02](https://defra.github.io/architecture/guardrails/data/#gr-data-02) Use authoritative sources | The service reads from the authoritative sources as designed, tested with the source owners |
    | [GR-DATA-03](https://defra.github.io/architecture/guardrails/data/#gr-data-03) Use agreed data standards and identifiers | Data stored and exchanged using the agreed standards, checked in testing |
    | [GR-DATA-04](https://defra.github.io/architecture/guardrails/data/#gr-data-04) Collect once, share safely | Journey design showing users are not asked for information Defra already holds, and data sharing agreements where required |
    | [GR-DATA-05](https://defra.github.io/architecture/guardrails/data/#gr-data-05) Describe your data | Published metadata records in UK GEMINI or DCAT |
    | [GR-DATA-07](https://defra.github.io/architecture/guardrails/data/#gr-data-07) Open by default | Link to the published open data and its licence |
    | [GR-DATA-08](https://defra.github.io/architecture/guardrails/data/#gr-data-08) Manage data quality | Data quality measures and regular reports |
    | [GR-DATA-10](https://defra.github.io/architecture/guardrails/data/#gr-data-10) Handle research data safely | Research data from earlier phases deleted on schedule, and the same controls for beta research |
    | [GR-DATA-11](https://defra.github.io/architecture/guardrails/data/#gr-data-11) No real personal data in prototypes | Test and research environments use synthetic or anonymised data; any exception agreed through a DPIA |
    | [GR-DIG-02](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-02) Design across organisational boundaries | A map of the whole service, including the parts other teams and organisations deliver, and agreed hand-offs between them |
    | [GR-DIG-03](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-03) Provide assisted digital and offline routes | Assisted digital and offline routes designed and tested with users who need them |
    | [GR-FIELD-02](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-02) Design field tools to work offline | Field journeys tested with no connection, including sync after reconnecting and conflict handling |
    | [GR-FIELD-03](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-03) Manage and secure every device | Devices enrolled in Defra device management, with encryption, patching, screen lock and remote wipe confirmed |
    | [GR-FE-03](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-03) Progressive enhancement | Core journeys tested with JavaScript turned off |
    | [GR-FE-05](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-05) Design for low bandwidth and rural users | Page weight budget, save-progress design and testing on slow connections |
    | [GR-FE-07](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-07) Tell users what is happening when things fail or are slow | The front end shows the designed content when a dependency fails or is slow, tested by switching dependencies off |
    | [GR-HOST-02](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-02) Public cloud first | The service runs in a Defra-managed public cloud tenancy |
    | [GR-HOST-03](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-03) Everything as code | Infrastructure, configuration and pipelines defined as code in the repository, with no manual changes to production |
    | [GR-HOST-04](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-04) Use managed services before self-managed | Hosting design listing the managed services used |
    | [GR-HOST-05](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-05) Consistent, disposable environments | Environments created from the same code, and how lower environments avoid real personal data |
    | [GR-HOST-06](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-06) Host data in the UK | Data location confirmed for every data store and backup as built |
    | [GR-HOST-07](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-07) Design for the resilience the service needs | Multi-zone design built, and recovery tested before go-live |
    | [GR-IAM-04](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-04) Separate authentication from authorisation | Authorisation rules written down and covered by automated tests |
    | [GR-OPS-01](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-01) Use the platform's observability tooling | Logs, metrics and traces reaching the platform's observability tooling, and security events reaching the security operations centre |
    | [GR-OPS-02](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-02) Log in a structured, safe way | Structured logs with correlation identifiers, tested to show no secrets or unnecessary personal data are logged |
    | [GR-OPS-03](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-03) Define and measure service levels | Agreed service level objectives with monitoring and alerts |
    | [GR-OPS-04](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-04) Health checks and graceful degradation | Health endpoints, timeout and retry settings, and a design for when dependencies fail |
    | [GR-OPS-07](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-07) Measure performance and cost | Published key performance indicators and cost tags on cloud resources |
    | [GR-OPEN-02](https://defra.github.io/architecture/guardrails/open-source/#gr-open-02) Licence clearly | LICENCE file with the Open Government Licence or MIT licence in every repository |
    | [GR-OPEN-03](https://defra.github.io/architecture/guardrails/open-source/#gr-open-03) Publish safely | Secret scanning and push protection on for every repository |
    | [GR-OPEN-04](https://defra.github.io/architecture/guardrails/open-source/#gr-open-04) Reuse and contribute back | Reuse and upstream contributions noted in ADRs and pull requests |
    | [GR-PROD-01](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-01) Fund and run products, not projects | A named, long-lived team responsible for the product, with a roadmap beyond the current funding period |
    | [GR-PROD-02](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-02) Name the product owner and service owner | Named product owner and service owner, recorded in the service catalogue |
    | [GR-PROD-03](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-03) Contribute to platforms rather than working around them | Requests and contributions raised with platform teams, and ADRs where the team worked around a platform |
    | [GR-SEC-08](https://defra.github.io/architecture/guardrails/security/#gr-sec-08) Protect the supply chain | Dependencies pinned and verified, and a software bill of materials produced in the pipeline |
    | [GR-DEV-03](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-03) Protect the main branch | Branch protection requiring at least one review and passing checks |
    | [GR-DEV-04](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-04) Continuous integration and delivery | Every change built, tested, scanned and deployed by an automated pipeline, with rollback tested |
    | [GR-DEV-05](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-05) Automated testing at the right levels | Test results from the pipeline at each level |
    | [GR-DEV-06](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-06) Manage dependencies actively | Dependabot or Renovate configured, software composition analysis in the pipeline, and runtimes on supported versions |
    | [GR-DEV-07](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-07) Follow shared coding standards | Linting and formatting checks in the pipeline |
    | [GR-DEV-08](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-08) Document as you go | README explaining what the service does and how to run, test and deploy it, with links to its ADRs |
    | [GR-DEV-09](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-09) Record significant decisions as ADRs | ADR log in the repository or linked from its README |
    | [GR-SUS-02](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-02) Right-size and switch off | Autoscaling and out-of-hours schedules for non-production environments |
    | [GR-SUS-04](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-04) Keep data and pages lean | Data retention settings and page weight measurements |

??? note "Could (1)"

    | Guardrail | What to show |
    | --- | --- |
    | [GR-OPEN-05](https://defra.github.io/architecture/guardrails/open-source/#gr-open-05) Blog and show the thing | Blog posts, show and tells or contributions to this site |

## Architecture artefacts

| Artefact | What to do in this phase |
| --- | --- |
| [Architecture decision record (ADR) log](https://defra.github.io/architecture/governance/architecture-decision-records/) ([template](https://defra.github.io/architecture/governance/templates/adr/)) | Keep it current as the design changes. |
| [C4 container diagram](https://c4model.com/) | Update it to match what you built. |
| [Threat model](https://defra.github.io/architecture/security/threat-modelling/) ([template](https://defra.github.io/architecture/governance/templates/threat-model/)) | Review it as controls are built and tested. |
| [Data protection impact assessment (DPIA)](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/) | Update it for anything that has changed. |
| [Non-functional requirements (NFRs)](https://defra.github.io/architecture/nfrs/catalogue/) | Test against them and record the results. |
| [Exit plan](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) | Confirm contracts give Defra its data and the right to export it. |
| [Runbooks and support model](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05) | Write them and agree the support model before public beta. |

## Governance touchpoints

- Go through the operational service design review board at the start of beta - see [operational service readiness](https://digital.defra.gov.uk/delivery-groups/follow-delivery-governance/assurance/operational-service-readiness) in the Defra Digital Service Manual.
- Commission an IT health check before go-live ([GR-SEC-06](https://defra.github.io/architecture/guardrails/security/#gr-sec-06)).
- Get residual security risks accepted through the [security exception process](https://defra.github.io/architecture/security/managing-exceptions/).
- Share the updated evidence pack with your solution design authority before the beta assessment.

## Evidence pack

Bring these together once and reuse them for your solution design authority, service assessment, spend control and security assurance:

- Architecture decision record (ADR) log
- C4 container diagram
- Threat model
- Data protection impact assessment (DPIA)
- Non-functional requirements (NFRs)
- Exit plan
- Runbooks and support model
- evidence for each Must guardrail above (25)

Use the [beta evidence checklist](https://defra.github.io/architecture/deliver/checklists/beta/) to gather and print it.

For how the phase works and what assessors look for, see the GOV.UK Service Manual on [beta](https://www.gov.uk/service-manual/agile-delivery/how-the-beta-phase-works) and the [Defra Digital Service Manual](https://digital.defra.gov.uk/service-manual). This site covers the architecture evidence only.


