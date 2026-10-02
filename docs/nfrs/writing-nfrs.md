# Writing good NFRs

<p class="lead">A good NFR is specific, measurable and testable. If you cannot write a test for it, it is not finished.</p>

## Drafting requirements

Write each NFR as a statement anyone can check:

> **[What]** must **[measurable target]** **[under what conditions]**, shown by **[how it will be verified]**.

| Weak | Better |
| --- | --- |
| The service must be fast. | 95% of page requests complete within 2 seconds at the expected peak of 500 concurrent users, shown by a load test before go-live. |
| The service must be highly available. | The service is available 99.5% of the time between 7am and 8pm, Monday to Saturday, measured monthly by synthetic monitoring. |
| The system must be secure. | Critical vulnerabilities are fixed within 14 days, shown by scanner reports in the pipeline. |
| It must be accessible. | The service meets WCAG 2.2 AA, shown by automated checks on every change and an accessibility audit before public beta. |

### Checklist

- **Specific** - one quality per requirement
- **Measurable** - a number, a threshold or a clear pass/fail
- **Testable** - you know how you will prove it, ideally automatically
- **Proportionate** - the target matches the [service tier](service-tiers.md), not the highest possible
- **Owned** - someone is responsible for meeting and monitoring it
- **Traceable** - it has an id and links to the user need, guardrail or policy behind it

## Specific guidance

| Topic | Guidance |
| --- | --- |
| Performance testing | [GOV.UK Service Manual: technology](https://www.gov.uk/service-manual/technology) and the [catalogue performance NFRs](catalogue.md#nfr-prf) |
| Accessibility | [Front end and accessibility guardrails](../guardrails/front-end-and-accessibility.md) and [GOV.UK: making your service accessible](https://www.gov.uk/service-manual/helping-people-to-use-your-service/making-your-service-accessible-an-introduction) |
| Security | [Secure by Design in Defra](../security/secure-by-design.md) and [threat modelling](../security/threat-modelling.md) |
| Resilience | [Hosting and platforms guardrails](../guardrails/hosting-and-platforms.md) |
| Monitoring | [Observability and operations guardrails](../guardrails/observability-and-operations.md) |
| Engineering practice | [Defra software development standards](https://defra.github.io/software-development-standards/) |

## Useful resources

- [GOV.UK Service Manual: technology](https://www.gov.uk/service-manual/technology)
- [Service Standard point 14: operate a reliable service](https://www.gov.uk/service-manual/service-standard/point-14-operate-a-reliable-service)
- [NCSC Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/cyber-assessment-framework)
- [Government Data Quality Framework](https://www.gov.uk/government/publications/the-government-data-quality-framework)

## NFR updates and amendments

The catalogue changes through pull requests, like the rest of this site:

1. Propose a new NFR or a change to a target by editing [`nfrs/catalogue.yaml`](https://github.com/DEFRA/architecture/blob/main/nfrs/catalogue.yaml), or [open an issue](https://github.com/DEFRA/architecture/issues) if you prefer.
2. The architecture team reviews it. Changes to tier values or to targets that affect many services go to the [Technical Design Authority](../governance/tda.md).
3. Once merged, the change is published here and recorded in [what's new](../about/changelog.md).

Never reuse or renumber an NFR id - other teams may reference it. Retire an NFR by marking it as retired in its description.
