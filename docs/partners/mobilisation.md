# Mobilisation checklist

<p class="lead">What a delivery partner needs in place to start work on a Defra engagement, and who to meet in the first week. Start early: some access takes weeks.</p>

Work through this with your Defra engagement lead before and during your first weeks.

!!! warning "To be confirmed"
    **TODO:** typical lead times for security clearance, Defra devices and accounts, GitHub organisation access and Core Delivery Platform access, and who arranges each.

## Before day one

| What | Why | Who arranges it | Lead time |
| --- | --- | --- | --- |
| Security clearance for each team member, at the level the work needs | Access to Defra systems and data | Supplier, with the Defra engagement lead | To be confirmed |
| Defra devices or an approved way to use your own | Access to Defra systems from a managed device | Defra engagement lead | To be confirmed |
| Defra accounts (Microsoft Entra ID) with multi-factor authentication | Single sign-on to Defra tools ([GR-IAM-02](../guardrails/identity-and-access.md#gr-iam-02)) | Defra engagement lead | To be confirmed |
| Access to the Defra GitHub organisation | All code lives there from day one ([GR-DEV-02](../guardrails/software-development.md#gr-dev-02)) | Defra engagement lead | To be confirmed |
| Access to the Core Delivery Platform | Hosting, pipelines and environments ([GR-HOST-01](../guardrails/hosting-and-platforms.md#gr-host-01)). The CDP portal needs a Defra device or the Defra VPN | Platform team - see [getting onto Defra platforms](../deliver/platforms.md#cdp) | To be confirmed |
| A cloud account, separate from your standard Defra login, if you need the DEV or TEST environments, infrastructure admin or to deploy to the Defra Cloud Platform | Requested through the Defra Service Desk - see [common security tasks](https://digital.defra.gov.uk/security/common-tasks) in the Defra Digital Service Manual | Each team member, through the Service Desk | To be confirmed |
| Agreement on any AI coding assistants you plan to use | [GR-AI-07](../guardrails/ai.md#gr-ai-07) | Supplier, with the Defra engagement lead | - |

## In the first week

Meet:

- **your Defra engagement lead and service owner**, to agree outcomes, ways of working and how decisions are made
- **the solution design authority** for your area, to agree how you will share designs and decisions - see [solution design authorities](../governance/solution-design-authorities.md)
- **the architecture team**, for the relevant [reference architecture](../handrail/reference-architectures/index.md), patterns and guardrails
- **the platform team**, for onboarding to the Core Delivery Platform
- **a security architect and the service's risk owner**, to plan [Secure by Design](../security/secure-by-design.md) activities and the first threat model
- **teams you depend on or that depend on you** - see [working with other suppliers](multi-supplier.md)

Set up:

- the service repository, with a README, a LICENCE file, a `docs/adr` folder and branch protection ([GR-DEV-08](../guardrails/software-development.md#gr-dev-08), [GR-OPEN-02](../guardrails/open-source.md#gr-open-02), [GR-DEV-03](../guardrails/software-development.md#gr-dev-03))
- secret scanning, push protection and automated dependency updates ([GR-OPEN-03](../guardrails/open-source.md#gr-open-03), [GR-DEV-06](../guardrails/software-development.md#gr-dev-06))
- the [guardrail check](../deliver/guardrail-check.md) in your pipeline, so gaps show up from the first pull request
- your first ADR, recording the options you will explore
- a date for your first [decision check](../governance/decision-check.md) and self-assurance against the [guardrails for your phase](../deliver/index.md)

## By the end of the first month

- Architecture approach shared with the solution design authority
- First threat model session held (alpha onwards)
- Service tier proposed with the service owner
- Knowledge sharing with Defra staff planned - pairing, show and tells, documentation
