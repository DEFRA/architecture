<!-- https://defra.github.io/architecture/about/using-this-site/ | maturity: published | site version 0.3.0 | generated from about/using-this-site.md -->

# Using this site

<p class="lead">How to find what you need, depending on who you are and what you are doing.</p>

## If you are...

### Starting a new service

Follow [Deliver a service](https://defra.github.io/architecture/deliver/) for the guardrails, artefacts and evidence in each phase. In short:

1. Map your service to the [business capabilities](https://defra.github.io/architecture/handrail/business-capabilities/).
2. Check the [technology capabilities](https://defra.github.io/architecture/handrail/technology-capabilities/) for what to reuse.
3. Start from a [service pattern](https://defra.github.io/architecture/patterns/service/) if one fits.
4. Agree your [service tier](https://defra.github.io/architecture/nfrs/service-tiers/) and pick your [non-functional requirements](https://defra.github.io/architecture/nfrs/catalogue/).
5. Read the [guardrails](https://defra.github.io/architecture/guardrails/) and run the 10-minute self-assurance checklist.
6. Use the [decision check](https://defra.github.io/architecture/governance/decision-check/) to find your governance route.

### A delivery partner

Read [working with us as a delivery partner](https://defra.github.io/architecture/about/delivery-partners/), then the [guardrails](https://defra.github.io/architecture/guardrails/). They describe what we expect from any team building for Defra.

### Making a design decision

Check the relevant [guardrail](https://defra.github.io/architecture/guardrails/), then record your decision as an [ADR](https://defra.github.io/architecture/governance/architecture-decision-records/). If you cannot meet a guardrail, see [exceptions](https://defra.github.io/architecture/governance/exceptions/).

### Preparing for an assessment

Use the [evidence checklist for your phase](https://defra.github.io/architecture/deliver/#phases-and-events). Gather your ADR log, architecture diagrams and [threat model](https://defra.github.io/architecture/security/threat-modelling/), and check the [Defra Digital Service Manual](https://digital.defra.gov.uk/service-manual) for assessment guidance.

### Planning a portfolio

Use [capability mapping](https://defra.github.io/architecture/handrail/capability-mapping/) to find duplication and gaps, and talk to the [architecture team](https://defra.github.io/architecture/about/team/).

## Must, should and could

Throughout this site, **must** means a requirement, **should** means a strong default you can depart from with a recorded reason, and **could** means a recommendation. See [how to read a guardrail](https://defra.github.io/architecture/guardrails/#how-to-read-a-guardrail).

## Searching

Press ++slash++ or ++s++ to search. You can search for guardrail ids (such as `GR-HOST-01`) and business capability ids (such as `BC05`).

## Using this site with tools and AI

The site is published in forms that tools, dashboards and AI assistants can read:

- <a href="../../llms.txt"><code>llms.txt</code></a> - a short guide for AI tools to every page and data file
- a Markdown copy of every page, at the page's address followed by `index.md`
- <a href="../../guardrails.json"><code>guardrails.json</code></a> - every guardrail and principle, with its statement, why, how to meet it, the evidence for each phase and its status
- <a href="../../nfrs.json"><code>nfrs.json</code></a>, <a href="../../capabilities.json"><code>capabilities.json</code></a> and <a href="../../pages.json"><code>pages.json</code></a>

Each page is marked as published, draft or prototype. Treat draft and prototype content as work in progress, not agreed policy. Cite guardrails by their id, such as `GR-HOST-01`, and the [version](https://defra.github.io/architecture/about/releases/) you checked against.

