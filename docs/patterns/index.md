# Architecture patterns

<p class="lead">Proven technical solutions to problems Defra teams meet again and again. Each pattern explains the problem, a solution that stays inside the guardrails, and when not to use it.</p>

!!! note "Looking for design patterns?"
    These are **architecture** patterns: how to build a recurring technical solution. For design patterns - screens, components and user journeys - use the [GOV.UK Design System](https://design-system.service.gov.uk/) and [components and patterns](https://digital.defra.gov.uk/design/components-and-patterns) in the Defra Digital Service Manual.

Patterns sit between the [guardrails](../guardrails/index.md), which say what good looks like, and the [reference architectures](../handrail/reference-architectures/index.md), which show the shape of a whole service. A pattern solves one recurring problem inside a service.

Every pattern lists:

- the **context** - the problem and when you will meet it
- the **solution**, with a diagram
- the **guardrails** it helps you meet, so you can cite it in your ADRs and evidence
- related artefacts in the cross-government [Secure by Design artefact library](https://github.com/co-cddo/SbD)
- **when not to use it**

We model this section on the [Department for Education's architecture patterns](https://dfe-digital.github.io/architecture/), and reuse their structure so people moving between departments find their way around.

!!! example "See it all together"
    The [worked example: apply for a licence](worked-example/index.md) follows a fictional Defra service through the transactional reference architecture, with C4 diagrams, three sample ADRs and an excerpt from a threat model.

<!-- patterns:catalogue -->

## Status

| Status | Means |
| --- | --- |
| Proposed | An idea we want to develop. Comment on it before relying on it. |
| Draft | Written and usable, but not yet reviewed by the [Technical Design Authority](../governance/tda.md). |
| Endorsed | Reviewed by the TDA. Following it is a straightforward way to meet the guardrails it lists. |

## User experience

Every pattern has three sections for designers and researchers: **what users see**, **content to design** and **what to test with users**. They link to [GOV.UK Design System](https://design-system.service.gov.uk/) patterns and components where they exist. The catalogue shows whether a pattern's sections are written or still to be confirmed.

## Contribute a pattern

If your team has solved a problem others will meet, write it up. Copy an existing pattern page, keep the same sections, and set its front matter. The [contribution guide](../contribute/index.md#add-a-pattern) explains how.
