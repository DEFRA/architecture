<!-- https://defra.github.io/architecture/deliver/alpha/ | maturity: prototype | site version 0.3.0 | generated from deliver/alpha.md -->

# Alpha

<p class="lead">Alpha is where you test the riskiest design assumptions. Most of the architecture decisions that are expensive to reverse are made here, so this is the phase that needs the most architecture attention.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



## What it means for architecture

- Try out options for hosting, identity, integration and data, starting from the strategic options in the [handrail](https://defra.github.io/architecture/handrail/).
- Start from a [service pattern](https://defra.github.io/architecture/patterns/service/) where one fits.
- Run your first threat model with the whole team.
- Agree your service tier and non-functional requirements, so beta has targets to build and test against.

## Guardrails that apply

These guardrails apply in alpha, taken from each guardrail's metadata. Meet every Must, or have an approved [exception](https://defra.github.io/architecture/governance/exceptions/). Depart from a Should only with a recorded reason.

### Must (18)

| Guardrail | What to show |
| --- | --- |
| [GR-AI-02](https://defra.github.io/architecture/guardrails/ai/#gr-ai-02) Use approved AI services and tenancies | AI services chosen for the design, each confirmed as running in a Defra tenancy or under an approved agreement |
| [GR-AI-03](https://defra.github.io/architecture/guardrails/ai/#gr-ai-03) Keep a human accountable | Design of the human oversight and challenge route for decisions with significant effects, tested with users in prototypes |
| [GR-API-07](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-07) Secure every API | Authentication, authorisation, input validation and rate limiting designed for each API |
| [GR-TECH-01](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-01) Look for something to reuse first | ADR recording the reuse options considered and why they did or did not fit |
| [GR-TECH-04](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-04) Assess SaaS before you adopt it | Security, data protection, data location, accessibility and single sign-on assessed before contract |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | Draft DPIA, with data minimisation and retention designed in |
| [GR-FE-01](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-01) Meet WCAG 2.2 AA | Prototypes built with accessible components, and a plan for an accessibility audit and assistive technology testing |
| [GR-FE-02](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-02) Use the GOV.UK Design System | Prototypes built with the GOV.UK Design System, with departures recorded and researched |
| [GR-FE-06](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-06) Support Welsh where required | Whether the Welsh Language Standards apply decided, and the service designed for translation |
| [GR-HOST-01](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-01) Use Defra's strategic delivery platform by default | The design runs on the Core Delivery Platform, or an exception has been requested |
| [GR-IAM-01](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-01) Use the strategic customer identity services | Sign-in designed with Defra Customer Identity, and tested with users |
| [GR-IAM-05](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-05) No secrets in code | Secret scanning on from the first commit, and secrets held in a managed store from the start |
| [GR-OPEN-01](https://defra.github.io/architecture/guardrails/open-source/#gr-open-01) Code in the open | Code public in a Defra GitHub organisation from the first commit, or a recorded reason for keeping a repository private |
| [GR-SEC-01](https://defra.github.io/architecture/guardrails/security/#gr-sec-01) Follow Secure by Design | Secure by Design activities for alpha completed, including security requirements in the backlog |
| [GR-SEC-02](https://defra.github.io/architecture/guardrails/security/#gr-sec-02) Keep a current threat model | First threat model, created by the team |
| [GR-SEC-03](https://defra.github.io/architecture/guardrails/security/#gr-sec-03) Classify information | Controls in the design that match the classification |
| [GR-SEC-09](https://defra.github.io/architecture/guardrails/security/#gr-sec-09) Manage risk explicitly | Risks from controls that cannot be met recorded, with an owner |
| [GR-DEV-02](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-02) All code in Defra source control | All code, including prototypes and infrastructure code written by suppliers, in a Defra-owned GitHub organisation from the first commit |

??? note "Should (52)"

    | Guardrail | What to show |
    | --- | --- |
    | [GR-AI-01](https://defra.github.io/architecture/guardrails/ai/#gr-ai-01) Consider AI first | ADR recording the AI options considered and why they were or were not used |
    | [GR-AI-05](https://defra.github.io/architecture/guardrails/ai/#gr-ai-05) Evaluate, monitor and threat model | Evaluation plan for accuracy, bias and safety, and AI-specific threats in the threat model |
    | [GR-AI-06](https://defra.github.io/architecture/guardrails/ai/#gr-ai-06) Talk to the TDA about novel use | Technical Design Authority review outcome recorded in the ADR |
    | [GR-AI-07](https://defra.github.io/architecture/guardrails/ai/#gr-ai-07) Suppliers use AI coding assistants openly and safely | Supplier's agreed list of AI coding assistants and how each runs within Defra-approved terms, the review process for generated code, and disclosure in pull requests or delivery reports |
    | [GR-AI-08](https://defra.github.io/architecture/guardrails/ai/#gr-ai-08) Give agents the least privilege they need | Each agent's tools and permissions listed in the design, with a workload identity for the agent |
    | [GR-AI-09](https://defra.github.io/architecture/guardrails/ai/#gr-ai-09) Get human approval for consequential actions | Agent actions classified, and the actions that need human approval identified in the design |
    | [GR-AI-11](https://defra.github.io/architecture/guardrails/ai/#gr-ai-11) Defend agents against prompt injection | Threat model covering prompt injection through every input the agent reads |
    | [GR-API-01](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-01) API first | API specification written before or alongside the user interface |
    | [GR-API-02](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-02) Describe APIs with open specifications | Draft OpenAPI 3 or AsyncAPI documents for the interfaces you are prototyping |
    | [GR-API-03](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-03) Follow government API standards | API design reviewed against the GDS API technical and data standards |
    | [GR-API-05](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-05) No integration through shared databases | Container diagram showing integration only through APIs, events or governed data products |
    | [GR-API-06](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-06) Use events for change notifications | Event and message definitions described in AsyncAPI |
    | [GR-TECH-02](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-02) Buy commodity, build differentiating | Buy or build options appraisal in the ADR or business case |
    | [GR-TECH-03](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) Plan your exit before you enter | Draft exit plan for each new product, platform or significant supplier |
    | [GR-TECH-05](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-05) Prefer open standards and portable technology | ADR noting the open standards used and how portable the choice is |
    | [GR-DATA-01](https://defra.github.io/architecture/guardrails/data/#gr-data-01) Every data set has an owner | Each data set the service will create or hold identified, with a proposed information asset owner |
    | [GR-DATA-02](https://defra.github.io/architecture/guardrails/data/#gr-data-02) Use authoritative sources | Data flow diagram naming the authoritative source for each shared entity, and how any copies are refreshed |
    | [GR-DATA-03](https://defra.github.io/architecture/guardrails/data/#gr-data-03) Use agreed data standards and identifiers | Data model using the agreed data standards and identifiers |
    | [GR-DATA-04](https://defra.github.io/architecture/guardrails/data/#gr-data-04) Collect once, share safely | Journey design showing users are not asked for information Defra already holds, and data sharing agreements where required |
    | [GR-DATA-10](https://defra.github.io/architecture/guardrails/data/#gr-data-10) Handle research data safely | The same for alpha research, with DPIA screening done for the research and any new research tool assessed |
    | [GR-DATA-11](https://defra.github.io/architecture/guardrails/data/#gr-data-11) No real personal data in prototypes | Prototypes and research materials use made-up data, including data a participant types in during a session |
    | [GR-DIG-01](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-01) Challenge paper and manual processes | Discovery findings showing paper, email and manual steps in the current process and how the new design removes or justifies each one |
    | [GR-DIG-02](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-02) Design across organisational boundaries | A map of the whole service, including the parts other teams and organisations deliver, and agreed hand-offs between them |
    | [GR-DIG-03](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-03) Provide assisted digital and offline routes | Assisted digital and offline routes designed and tested with users who need them |
    | [GR-FIELD-01](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-01) Choose devices that suit the job | User research on the working environment, and the device choice recorded in an ADR |
    | [GR-FIELD-02](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-02) Design field tools to work offline | Field journeys tested with no connection, including sync after reconnecting and conflict handling |
    | [GR-FIELD-03](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-03) Manage and secure every device | Device management approach agreed for the devices the service will use |
    | [GR-FE-03](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-03) Progressive enhancement | Core journeys tested with JavaScript turned off |
    | [GR-FE-04](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-04) Consider forms platforms first | ADR noting whether the forms capability was considered |
    | [GR-FE-05](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-05) Design for low bandwidth and rural users | Page weight budget, save-progress design and testing on slow connections |
    | [GR-FE-07](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-07) Tell users what is happening when things fail or are slow | Each dependency that can fail or be slow identified with the developers, and what users see in each case designed and tested in the prototype |
    | [GR-HOST-02](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-02) Public cloud first | Where the platform cannot be used, the hosting design uses a Defra-managed public cloud tenancy |
    | [GR-HOST-04](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-04) Use managed services before self-managed | Hosting design listing the managed services used |
    | [GR-HOST-05](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-05) Consistent, disposable environments | Environments created from the same code, and how lower environments avoid real personal data |
    | [GR-HOST-06](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-06) Host data in the UK | Hosting design places every data store and backup in UK regions |
    | [GR-HOST-07](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-07) Design for the resilience the service needs | Recovery time and recovery point objectives agreed with the service owner, and a design that meets them |
    | [GR-IAM-04](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-04) Separate authentication from authorisation | Authorisation rules written down and covered by automated tests |
    | [GR-OPEN-02](https://defra.github.io/architecture/guardrails/open-source/#gr-open-02) Licence clearly | LICENCE file in every repository from the start |
    | [GR-OPEN-03](https://defra.github.io/architecture/guardrails/open-source/#gr-open-03) Publish safely | Secret scanning and push protection on for every repository from the first commit |
    | [GR-OPEN-04](https://defra.github.io/architecture/guardrails/open-source/#gr-open-04) Reuse and contribute back | Reuse and upstream contributions noted in ADRs and pull requests |
    | [GR-PROD-01](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-01) Fund and run products, not projects | A named, long-lived team responsible for the product, with a roadmap beyond the current funding period |
    | [GR-PROD-02](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-02) Name the product owner and service owner | Named product owner and service owner, recorded in the service catalogue |
    | [GR-PROD-03](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-03) Contribute to platforms rather than working around them | Requests and contributions raised with platform teams, and ADRs where the team worked around a platform |
    | [GR-SEC-08](https://defra.github.io/architecture/guardrails/security/#gr-sec-08) Protect the supply chain | Security assessment of suppliers and third-party products in the design |
    | [GR-DEV-01](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-01) Use the supported languages and frameworks | ADR recording the reason wherever the service uses a different stack |
    | [GR-DEV-03](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-03) Protect the main branch | Main branch protected from the start, with changes through reviewed pull requests |
    | [GR-DEV-05](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-05) Automated testing at the right levels | Test results from the pipeline at each level |
    | [GR-DEV-07](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-07) Follow shared coding standards | Linting and formatting checks in the pipeline |
    | [GR-DEV-08](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-08) Document as you go | README explaining what the service does and how to run, test and deploy it, with links to its ADRs |
    | [GR-DEV-09](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-09) Record significant decisions as ADRs | ADR log in the repository or linked from its README |
    | [GR-SUS-01](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-01) Consider sustainability in design decisions | Environmental impact recorded in ADRs for hosting and technology choices |
    | [GR-SUS-04](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-04) Keep data and pages lean | Data retention settings and page weight measurements |

??? note "Could (3)"

    | Guardrail | What to show |
    | --- | --- |
    | [GR-FIELD-04](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-04) Check connectivity before you design | Connectivity in the places the service will be used checked, and the approach recorded |
    | [GR-OPEN-05](https://defra.github.io/architecture/guardrails/open-source/#gr-open-05) Blog and show the thing | Blog posts, show and tells or contributions to this site |
    | [GR-SUS-03](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-03) Choose lower-carbon regions and services | Region and service choice recorded with its carbon intensity |

## Architecture artefacts

| Artefact | What to do in this phase |
| --- | --- |
| [Architecture decision record (ADR) log](https://defra.github.io/architecture/governance/architecture-decision-records/) ([template](https://defra.github.io/architecture/governance/templates/adr/)) | Record hosting, identity, integration and data decisions. |
| [C4 system context diagram](https://c4model.com/) | Confirm the context. |
| [C4 container diagram](https://c4model.com/) | Draw the containers for the options you are testing. |
| [Threat model](https://defra.github.io/architecture/security/threat-modelling/) ([template](https://defra.github.io/architecture/governance/templates/threat-model/)) | Run the first collaborative threat model. |
| [Data protection impact assessment (DPIA)](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/) | Complete the DPIA if you process personal data. |
| [Service tier](https://defra.github.io/architecture/nfrs/service-tiers/) | Agree the tier with the service owner. |
| [Non-functional requirements (NFRs)](https://defra.github.io/architecture/nfrs/catalogue/) | Choose NFRs from the catalogue for your tier. |
| [Exit plan](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) | Draft an exit plan for each new product or supplier. |

## Governance touchpoints

- Share your architecture, ADR log and threat model with your solution design authority before the alpha assessment.
- Take novel or cross-cutting designs, and any exception to a Must, to the [Technical Design Authority](https://defra.github.io/architecture/governance/tda/).
- Engage the platform teams - see [getting onto Defra platforms](https://defra.github.io/architecture/deliver/platforms/).

## Evidence pack

Bring these together once and reuse them for your solution design authority, service assessment, spend control and security assurance:

- Architecture decision record (ADR) log
- C4 system context diagram
- C4 container diagram
- Threat model
- Data protection impact assessment (DPIA)
- Service tier
- Non-functional requirements (NFRs)
- Exit plan
- evidence for each Must guardrail above (18)

Use the [alpha evidence checklist](https://defra.github.io/architecture/deliver/checklists/alpha/) to gather and print it.

For how the phase works and what assessors look for, see the GOV.UK Service Manual on [alpha](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works) and the [Defra Digital Service Manual](https://digital.defra.gov.uk/service-manual). This site covers the architecture evidence only.


