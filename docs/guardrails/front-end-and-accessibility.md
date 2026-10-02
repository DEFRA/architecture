---
applicability: tbc
principles: [GR-PRIN-02, GR-PRIN-08]
# Metadata for every guardrail on this page. See the contribution guide for the fields.
guardrail_defaults:
  status: draft
  owner: Architecture team
  automated_check: manual
  last_reviewed: 2026-10-01
  since_version: 0.1.0
guardrails:
  GR-FE-01:
    phases: [alpha, beta, live]
    lead_roles: [interaction-designer, developer]
    evidence: Accessibility audit, assistive technology testing results and a published accessibility statement
    evidence_by_phase:
      alpha: Prototypes built with accessible components, and a plan for an accessibility audit and assistive technology testing
      beta: Accessibility audit and assistive technology testing completed, issues fixed, and an accessibility statement published
      live: Accessibility statement kept current, and accessibility re-tested after significant change
    automated_check: Automated accessibility tests such as axe in the pipeline. These find some issues only; manual testing is still needed.
    service_standard_points: [5]
    tcop_points: [2]
  GR-FE-02:
    phases: [alpha, beta, live]
    lead_roles: [interaction-designer, developer]
    evidence: The service uses GOV.UK Frontend and design decisions record where it departs from the patterns
    evidence_by_phase:
      alpha: Prototypes built with the GOV.UK Design System, with departures recorded and researched
      beta: The service uses GOV.UK Frontend, with design decisions recording any departures
      live: GOV.UK Frontend kept up to date
    service_standard_points: [4, 13]
    tcop_points: [2]
  GR-FE-03:
    phases: [alpha, beta]
    lead_roles: [developer, interaction-designer]
    evidence: Core journeys tested with JavaScript turned off
    service_standard_points: [5]
  GR-FE-04:
    phases: [discovery, alpha]
    lead_roles: [service-designer, technical-architect]
    evidence: ADR noting whether the forms capability was considered
    tcop_points: [8]
  GR-FE-05:
    phases: [alpha, beta]
    lead_roles: [service-designer, user-researcher]
    evidence: Page weight budget, save-progress design and testing on slow connections
    service_standard_points: [5]
  GR-FE-06:
    phases: [alpha, beta, live]
    lead_roles: [content-designer]
    evidence: Assessment of whether the Welsh Language Standards apply and translated content where they do
    evidence_by_phase:
      alpha: Whether the Welsh Language Standards apply decided, and the service designed for translation
      beta: Welsh content and journeys built and tested where the standards apply
      live: Welsh content kept in step with English content
    service_standard_points: [5]
---

# Front end and accessibility

<p class="lead">Defra services should look like government, work for everyone and work on any device.</p>

See the Defra Digital Service Manual for how to do this: [make sure everyone can use the service](https://digital.defra.gov.uk/accessibility), [components and patterns](https://digital.defra.gov.uk/design/components-and-patterns), [content design](https://digital.defra.gov.uk/content) and [Welsh language translation](https://digital.defra.gov.uk/content/welsh-language-translation). These guardrails cover the architecture choices that make it possible.

## GR-FE-01 Meet WCAG 2.2 AA {#gr-fe-01}

<span class="rfc rfc--must">Must</span> Public and staff-facing services meet [WCAG 2.2 level AA](https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps), are tested with assistive technology and publish an accessibility statement.

**Why:** It is the law (Public Sector Bodies Accessibility Regulations 2018) and Service Standard point 5.

## GR-FE-02 Use the GOV.UK Design System {#gr-fe-02}

<span class="rfc rfc--must">Must</span> Public-facing services use [GOV.UK Frontend](https://design-system.service.gov.uk/) and patterns. Staff-facing services should use them too.

## GR-FE-03 Progressive enhancement {#gr-fe-03}

<span class="rfc rfc--should">Should</span> Core journeys work without JavaScript, and are server-rendered. Use JavaScript to enhance, not to make things work.

## GR-FE-04 Consider forms platforms first {#gr-fe-04}

<span class="rfc rfc--should">Should</span> For form-based services, consider the forms capability ([TC03](../handrail/technology-capabilities.md#tc03)) before building a bespoke front end.

## GR-FE-05 Design for low bandwidth and rural users {#gr-fe-05}

<span class="rfc rfc--should">Should</span> Many Defra users - farmers, land managers, field staff - work in places with poor connectivity. Keep pages light, support saving progress, and consider offline working for field tools.

## GR-FE-06 Support Welsh where required {#gr-fe-06}

<span class="rfc rfc--must">Must</span> Services used in Wales meet the Welsh Language Standards where they apply. Design for translation from the start.
