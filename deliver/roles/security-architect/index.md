<!-- https://defra.github.io/architecture/deliver/roles/security-architect/ | maturity: prototype | site version 0.3.0 | generated from deliver/roles/security-architect.md -->

# Security architect

<p class="lead">The guardrails a security architect leads, what to show in each phase, the patterns that help and when to work with an architect.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



You make sure the service is secure by design and that risks are owned. You lead threat modelling, security testing and risk acceptance.

You lead **20 guardrails**, often with other roles. Leading means making sure the team meets them and can show it, not doing all the work. See them all in the <a href="../../../guardrails/library/#role=security-architect">guardrail library, filtered to your role</a>.

## Your guardrails, phase by phase

### Discovery

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-02](https://defra.github.io/architecture/guardrails/ai/#gr-ai-02) Use approved AI services and tenancies | Must | Any AI services you are exploring identified, with the Defra tenancy or enterprise agreement they would run under |
| [GR-TECH-04](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-04) Assess SaaS before you adopt it | Must | SaaS and third-party products under consideration listed, with the assessments they will need |
| [GR-SEC-01](https://defra.github.io/architecture/guardrails/security/#gr-sec-01) Follow Secure by Design | Must | Named risk owner, and the information and threats the service is likely to face identified |
| [GR-SEC-03](https://defra.github.io/architecture/guardrails/security/#gr-sec-03) Classify information | Must | Security classification and the types of data the service will handle identified |

More on the [discovery page](https://defra.github.io/architecture/deliver/discovery/).

### Alpha

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-02](https://defra.github.io/architecture/guardrails/ai/#gr-ai-02) Use approved AI services and tenancies | Must | AI services chosen for the design, each confirmed as running in a Defra tenancy or under an approved agreement |
| [GR-API-07](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-07) Secure every API | Must | Authentication, authorisation, input validation and rate limiting designed for each API |
| [GR-TECH-04](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-04) Assess SaaS before you adopt it | Must | Security, data protection, data location, accessibility and single sign-on assessed before contract |
| [GR-SEC-01](https://defra.github.io/architecture/guardrails/security/#gr-sec-01) Follow Secure by Design | Must | Secure by Design activities for alpha completed, including security requirements in the backlog |
| [GR-SEC-02](https://defra.github.io/architecture/guardrails/security/#gr-sec-02) Keep a current threat model | Must | First threat model, created by the team |
| [GR-SEC-03](https://defra.github.io/architecture/guardrails/security/#gr-sec-03) Classify information | Must | Controls in the design that match the classification |
| [GR-SEC-09](https://defra.github.io/architecture/guardrails/security/#gr-sec-09) Manage risk explicitly | Must | Risks from controls that cannot be met recorded, with an owner |
| [GR-AI-05](https://defra.github.io/architecture/guardrails/ai/#gr-ai-05) Evaluate, monitor and threat model | Should | Evaluation plan for accuracy, bias and safety, and AI-specific threats in the threat model |
| [GR-AI-08](https://defra.github.io/architecture/guardrails/ai/#gr-ai-08) Give agents the least privilege they need | Should | Each agent's tools and permissions listed in the design, with a workload identity for the agent |
| [GR-AI-11](https://defra.github.io/architecture/guardrails/ai/#gr-ai-11) Defend agents against prompt injection | Should | Threat model covering prompt injection through every input the agent reads |
| [GR-FIELD-03](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-03) Manage and secure every device | Should | Device management approach agreed for the devices the service will use |
| [GR-HOST-06](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-06) Host data in the UK | Should | Hosting design places every data store and backup in UK regions |
| [GR-OPEN-03](https://defra.github.io/architecture/guardrails/open-source/#gr-open-03) Publish safely | Should | Secret scanning and push protection on for every repository from the first commit |
| [GR-SEC-08](https://defra.github.io/architecture/guardrails/security/#gr-sec-08) Protect the supply chain | Should | Security assessment of suppliers and third-party products in the design |

More on the [alpha page](https://defra.github.io/architecture/deliver/alpha/).

### Beta

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-02](https://defra.github.io/architecture/guardrails/ai/#gr-ai-02) Use approved AI services and tenancies | Must | The AI services in the built service run only in approved tenancies, shown in the hosting design and configuration |
| [GR-API-07](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-07) Secure every API | Must | These controls built and covered by security testing |
| [GR-IAM-03](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-03) Authorise on least privilege | Must | Role and group model built, with users, services and pipelines given only the permissions they need |
| [GR-IAM-06](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-06) Privileged access is controlled and audited | Must | Just-in-time privileged access with phishing-resistant MFA configured, and logged to the security operations centre |
| [GR-SEC-01](https://defra.github.io/architecture/guardrails/security/#gr-sec-01) Follow Secure by Design | Must | Secure by Design activities for beta completed, including controls built and tested |
| [GR-SEC-02](https://defra.github.io/architecture/guardrails/security/#gr-sec-02) Keep a current threat model | Must | Threat model updated as controls are built and tested |
| [GR-SEC-04](https://defra.github.io/architecture/guardrails/security/#gr-sec-04) Encrypt in transit and at rest | Must | TLS 1.2 or higher for all traffic and encryption at rest for every data store, confirmed as built |
| [GR-SEC-06](https://defra.github.io/architecture/guardrails/security/#gr-sec-06) Test before go-live and after major change | Must | IT health check before go-live, and a remediation tracker |
| [GR-SEC-07](https://defra.github.io/architecture/guardrails/security/#gr-sec-07) Log for detection and response | Must | Authentication, authorisation failures, administrative actions and data exports sent to the security operations centre, and tested |
| [GR-SEC-09](https://defra.github.io/architecture/guardrails/security/#gr-sec-09) Manage risk explicitly | Must | Residual risks accepted by the right owner through the security exception process, each with an expiry date |
| [GR-AI-05](https://defra.github.io/architecture/guardrails/ai/#gr-ai-05) Evaluate, monitor and threat model | Should | Evaluation results for accuracy, bias and safety before release, and mitigations for AI threats tested |
| [GR-AI-08](https://defra.github.io/architecture/guardrails/ai/#gr-ai-08) Give agents the least privilege they need | Should | Agent permissions configured as designed and tested, including that the agent cannot reach tools it should not |
| [GR-AI-10](https://defra.github.io/architecture/guardrails/ai/#gr-ai-10) Keep an audit trail of what agents do | Should | Audit records of agent inputs, tool calls, approvals and outcomes produced and sent to security monitoring |
| [GR-AI-11](https://defra.github.io/architecture/guardrails/ai/#gr-ai-11) Defend agents against prompt injection | Should | Prompt injection mitigations tested, including attempts to misuse tools and leak data |
| [GR-FIELD-03](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-03) Manage and secure every device | Should | Devices enrolled in Defra device management, with encryption, patching, screen lock and remote wipe confirmed |
| [GR-HOST-06](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-06) Host data in the UK | Should | Data location confirmed for every data store and backup as built |
| [GR-OPEN-03](https://defra.github.io/architecture/guardrails/open-source/#gr-open-03) Publish safely | Should | Secret scanning and push protection on for every repository |
| [GR-SEC-08](https://defra.github.io/architecture/guardrails/security/#gr-sec-08) Protect the supply chain | Should | Dependencies pinned and verified, and a software bill of materials produced in the pipeline |

More on the [beta page](https://defra.github.io/architecture/deliver/beta/).

### Live

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-02](https://defra.github.io/architecture/guardrails/ai/#gr-ai-02) Use approved AI services and tenancies | Must | List of AI services in use, reviewed when services or agreements change |
| [GR-API-07](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-07) Secure every API | Must | API access reviewed, and controls re-tested after significant change |
| [GR-IAM-03](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-03) Authorise on least privilege | Must | Record of regular access reviews |
| [GR-IAM-06](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-06) Privileged access is controlled and audited | Must | Privileged access reviewed regularly |
| [GR-SEC-01](https://defra.github.io/architecture/guardrails/security/#gr-sec-01) Follow Secure by Design | Must | Secure by Design activities for live continuing, including monitoring and review |
| [GR-SEC-02](https://defra.github.io/architecture/guardrails/security/#gr-sec-02) Keep a current threat model | Must | Threat model reviewed at least once a year, with the date of the last review |
| [GR-SEC-04](https://defra.github.io/architecture/guardrails/security/#gr-sec-04) Encrypt in transit and at rest | Must | Encryption settings checked when new stores or connections are added |
| [GR-SEC-06](https://defra.github.io/architecture/guardrails/security/#gr-sec-06) Test before go-live and after major change | Must | IT health check after significant change, with remediation tracked |
| [GR-SEC-07](https://defra.github.io/architecture/guardrails/security/#gr-sec-07) Log for detection and response | Must | Security events reviewed and alerts acted on |
| [GR-SEC-09](https://defra.github.io/architecture/guardrails/security/#gr-sec-09) Manage risk explicitly | Must | Accepted risks reviewed before they expire |
| [GR-AI-05](https://defra.github.io/architecture/guardrails/ai/#gr-ai-05) Evaluate, monitor and threat model | Should | Monitoring of model performance and drift in live, with evaluation repeated when the model or data changes |
| [GR-AI-08](https://defra.github.io/architecture/guardrails/ai/#gr-ai-08) Give agents the least privilege they need | Should | Agent permissions reviewed regularly, as for a privileged user |
| [GR-AI-10](https://defra.github.io/architecture/guardrails/ai/#gr-ai-10) Keep an audit trail of what agents do | Should | Audit records retained and reviewed, and used to investigate any problem |
| [GR-AI-11](https://defra.github.io/architecture/guardrails/ai/#gr-ai-11) Defend agents against prompt injection | Should | Prompt injection defences re-tested when inputs, tools or models change |
| [GR-FIELD-03](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-03) Manage and secure every device | Should | Device compliance monitored, and lost devices wiped |
| [GR-HOST-06](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-06) Host data in the UK | Should | Data location checked when new stores or services are added |
| [GR-OPEN-03](https://defra.github.io/architecture/guardrails/open-source/#gr-open-03) Publish safely | Should | Secret scanning alerts dealt with promptly |
| [GR-SEC-08](https://defra.github.io/architecture/guardrails/security/#gr-sec-08) Protect the supply chain | Should | Software bill of materials kept current, and supplier assessments reviewed at renewal |

More on the [live page](https://defra.github.io/architecture/deliver/live/).

### Significant change

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-SEC-01](https://defra.github.io/architecture/guardrails/security/#gr-sec-01) Follow Secure by Design | Must | Secure by Design activities repeated for the change, with the risk owner involved |
| [GR-SEC-02](https://defra.github.io/architecture/guardrails/security/#gr-sec-02) Keep a current threat model | Must | Threat model revisited for the change before it is built |
| [GR-SEC-06](https://defra.github.io/architecture/guardrails/security/#gr-sec-06) Test before go-live and after major change | Must | IT health check scoped and booked for the change where it is significant |

More on the [significant change page](https://defra.github.io/architecture/deliver/significant-change/).

### Retire a service

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-IAM-03](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-03) Authorise on least privilege | Must | All access to the service's systems and data removed |

More on the [retire a service page](https://defra.github.io/architecture/deliver/retire/).

## Patterns that help

- [Acting on behalf of an organisation or holding](https://defra.github.io/architecture/patterns/acting-on-behalf/) - Users act for a business, a land holding or another person, and the service must check they are allowed to.
- [Reading from an authoritative source](https://defra.github.io/architecture/patterns/authoritative-source/) - A service needs shared data - customers, organisations, holdings, locations or species - that another part of Defra owns.
- [File upload with malware scanning](https://defra.github.io/architecture/patterns/file-upload/) - Users upload documents or images, and the files must be scanned and stored safely before anyone opens them.
- [Publishing open data with metadata](https://defra.github.io/architecture/patterns/open-data-publishing/) - You hold non-personal data that others could use, and want to publish it so it can be found, trusted and reused.

## Working with architects

- Run the first threat model with the whole team in alpha - see [threat modelling](https://defra.github.io/architecture/security/threat-modelling/).
- Agree the IT health check scope before beta.



