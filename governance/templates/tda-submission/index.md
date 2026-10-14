<!-- https://defra.github.io/architecture/governance/templates/tda-submission/ | maturity: published | site version 0.3.0 | generated from governance/templates/tda-submission.md -->

# TDA submission template

Send to the [Technical Design Authority](https://defra.github.io/architecture/governance/tda/) at least 5 working days before the meeting. Aim for no more than five pages.

```markdown
# TDA submission: <title>

| | |
| --- | --- |
| Team / programme | |
| Presenter(s) | |
| Delivery partner (if any) | |
| Phase | Discovery / Alpha / Beta / Live |
| SDA consulted | Yes / No - name |
| What you need from the TDA | Decision / Advice / Exception |

## 1. Summary

Two or three sentences: what you are doing, why, and what you need.

## 2. Problem and outcomes

- User and business need
- Business capabilities affected (e.g. BC06 Enforce compliance)
- How success will be measured

## 3. Why the TDA?

Novel / cross-cutting / exception to a Must guardrail / technology capability gap / escalated by SDA

## 4. Options considered

Include the strategic options from the technology capability catalogue and why
they do or do not fit.

## 5. Proposed design

- Context diagram
- Container diagram
- Key integrations and data flows
- Technology capabilities used (level 2, e.g. Security & Compliance, Enabling Platforms)

## 6. Guardrails

| Guardrail | Met? | Notes |
| --- | --- | --- |
| GR-HOST-01 | Yes / No / Partly | |

## 7. Risks

Including security (link to current threat model) and data protection (DPIA status).

## 8. Decisions and ADRs

Links to relevant ADRs.
```

