# Exceptions to guardrails

<p class="lead">Guardrails are defaults, and sometimes the right answer is different. The exception process gives you a quick, recorded decision - and tells us when a guardrail needs to change.</p>

## Which process

| You cannot meet... | Route | Record |
| --- | --- | --- |
| A **Could** guardrail | No process needed | Optional |
| A **Should** guardrail | Your [solution design authority](solution-design-authorities.md) | An ADR |
| A **Must** guardrail | The [Technical Design Authority](tda.md) | An [exception request](templates/exception-request.md) and an ADR |
| A **security control** | The [security exception process](../security/managing-exceptions.md), alongside the above | A security risk record |

## What a good exception request includes

- The guardrail id and what you propose instead
- Why the guardrail cannot be met - the user, business, technical or commercial reason
- The risks of the exception and how you will manage them
- How long the exception is needed, and what would let you return to the guardrail
- The cost of meeting the guardrail, if that is the reason

## Principles

- **Time-limited.** Exceptions have an expiry date, normally no more than 12 months, and are reviewed before renewal.
- **Recorded in the open.** The exception register is published, except for security-sensitive details.
- **Quick.** The TDA aims to decide within 10 working days of a complete request. Urgent requests can be handled out of cycle by the chair.
- **Feedback loop.** Every quarter, the architecture team reviews exceptions. Where several teams need the same one, we propose a guardrail change to the TGB.
