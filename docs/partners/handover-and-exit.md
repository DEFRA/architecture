# Handover and exit

<p class="lead">What "done" means when a partner hands a service to Defra or to another supplier, so the next team can run and change it without the people who built it.</p>

Plan handover from the start, not in the last month. The [exit plan](../guardrails/choosing-technology.md#gr-tech-03) and the evidence below should exist and be kept current throughout the contract.

## Definition of done for handover

Each item is checked against the guardrail it comes from. The incoming team, or Defra, confirms each one.

### Code and documentation - GR-DEV-08

| Done when | Evidence |
| --- | --- |
| Every repository has a README explaining what it does and how to run, test and deploy it locally | README reviewed by the incoming team, who run the service from it |
| All code, infrastructure and pipeline definitions are in the Defra GitHub organisation, with nothing held only by the supplier | Repository list agreed; supplier accounts removed after handover ([GR-DEV-02](../guardrails/software-development.md#gr-dev-02)) |
| The ADR log is complete and current | ADRs cover every significant decision, including departures from guardrails ([GR-DEV-09](../guardrails/software-development.md#gr-dev-09)) |
| Architecture diagrams match what is running | C4 context and container diagrams reviewed against the live service |
| The incoming team can make, test and release a change | The incoming team has shipped a small change to production through the pipeline |

### Running the service - GR-OPS-05

| Done when | Evidence |
| --- | --- |
| Runbooks cover deployment, rollback, recovery and common incidents | Runbooks used in a handover exercise |
| Support model, on-call and escalation routes name the incoming team | Support rota and contacts updated |
| Dashboards, alerts and service level objectives are understood by the incoming team | Walkthrough held; alerts routed to the incoming team |
| Known issues, risks and technical debt are written down | Backlog and risk register handed over, with accepted security risks and their expiry dates ([GR-SEC-09](../guardrails/security.md#gr-sec-09)) |
| The service is registered in the service catalogue with its live owner | Catalogue entry updated |

### Exit and data - GR-TECH-03

| Done when | Evidence |
| --- | --- |
| All Defra data can be exported in open formats, and the export has been tested | Test export checked by the information asset owner |
| Licences, subscriptions and accounts for third-party products are in Defra's name, or transferred | List of products and their contract owners |
| Secrets, keys and credentials held by the outgoing supplier are rotated or revoked | Rotation record ([GR-IAM-05](../guardrails/identity-and-access.md#gr-iam-05)) |
| Supplier access to systems, repositories and data is removed | Access review completed ([GR-IAM-03](../guardrails/identity-and-access.md#gr-iam-03)) |
| The exit plan's switching cost and risks are updated for the next contract | Updated exit plan |

## Knowledge transfer

Documents are not enough on their own. Plan for:

- **pairing and shadowing** - the incoming team works alongside the outgoing team for long enough to handle a release and an incident
- **a handover exercise** - the incoming team runs a deployment and a simulated incident while the outgoing team watches
- **a defined overlap period** agreed in the contract

!!! warning "To be confirmed"
    **TODO:** Defra's standard overlap period for supplier transitions, and who signs off that handover is complete.
