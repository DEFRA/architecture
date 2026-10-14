<!-- https://defra.github.io/architecture/about/roadmap/ | maturity: published | site version 0.3.0 | generated from about/roadmap.md -->

# Roadmap

<p class="lead">What we are working on, what comes next and what we are considering. This site is in <strong>alpha</strong>: we are developing it in the open and it will change as we learn from the teams and partners who use it.</p>

<div class="da-roadmap" markdown>

<section class="da-roadmap__col da-roadmap__col--now" aria-labelledby="roadmap-now" markdown>

<h2 id="roadmap-now"><span class="da-roadmap__tag">Now</span> Iterate, refine and embed guardrails</h2>

- Test the [guardrails](https://defra.github.io/architecture/guardrails/) and [decision check](https://defra.github.io/architecture/governance/decision-check/) with delivery teams and partners, and act on what we learn
- Confirm the content marked **Draft - to be confirmed**, starting with governance, the [NFR targets](https://defra.github.io/architecture/nfrs/catalogue/) and [service tiers](https://defra.github.io/architecture/nfrs/service-tiers/)
- Embed the guardrails in [solution design authorities](https://defra.github.io/architecture/governance/solution-design-authorities/) and the [TDA](https://defra.github.io/architecture/governance/tda/), so reviews start from the same defaults
- Refine the [DDTS doctrine](https://defra.github.io/architecture/principles/doctrine/) with colleagues across DDTS
- Answer the [open questions](https://defra.github.io/architecture/about/open-questions/) - names, lead times, approvals and contacts we have not yet confirmed
- Take the draft guardrails and the [approval status](https://defra.github.io/architecture/about/approval-status/) of each section to the TDA and TGB, and cut the first citable [release](https://defra.github.io/architecture/about/releases/)
- Move the site to a [Defra GitHub organisation](https://defra.github.io/architecture/about/moving-to-defra/), with redirects so existing links keep working

</section>

<section class="da-roadmap__col da-roadmap__col--next" aria-labelledby="roadmap-next" markdown>

<h2 id="roadmap-next"><span class="da-roadmap__tag">Next</span> Capabilities and decisions</h2>

- Refine the [business capabilities](https://defra.github.io/architecture/handrail/business-capabilities/), agreeing the level 2 capabilities with business owners
- Map business capabilities to [technology capabilities](https://defra.github.io/architecture/handrail/technology-capabilities/), and to the products and platforms that deliver them
- Collate [architecture decision records](https://defra.github.io/architecture/governance/architecture-decision-records/) from across Defra into a searchable register, so teams can reuse each other's decisions
- **AI architecture facilitator agent:** with the team's agreement, an agent joins stand-ups and design conversations to:
    - spot decisions as they are made and draft [decision records](https://defra.github.io/architecture/governance/architecture-decision-records/)
    - check them against the [guardrails](https://defra.github.io/architecture/guardrails/) and the [decision check](https://defra.github.io/architecture/governance/decision-check/)
    - raise risks, missing evidence and exceptions early

    A named person always confirms what is recorded ([GR-AI-03](https://defra.github.io/architecture/guardrails/ai/#gr-ai-03)), and the trial will have a DPIA and be published as an algorithmic transparency record ([GR-AI-04](https://defra.github.io/architecture/guardrails/ai/#gr-ai-04))

</section>

<section class="da-roadmap__col da-roadmap__col--later" aria-labelledby="roadmap-later" markdown>

<h2 id="roadmap-later"><span class="da-roadmap__tag">Later</span> Proposed</h2>

- Develop the proposed [service patterns](https://defra.github.io/architecture/patterns/service/) for field inspection, incident response and grants with the teams who own those capabilities
- Grow the [patterns](https://defra.github.io/architecture/patterns/) library, starting with infrastructure patterns
- Measure how quickly teams get to a decision, and publish the results
- **AI tools:** an assistant that answers architecture questions from this site, suggests which guardrails and capabilities apply to a design, and drafts decision records for teams to check
- **Architecture review automation:** extend the [guardrail check](https://defra.github.io/architecture/deliver/guardrail-check/) beyond its first seven guardrails - for example hosting and infrastructure as code - so reviews focus on judgement rather than checklists
- Assess our architecture practice with the cross-government [maturity self-assessment](https://architecture.cddo.cabinetoffice.gov.uk/Tools/index.html), and publish what we will improve
- Move to beta

</section>

</div>

## Done recently

- Structured metadata for every guardrail, with phase and status filters in the [guardrail library](https://defra.github.io/architecture/guardrails/library/)
- [Deliver a service](https://defra.github.io/architecture/deliver/): what each phase needs, with evidence checklists and [getting onto Defra platforms](https://defra.github.io/architecture/deliver/platforms/)
- [Patterns](https://defra.github.io/architecture/patterns/), a [worked example](https://defra.github.io/architecture/patterns/worked-example/) and proposed service patterns for the capability gaps
- [Delivery partners](https://defra.github.io/architecture/about/delivery-partners/): contracting, mobilisation, handover and working with other suppliers
- [Releases](https://defra.github.io/architecture/about/releases/), [approval status](https://defra.github.io/architecture/about/approval-status/), the [exception register](https://defra.github.io/architecture/governance/exception-register/) and [guardrails health](https://defra.github.io/architecture/governance/guardrails-health/)
- The first automated [guardrail check](https://defra.github.io/architecture/deliver/guardrail-check/) for repositories


## Guardrail backlog {#guardrail-backlog}

Work on the roadmap and the backlog is tracked in the repository's GitHub Project - see [where things live](https://defra.github.io/architecture/contribute/where-things-live/#where-to-find-and-change-things).

Guardrails we know we are missing, found by tracing each [doctrine and principle](https://defra.github.io/architecture/principles/#how-the-doctrine-principles-and-guardrails-line-up) to the guardrails that put it into practice. Priorities are a starting point for discussion.

| Priority | Proposed guardrails | The gap | Doctrine and principle |
| --- | --- | --- | --- |
| High | **Agreed Defra on a page** | Publish the agreed enterprise data model to replace the draft [Defra on a page](https://defra.github.io/architecture/data/defra-on-a-page/), with the authoritative source for each entity confirmed | [4. Data is an enterprise asset](https://defra.github.io/architecture/principles/doctrine/#ddts-04) · [Principle 4](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-04) |
| High | **Products and platforms** - drafted as [GR-PROD-01 to 04](https://defra.github.io/architecture/guardrails/products-and-platforms/) | Nothing yet says how to build as products: long-lived product teams, product ownership, contributing back to shared platforms, and retiring products | [1. Platforms before projects](https://defra.github.io/architecture/principles/doctrine/#ddts-01) · [Principles 1 and 3](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-03) |
| High | **Digital first and end-to-end services** - drafted as [GR-DIG-01 to 03](https://defra.github.io/architecture/guardrails/digital-first/) | No guardrail asks teams to challenge paper processes, design across organisational boundaries or provide assisted digital routes | [6. Outcomes over structures](https://defra.github.io/architecture/principles/doctrine/#ddts-06), [7. Digital first](https://defra.github.io/architecture/principles/doctrine/#ddts-07) · [Principle 2](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-02) |
| High | **Field working and end-user devices** - drafted as [GR-FIELD-01 to 04](https://defra.github.io/architecture/guardrails/field-working-and-devices/) | Principle 8 has almost no guardrails: devices suited to the job, offline-first working, connectivity in remote areas and device security | [7. Digital first](https://defra.github.io/architecture/principles/doctrine/#ddts-07) · [Principle 8](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-08) |
| High | **Agentic AI** - drafted as [GR-AI-08 to 11](https://defra.github.io/architecture/guardrails/ai/#gr-ai-08) | AI agents that take actions need extra controls: least-privilege tool access, human approval for consequential actions, audit trails and protection from prompt injection | [5. Assume AI](https://defra.github.io/architecture/principles/doctrine/#ddts-05) · [Principles 6 and 7](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-07) |
| High | **Research data** - drafted as [GR-DATA-10 and 11](https://defra.github.io/architecture/guardrails/data/#gr-data-10), draft for comment | Research recordings, notes and prototypes hold personal data: consent, approved storage and tools, deletion, DPIA screening and no real data in prototypes. Builds on the manual's user research standards | [4. Data is an enterprise asset](https://defra.github.io/architecture/principles/doctrine/#ddts-04) · [Principle 4](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-04) |
| High | **Telling users when things fail or are slow** - drafted as [GR-FE-07](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-07), draft for comment | GR-OPS-04 asks services to degrade gracefully, but nothing asks teams to design what users see when they do | [7. Digital first](https://defra.github.io/architecture/principles/doctrine/#ddts-07) · [Principle 2](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-02) |
| Medium | **Experimentation and sandboxes** | How to experiment safely and quickly: sandbox environments, synthetic data, time-boxed prototypes and the route from experiment to production | [5. Assume AI](https://defra.github.io/architecture/principles/doctrine/#ddts-05) · [Principle 7](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-07) |
| Medium | **Low-code and Power Platform** | Environment strategy, application lifecycle, data loss prevention and support for low-code solutions built outside delivery teams | [3. Reuse before buy](https://defra.github.io/architecture/principles/doctrine/#ddts-03) · [Principle 3](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-03) |
| Medium | **Resilience and continuity** | Business continuity and disaster recovery beyond hosting: dependency mapping, exercising and recovery testing by [service tier](https://defra.github.io/architecture/nfrs/service-tiers/) | [2. Standards before exceptions](https://defra.github.io/architecture/principles/doctrine/#ddts-02) · [Principles 1 and 6](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-06) |
| Medium | **Cost management (FinOps)** | Tagging, budgets and alerts, showing cost per service and per business capability | [3. Reuse before buy](https://defra.github.io/architecture/principles/doctrine/#ddts-03) · [Principle 3](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-03) |
| Medium | **Legacy and technical debt** | A debt register, time-bound exceptions for legacy, and plans to retire systems and archive their data | [1. Platforms before projects](https://defra.github.io/architecture/principles/doctrine/#ddts-01) · [Principle 3](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-03) |
| Medium | **Domains, email and web security** | GOV.UK domain rules, email security (DMARC), cookies and privacy notices | [2. Standards before exceptions](https://defra.github.io/architecture/principles/doctrine/#ddts-02) · [Principle 6](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-06) |
| Low | **Networks and zero trust** | Connectivity between Defra group bodies, partners and clouds, moving to zero trust access | [2. Standards before exceptions](https://defra.github.io/architecture/principles/doctrine/#ddts-02) · [Principle 6](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-06) |
| Low | **Mobile apps** | When a native app is justified rather than a responsive web service | [7. Digital first](https://defra.github.io/architecture/principles/doctrine/#ddts-07) · [Principle 2](https://defra.github.io/architecture/principles/architecture-principles/#gr-prin-02) |

Want to take one on, or think something is missing? [Propose a guardrail](https://github.com/DEFRA/architecture/issues/new?template=guardrail-change.yml).

## Shape the roadmap

Tell us what would help you most. [Open an issue](https://github.com/DEFRA/architecture/issues), comment on an existing one, or raise it with your solution design authority. Significant changes are recorded in [what's new](https://defra.github.io/architecture/about/changelog/).

