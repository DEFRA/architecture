<!-- https://defra.github.io/architecture/deliver/roles/developer/ | maturity: prototype | site version 0.3.0 | generated from deliver/roles/developer.md -->

# Developer

<p class="lead">The guardrails a developer leads, what to show in each phase, the patterns that help and when to work with an architect.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



You build and run the service. Most technical guardrails are yours day to day - code, pipelines, testing, logging, secrets and dependencies.

You lead **41 guardrails**, often with other roles. Leading means making sure the team meets them and can show it, not doing all the work. See them all in the <a href="../../../guardrails/library/#role=developer">guardrail library, filtered to your role</a>.

## Your guardrails, phase by phase

### Discovery

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-DATA-11](https://defra.github.io/architecture/guardrails/data/#gr-data-11) No real personal data in prototypes | Should | Any prototype uses made-up data |

More on the [discovery page](https://defra.github.io/architecture/deliver/discovery/).

### Alpha

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-API-07](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-07) Secure every API | Must | Authentication, authorisation, input validation and rate limiting designed for each API |
| [GR-FE-01](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-01) Meet WCAG 2.2 AA | Must | Prototypes built with accessible components, and a plan for an accessibility audit and assistive technology testing |
| [GR-FE-02](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-02) Use the GOV.UK Design System | Must | Prototypes built with the GOV.UK Design System, with departures recorded and researched |
| [GR-IAM-05](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-05) No secrets in code | Must | Secret scanning on from the first commit, and secrets held in a managed store from the start |
| [GR-OPEN-01](https://defra.github.io/architecture/guardrails/open-source/#gr-open-01) Code in the open | Must | Code public in a Defra GitHub organisation from the first commit, or a recorded reason for keeping a repository private |
| [GR-SEC-02](https://defra.github.io/architecture/guardrails/security/#gr-sec-02) Keep a current threat model | Must | First threat model, created by the team |
| [GR-DEV-02](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-02) All code in Defra source control | Must | All code, including prototypes and infrastructure code written by suppliers, in a Defra-owned GitHub organisation from the first commit |
| [GR-AI-07](https://defra.github.io/architecture/guardrails/ai/#gr-ai-07) Suppliers use AI coding assistants openly and safely | Should | Supplier's agreed list of AI coding assistants and how each runs within Defra-approved terms, the review process for generated code, and disclosure in pull requests or delivery reports |
| [GR-AI-11](https://defra.github.io/architecture/guardrails/ai/#gr-ai-11) Defend agents against prompt injection | Should | Threat model covering prompt injection through every input the agent reads |
| [GR-API-02](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-02) Describe APIs with open specifications | Should | Draft OpenAPI 3 or AsyncAPI documents for the interfaces you are prototyping |
| [GR-API-03](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-03) Follow government API standards | Should | API design reviewed against the GDS API technical and data standards |
| [GR-API-06](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-06) Use events for change notifications | Should | Event and message definitions described in AsyncAPI |
| [GR-DATA-11](https://defra.github.io/architecture/guardrails/data/#gr-data-11) No real personal data in prototypes | Should | Prototypes and research materials use made-up data, including data a participant types in during a session |
| [GR-FIELD-02](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-02) Design field tools to work offline | Should | Field journeys tested with no connection, including sync after reconnecting and conflict handling |
| [GR-FE-03](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-03) Progressive enhancement | Should | Core journeys tested with JavaScript turned off |
| [GR-FE-07](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-07) Tell users what is happening when things fail or are slow | Should | Each dependency that can fail or be slow identified with the developers, and what users see in each case designed and tested in the prototype |
| [GR-HOST-04](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-04) Use managed services before self-managed | Should | Hosting design listing the managed services used |
| [GR-HOST-05](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-05) Consistent, disposable environments | Should | Environments created from the same code, and how lower environments avoid real personal data |
| [GR-IAM-04](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-04) Separate authentication from authorisation | Should | Authorisation rules written down and covered by automated tests |
| [GR-OPEN-02](https://defra.github.io/architecture/guardrails/open-source/#gr-open-02) Licence clearly | Should | LICENCE file in every repository from the start |
| [GR-OPEN-03](https://defra.github.io/architecture/guardrails/open-source/#gr-open-03) Publish safely | Should | Secret scanning and push protection on for every repository from the first commit |
| [GR-OPEN-04](https://defra.github.io/architecture/guardrails/open-source/#gr-open-04) Reuse and contribute back | Should | Reuse and upstream contributions noted in ADRs and pull requests |
| [GR-SEC-08](https://defra.github.io/architecture/guardrails/security/#gr-sec-08) Protect the supply chain | Should | Security assessment of suppliers and third-party products in the design |
| [GR-DEV-01](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-01) Use the supported languages and frameworks | Should | ADR recording the reason wherever the service uses a different stack |
| [GR-DEV-03](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-03) Protect the main branch | Should | Main branch protected from the start, with changes through reviewed pull requests |
| [GR-DEV-05](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-05) Automated testing at the right levels | Should | Test results from the pipeline at each level |
| [GR-DEV-07](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-07) Follow shared coding standards | Should | Linting and formatting checks in the pipeline |
| [GR-DEV-08](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-08) Document as you go | Should | README explaining what the service does and how to run, test and deploy it, with links to its ADRs |
| [GR-SUS-04](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-04) Keep data and pages lean | Should | Data retention settings and page weight measurements |

More on the [alpha page](https://defra.github.io/architecture/deliver/alpha/).

### Beta

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-API-07](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-07) Secure every API | Must | These controls built and covered by security testing |
| [GR-FE-01](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-01) Meet WCAG 2.2 AA | Must | Accessibility audit and assistive technology testing completed, issues fixed, and an accessibility statement published |
| [GR-FE-02](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-02) Use the GOV.UK Design System | Must | The service uses GOV.UK Frontend, with design decisions recording any departures |
| [GR-IAM-03](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-03) Authorise on least privilege | Must | Role and group model built, with users, services and pipelines given only the permissions they need |
| [GR-IAM-05](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-05) No secrets in code | Must | All secrets in a managed store with rotation, using workload identity where possible |
| [GR-OPEN-01](https://defra.github.io/architecture/guardrails/open-source/#gr-open-01) Code in the open | Must | Repositories public, or the reasons for keeping them private reviewed |
| [GR-SEC-02](https://defra.github.io/architecture/guardrails/security/#gr-sec-02) Keep a current threat model | Must | Threat model updated as controls are built and tested |
| [GR-SEC-04](https://defra.github.io/architecture/guardrails/security/#gr-sec-04) Encrypt in transit and at rest | Must | TLS 1.2 or higher for all traffic and encryption at rest for every data store, confirmed as built |
| [GR-SEC-05](https://defra.github.io/architecture/guardrails/security/#gr-sec-05) Scan continuously and fix quickly | Must | Static analysis, dependency, container and infrastructure scanning running in the pipeline |
| [GR-SEC-07](https://defra.github.io/architecture/guardrails/security/#gr-sec-07) Log for detection and response | Must | Authentication, authorisation failures, administrative actions and data exports sent to the security operations centre, and tested |
| [GR-DEV-02](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-02) All code in Defra source control | Must | All source, infrastructure and pipeline code in the Defra GitHub organisation, with nothing held only by a supplier |
| [GR-AI-07](https://defra.github.io/architecture/guardrails/ai/#gr-ai-07) Suppliers use AI coding assistants openly and safely | Should | Supplier's agreed list of AI coding assistants and how each runs within Defra-approved terms, the review process for generated code, and disclosure in pull requests or delivery reports |
| [GR-AI-10](https://defra.github.io/architecture/guardrails/ai/#gr-ai-10) Keep an audit trail of what agents do | Should | Audit records of agent inputs, tool calls, approvals and outcomes produced and sent to security monitoring |
| [GR-AI-11](https://defra.github.io/architecture/guardrails/ai/#gr-ai-11) Defend agents against prompt injection | Should | Prompt injection mitigations tested, including attempts to misuse tools and leak data |
| [GR-API-02](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-02) Describe APIs with open specifications | Should | OpenAPI 3 or AsyncAPI documents in the repository, checked in the pipeline against the running API |
| [GR-API-03](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-03) Follow government API standards | Should | API design reviewed against the GDS API technical and data standards |
| [GR-API-06](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-06) Use events for change notifications | Should | Event and message definitions described in AsyncAPI |
| [GR-DATA-11](https://defra.github.io/architecture/guardrails/data/#gr-data-11) No real personal data in prototypes | Should | Test and research environments use synthetic or anonymised data; any exception agreed through a DPIA |
| [GR-FIELD-02](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-02) Design field tools to work offline | Should | Field journeys tested with no connection, including sync after reconnecting and conflict handling |
| [GR-FE-03](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-03) Progressive enhancement | Should | Core journeys tested with JavaScript turned off |
| [GR-FE-07](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-07) Tell users what is happening when things fail or are slow | Should | The front end shows the designed content when a dependency fails or is slow, tested by switching dependencies off |
| [GR-HOST-03](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-03) Everything as code | Should | Infrastructure, configuration and pipelines defined as code in the repository, with no manual changes to production |
| [GR-HOST-04](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-04) Use managed services before self-managed | Should | Hosting design listing the managed services used |
| [GR-HOST-05](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-05) Consistent, disposable environments | Should | Environments created from the same code, and how lower environments avoid real personal data |
| [GR-IAM-04](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-04) Separate authentication from authorisation | Should | Authorisation rules written down and covered by automated tests |
| [GR-OPS-01](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-01) Use the platform's observability tooling | Should | Logs, metrics and traces reaching the platform's observability tooling, and security events reaching the security operations centre |
| [GR-OPS-02](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-02) Log in a structured, safe way | Should | Structured logs with correlation identifiers, tested to show no secrets or unnecessary personal data are logged |
| [GR-OPS-04](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-04) Health checks and graceful degradation | Should | Health endpoints, timeout and retry settings, and a design for when dependencies fail |
| [GR-OPEN-02](https://defra.github.io/architecture/guardrails/open-source/#gr-open-02) Licence clearly | Should | LICENCE file with the Open Government Licence or MIT licence in every repository |
| [GR-OPEN-03](https://defra.github.io/architecture/guardrails/open-source/#gr-open-03) Publish safely | Should | Secret scanning and push protection on for every repository |
| [GR-OPEN-04](https://defra.github.io/architecture/guardrails/open-source/#gr-open-04) Reuse and contribute back | Should | Reuse and upstream contributions noted in ADRs and pull requests |
| [GR-SEC-08](https://defra.github.io/architecture/guardrails/security/#gr-sec-08) Protect the supply chain | Should | Dependencies pinned and verified, and a software bill of materials produced in the pipeline |
| [GR-DEV-03](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-03) Protect the main branch | Should | Branch protection requiring at least one review and passing checks |
| [GR-DEV-04](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-04) Continuous integration and delivery | Should | Every change built, tested, scanned and deployed by an automated pipeline, with rollback tested |
| [GR-DEV-05](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-05) Automated testing at the right levels | Should | Test results from the pipeline at each level |
| [GR-DEV-06](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-06) Manage dependencies actively | Should | Dependabot or Renovate configured, software composition analysis in the pipeline, and runtimes on supported versions |
| [GR-DEV-07](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-07) Follow shared coding standards | Should | Linting and formatting checks in the pipeline |
| [GR-DEV-08](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-08) Document as you go | Should | README explaining what the service does and how to run, test and deploy it, with links to its ADRs |
| [GR-SUS-02](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-02) Right-size and switch off | Should | Autoscaling and out-of-hours schedules for non-production environments |
| [GR-SUS-04](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-04) Keep data and pages lean | Should | Data retention settings and page weight measurements |

More on the [beta page](https://defra.github.io/architecture/deliver/beta/).

### Live

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-API-07](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-07) Secure every API | Must | API access reviewed, and controls re-tested after significant change |
| [GR-FE-01](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-01) Meet WCAG 2.2 AA | Must | Accessibility statement kept current, and accessibility re-tested after significant change |
| [GR-FE-02](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-02) Use the GOV.UK Design System | Must | GOV.UK Frontend kept up to date |
| [GR-IAM-03](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-03) Authorise on least privilege | Must | Record of regular access reviews |
| [GR-IAM-05](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-05) No secrets in code | Must | Secrets rotated, and secret scanning alerts dealt with |
| [GR-OPEN-01](https://defra.github.io/architecture/guardrails/open-source/#gr-open-01) Code in the open | Must | Repositories still public, or private for a recorded reason |
| [GR-SEC-02](https://defra.github.io/architecture/guardrails/security/#gr-sec-02) Keep a current threat model | Must | Threat model reviewed at least once a year, with the date of the last review |
| [GR-SEC-04](https://defra.github.io/architecture/guardrails/security/#gr-sec-04) Encrypt in transit and at rest | Must | Encryption settings checked when new stores or connections are added |
| [GR-SEC-05](https://defra.github.io/architecture/guardrails/security/#gr-sec-05) Scan continuously and fix quickly | Must | Time taken to fix critical and high vulnerabilities, within 14 and 30 days, or a recorded risk decision |
| [GR-SEC-07](https://defra.github.io/architecture/guardrails/security/#gr-sec-07) Log for detection and response | Must | Security events reviewed and alerts acted on |
| [GR-DEV-02](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-02) All code in Defra source control | Must | All changes made in the Defra GitHub organisation |
| [GR-AI-07](https://defra.github.io/architecture/guardrails/ai/#gr-ai-07) Suppliers use AI coding assistants openly and safely | Should | Supplier's agreed list of AI coding assistants and how each runs within Defra-approved terms, the review process for generated code, and disclosure in pull requests or delivery reports |
| [GR-AI-10](https://defra.github.io/architecture/guardrails/ai/#gr-ai-10) Keep an audit trail of what agents do | Should | Audit records retained and reviewed, and used to investigate any problem |
| [GR-AI-11](https://defra.github.io/architecture/guardrails/ai/#gr-ai-11) Defend agents against prompt injection | Should | Prompt injection defences re-tested when inputs, tools or models change |
| [GR-API-02](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-02) Describe APIs with open specifications | Should | Specifications kept in step with every released change |
| [GR-API-03](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-03) Follow government API standards | Should | API design reviewed against the GDS API technical and data standards |
| [GR-FIELD-02](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-02) Design field tools to work offline | Should | Field journeys tested with no connection, including sync after reconnecting and conflict handling |
| [GR-FE-07](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-07) Tell users what is happening when things fail or are slow | Should | Failure and delay content kept accurate as dependencies and processing times change |
| [GR-HOST-03](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-03) Everything as code | Should | Drift detection running, and no manual changes to production in the change history |
| [GR-HOST-05](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-05) Consistent, disposable environments | Should | Environments created from the same code, and how lower environments avoid real personal data |
| [GR-OPS-01](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-01) Use the platform's observability tooling | Should | Dashboards and alerts in use by the team that runs the service |
| [GR-OPS-02](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-02) Log in a structured, safe way | Should | Logging reviewed when new data or features are added |
| [GR-OPS-04](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-04) Health checks and graceful degradation | Should | Health endpoints, timeout and retry settings, and a design for when dependencies fail |
| [GR-OPEN-02](https://defra.github.io/architecture/guardrails/open-source/#gr-open-02) Licence clearly | Should | LICENCE file in every new repository |
| [GR-OPEN-03](https://defra.github.io/architecture/guardrails/open-source/#gr-open-03) Publish safely | Should | Secret scanning alerts dealt with promptly |
| [GR-OPEN-04](https://defra.github.io/architecture/guardrails/open-source/#gr-open-04) Reuse and contribute back | Should | Reuse and upstream contributions noted in ADRs and pull requests |
| [GR-SEC-08](https://defra.github.io/architecture/guardrails/security/#gr-sec-08) Protect the supply chain | Should | Software bill of materials kept current, and supplier assessments reviewed at renewal |
| [GR-DEV-03](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-03) Protect the main branch | Should | Branch protection still in place on every repository |
| [GR-DEV-04](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-04) Continuous integration and delivery | Should | Deployment history showing small, frequent, reversible releases |
| [GR-DEV-05](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-05) Automated testing at the right levels | Should | Test results from the pipeline at each level |
| [GR-DEV-06](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-06) Manage dependencies actively | Should | Dependency updates merged promptly and runtimes upgraded before they go out of support |
| [GR-DEV-07](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-07) Follow shared coding standards | Should | Linting and formatting checks in the pipeline |
| [GR-DEV-08](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-08) Document as you go | Should | README explaining what the service does and how to run, test and deploy it, with links to its ADRs |
| [GR-SUS-02](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-02) Right-size and switch off | Should | Autoscaling and out-of-hours schedules for non-production environments |
| [GR-SUS-04](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-04) Keep data and pages lean | Should | Data retention settings and page weight measurements |

More on the [live page](https://defra.github.io/architecture/deliver/live/).

### Significant change

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-SEC-02](https://defra.github.io/architecture/guardrails/security/#gr-sec-02) Keep a current threat model | Must | Threat model revisited for the change before it is built |

More on the [significant change page](https://defra.github.io/architecture/deliver/significant-change/).

### Retire a service

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-IAM-03](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-03) Authorise on least privilege | Must | All access to the service's systems and data removed |
| [GR-IAM-05](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-05) No secrets in code | Must | Secrets, keys and credentials revoked |
| [GR-OPEN-01](https://defra.github.io/architecture/guardrails/open-source/#gr-open-01) Code in the open | Must | Repositories archived, not deleted, so the code and decisions stay available |
| [GR-SUS-02](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-02) Right-size and switch off | Should | Autoscaling and out-of-hours schedules for non-production environments |

More on the [retire a service page](https://defra.github.io/architecture/deliver/retire/).

## Patterns that help

- [Acting on behalf of an organisation or holding](https://defra.github.io/architecture/patterns/acting-on-behalf/) - Users act for a business, a land holding or another person, and the service must check they are allowed to.
- [Asynchronous submission with an outbox](https://defra.github.io/architecture/patterns/async-submission/) - A user submits something that other systems must process, and you do not want those systems' availability to block the user.
- [Reading from an authoritative source](https://defra.github.io/architecture/patterns/authoritative-source/) - A service needs shared data - customers, organisations, holdings, locations or species - that another part of Defra owns.
- [File upload with malware scanning](https://defra.github.io/architecture/patterns/file-upload/) - Users upload documents or images, and the files must be scanned and stored safely before anyone opens them.

## Working with architects

- Add the [guardrail check](https://defra.github.io/architecture/deliver/guardrail-check/) to your repository on day one.
- Raise anything that would need an exception early, with an ADR.



