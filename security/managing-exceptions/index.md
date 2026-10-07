<!-- https://defra.github.io/architecture/security/managing-exceptions/ | maturity: draft | site version 0.3.0 | generated from security/managing-exceptions.md -->

# Managing security exceptions

<p class="lead">Sometimes a security control cannot be met - because of a legacy dependency, a supplier constraint or a delivery deadline. That is a risk decision, and it must be made explicitly, by the right person, for a limited time.</p>

!!! warning "Draft - to be confirmed"
    Parts of this page, such as names, timings and thresholds, are still being confirmed by the architecture team. Use it as a guide, and check with your solution design authority before relying on the detail.



Required by guardrail [GR-SEC-09](https://defra.github.io/architecture/guardrails/security/#gr-sec-09).

## The process

```mermaid
flowchart LR
    accTitle: Security exception process
    accDescr: Identify the gap, assess the risk, mitigate what you can, record and request acceptance. Risks within the owner's appetite are accepted by the service owner, otherwise escalated to the SIRO or CISO. Accepted risks are tracked, reviewed and closed.
    I["Identify<br/>the gap"] --> A["Assess<br/>the risk"]
    A --> M["Mitigate what<br/>you can"]
    M --> R["Record and<br/>request acceptance"]
    R --> D{"Within the risk<br/>owner's appetite?"}
    D -->|Yes| SO["Service owner<br/>accepts"]
    D -->|No| SIRO["Escalate to<br/>SIRO / CISO"]
    SO --> T["Track, review<br/>and close"]
    SIRO --> T
```

1. **Identify** the control or guardrail that cannot be met, and why.
2. **Assess** the risk with a security architect: likelihood, impact, and what an attacker could do.
3. **Mitigate** what you can with compensating controls - for example extra monitoring, network isolation or reduced data.
4. **Record** the residual risk in the risk register, with an owner and expiry date.
5. **Accept** at the right level:

    | Residual risk | Accepted by |
    | --- | --- |
    | Low | Service owner |
    | Medium | Service owner, with the security architect's agreement |
    | High | SIRO, on the advice of the CISO |
    | Very high / outside appetite | Not normally accepted - the service should not proceed until reduced |

6. **Track** remediation. Accepted risks expire - normally within 6 months for high risks and 12 months for others - and must be reviewed before renewal.

## Relationship to guardrail exceptions

If the gap is also a **Must** guardrail, raise a [guardrail exception](https://defra.github.io/architecture/governance/exceptions/) with the TDA at the same time. One request, with the security risk record attached, covers both.

## What we do not accept

- Secrets in source code
- Unauthenticated access to personal or sensitive data
- Known-exploited critical vulnerabilities on internet-facing services without immediate mitigation
- Production changes outside an audited pipeline as a standing practice

