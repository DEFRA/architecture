---
hide:
  - toc
---

# Roadmap

<p class="lead">What we are working on, what comes next and what we are considering. This site is in <strong>alpha</strong>: we are developing it in the open and it will change as we learn from the teams and partners who use it.</p>

<div class="da-roadmap" markdown>

<section class="da-roadmap__col da-roadmap__col--now" aria-labelledby="roadmap-now" markdown>

<h2 id="roadmap-now"><span class="da-roadmap__tag">Now</span> Iterate, refine and embed guardrails</h2>

- Test the [guardrails](../guardrails/index.md) and [decision check](../governance/decision-check.md) with delivery teams and partners, and act on what we learn
- Confirm the content marked **Draft - to be confirmed**, starting with governance, the [NFR targets](../nfrs/catalogue.md) and [service tiers](../nfrs/service-tiers.md)
- Embed the guardrails in [solution design authorities](../governance/solution-design-authorities.md) and the [TDA](../governance/tda.md), so reviews start from the same defaults
- Refine the [DDTS doctrine](../principles/doctrine.md) with colleagues across DDTS

</section>

<section class="da-roadmap__col da-roadmap__col--next" aria-labelledby="roadmap-next" markdown>

<h2 id="roadmap-next"><span class="da-roadmap__tag">Next</span> Capabilities and decisions</h2>

- Refine the [business capabilities](../handrail/business-capabilities.md), agreeing the level 2 capabilities with business owners
- Map business capabilities to [technology capabilities](../handrail/technology-capabilities.md), and to the products and platforms that deliver them
- Collate [architecture decision records](../governance/architecture-decision-records.md) from across Defra into a searchable register, so teams can reuse each other's decisions
- **AI architecture facilitator agent:** with the team's agreement, an agent joins stand-ups and design conversations to:
    - spot decisions as they are made and draft [decision records](../governance/architecture-decision-records.md)
    - check them against the [guardrails](../guardrails/index.md) and the [decision check](../governance/decision-check.md)
    - raise risks, missing evidence and exceptions early

    A named person always confirms what is recorded ([GR-AI-03](../guardrails/ai.md#gr-ai-03)), and the trial will have a DPIA and be published as an algorithmic transparency record ([GR-AI-04](../guardrails/ai.md#gr-ai-04))

</section>

<section class="da-roadmap__col da-roadmap__col--later" aria-labelledby="roadmap-later" markdown>

<h2 id="roadmap-later"><span class="da-roadmap__tag">Later</span> Proposed</h2>

- Add [reference architectures](../handrail/reference-architectures/index.md) for the capability gaps: field inspection, incident response, grants
- Build a library of reusable patterns, linked to the [Secure by Design artefact library](https://github.com/co-cddo/SbD)
- Measure how quickly teams get to a decision, and publish the results
- **AI tools:** an assistant that answers architecture questions from this site, suggests which guardrails and capabilities apply to a design, and drafts decision records for teams to check
- **Architecture review automation:** check guardrails automatically in delivery pipelines - for example hosting, secrets, dependencies and API specifications - so reviews focus on judgement rather than checklists
- Assess our architecture practice with the cross-government [maturity self-assessment](https://architecture.cddo.cabinetoffice.gov.uk/Tools/index.html), and publish what we will improve
- Move to beta, and to the Defra GitHub organisation

</section>

</div>

## Shape the roadmap

Tell us what would help you most. [Open an issue](https://github.com/howellsr/architecture/issues), comment on an existing one, or raise it with your solution design authority. Significant changes are recorded in [what's new](changelog.md).
