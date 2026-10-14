<!-- https://defra.github.io/architecture/deliver/roles/service-designer/ | maturity: prototype | site version 0.3.0 | generated from deliver/roles/service-designer.md -->

# Service designer

<p class="lead">The guardrails a service designer leads, what to show in each phase, the patterns that help and when to work with an architect.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



You design the whole service, across channels and organisations. Decisions about identity, acting on behalf, data Defra already holds and what happens when things go wrong shape the user experience and are architecture decisions too.

You lead **11 guardrails**, often with other roles. Leading means making sure the team meets them and can show it, not doing all the work. See them all in the <a href="../../../guardrails/library/#role=service-designer">guardrail library, filtered to your role</a>.

## Your guardrails, phase by phase

### Discovery

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-IAM-01](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-01) Use the strategic customer identity services | Must | Identity team engaged about the level of identity assurance needed and how users act for organisations |
| [GR-AI-01](https://defra.github.io/architecture/guardrails/ai/#gr-ai-01) Consider AI first | Should | ADR recording the AI options considered and why they were or were not used |
| [GR-DIG-01](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-01) Challenge paper and manual processes | Should | Discovery findings showing paper, email and manual steps in the current process and how the new design removes or justifies each one |
| [GR-DIG-02](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-02) Design across organisational boundaries | Should | A map of the whole service, including the parts other teams and organisations deliver, and agreed hand-offs between them |
| [GR-FIELD-01](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-01) Choose devices that suit the job | Should | User research on the working environment, and the device choice recorded in an ADR |
| [GR-FE-04](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-04) Consider forms platforms first | Should | ADR noting whether the forms capability was considered |

More on the [discovery page](https://defra.github.io/architecture/deliver/discovery/).

### Alpha

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-03](https://defra.github.io/architecture/guardrails/ai/#gr-ai-03) Keep a human accountable | Must | Design of the human oversight and challenge route for decisions with significant effects, tested with users in prototypes |
| [GR-IAM-01](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-01) Use the strategic customer identity services | Must | Sign-in designed with Defra Customer Identity, and tested with users |
| [GR-AI-01](https://defra.github.io/architecture/guardrails/ai/#gr-ai-01) Consider AI first | Should | ADR recording the AI options considered and why they were or were not used |
| [GR-AI-09](https://defra.github.io/architecture/guardrails/ai/#gr-ai-09) Get human approval for consequential actions | Should | Agent actions classified, and the actions that need human approval identified in the design |
| [GR-DATA-04](https://defra.github.io/architecture/guardrails/data/#gr-data-04) Collect once, share safely | Should | Journey design showing users are not asked for information Defra already holds, and data sharing agreements where required |
| [GR-DIG-01](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-01) Challenge paper and manual processes | Should | Discovery findings showing paper, email and manual steps in the current process and how the new design removes or justifies each one |
| [GR-DIG-02](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-02) Design across organisational boundaries | Should | A map of the whole service, including the parts other teams and organisations deliver, and agreed hand-offs between them |
| [GR-DIG-03](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-03) Provide assisted digital and offline routes | Should | Assisted digital and offline routes designed and tested with users who need them |
| [GR-FIELD-01](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-01) Choose devices that suit the job | Should | User research on the working environment, and the device choice recorded in an ADR |
| [GR-FE-04](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-04) Consider forms platforms first | Should | ADR noting whether the forms capability was considered |
| [GR-FE-05](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-05) Design for low bandwidth and rural users | Should | Page weight budget, save-progress design and testing on slow connections |

More on the [alpha page](https://defra.github.io/architecture/deliver/alpha/).

### Beta

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-03](https://defra.github.io/architecture/guardrails/ai/#gr-ai-03) Keep a human accountable | Must | Human review and challenge built into the service and tested with users and staff |
| [GR-IAM-01](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-01) Use the strategic customer identity services | Must | Integration with Defra Customer Identity built and tested |
| [GR-AI-09](https://defra.github.io/architecture/guardrails/ai/#gr-ai-09) Get human approval for consequential actions | Should | Approval enforced in the tool layer, with tests showing the agent cannot act without it |
| [GR-DATA-04](https://defra.github.io/architecture/guardrails/data/#gr-data-04) Collect once, share safely | Should | Journey design showing users are not asked for information Defra already holds, and data sharing agreements where required |
| [GR-DIG-02](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-02) Design across organisational boundaries | Should | A map of the whole service, including the parts other teams and organisations deliver, and agreed hand-offs between them |
| [GR-DIG-03](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-03) Provide assisted digital and offline routes | Should | Assisted digital and offline routes designed and tested with users who need them |
| [GR-FE-05](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-05) Design for low bandwidth and rural users | Should | Page weight budget, save-progress design and testing on slow connections |

More on the [beta page](https://defra.github.io/architecture/deliver/beta/).

### Live

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-03](https://defra.github.io/architecture/guardrails/ai/#gr-ai-03) Keep a human accountable | Must | Records of human review, challenges raised and their outcomes, reviewed regularly |
| [GR-IAM-01](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-01) Use the strategic customer identity services | Must | No other sign-in introduced |
| [GR-AI-09](https://defra.github.io/architecture/guardrails/ai/#gr-ai-09) Get human approval for consequential actions | Should | Approval records reviewed, and the classification updated when the agent gains new tools |
| [GR-DIG-03](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-03) Provide assisted digital and offline routes | Should | Assisted digital and offline routes designed and tested with users who need them |

More on the [live page](https://defra.github.io/architecture/deliver/live/).

## Patterns that help

- [Acting on behalf of an organisation or holding](https://defra.github.io/architecture/patterns/acting-on-behalf/) - Users act for a business, a land holding or another person, and the service must check they are allowed to.
- [Reading from an authoritative source](https://defra.github.io/architecture/patterns/authoritative-source/) - A service needs shared data - customers, organisations, holdings, locations or species - that another part of Defra owns.

## Working with architects

- In discovery, map the current journey against the systems and data behind it with an architect.
- In alpha, test the riskiest assumptions on both the user and the technical side together.
- Record decisions that shape the user experience in ADRs, as a contributor.



