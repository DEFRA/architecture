<!-- https://defra.github.io/architecture/deliver/discovery/ | maturity: prototype | site version 0.3.0 | generated from deliver/discovery.md -->

# Discovery

<p class="lead">Discovery is about understanding the problem, not choosing technology. The architecture job is to find what already exists, spot constraints early and avoid committing to a solution too soon.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



## What it means for architecture

- Say which whole service and service your work is part of, and which products it changes - see [services and capabilities](https://defra.github.io/architecture/handrail/services-and-capabilities/).
- Find out which [business capabilities](https://defra.github.io/architecture/handrail/business-capabilities/) the service supports and what Defra already has that you can reuse.
- Identify the authoritative sources for the data you will need - see [Defra on a page](https://defra.github.io/architecture/data/defra-on-a-page/).
- Spot constraints early: personal data, security classification, legacy systems, suppliers and contracts.
- Do not start a procurement or commit to a product without talking to the architecture team.

## Guardrails that apply

These guardrails apply in discovery, taken from each guardrail's metadata. Meet every Must, or have an approved [exception](https://defra.github.io/architecture/governance/exceptions/). Depart from a Should only with a recorded reason.

### Must (9)

| Guardrail | What to show |
| --- | --- |
| [GR-AI-02](https://defra.github.io/architecture/guardrails/ai/#gr-ai-02) Use approved AI services and tenancies | Any AI services you are exploring identified, with the Defra tenancy or enterprise agreement they would run under |
| [GR-TECH-01](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-01) Look for something to reuse first | Existing Defra and cross-government options for the need identified from the technology capability catalogue |
| [GR-TECH-04](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-04) Assess SaaS before you adopt it | SaaS and third-party products under consideration listed, with the assessments they will need |
| [GR-TECH-06](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-06) Get spend approval early | Architecture team consulted before any procurement under spend control starts |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | DPIA screening completed, showing whether personal data is involved |
| [GR-HOST-01](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-01) Use Defra's strategic delivery platform by default | Platform team engaged, and any hosting needs the Core Delivery Platform might not meet identified |
| [GR-IAM-01](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-01) Use the strategic customer identity services | Identity team engaged about the level of identity assurance needed and how users act for organisations |
| [GR-SEC-01](https://defra.github.io/architecture/guardrails/security/#gr-sec-01) Follow Secure by Design | Named risk owner, and the information and threats the service is likely to face identified |
| [GR-SEC-03](https://defra.github.io/architecture/guardrails/security/#gr-sec-03) Classify information | Security classification and the types of data the service will handle identified |

??? note "Should (13)"

    | Guardrail | What to show |
    | --- | --- |
    | [GR-AI-01](https://defra.github.io/architecture/guardrails/ai/#gr-ai-01) Consider AI first | ADR recording the AI options considered and why they were or were not used |
    | [GR-AI-06](https://defra.github.io/architecture/guardrails/ai/#gr-ai-06) Talk to the TDA about novel use | Novel or generative AI use in decision making identified, and a conversation with the Technical Design Authority booked |
    | [GR-TECH-02](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-02) Buy commodity, build differentiating | Buy or build options appraisal in the ADR or business case |
    | [GR-DATA-02](https://defra.github.io/architecture/guardrails/data/#gr-data-02) Use authoritative sources | Shared entities the service needs identified, with their authoritative sources |
    | [GR-DATA-10](https://defra.github.io/architecture/guardrails/data/#gr-data-10) Handle research data safely | Consent forms and privacy notice in use, recordings and notes stored only in approved places, and a deletion date set |
    | [GR-DATA-11](https://defra.github.io/architecture/guardrails/data/#gr-data-11) No real personal data in prototypes | Any prototype uses made-up data |
    | [GR-DIG-01](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-01) Challenge paper and manual processes | Discovery findings showing paper, email and manual steps in the current process and how the new design removes or justifies each one |
    | [GR-DIG-02](https://defra.github.io/architecture/guardrails/digital-first/#gr-dig-02) Design across organisational boundaries | A map of the whole service, including the parts other teams and organisations deliver, and agreed hand-offs between them |
    | [GR-FIELD-01](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-01) Choose devices that suit the job | User research on the working environment, and the device choice recorded in an ADR |
    | [GR-FE-04](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-04) Consider forms platforms first | ADR noting whether the forms capability was considered |
    | [GR-PROD-02](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-02) Name the product owner and service owner | Named product owner and service owner, recorded in the service catalogue |
    | [GR-DEV-09](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-09) Record significant decisions as ADRs | ADR log in the repository or linked from its README |
    | [GR-SUS-01](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-01) Consider sustainability in design decisions | Environmental impact recorded in ADRs for hosting and technology choices |

??? note "Could (2)"

    | Guardrail | What to show |
    | --- | --- |
    | [GR-FIELD-04](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-04) Check connectivity before you design | Connectivity in the places the service will be used checked, and the approach recorded |
    | [GR-OPEN-05](https://defra.github.io/architecture/guardrails/open-source/#gr-open-05) Blog and show the thing | Blog posts, show and tells or contributions to this site |

## Architecture artefacts

| Artefact | What to do in this phase |
| --- | --- |
| [Architecture decision record (ADR) log](https://defra.github.io/architecture/governance/architecture-decision-records/) ([template](https://defra.github.io/architecture/governance/templates/adr/)) | Start the log. Record the reuse options you considered. |
| [C4 system context diagram](https://c4model.com/) | Sketch the context - users, Defra systems and partners involved. |
| [Service tier](https://defra.github.io/architecture/nfrs/service-tiers/) | Propose a tier with the service owner. |
| [Data protection impact assessment (DPIA)](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/) | Screen for personal data and decide whether you need a full DPIA. |

## Governance touchpoints

- Map the service to [business capabilities](https://defra.github.io/architecture/handrail/business-capabilities/) and check [technology capabilities](https://defra.github.io/architecture/handrail/technology-capabilities/) for something to reuse.
- Use the [decision check](https://defra.github.io/architecture/governance/decision-check/) to agree your governance route and [solution design authority](https://defra.github.io/architecture/governance/solution-design-authorities/).
- Talk to the architecture team before any procurement starts, and record spend as described in [spend control](https://digital.defra.gov.uk/delivery-groups/follow-delivery-governance/assurance/spend-control) ([GR-TECH-06](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-06)).
- Name the security risk owner ([GR-SEC-01](https://defra.github.io/architecture/guardrails/security/#gr-sec-01)).

## Evidence pack

Bring these together once and reuse them for your solution design authority, service assessment, spend control and security assurance:

- Architecture decision record (ADR) log
- C4 system context diagram
- Service tier
- Data protection impact assessment (DPIA)
- evidence for each Must guardrail above (9)

Use the [discovery evidence checklist](https://defra.github.io/architecture/deliver/checklists/discovery/) to gather and print it.

For how the phase works and what assessors look for, see the GOV.UK Service Manual on [discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) and the [Defra Digital Service Manual](https://digital.defra.gov.uk/service-manual). This site covers the architecture evidence only.


