# Guardrail exception request template

Use when you cannot meet a **Must** guardrail. See [exceptions to guardrails](../exceptions.md).

```markdown
# Exception request: <guardrail id> for <service>

| | |
| --- | --- |
| Guardrail | e.g. GR-HOST-01 Use Defra's strategic delivery platform by default |
| Service / product | |
| Requested by | |
| SDA view | Supports / Does not support / Not consulted |
| Duration requested | Until YYYY-MM-DD (maximum 12 months) |

## What we propose instead

## Why the guardrail cannot be met

User, business, technical, commercial or timing reasons. If cost, give the
estimated cost of meeting the guardrail.

## Risks and mitigations

| Risk | Likelihood | Impact | Mitigation | Owner |
| --- | --- | --- | --- | --- |

## Route back to the guardrail

What would need to change for the service to meet the guardrail, and when.

## Related

- ADR:
- Threat model:
- Security risk record (if a security control is affected):
```
