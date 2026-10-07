<!-- https://defra.github.io/architecture/principles/ | maturity: published | site version 0.3.0 | generated from principles/index.md -->

# Principles

<p class="lead">How Defra decides. The DDTS doctrine sets the non-negotiables. The architecture principles apply them to technology change. The guardrails turn both into practical defaults for delivery teams.</p>

```mermaid
flowchart TB
    accTitle: From doctrine to delivery decisions
    accDescr: The DDTS doctrine sets seven non-negotiables. The eight architecture principles apply the doctrine to technology change. The guardrails turn the principles into Must, Should and Could defaults. Delivery teams use the guardrails to decide, escalating only exceptions.
    D["<b>DDTS doctrine</b><br/>7 non-negotiables<br/><i>draft, awaiting endorsement</i>"]
    P["<b>Architecture principles</b><br/>8 principles<br/><i>how architecture applies the doctrine</i>"]
    G["<b>Guardrails</b><br/>Must, Should and Could defaults<br/><i>what teams do in practice</i>"]
    T["<b>Delivery decisions</b><br/>made by teams, recorded as ADRs"]
    D --> P --> G --> T
```

<div class="grid cards" markdown>

-   **[DDTS doctrine](https://defra.github.io/architecture/principles/doctrine/)**

    ---

    Seven non-negotiables for Digital, Data and Technology Services: platforms before projects, standards before exceptions, reuse before buy, data as an enterprise asset, assume AI, outcomes over structures, and digital first.

-   **[Architecture principles](https://defra.github.io/architecture/principles/architecture-principles/)**

    ---

    Defra's eight Strategic Architecture Principles, with the rationale for each and how to follow it.

-   **[Guardrails](https://defra.github.io/architecture/guardrails/)**

    ---

    The practical defaults that put the doctrine and principles into practice. Search them all in the [guardrail library](https://defra.github.io/architecture/guardrails/library/).

</div>

## How to use them

- **Making a decision?** Start with the [decision check](https://defra.github.io/architecture/governance/decision-check/). It tests your choice against the guardrails, which already reflect the doctrine and principles.
- **No guardrail covers it?** Ask which option best fits the principles, and which the doctrine would expect.
- **Need an exception?** The doctrine says standards come before exceptions, so explain why the default does not work in an [exception request](https://defra.github.io/architecture/governance/exceptions/).

## How the doctrine, principles and guardrails line up

Generated from the site's content each time it is published, so it always shows the current picture - including where guardrails are still thin.

| Doctrine | Architecture principles | Guardrail areas | Guardrails |
| --- | --- | --- | ---: |
| [1. Platforms before projects. Built as products](https://defra.github.io/architecture/principles/doctrine/#ddts-01) | [1. Delivery-focused architecture](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-01)<br>[3. Maximise value, minimise waste](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-03) | [Choosing technology](https://defra.github.io/architecture/guardrails/choosing-technology/), [Hosting and platforms](https://defra.github.io/architecture/guardrails/hosting-and-platforms/), [Observability and operations](https://defra.github.io/architecture/guardrails/observability-and-operations/), [Products and platforms](https://defra.github.io/architecture/guardrails/products-and-platforms/), [Software development](https://defra.github.io/architecture/guardrails/software-development/), [Open source and working in the open](https://defra.github.io/architecture/guardrails/open-source/), [Sustainability](https://defra.github.io/architecture/guardrails/sustainability/) | 43 |
| [2. Standards and guardrails before exceptions](https://defra.github.io/architecture/principles/doctrine/#ddts-02) | [1. Delivery-focused architecture](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-01)<br>[6. Secure today, safe tomorrow](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-06) | [Choosing technology](https://defra.github.io/architecture/guardrails/choosing-technology/), [Hosting and platforms](https://defra.github.io/architecture/guardrails/hosting-and-platforms/), [Observability and operations](https://defra.github.io/architecture/guardrails/observability-and-operations/), [Products and platforms](https://defra.github.io/architecture/guardrails/products-and-platforms/), [Software development](https://defra.github.io/architecture/guardrails/software-development/), [Identity and access](https://defra.github.io/architecture/guardrails/identity-and-access/), [Security](https://defra.github.io/architecture/guardrails/security/) | 48 |
| [3. Reuse before buy](https://defra.github.io/architecture/principles/doctrine/#ddts-03) | [3. Maximise value, minimise waste](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-03) | [Choosing technology](https://defra.github.io/architecture/guardrails/choosing-technology/), [Hosting and platforms](https://defra.github.io/architecture/guardrails/hosting-and-platforms/), [Open source and working in the open](https://defra.github.io/architecture/guardrails/open-source/), [Products and platforms](https://defra.github.io/architecture/guardrails/products-and-platforms/), [Software development](https://defra.github.io/architecture/guardrails/software-development/), [Sustainability](https://defra.github.io/architecture/guardrails/sustainability/) | 36 |
| [4. Data is an enterprise asset](https://defra.github.io/architecture/principles/doctrine/#ddts-04) | [4. Clean data, clear decisions](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-04)<br>[5. Connect and collaborate](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-05) | [Artificial intelligence](https://defra.github.io/architecture/guardrails/ai/), [Data](https://defra.github.io/architecture/guardrails/data/), [APIs and integration](https://defra.github.io/architecture/guardrails/apis-and-integration/), [Identity and access](https://defra.github.io/architecture/guardrails/identity-and-access/) | 36 |
| [5. Assume AI until proven otherwise](https://defra.github.io/architecture/principles/doctrine/#ddts-05) | [7. Empower to innovate](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-07)<br>[4. Clean data, clear decisions](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-04) | [Artificial intelligence](https://defra.github.io/architecture/guardrails/ai/), [Open source and working in the open](https://defra.github.io/architecture/guardrails/open-source/), [Data](https://defra.github.io/architecture/guardrails/data/) | 27 |
| [6. Outcomes and services over organisational structures](https://defra.github.io/architecture/principles/doctrine/#ddts-06) | [2. Design for users](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-02)<br>[5. Connect and collaborate](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-05) | [Digital first and end-to-end services](https://defra.github.io/architecture/guardrails/digital-first/), [Front end and accessibility](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/), [APIs and integration](https://defra.github.io/architecture/guardrails/apis-and-integration/), [Identity and access](https://defra.github.io/architecture/guardrails/identity-and-access/) | 24 |
| [7. Digital first where appropriate](https://defra.github.io/architecture/principles/doctrine/#ddts-07) | [2. Design for users](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-02)<br>[8. Right tools, right place](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-08) | [Digital first and end-to-end services](https://defra.github.io/architecture/guardrails/digital-first/), [Front end and accessibility](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/), [Field working and devices](https://defra.github.io/architecture/guardrails/field-working-and-devices/) | 14 |


