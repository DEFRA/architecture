# Architecture patterns

<p class="lead">Patterns are reusable shapes for building Defra services. They are early, exploratory work: starting points for discussion, not agreed designs.</p>

There are two kinds:

| Kind | What it covers | Example |
| --- | --- | --- |
| [Service patterns](service/index.md) | The shape of a whole kind of service and how its main building blocks connect | [Transactional digital service](service/transactional-service.md) |
| [Solution patterns](#solution-patterns) | One recurring technical problem inside a service | [File upload and scanning](file-upload.md) |

A service pattern usually uses several solution patterns. The [worked example](worked-example/index.md) shows both together.

!!! note "Looking for design patterns?"
    These are **architecture** patterns: how to build a recurring technical solution. For design patterns - screens, components and user journeys - use the [GOV.UK Design System](https://design-system.service.gov.uk/) and [components and patterns](https://digital.defra.gov.uk/design/components-and-patterns) in the Defra Digital Service Manual.

## Solution patterns

Each solution pattern explains the problem, a solution that stays inside the [guardrails](../guardrails/index.md), and when not to use it. Every solution pattern lists:

- the **context** - the problem and when you will meet it
- the **solution**, with a diagram
- the **guardrails** it helps you meet, so you can cite it in your ADRs and evidence
- related artefacts in the cross-government [Secure by Design artefact library](https://github.com/co-cddo/SbD)
- **when not to use it**

We model this section on the [Department for Education's architecture patterns](https://dfe-digital.github.io/architecture/), and reuse their structure so people moving between departments find their way around.

!!! example "See it all together"
    The [worked example: apply for a licence](worked-example/index.md) follows a fictional Defra service through the transactional service pattern, with C4 diagrams, three sample ADRs and an excerpt from a threat model.

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
