---
status: draft
---

# Technology capabilities

Technology capabilities describe what technology must do to enable Defra's business capabilities.

They provide a common language for understanding technology across Defra and help teams:

- identify the capabilities needed to support a service
- discover opportunities for reuse
- align technology decisions with strategic outcomes
- understand where existing platforms and services can be used
- support investment, roadmap and architecture decisions

> Technology capabilities describe **what we need to do**.  
> Guardrails describe **how we recommend doing it**.

---

## Draft - evolving with delivery

Technology capabilities continue to evolve as Defra's services, platforms and technology landscape change.

The capability catalogue is maintained by Strategic Architecture and reflects our current understanding of the capabilities needed across Defra.

Parts of this page, such as names, structures and classifications, may continue to evolve as we mature the model.

---

## Aligned with industry and government models

Defra's technology capability model draws on:

- Technology Business Management (TBM)
- Government capability models
- Defra delivery experience
- Strategic Architecture guidance

Using a common capability language helps teams compare, share and reuse technology across organisational boundaries.

---

## How technology capabilities fit together

Technology capabilities provide the bridge between business needs and technology implementation.

```text
Business Capability
        ↓
Technology Capability
        ↓
Guardrail
        ↓
Reference Architecture
        ↓
Implementation
```

This helps teams answer four simple questions:

1. What capability do we need?
2. Does Defra already provide it?
3. What approach is recommended?
4. Where can we reuse existing platforms and services?

---

## Browse the technology capability catalogue

The authoritative technology capability catalogue is maintained internally by Strategic Architecture.

The catalogue contains:

- capability definitions
- capability hierarchy
- capability ownership
- lifecycle status
- supporting descriptions
- relationships between capabilities

### View the catalogue

➡️ [Technology Capability Catalogue](https://defra.sharepoint.com/teams/Team3221/Lists/Technical%20Capabilities/AllItems.aspx)

---

## Using technology capabilities

### Designing a new service

Identify the technology capabilities required before selecting products, platforms or suppliers.

### Looking for reuse opportunities

Check whether Defra already provides the capability you need before creating a new solution.

### Creating technology strategies and roadmaps

Use capabilities to identify strengths, gaps and investment priorities.

### Supporting architecture decisions

Technology capabilities provide a consistent language for discussing technology choices across teams and organisations.

---

## Related architecture guidance

### Guardrails

Guardrails explain the preferred approaches for delivering technology capabilities.

➡️ ../../guardrails/library/

### Business capabilities

Business capabilities describe what Defra needs to do to deliver outcomes for citizens, customers and partners.

Technology capabilities describe how technology enables those outcomes.

➡️ ../business-capabilities/

### Strategic Architecture Methods & Guidance

Detailed guidance, standards, decision trees, reference architectures and governance information are available internally.

➡️ [Strategic Architecture Methods & Guidance](https://defra.sharepoint.com/teams/Team3221/SitePages/New-Landing-Page.aspx)

---

## Need help?

Not sure which technology capability applies to your work?

Start with the relevant guardrail, review the supporting guidance, or contact Strategic Architecture for assistance.

➡️ [Browse Guardrails]/architecture/guardrails/library/

## Deprecated - don not use

Deprecated - now  aligned to the Defra TBM

# Technology capabilities

<p class="lead">Technology capabilities describe what technology must do to enable Defra's business capabilities, and the strategic option to use first for each.</p>

!!! info "Aligned with the government capability model"
    Each technology capability shows where it sits in the cross-government [Digital Technology Capability Model](https://architecture.cddo.cabinetoffice.gov.uk/digital-capability-model/index.html), from service applications (level 1) to security (level 6). Using the same language as other departments makes it easier to compare, share and reuse.

## The technology stack at a glance

Defra's technology capabilities as layers, from what users touch at the top to the foundations every service runs on. Select a capability for what to use.

<!-- capabilities:stack -->

<!-- capabilities:technology-summary -->

| Status | Meaning | What you should do |
| --- | --- | --- |
| <span class="cap-status cap-status--strategic">Strategic</span> | There is an agreed Defra or cross-government answer. | Use it. Departing from it needs an [ADR](../governance/architecture-decision-records.md) and your SDA's agreement. |
| <span class="cap-status cap-status--emerging">Emerging</span> | An answer is being established. | Talk to the architecture team before choosing, so you can shape it and avoid rework. |
| <span class="cap-status cap-status--gap">Gap</span> | No Defra-wide answer yet. | Raise it with the [TDA](../governance/tda.md). If several teams need it, we should solve it once. |

!!! note "Products named here"
    Products and platforms are named to help teams find the right people quickly. The capability is what matters - products change over time, and this page will be updated when they do.

<!-- capabilities:technology-catalogue -->

