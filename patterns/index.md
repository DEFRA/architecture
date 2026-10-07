<!-- https://defra.github.io/architecture/patterns/ | maturity: published | site version 0.3.0 | generated from patterns/index.md -->

# Architecture patterns

<p class="lead">Patterns are reusable shapes for building Defra services. They are early, exploratory work: starting points for discussion, not agreed designs.</p>

There are two kinds:

| Kind | What it covers | Example |
| --- | --- | --- |
| [Service patterns](https://defra.github.io/architecture/patterns/service/) | The shape of a whole kind of service and how its main building blocks connect | [Transactional digital service](https://defra.github.io/architecture/patterns/service/transactional-service/) |
| [Solution patterns](https://defra.github.io/architecture/patterns/#solution-patterns) | One recurring technical problem inside a service | [File upload and scanning](https://defra.github.io/architecture/patterns/file-upload/) |

A service pattern usually uses several solution patterns. The [worked example](https://defra.github.io/architecture/patterns/worked-example/) shows both together.

!!! note "Looking for design patterns?"
    These are **architecture** patterns: how to build a recurring technical solution. For design patterns - screens, components and user journeys - use the [GOV.UK Design System](https://design-system.service.gov.uk/) and [components and patterns](https://digital.defra.gov.uk/design/components-and-patterns) in the Defra Digital Service Manual.

## Solution patterns

Each solution pattern explains the problem, a solution that stays inside the [guardrails](https://defra.github.io/architecture/guardrails/), and when not to use it. Every solution pattern lists:

- the **context** - the problem and when you will meet it
- the **solution**, with a diagram
- the **guardrails** it helps you meet, so you can cite it in your ADRs and evidence
- related artefacts in the cross-government [Secure by Design artefact library](https://github.com/co-cddo/SbD)
- **when not to use it**

We model this section on the [Department for Education's architecture patterns](https://dfe-digital.github.io/architecture/), and reuse their structure so people moving between departments find their way around.

!!! example "See it all together"
    The [worked example: apply for a licence](https://defra.github.io/architecture/patterns/worked-example/) follows a fictional Defra service through the transactional service pattern, with C4 diagrams, three sample ADRs and an excerpt from a threat model.

## Infrastructure {#infrastructure}

No patterns yet. [Propose one](https://github.com/DEFRA/architecture/issues) if your team has solved a problem others will meet.

## Integration {#integration}

| Pattern | Use it when | Status | User experience | Guardrails |
| --- | --- | --- | --- | --- |
| [Asynchronous submission with an outbox](https://defra.github.io/architecture/patterns/async-submission/) | A user submits something that other systems must process, and you do not want those systems' availability to block the user. | Draft | Written | `GR-API-05`, `GR-API-06`, `GR-API-02`, `GR-OPS-04`, `GR-OPS-02` |

## Security and identity {#security}

| Pattern | Use it when | Status | User experience | Guardrails |
| --- | --- | --- | --- | --- |
| [Acting on behalf of an organisation or holding](https://defra.github.io/architecture/patterns/acting-on-behalf/) | Users act for a business, a land holding or another person, and the service must check they are allowed to. | Draft | Written | `GR-IAM-01`, `GR-IAM-04`, `GR-IAM-03`, `GR-DATA-02`, `GR-SEC-07` |
| [File upload with malware scanning](https://defra.github.io/architecture/patterns/file-upload/) | Users upload documents or images, and the files must be scanned and stored safely before anyone opens them. | Draft | Written | `GR-SEC-04`, `GR-SEC-07`, `GR-HOST-06`, `GR-DATA-06`, `GR-DATA-09`, `GR-OPS-04` |

## Data {#data}

| Pattern | Use it when | Status | User experience | Guardrails |
| --- | --- | --- | --- | --- |
| [Reading from an authoritative source](https://defra.github.io/architecture/patterns/authoritative-source/) | A service needs shared data - customers, organisations, holdings, locations or species - that another part of Defra owns. | Draft | To be confirmed | `GR-DATA-02`, `GR-DATA-03`, `GR-DATA-04`, `GR-API-05`, `GR-API-07`, `GR-OPS-04` |
| [Publishing open data with metadata](https://defra.github.io/architecture/patterns/open-data-publishing/) | You hold non-personal data that others could use, and want to publish it so it can be found, trusted and reused. | Draft | To be confirmed | `GR-DATA-07`, `GR-DATA-05`, `GR-DATA-03`, `GR-DATA-08`, `GR-DATA-01`, `GR-SEC-03` |



## Status

| Status | Means |
| --- | --- |
| Proposed | An idea we want to develop. Comment on it before relying on it. |
| Draft | Written and usable, but not yet reviewed by the [Technical Design Authority](https://defra.github.io/architecture/governance/tda/). |
| Endorsed | Reviewed by the TDA. Following it is a straightforward way to meet the guardrails it lists. |

## User experience

Every pattern has three sections for designers and researchers: **what users see**, **content to design** and **what to test with users**. They link to [GOV.UK Design System](https://design-system.service.gov.uk/) patterns and components where they exist. The catalogue shows whether a pattern's sections are written or still to be confirmed.

## Contribute a pattern

If your team has solved a problem others will meet, write it up. Copy an existing pattern page, keep the same sections, and set its front matter. The [contribution guide](https://defra.github.io/architecture/contribute/#add-a-pattern) explains how.

