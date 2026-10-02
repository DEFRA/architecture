---
pattern:
  category: security
  status: draft
  summary: Users act for a business, a land holding or another person, and the service must check they are allowed to.
  guardrails: [GR-IAM-01, GR-IAM-04, GR-IAM-03, GR-DATA-02, GR-SEC-07]
  sbd: [access-control, one-login-pattern, stride-template]
---

# Acting on behalf of an organisation or holding

<p class="lead">Separate who someone is from what they are allowed to do, so farmers, businesses, agents and land managers can act for the organisations and holdings they represent - and nobody else.</p>

## Context

Many Defra users do not act for themselves. A farm business has several partners. A land agent manages dozens of holdings for different owners. An accountant claims a grant for a client. A vet certifies animals for a keeper.

Sign-in tells you **who** the person is. It does not tell you **which organisations or holdings they can act for**, or **what they can do** for each one. Services that mix the two up, or rebuild the rules themselves, give the wrong people access or lock out the right ones.

## Solution

Use the strategic customer identity service to authenticate the person. Get the **relationships** - which organisations and holdings they can act for, and in what role - from the authoritative source. Then make the service's own **authorisation decision** explicitly, in one place, and test it.

```mermaid
flowchart LR
    accTitle: Acting on behalf of an organisation or holding
    accDescr: A user signs in through customer identity, which returns who they are. The service asks the authoritative source of customer and organisation relationships which organisations and holdings the user can act for, and the user picks one. An authorisation component in the service checks the user's role for that organisation against the action requested, allows or refuses it, and logs the decision for security monitoring.
    U(["User or agent"]) -->|"sign in"| ID["Defra Customer Identity<br/>(Defra ID)"]
    ID -->|"who they are"| SVC["Service"]
    SVC -->|"which organisations and<br/>holdings can they act for?"| REL["Authoritative source of<br/>customers, organisations<br/>and relationships"]
    U -->|"choose organisation<br/>or holding"| SVC
    SVC --> AZ{"Authorisation<br/>check"}
    AZ -->|"allowed"| ACT["Carry out the action"]
    AZ -->|"refused"| NO["Explain why and<br/>how to get access"]
    AZ -.->|"decision logged"| SOC["Security monitoring"]
```

How it works:

1. The user signs in with [Defra Customer Identity](../deliver/platforms.md#defra-id), which uses GOV.UK One Login and Government Gateway behind the scenes. The service never stores passwords or builds its own sign-in.
2. The service gets the organisations and holdings the user can act for, and their role for each, from the authoritative source - not from a local table that drifts. Defra Customer Identity stores users' organisation accounts and the relationships between them centrally, so start there.
3. If the user can act for more than one, they choose which one they are acting for now, and the service shows it on every page.
4. Before every action, an **authorisation component** checks the role against the action - for example "an agent can submit a claim but cannot change bank details". Keep these rules in code, readable and covered by tests.
5. Every decision, especially refusals, is logged with the user, the organisation and the action.

## Guardrails it helps you meet

<!-- patterns:guardrails -->

## Related Secure by Design artefacts

<!-- patterns:sbd -->

Threats to consider: a user changing an organisation id in a request to act for someone else (an insecure direct object reference), stale relationships after someone leaves a business, and agents with more access than they need. Check authorisation on the server for every request, not only when the page loads.

## When not to use it

- **Users only ever act for themselves**, such as a member of the public reporting an incident. Authentication alone is enough.
- **Staff-facing services.** Staff sign in with Microsoft Entra ID ([GR-IAM-02](../guardrails/identity-and-access.md#gr-iam-02)) and get permissions through roles and groups.

!!! warning "To be confirmed"
    **TODO:** whether relationships to land holdings, as well as organisations, come from Defra Customer Identity, and how services should query it.

## Related

- [Reading from an authoritative source](authoritative-source.md)
- [Identity and access guardrails](../guardrails/identity-and-access.md)
