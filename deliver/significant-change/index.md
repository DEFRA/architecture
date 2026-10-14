<!-- https://defra.github.io/architecture/deliver/significant-change/ | maturity: prototype | site version 0.3.0 | generated from deliver/significant-change.md -->

# Significant change

<p class="lead">A significant change is one that changes the service's architecture, risks or users enough that the evidence from its last assessment no longer holds. Treat it as a small piece of delivery with its own design, evidence and governance.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



## What counts as significant

- Examples: a new integration or data source, a new supplier or product, moving platform, processing new kinds of personal data, using AI in a new way, or a large increase in users.
- Not usually significant: new features within the existing design, routine dependency updates, or changes to content.
- If you are not sure, use the [decision check](https://defra.github.io/architecture/governance/decision-check/) or ask your solution design authority.

## Guardrails that apply

These guardrails need particular attention when you significant change. The guardrails for the phase the service is in still apply.

### Must (7)

| Guardrail | What to show |
| --- | --- |
| [GR-SEC-01](https://defra.github.io/architecture/guardrails/security/#gr-sec-01) Follow Secure by Design | Secure by Design activities repeated for the change, with the risk owner involved |
| [GR-SEC-02](https://defra.github.io/architecture/guardrails/security/#gr-sec-02) Keep a current threat model | Threat model revisited for the change before it is built |
| [GR-SEC-06](https://defra.github.io/architecture/guardrails/security/#gr-sec-06) Test before go-live and after major change | IT health check scoped and booked for the change where it is significant |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | DPIA updated for any change in how personal data is processed |
| [GR-TECH-01](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-01) Look for something to reuse first | ADR showing reuse options considered for any new component |
| [GR-TECH-06](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-06) Get spend approval early | Architecture team consulted before new procurement for the change |
| [GR-OPS-05](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05) Be ready for live before you go live | Runbooks and support arrangements updated before the change goes live |

??? note "Should (5)"

    | Guardrail | What to show |
    | --- | --- |
    | [GR-API-04](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-04) Version and deprecate deliberately | Consumers told about breaking changes in advance, with a new version and a retirement date for the old one |
    | [GR-DEV-09](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-09) Record significant decisions as ADRs | ADR log in the repository or linked from its README |
    | [GR-TECH-03](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) Plan your exit before you enter | Exit plan updated for any new product or supplier |
    | [GR-AI-06](https://defra.github.io/architecture/guardrails/ai/#gr-ai-06) Talk to the TDA about novel use | Technical Design Authority review of any new AI use introduced by the change |
    | [GR-HOST-07](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-07) Design for the resilience the service needs | Recovery objectives and design checked for the change |

## Architecture artefacts

| Artefact | What to do in this phase |
| --- | --- |
| [Architecture decision record (ADR) log](https://defra.github.io/architecture/governance/architecture-decision-records/) ([template](https://defra.github.io/architecture/governance/templates/adr/)) | Record the change, the options and why. |
| [C4 container diagram](https://c4model.com/) | Update it before you build. |
| [Threat model](https://defra.github.io/architecture/security/threat-modelling/) ([template](https://defra.github.io/architecture/governance/templates/threat-model/)) | Revisit it for the change. |
| [Data protection impact assessment (DPIA)](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/) | Update it if personal data processing changes. |
| [Non-functional requirements (NFRs)](https://defra.github.io/architecture/nfrs/catalogue/) | Check the change does not breach them, or agree new ones. |
| [Exit plan](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) | Update it if you add a product or supplier. |
| [Runbooks and support model](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05) | Update them before the change goes live. |

## Governance touchpoints

- Use the [decision check](https://defra.github.io/architecture/governance/decision-check/) - most changes stay with the team or the solution design authority.
- Share the ADR and updated threat model with your solution design authority before you start.
- Re-test security after the change where it is significant ([GR-SEC-06](https://defra.github.io/architecture/guardrails/security/#gr-sec-06)).

## Evidence pack

Bring these together once and reuse them for your solution design authority, service assessment, spend control and security assurance:

- Architecture decision record (ADR) log
- C4 container diagram
- Threat model
- Data protection impact assessment (DPIA)
- Non-functional requirements (NFRs)
- Exit plan
- Runbooks and support model
- evidence for each Must guardrail above (7)

Use the [significant change evidence checklist](https://defra.github.io/architecture/deliver/checklists/significant-change/) to gather and print it.


