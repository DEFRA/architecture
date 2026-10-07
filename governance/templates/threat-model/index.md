<!-- https://defra.github.io/architecture/governance/templates/threat-model/ | maturity: published | site version 0.3.0 | generated from governance/templates/threat-model.md -->

# Threat model template

See [threat modelling](https://defra.github.io/architecture/security/threat-modelling/) for guidance, and the [Secure by Design artefact library](https://github.com/co-cddo/SbD) for example threat models. Keep it in your repository (or in a private location if it contains sensitive detail) and update it with every significant change.

```markdown
# Threat model: <service>

| | |
| --- | --- |
| Version / date | |
| Participants | |
| Risk owner | |
| Classification of data | e.g. OFFICIAL, personal data |
| Scope | What is in and out of scope |

## 1. What are we working on?

- Data flow diagram with trust boundaries
- Assets: data, functions and infrastructure worth protecting
- Actors: users, staff, systems, suppliers

## 2. What can go wrong?

| ID | Element | STRIDE category | Threat | Existing controls |
| --- | --- | --- | --- | --- |
| T1 | Login | Spoofing | Credential stuffing against customer accounts | Defra ID with MFA |

STRIDE: Spoofing, Tampering, Repudiation, Information disclosure,
Denial of service, Elevation of privilege. Add AI-specific threats where relevant.

## 3. What are we going to do about it?

| Threat | Response (mitigate / accept / transfer / avoid) | Action | Owner | Ticket |
| --- | --- | --- | --- | --- |

## 4. Did we do a good enough job?

- Gaps and assumptions
- Risks to be accepted through the security exception process
- Date of next review
```

