<!-- https://defra.github.io/architecture/deliver/roles/technical-architect/ | maturity: prototype | site version 0.3.0 | generated from deliver/roles/technical-architect.md -->

# Technical architect

<p class="lead">The guardrails a technical architect leads, what to show in each phase, the patterns that help and when to work with an architect.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



You shape the design so that it stays inside the guardrails, reuses what exists and can change safely. You lead decisions on hosting, integration and technology choices, and record them.

You lead **32 guardrails**, often with other roles. Leading means making sure the team meets them and can show it, not doing all the work. See them all in the <a href="../../../guardrails/library/#role=technical-architect">guardrail library, filtered to your role</a>.

## Your guardrails, phase by phase

### Discovery

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-02](https://defra.github.io/architecture/guardrails/ai/#gr-ai-02) Use approved AI services and tenancies | Must | Any AI services you are exploring identified, with the Defra tenancy or enterprise agreement they would run under |
| [GR-TECH-01](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-01) Look for something to reuse first | Must | Existing Defra and cross-government options for the need identified from the technology capability catalogue |
| [GR-TECH-04](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-04) Assess SaaS before you adopt it | Must | SaaS and third-party products under consideration listed, with the assessments they will need |
| [GR-HOST-01](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-01) Use Defra's strategic delivery platform by default | Must | Platform team engaged, and any hosting needs the Core Delivery Platform might not meet identified |
| [GR-IAM-01](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-01) Use the strategic customer identity services | Must | Identity team engaged about the level of identity assurance needed and how users act for organisations |
| [GR-AI-06](https://defra.github.io/architecture/guardrails/ai/#gr-ai-06) Talk to the TDA about novel use | Should | Novel or generative AI use in decision making identified, and a conversation with the Technical Design Authority booked |
| [GR-TECH-02](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-02) Buy commodity, build differentiating | Should | Buy or build options appraisal in the ADR or business case |
| [GR-FE-04](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-04) Consider forms platforms first | Should | ADR noting whether the forms capability was considered |
| [GR-DEV-09](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-09) Record significant decisions as ADRs | Should | ADR log in the repository or linked from its README |
| [GR-SUS-01](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-01) Consider sustainability in design decisions | Should | Environmental impact recorded in ADRs for hosting and technology choices |
| [GR-FIELD-04](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-04) Check connectivity before you design | Could | Connectivity in the places the service will be used checked, and the approach recorded |

More on the [discovery page](https://defra.github.io/architecture/deliver/discovery/).

### Alpha

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-02](https://defra.github.io/architecture/guardrails/ai/#gr-ai-02) Use approved AI services and tenancies | Must | AI services chosen for the design, each confirmed as running in a Defra tenancy or under an approved agreement |
| [GR-TECH-01](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-01) Look for something to reuse first | Must | ADR recording the reuse options considered and why they did or did not fit |
| [GR-TECH-04](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-04) Assess SaaS before you adopt it | Must | Security, data protection, data location, accessibility and single sign-on assessed before contract |
| [GR-HOST-01](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-01) Use Defra's strategic delivery platform by default | Must | The design runs on the Core Delivery Platform, or an exception has been requested |
| [GR-IAM-01](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-01) Use the strategic customer identity services | Must | Sign-in designed with Defra Customer Identity, and tested with users |
| [GR-AI-06](https://defra.github.io/architecture/guardrails/ai/#gr-ai-06) Talk to the TDA about novel use | Should | Technical Design Authority review outcome recorded in the ADR |
| [GR-AI-08](https://defra.github.io/architecture/guardrails/ai/#gr-ai-08) Give agents the least privilege they need | Should | Each agent's tools and permissions listed in the design, with a workload identity for the agent |
| [GR-AI-09](https://defra.github.io/architecture/guardrails/ai/#gr-ai-09) Get human approval for consequential actions | Should | Agent actions classified, and the actions that need human approval identified in the design |
| [GR-API-01](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-01) API first | Should | API specification written before or alongside the user interface |
| [GR-API-03](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-03) Follow government API standards | Should | API design reviewed against the GDS API technical and data standards |
| [GR-API-05](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-05) No integration through shared databases | Should | Container diagram showing integration only through APIs, events or governed data products |
| [GR-API-06](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-06) Use events for change notifications | Should | Event and message definitions described in AsyncAPI |
| [GR-TECH-02](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-02) Buy commodity, build differentiating | Should | Buy or build options appraisal in the ADR or business case |
| [GR-TECH-03](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) Plan your exit before you enter | Should | Draft exit plan for each new product, platform or significant supplier |
| [GR-TECH-05](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-05) Prefer open standards and portable technology | Should | ADR noting the open standards used and how portable the choice is |
| [GR-FE-04](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-04) Consider forms platforms first | Should | ADR noting whether the forms capability was considered |
| [GR-HOST-02](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-02) Public cloud first | Should | Where the platform cannot be used, the hosting design uses a Defra-managed public cloud tenancy |
| [GR-HOST-04](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-04) Use managed services before self-managed | Should | Hosting design listing the managed services used |
| [GR-HOST-06](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-06) Host data in the UK | Should | Hosting design places every data store and backup in UK regions |
| [GR-HOST-07](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-07) Design for the resilience the service needs | Should | Recovery time and recovery point objectives agreed with the service owner, and a design that meets them |
| [GR-IAM-04](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-04) Separate authentication from authorisation | Should | Authorisation rules written down and covered by automated tests |
| [GR-PROD-03](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-03) Contribute to platforms rather than working around them | Should | Requests and contributions raised with platform teams, and ADRs where the team worked around a platform |
| [GR-DEV-01](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-01) Use the supported languages and frameworks | Should | ADR recording the reason wherever the service uses a different stack |
| [GR-DEV-09](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-09) Record significant decisions as ADRs | Should | ADR log in the repository or linked from its README |
| [GR-SUS-01](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-01) Consider sustainability in design decisions | Should | Environmental impact recorded in ADRs for hosting and technology choices |
| [GR-FIELD-04](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-04) Check connectivity before you design | Could | Connectivity in the places the service will be used checked, and the approach recorded |
| [GR-SUS-03](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-03) Choose lower-carbon regions and services | Could | Region and service choice recorded with its carbon intensity |

More on the [alpha page](https://defra.github.io/architecture/deliver/alpha/).

### Beta

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-02](https://defra.github.io/architecture/guardrails/ai/#gr-ai-02) Use approved AI services and tenancies | Must | The AI services in the built service run only in approved tenancies, shown in the hosting design and configuration |
| [GR-HOST-01](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-01) Use Defra's strategic delivery platform by default | Must | The service runs on the Core Delivery Platform, or under an approved exception |
| [GR-IAM-01](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-01) Use the strategic customer identity services | Must | Integration with Defra Customer Identity built and tested |
| [GR-IAM-02](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-02) Staff sign in with Microsoft Entra ID | Must | Staff sign in through Microsoft Entra ID with multi-factor authentication, and there are no local staff accounts |
| [GR-AI-08](https://defra.github.io/architecture/guardrails/ai/#gr-ai-08) Give agents the least privilege they need | Should | Agent permissions configured as designed and tested, including that the agent cannot reach tools it should not |
| [GR-AI-09](https://defra.github.io/architecture/guardrails/ai/#gr-ai-09) Get human approval for consequential actions | Should | Approval enforced in the tool layer, with tests showing the agent cannot act without it |
| [GR-API-01](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-01) API first | Should | API specification written before or alongside the user interface |
| [GR-API-03](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-03) Follow government API standards | Should | API design reviewed against the GDS API technical and data standards |
| [GR-API-04](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-04) Version and deprecate deliberately | Should | Versioning approach published for each API and event |
| [GR-API-05](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-05) No integration through shared databases | Should | Built integrations match the container diagram, with no access to another service's database |
| [GR-API-06](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-06) Use events for change notifications | Should | Event and message definitions described in AsyncAPI |
| [GR-API-08](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-08) Make APIs discoverable | Should | Entry in the platform API catalogue |
| [GR-TECH-03](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) Plan your exit before you enter | Should | Exit plan agreed, with contracts giving Defra its data and the right to export it in open formats |
| [GR-HOST-02](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-02) Public cloud first | Should | The service runs in a Defra-managed public cloud tenancy |
| [GR-HOST-04](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-04) Use managed services before self-managed | Should | Hosting design listing the managed services used |
| [GR-HOST-06](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-06) Host data in the UK | Should | Data location confirmed for every data store and backup as built |
| [GR-HOST-07](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-07) Design for the resilience the service needs | Should | Multi-zone design built, and recovery tested before go-live |
| [GR-IAM-04](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-04) Separate authentication from authorisation | Should | Authorisation rules written down and covered by automated tests |
| [GR-OPS-03](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-03) Define and measure service levels | Should | Agreed service level objectives with monitoring and alerts |
| [GR-PROD-03](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-03) Contribute to platforms rather than working around them | Should | Requests and contributions raised with platform teams, and ADRs where the team worked around a platform |
| [GR-DEV-09](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-09) Record significant decisions as ADRs | Should | ADR log in the repository or linked from its README |

More on the [beta page](https://defra.github.io/architecture/deliver/beta/).

### Live

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-02](https://defra.github.io/architecture/guardrails/ai/#gr-ai-02) Use approved AI services and tenancies | Must | List of AI services in use, reviewed when services or agreements change |
| [GR-HOST-01](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-01) Use Defra's strategic delivery platform by default | Must | The service still runs on the platform, and any exception is reviewed before it expires |
| [GR-IAM-01](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-01) Use the strategic customer identity services | Must | No other sign-in introduced |
| [GR-IAM-02](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-02) Staff sign in with Microsoft Entra ID | Must | Staff access reviewed regularly through Entra ID groups |
| [GR-AI-08](https://defra.github.io/architecture/guardrails/ai/#gr-ai-08) Give agents the least privilege they need | Should | Agent permissions reviewed regularly, as for a privileged user |
| [GR-AI-09](https://defra.github.io/architecture/guardrails/ai/#gr-ai-09) Get human approval for consequential actions | Should | Approval records reviewed, and the classification updated when the agent gains new tools |
| [GR-API-03](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-03) Follow government API standards | Should | API design reviewed against the GDS API technical and data standards |
| [GR-API-04](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-04) Version and deprecate deliberately | Should | Deprecation notices sent to consumers and retirement dates published for old versions |
| [GR-API-05](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-05) No integration through shared databases | Should | Integrations reviewed when the service or its dependencies change |
| [GR-API-08](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-08) Make APIs discoverable | Should | Entry in the platform API catalogue |
| [GR-TECH-03](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) Plan your exit before you enter | Should | Exit plan reviewed at contract renewal, with switching cost estimated |
| [GR-HOST-02](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-02) Public cloud first | Should | No on-premises hosting introduced |
| [GR-HOST-06](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-06) Host data in the UK | Should | Data location checked when new stores or services are added |
| [GR-HOST-07](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-07) Design for the resilience the service needs | Should | Recovery tested at least once a year, with the date of the last test |
| [GR-OPS-03](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-03) Define and measure service levels | Should | Agreed service level objectives with monitoring and alerts |
| [GR-PROD-03](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-03) Contribute to platforms rather than working around them | Should | Requests and contributions raised with platform teams, and ADRs where the team worked around a platform |
| [GR-DEV-09](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-09) Record significant decisions as ADRs | Should | ADR log in the repository or linked from its README |
| [GR-SUS-05](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-05) Measure and report | Could | Carbon footprint reported alongside cost |

More on the [live page](https://defra.github.io/architecture/deliver/live/).

### Significant change

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-TECH-01](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-01) Look for something to reuse first | Must | ADR showing reuse options considered for any new component |
| [GR-API-04](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-04) Version and deprecate deliberately | Should | Consumers told about breaking changes in advance, with a new version and a retirement date for the old one |
| [GR-DEV-09](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-09) Record significant decisions as ADRs | Should | ADR log in the repository or linked from its README |
| [GR-TECH-03](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) Plan your exit before you enter | Should | Exit plan updated for any new product or supplier |
| [GR-AI-06](https://defra.github.io/architecture/guardrails/ai/#gr-ai-06) Talk to the TDA about novel use | Should | Technical Design Authority review of any new AI use introduced by the change |
| [GR-HOST-07](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-07) Design for the resilience the service needs | Should | Recovery objectives and design checked for the change |

More on the [significant change page](https://defra.github.io/architecture/deliver/significant-change/).

### Retire a service

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-API-04](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-04) Version and deprecate deliberately | Should | Consumers told the retirement date in advance, and moved to a replacement |
| [GR-TECH-03](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) Plan your exit before you enter | Should | Exit plan carried out - data exported in open formats and contracts ended |

More on the [retire a service page](https://defra.github.io/architecture/deliver/retire/).

## Patterns that help

- [Acting on behalf of an organisation or holding](https://defra.github.io/architecture/patterns/acting-on-behalf/) - Users act for a business, a land holding or another person, and the service must check they are allowed to.
- [Asynchronous submission with an outbox](https://defra.github.io/architecture/patterns/async-submission/) - A user submits something that other systems must process, and you do not want those systems' availability to block the user.
- [Reading from an authoritative source](https://defra.github.io/architecture/patterns/authoritative-source/) - A service needs shared data - customers, organisations, holdings, locations or species - that another part of Defra owns.
- [File upload with malware scanning](https://defra.github.io/architecture/patterns/file-upload/) - Users upload documents or images, and the files must be scanned and stored safely before anyone opens them.

## Working with architects

- Take novel or cross-cutting designs to the [Technical Design Authority](https://defra.github.io/architecture/governance/tda/).
- Keep the ADR log and C4 diagrams current through every phase.



