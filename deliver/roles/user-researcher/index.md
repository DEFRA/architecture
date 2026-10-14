<!-- https://defra.github.io/architecture/deliver/roles/user-researcher/ | maturity: prototype | site version 0.3.0 | generated from deliver/roles/user-researcher.md -->

# User researcher

<p class="lead">The guardrails an user researcher leads, what to show in each phase, the patterns that help and when to work with an architect.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



You find out what users need and test whether the service meets it. Research also tests architecture decisions - offline working, acting for others, human oversight of AI - and research data must be handled safely.

You lead **8 guardrails**, often with other roles. Leading means making sure the team meets them and can show it, not doing all the work. See them all in the <a href="../../../guardrails/library/#role=user-researcher">guardrail library, filtered to your role</a>.

## Your guardrails, phase by phase

### Discovery

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-DATA-10](https://defra.github.io/architecture/guardrails/data/#gr-data-10) Handle research data safely | Should | Consent forms and privacy notice in use, recordings and notes stored only in approved places, and a deletion date set |
| [GR-DATA-11](https://defra.github.io/architecture/guardrails/data/#gr-data-11) No real personal data in prototypes | Should | Any prototype uses made-up data |
| [GR-DIG-01](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-01) Challenge paper and manual processes | Should | Discovery findings showing paper, email and manual steps in the current process and how the new design removes or justifies each one |
| [GR-FIELD-01](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-01) Choose devices that suit the job | Should | User research on the working environment, and the device choice recorded in an ADR |
| [GR-FIELD-04](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-04) Check connectivity before you design | Could | Connectivity in the places the service will be used checked, and the approach recorded |

More on the [discovery page](https://defra.github.io/architecture/deliver/discovery/).

### Alpha

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-03](https://defra.github.io/architecture/guardrails/ai/#gr-ai-03) Keep a human accountable | Must | Design of the human oversight and challenge route for decisions with significant effects, tested with users in prototypes |
| [GR-DATA-10](https://defra.github.io/architecture/guardrails/data/#gr-data-10) Handle research data safely | Should | The same for alpha research, with DPIA screening done for the research and any new research tool assessed |
| [GR-DATA-11](https://defra.github.io/architecture/guardrails/data/#gr-data-11) No real personal data in prototypes | Should | Prototypes and research materials use made-up data, including data a participant types in during a session |
| [GR-DIG-01](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-01) Challenge paper and manual processes | Should | Discovery findings showing paper, email and manual steps in the current process and how the new design removes or justifies each one |
| [GR-DIG-03](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-03) Provide assisted digital and offline routes | Should | Assisted digital and offline routes designed and tested with users who need them |
| [GR-FIELD-01](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-01) Choose devices that suit the job | Should | User research on the working environment, and the device choice recorded in an ADR |
| [GR-FE-05](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-05) Design for low bandwidth and rural users | Should | Page weight budget, save-progress design and testing on slow connections |
| [GR-FIELD-04](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-04) Check connectivity before you design | Could | Connectivity in the places the service will be used checked, and the approach recorded |

More on the [alpha page](https://defra.github.io/architecture/deliver/alpha/).

### Beta

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-03](https://defra.github.io/architecture/guardrails/ai/#gr-ai-03) Keep a human accountable | Must | Human review and challenge built into the service and tested with users and staff |
| [GR-DATA-10](https://defra.github.io/architecture/guardrails/data/#gr-data-10) Handle research data safely | Should | Research data from earlier phases deleted on schedule, and the same controls for beta research |
| [GR-DATA-11](https://defra.github.io/architecture/guardrails/data/#gr-data-11) No real personal data in prototypes | Should | Test and research environments use synthetic or anonymised data; any exception agreed through a DPIA |
| [GR-DIG-03](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-03) Provide assisted digital and offline routes | Should | Assisted digital and offline routes designed and tested with users who need them |
| [GR-FE-05](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-05) Design for low bandwidth and rural users | Should | Page weight budget, save-progress design and testing on slow connections |

More on the [beta page](https://defra.github.io/architecture/deliver/beta/).

### Live

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-03](https://defra.github.io/architecture/guardrails/ai/#gr-ai-03) Keep a human accountable | Must | Records of human review, challenges raised and their outcomes, reviewed regularly |
| [GR-DATA-10](https://defra.github.io/architecture/guardrails/data/#gr-data-10) Handle research data safely | Should | Research data handled the same way for ongoing research, and deletion checked |
| [GR-DIG-03](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-03) Provide assisted digital and offline routes | Should | Assisted digital and offline routes designed and tested with users who need them |

More on the [live page](https://defra.github.io/architecture/deliver/live/).

## Patterns that help

No patterns yet. See the [patterns](https://defra.github.io/architecture/patterns/) section.

## Working with architects

- Share research findings that affect technical choices with the architect, such as connectivity, devices or who acts for whom.
- Invite the architect to research playbacks.



