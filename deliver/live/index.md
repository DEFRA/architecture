<!-- https://defra.github.io/architecture/deliver/live/ | maturity: prototype | site version 0.3.0 | generated from deliver/live.md -->

# Live

<p class="lead">A live service is never finished. The architecture job is to keep it secure, supported and affordable, and to keep the evidence current so the next team can change it safely.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



## What it means for architecture

- Keep the threat model, ADR log and diagrams current.
- Watch service levels, cost and carbon, and act on what you learn.
- Patch and update dependencies continuously.
- Review exceptions before they expire, and treat significant changes as their own small delivery.

## Guardrails that apply

These guardrails apply in live, taken from each guardrail's metadata. Meet every Must, or have an approved [exception](https://defra.github.io/architecture/governance/exceptions/). Depart from a Should only with a recorded reason.

### Must (25)

| Guardrail | What to show |
| --- | --- |
| [GR-AI-02](https://defra.github.io/architecture/guardrails/ai/#gr-ai-02) Use approved AI services and tenancies | List of AI services in use, reviewed when services or agreements change |
| [GR-AI-03](https://defra.github.io/architecture/guardrails/ai/#gr-ai-03) Keep a human accountable | Records of human review, challenges raised and their outcomes, reviewed regularly |
| [GR-AI-04](https://defra.github.io/architecture/guardrails/ai/#gr-ai-04) Be transparent | Link to the published Algorithmic Transparency Recording Standard record, kept current |
| [GR-API-07](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-07) Secure every API | API access reviewed, and controls re-tested after significant change |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | DPIA reviewed when processing changes, and deletion running as designed |
| [GR-DATA-09](https://defra.github.io/architecture/guardrails/data/#gr-data-09) Retain and dispose of records properly | Retention applied and records of permanent value identified for The National Archives |
| [GR-FE-01](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-01) Meet WCAG 2.2 AA | Accessibility statement kept current, and accessibility re-tested after significant change |
| [GR-FE-02](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-02) Use the GOV.UK Design System | GOV.UK Frontend kept up to date |
| [GR-FE-06](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-06) Support Welsh where required | Welsh content kept in step with English content |
| [GR-HOST-01](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-01) Use Defra's strategic delivery platform by default | The service still runs on the platform, and any exception is reviewed before it expires |
| [GR-IAM-01](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-01) Use the strategic customer identity services | No other sign-in introduced |
| [GR-IAM-02](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-02) Staff sign in with Microsoft Entra ID | Staff access reviewed regularly through Entra ID groups |
| [GR-IAM-03](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-03) Authorise on least privilege | Record of regular access reviews |
| [GR-IAM-05](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-05) No secrets in code | Secrets rotated, and secret scanning alerts dealt with |
| [GR-IAM-06](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-06) Privileged access is controlled and audited | Privileged access reviewed regularly |
| [GR-OPS-05](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05) Be ready for live before you go live | Runbooks and support arrangements tested and kept current |
| [GR-OPEN-01](https://defra.github.io/architecture/guardrails/open-source/#gr-open-01) Code in the open | Repositories still public, or private for a recorded reason |
| [GR-SEC-01](https://defra.github.io/architecture/guardrails/security/#gr-sec-01) Follow Secure by Design | Secure by Design activities for live continuing, including monitoring and review |
| [GR-SEC-02](https://defra.github.io/architecture/guardrails/security/#gr-sec-02) Keep a current threat model | Threat model reviewed at least once a year, with the date of the last review |
| [GR-SEC-04](https://defra.github.io/architecture/guardrails/security/#gr-sec-04) Encrypt in transit and at rest | Encryption settings checked when new stores or connections are added |
| [GR-SEC-05](https://defra.github.io/architecture/guardrails/security/#gr-sec-05) Scan continuously and fix quickly | Time taken to fix critical and high vulnerabilities, within 14 and 30 days, or a recorded risk decision |
| [GR-SEC-06](https://defra.github.io/architecture/guardrails/security/#gr-sec-06) Test before go-live and after major change | IT health check after significant change, with remediation tracked |
| [GR-SEC-07](https://defra.github.io/architecture/guardrails/security/#gr-sec-07) Log for detection and response | Security events reviewed and alerts acted on |
| [GR-SEC-09](https://defra.github.io/architecture/guardrails/security/#gr-sec-09) Manage risk explicitly | Accepted risks reviewed before they expire |
| [GR-DEV-02](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-02) All code in Defra source control | All changes made in the Defra GitHub organisation |

??? note "Should (50)"

    | Guardrail | What to show |
    | --- | --- |
    | [GR-AI-05](https://defra.github.io/architecture/guardrails/ai/#gr-ai-05) Evaluate, monitor and threat model | Monitoring of model performance and drift in live, with evaluation repeated when the model or data changes |
    | [GR-AI-07](https://defra.github.io/architecture/guardrails/ai/#gr-ai-07) Suppliers use AI coding assistants openly and safely | Supplier's agreed list of AI coding assistants and how each runs within Defra-approved terms, the review process for generated code, and disclosure in pull requests or delivery reports |
    | [GR-AI-08](https://defra.github.io/architecture/guardrails/ai/#gr-ai-08) Give agents the least privilege they need | Agent permissions reviewed regularly, as for a privileged user |
    | [GR-AI-09](https://defra.github.io/architecture/guardrails/ai/#gr-ai-09) Get human approval for consequential actions | Approval records reviewed, and the classification updated when the agent gains new tools |
    | [GR-AI-10](https://defra.github.io/architecture/guardrails/ai/#gr-ai-10) Keep an audit trail of what agents do | Audit records retained and reviewed, and used to investigate any problem |
    | [GR-AI-11](https://defra.github.io/architecture/guardrails/ai/#gr-ai-11) Defend agents against prompt injection | Prompt injection defences re-tested when inputs, tools or models change |
    | [GR-API-02](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-02) Describe APIs with open specifications | Specifications kept in step with every released change |
    | [GR-API-03](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-03) Follow government API standards | API design reviewed against the GDS API technical and data standards |
    | [GR-API-04](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-04) Version and deprecate deliberately | Deprecation notices sent to consumers and retirement dates published for old versions |
    | [GR-API-05](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-05) No integration through shared databases | Integrations reviewed when the service or its dependencies change |
    | [GR-API-08](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-08) Make APIs discoverable | Entry in the platform API catalogue |
    | [GR-TECH-03](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) Plan your exit before you enter | Exit plan reviewed at contract renewal, with switching cost estimated |
    | [GR-DATA-01](https://defra.github.io/architecture/guardrails/data/#gr-data-01) Every data set has an owner | Register entries and owners kept current |
    | [GR-DATA-02](https://defra.github.io/architecture/guardrails/data/#gr-data-02) Use authoritative sources | Copies and refresh arrangements reviewed when sources change |
    | [GR-DATA-05](https://defra.github.io/architecture/guardrails/data/#gr-data-05) Describe your data | Published metadata records in UK GEMINI or DCAT |
    | [GR-DATA-07](https://defra.github.io/architecture/guardrails/data/#gr-data-07) Open by default | Link to the published open data and its licence |
    | [GR-DATA-08](https://defra.github.io/architecture/guardrails/data/#gr-data-08) Manage data quality | Data quality measures and regular reports |
    | [GR-DATA-10](https://defra.github.io/architecture/guardrails/data/#gr-data-10) Handle research data safely | Research data handled the same way for ongoing research, and deletion checked |
    | [GR-DIG-03](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-03) Provide assisted digital and offline routes | Assisted digital and offline routes designed and tested with users who need them |
    | [GR-FIELD-02](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-02) Design field tools to work offline | Field journeys tested with no connection, including sync after reconnecting and conflict handling |
    | [GR-FIELD-03](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-03) Manage and secure every device | Device compliance monitored, and lost devices wiped |
    | [GR-FE-07](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-07) Tell users what is happening when things fail or are slow | Failure and delay content kept accurate as dependencies and processing times change |
    | [GR-HOST-02](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-02) Public cloud first | No on-premises hosting introduced |
    | [GR-HOST-03](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-03) Everything as code | Drift detection running, and no manual changes to production in the change history |
    | [GR-HOST-05](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-05) Consistent, disposable environments | Environments created from the same code, and how lower environments avoid real personal data |
    | [GR-HOST-06](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-06) Host data in the UK | Data location checked when new stores or services are added |
    | [GR-HOST-07](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-07) Design for the resilience the service needs | Recovery tested at least once a year, with the date of the last test |
    | [GR-OPS-01](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-01) Use the platform's observability tooling | Dashboards and alerts in use by the team that runs the service |
    | [GR-OPS-02](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-02) Log in a structured, safe way | Logging reviewed when new data or features are added |
    | [GR-OPS-03](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-03) Define and measure service levels | Agreed service level objectives with monitoring and alerts |
    | [GR-OPS-04](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-04) Health checks and graceful degradation | Health endpoints, timeout and retry settings, and a design for when dependencies fail |
    | [GR-OPS-06](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-06) Learn from incidents | Post-incident reviews and the actions taken |
    | [GR-OPS-07](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-07) Measure performance and cost | Published key performance indicators and cost tags on cloud resources |
    | [GR-OPEN-02](https://defra.github.io/architecture/guardrails/open-source/#gr-open-02) Licence clearly | LICENCE file in every new repository |
    | [GR-OPEN-03](https://defra.github.io/architecture/guardrails/open-source/#gr-open-03) Publish safely | Secret scanning alerts dealt with promptly |
    | [GR-OPEN-04](https://defra.github.io/architecture/guardrails/open-source/#gr-open-04) Reuse and contribute back | Reuse and upstream contributions noted in ADRs and pull requests |
    | [GR-PROD-01](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-01) Fund and run products, not projects | A named, long-lived team responsible for the product, with a roadmap beyond the current funding period |
    | [GR-PROD-02](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-02) Name the product owner and service owner | Named product owner and service owner, recorded in the service catalogue |
    | [GR-PROD-03](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-03) Contribute to platforms rather than working around them | Requests and contributions raised with platform teams, and ADRs where the team worked around a platform |
    | [GR-PROD-04](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-04) Plan for the end of a product's life | Product lifecycle stage recorded, with a retirement plan for products being replaced |
    | [GR-SEC-08](https://defra.github.io/architecture/guardrails/security/#gr-sec-08) Protect the supply chain | Software bill of materials kept current, and supplier assessments reviewed at renewal |
    | [GR-DEV-03](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-03) Protect the main branch | Branch protection still in place on every repository |
    | [GR-DEV-04](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-04) Continuous integration and delivery | Deployment history showing small, frequent, reversible releases |
    | [GR-DEV-05](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-05) Automated testing at the right levels | Test results from the pipeline at each level |
    | [GR-DEV-06](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-06) Manage dependencies actively | Dependency updates merged promptly and runtimes upgraded before they go out of support |
    | [GR-DEV-07](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-07) Follow shared coding standards | Linting and formatting checks in the pipeline |
    | [GR-DEV-08](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-08) Document as you go | README explaining what the service does and how to run, test and deploy it, with links to its ADRs |
    | [GR-DEV-09](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-09) Record significant decisions as ADRs | ADR log in the repository or linked from its README |
    | [GR-SUS-02](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-02) Right-size and switch off | Autoscaling and out-of-hours schedules for non-production environments |
    | [GR-SUS-04](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-04) Keep data and pages lean | Data retention settings and page weight measurements |

??? note "Could (2)"

    | Guardrail | What to show |
    | --- | --- |
    | [GR-OPEN-05](https://defra.github.io/architecture/guardrails/open-source/#gr-open-05) Blog and show the thing | Blog posts, show and tells or contributions to this site |
    | [GR-SUS-05](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-05) Measure and report | Carbon footprint reported alongside cost |

## Architecture artefacts

| Artefact | What to do in this phase |
| --- | --- |
| [Architecture decision record (ADR) log](https://defra.github.io/architecture/governance/architecture-decision-records/) ([template](https://defra.github.io/architecture/governance/templates/adr/)) | Keep recording decisions. Supersede ADRs rather than deleting them. |
| [C4 container diagram](https://c4model.com/) | Keep it current. |
| [Threat model](https://defra.github.io/architecture/security/threat-modelling/) ([template](https://defra.github.io/architecture/governance/templates/threat-model/)) | Review it at least once a year. |
| [Runbooks and support model](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05) | Test them and keep them current. |
| [Exit plan](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) | Review it at contract renewal. |

## Governance touchpoints

- Share your evidence pack with your solution design authority before the live assessment.
- Review exceptions before they expire - see [exceptions to guardrails](https://defra.github.io/architecture/governance/exceptions/).
- Treat significant changes as their own small delivery - see [significant change](https://defra.github.io/architecture/deliver/significant-change/).

## Evidence pack

Bring these together once and reuse them for your solution design authority, service assessment, spend control and security assurance:

- Architecture decision record (ADR) log
- C4 container diagram
- Threat model
- Runbooks and support model
- Exit plan
- evidence for each Must guardrail above (25)

Use the [live evidence checklist](https://defra.github.io/architecture/deliver/checklists/live/) to gather and print it.

For how the phase works and what assessors look for, see the GOV.UK Service Manual on [live](https://www.gov.uk/service-manual/agile-delivery/how-the-live-phase-works) and the [Defra Digital Service Manual](https://digital.defra.gov.uk/service-manual). This site covers the architecture evidence only.


