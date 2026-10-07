<!-- https://defra.github.io/architecture/security/threat-modelling/ | maturity: published | site version 0.3.0 | generated from security/threat-modelling.md -->

# Threat modelling

<p class="lead">Threat modelling is a structured conversation about what could go wrong with a service and what to do about it. Done by the team, early and often, it is the most cost-effective security activity there is.</p>

Required by guardrail [GR-SEC-02](https://defra.github.io/architecture/guardrails/security/#gr-sec-02).

## When

- **Alpha:** the first threat model, as soon as there is a candidate architecture
- **Before beta and live assessments**
- **On significant change:** new integrations, new data, new hosting, new user groups, new use of AI
- **At least annually** for live services

## Who

The delivery team - developers, architects, product manager, and ideally a user researcher or designer - facilitated by a security architect or a trained team member. Delivery partners take part as members of the team. Keep it to 90 minutes.

## How: the four questions

We use the widely adopted four-question framework.

### 1. What are we working on?

Draw a data flow diagram: users, components, data stores, external systems and the **trust boundaries** between them. Note the data classification and any personal data.

### 2. What can go wrong?

Walk through each element and trust boundary using **STRIDE**:

| Threat | Asks | Typical control |
| --- | --- | --- |
| **S**poofing | Can someone pretend to be someone or something else? | Strong authentication, mutual TLS |
| **T**ampering | Can data or code be changed without permission? | Integrity checks, signed artefacts, access control |
| **R**epudiation | Can someone deny doing something? | Audit logging |
| **I**nformation disclosure | Can data leak to the wrong people? | Encryption, least privilege, data minimisation |
| **D**enial of service | Can the service be made unavailable? | Rate limiting, autoscaling, platform protection |
| **E**levation of privilege | Can someone do more than they should? | Authorisation on every request, least privilege |

For services using AI, also consider prompt injection, training data poisoning, model inversion and over-reliance on outputs.

### 3. What are we going to do about it?

For each threat: mitigate, accept, transfer or avoid. Put mitigations in the backlog as normal work items. Risks you propose to accept go through [managing security exceptions](https://defra.github.io/architecture/security/managing-exceptions/).

### 4. Did we do a good enough job?

Check coverage, record assumptions, and set the next review date.

## Tools

- A whiteboard or online diagramming tool is enough to start
- [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/) for diagram-based models that can be stored as code
- Example threat models and threat catalogues in the cross-government [Secure by Design artefact library](https://github.com/co-cddo/SbD)
- The [threat model template](https://defra.github.io/architecture/governance/templates/threat-model/)

## Storing threat models

Store the threat model with the service - in the repository if it contains nothing sensitive, otherwise in an access-controlled location linked from the repository. Threat models reveal weaknesses, so think before publishing detail.

