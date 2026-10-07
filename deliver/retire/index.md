<!-- https://defra.github.io/architecture/deliver/retire/ | maturity: prototype | site version 0.3.0 | generated from deliver/retire.md -->

# Retire a service

<p class="lead">Retiring a service well protects users, data and money. Plan it as carefully as a launch.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



## What it means for architecture

- Tell users and the services that depend on yours in good time, and point them to what replaces it.
- Decide what happens to the data and records: kept, transferred to The National Archives or destroyed.
- Remove access, secrets and infrastructure so nothing is left running or exposed.
- Archive the code and the decisions so the reasons survive.

## Guardrails that apply

These guardrails need particular attention when you retire a service. The guardrails for the phase the service is in still apply.

### Must (5)

| Guardrail | What to show |
| --- | --- |
| [GR-DATA-09](https://defra.github.io/architecture/guardrails/data/#gr-data-09) Retain and dispose of records properly | Records kept, transferred to The National Archives or destroyed, as agreed with the information asset owner |
| [GR-DATA-06](https://defra.github.io/architecture/guardrails/data/#gr-data-06) Protect personal data by design | Personal data deleted or transferred lawfully, as set out in the DPIA |
| [GR-IAM-03](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-03) Authorise on least privilege | All access to the service's systems and data removed |
| [GR-IAM-05](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-05) No secrets in code | Secrets, keys and credentials revoked |
| [GR-OPEN-01](https://defra.github.io/architecture/guardrails/open-source/#gr-open-01) Code in the open | Repositories archived, not deleted, so the code and decisions stay available |

??? note "Should (4)"

    | Guardrail | What to show |
    | --- | --- |
    | [GR-DATA-01](https://defra.github.io/architecture/guardrails/data/#gr-data-01) Every data set has an owner | Information asset register updated to show what happened to each data set |
    | [GR-API-04](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-04) Version and deprecate deliberately | Consumers told the retirement date in advance, and moved to a replacement |
    | [GR-TECH-03](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) Plan your exit before you enter | Exit plan carried out - data exported in open formats and contracts ended |
    | [GR-SUS-02](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-02) Right-size and switch off | Autoscaling and out-of-hours schedules for non-production environments |

## Architecture artefacts

| Artefact | What to do in this phase |
| --- | --- |
| [Architecture decision record (ADR) log](https://defra.github.io/architecture/governance/architecture-decision-records/) ([template](https://defra.github.io/architecture/governance/templates/adr/)) | Record the decision to retire and what replaces the service. |
| [Exit plan](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) | Carry it out - export data in open formats and end contracts. |
| [Runbooks and support model](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05) | Write the decommissioning runbook and keep it with the archived code. |
| [Data protection impact assessment (DPIA)](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/) | Confirm personal data is deleted or transferred lawfully. |

## Governance touchpoints

- Tell API and data consumers in advance, with a retirement date ([GR-API-04](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-04)).
- Agree with the information asset owner which records are kept, transferred to The National Archives or destroyed ([GR-DATA-09](https://defra.github.io/architecture/guardrails/data/#gr-data-09)).
- Update the information asset register and the technology capability catalogue.

## Evidence pack

Bring these together once and reuse them for your solution design authority, service assessment, spend control and security assurance:

- Architecture decision record (ADR) log
- Exit plan
- Runbooks and support model
- Data protection impact assessment (DPIA)
- evidence for each Must guardrail above (5)

Use the [retire a service evidence checklist](https://defra.github.io/architecture/deliver/checklists/retire/) to gather and print it.

For how the phase works and what assessors look for, see the GOV.UK Service Manual on [retire a service](https://www.gov.uk/service-manual/agile-delivery/retiring-your-service) and the [Defra Digital Service Manual](https://digital.defra.gov.uk/service-manual). This site covers the architecture evidence only.


