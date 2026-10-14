<!-- https://defra.github.io/architecture/patterns/acting-on-behalf/ | maturity: published | site version 0.3.0 | generated from patterns/acting-on-behalf.md -->

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

1. The user signs in with [Defra Customer Identity](https://defra.github.io/architecture/deliver/platforms/#defra-id), which uses GOV.UK One Login and Government Gateway behind the scenes. The service never stores passwords or builds its own sign-in.
2. The service gets the organisations and holdings the user can act for, and their role for each, from the authoritative source - not from a local table that drifts. Defra Customer Identity stores users' organisation accounts and the relationships between them centrally, so start there.
3. If the user can act for more than one, they choose which one they are acting for now, and the service shows it on every page.
4. Before every action, an **authorisation component** checks the role against the action - for example "an agent can submit a claim but cannot change bank details". Keep these rules in code, readable and covered by tests.
5. Every decision, especially refusals, is logged with the user, the organisation and the action.

## What users see

- **Sign in once**, through Defra Customer Identity. Users do not create a separate account for your service.
- **A choice of who they are acting for**, straight after sign-in, if they can act for more than one organisation or holding. Ask it as one question on its own page, using the GOV.UK Design System [question pages](https://design-system.service.gov.uk/patterns/question-pages/) pattern and [radios](https://design-system.service.gov.uk/components/radios/), and list each one with something users recognise, such as the business name and its reference. If they can act for only one, skip the question.
- **Who they are acting for, on every page**, with a way to switch. Agents with many clients need this most.
- **Only the actions their role allows.** Hide or explain actions they cannot take, rather than letting them fill in a form and refusing at the end.
- **A clear explanation when they cannot do something**, and how to get access.

## Content to design

| Situation | What to tell users |
| --- | --- |
| **Choosing who to act for** | A question such as "Which business are you applying for?", with names and references users recognise. Avoid internal terms such as "organisation id" or "relationship". |
| **Agent or owner** | Write for the person reading. An owner sees "your business"; an agent sees the client's name, such as "Applying for Brook Farm Ltd". Confirmation pages and emails say who submitted and who for. |
| **Missing permission** | Say what they cannot do and why, then how to fix it, for example: "You cannot change bank details for Brook Farm Ltd. Only the business owner can do this. Ask them to …". Do not just say "Access denied". |
| **No organisations or holdings found** | Explain that their account is not linked to any yet, and how to get linked or who to contact. |
| **Access has changed** | If a relationship is removed while they are using the service, tell them they no longer have access for that business and return them to the choice of who to act for. |
| **Acting for the wrong one** | Show the current business or holding clearly enough that users notice before they submit. |

How users get linked to an organisation or holding, and who they contact, depends on Defra Customer Identity. Check the current process with the Customer Identity team before writing this content - see [Defra Customer Identity](https://digital.defra.gov.uk/architecture-and-software-development/defra-customer-identity) in the Defra Digital Service Manual.

## What to test with users

- Do agents and owners **recognise the names and references** they are shown when choosing who to act for?
- Do users **notice who they are acting for** on each page, and can agents switch clients quickly?
- When a user **lacks permission**, do they understand why and know what to do next?
- Do partners, family members and employees working for one business understand **what they can and cannot do** in their role?
- Is the wording right for **both agents and owners**? Does each understand confirmation pages and emails written for the other?
- What happens in research when a user has **lots of relationships**, such as an agent with 50 clients? Does the choice page still work?

Recruit agents, not only owners: their needs are often different, and their mistakes affect someone else's business.

## Guardrails it helps you meet

| Guardrail | Level | What the guardrail asks |
| --- | --- | --- |
| [GR-IAM-01](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-01) Use the strategic customer identity services | <span class="rfc rfc--must">Must</span> | Services for citizens, farmers and businesses use Defra Customer Identity (Defra ID), which uses GOV.UK One Login and Government Gateway as identity providers, for authentication. Services do not build their own sign-in. See Defra Customer Identity in the Defra Digital Service Manual. |
| [GR-IAM-04](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-04) Separate authentication from authorisation | <span class="rfc rfc--should">Should</span> | Use the identity provider to establish who someone is; keep business authorisation rules (for example "can act for this holding") explicit, testable and in the right service. |
| [GR-IAM-03](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-03) Authorise on least privilege | <span class="rfc rfc--must">Must</span> | Users, services and pipelines get only the permissions they need, granted through roles or groups, and reviewed regularly. |
| [GR-DATA-02](https://defra.github.io/architecture/guardrails/data/#gr-data-02) Use authoritative sources | <span class="rfc rfc--should">Should</span> | Use the authoritative source for shared entities - customers, organisations, land parcels, holdings, locations, species - rather than creating local copies that drift. See Defra on a page. |
| [GR-SEC-07](https://defra.github.io/architecture/guardrails/security/#gr-sec-07) Log for detection and response | <span class="rfc rfc--must">Must</span> | Send security-relevant events (authentication, authorisation failures, administrative actions, data exports) to the security operations centre. See GR-OPS-01. |


## Related Secure by Design artefacts

- [Access control and authentication](https://github.com/co-cddo/SbD/tree/Main/Access%20Control%20%26%20Authentication)
- [GOV.UK One Login security pattern](https://github.com/co-cddo/SbD/tree/Main/Security%20Architecture%20/Security%20Patterns/GOV.UK%20One%20Login)
- [STRIDE threat modelling template](https://github.com/co-cddo/SbD/blob/Main/Risks%20and%20Threats/Stride%20Threat%20Modelling%20Template%20-%20Secure%20By%20Design%20Artefact%20Library.xlsx)
- The whole [Secure by Design artefact library](https://github.com/co-cddo/SbD)


Threats to consider: a user changing an organisation id in a request to act for someone else (an insecure direct object reference), stale relationships after someone leaves a business, and agents with more access than they need. Check authorisation on the server for every request, not only when the page loads.

## When not to use it

- **Users only ever act for themselves**, such as a member of the public reporting an incident. Authentication alone is enough.
- **Staff-facing services.** Staff sign in with Microsoft Entra ID ([GR-IAM-02](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-02)) and get permissions through roles and groups.

<div id="tbc-1"></div>

!!! warning "To be confirmed"
    **TODO:** whether relationships to land holdings, as well as organisations, come from Defra Customer Identity, and how services should query it.

## Related

- [Reading from an authoritative source](https://defra.github.io/architecture/patterns/authoritative-source/)
- [Identity and access guardrails](https://defra.github.io/architecture/guardrails/identity-and-access/)

