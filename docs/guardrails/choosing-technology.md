---
applicability: tbc
principles: [GR-PRIN-03, GR-PRIN-01]
# Metadata for every guardrail on this page. See the contribution guide for the fields.
guardrail_defaults:
  status: draft
  owner: Architecture team
  automated_check: manual
  last_reviewed: 2026-10-01
  since_version: 0.1.0
guardrails:
  GR-TECH-01:
    phases: [discovery, alpha]
    lead_roles: [technical-architect]
    evidence: ADR listing the reuse options considered from the technology capability catalogue and cross-government components
    evidence_by_phase:
      discovery: Existing Defra and cross-government options for the need identified from the technology capability catalogue
      alpha: ADR recording the reuse options considered and why they did or did not fit
      significant-change: ADR showing reuse options considered for any new component
    service_standard_points: [13]
    tcop_points: [8]
  GR-TECH-02:
    phases: [discovery, alpha]
    lead_roles: [technical-architect, product-manager]
    evidence: Buy or build options appraisal in the ADR or business case
    service_standard_points: [11]
    tcop_points: [11]
  GR-TECH-03:
    phases: [alpha, beta, live]
    lead_roles: [technical-architect, delivery-manager]
    evidence: Exit plan covering data export in open formats, contract terms and an estimate of switching cost
    evidence_by_phase:
      alpha: Draft exit plan for each new product, platform or significant supplier
      beta: Exit plan agreed, with contracts giving Defra its data and the right to export it in open formats
      live: Exit plan reviewed at contract renewal, with switching cost estimated
      significant-change: Exit plan updated for any new product or supplier
      retire: Exit plan carried out - data exported in open formats and contracts ended
    tcop_points: [11]
  GR-TECH-04:
    phases: [discovery, alpha]
    lead_roles: [security-architect, technical-architect]
    evidence: Supplier security assessment, DPIA where personal data is involved, data location, accessibility and single sign-on confirmed before contract
    evidence_by_phase:
      discovery: SaaS and third-party products under consideration listed, with the assessments they will need
      alpha: Security, data protection, data location, accessibility and single sign-on assessed before contract
    service_standard_points: [9]
    tcop_points: [6, 7, 11]
    sbd_principles: [2]
  GR-TECH-05:
    phases: [alpha]
    lead_roles: [technical-architect]
    evidence: ADR noting the open standards used and how portable the choice is
    service_standard_points: [13]
    tcop_points: [4]
  GR-TECH-06:
    phases: [discovery]
    lead_roles: [delivery-manager, product-manager]
    evidence: Record of the conversation with the architecture team before procurement started
    evidence_by_phase:
      discovery: Architecture team consulted before any procurement under spend control starts
      significant-change: Architecture team consulted before new procurement for the change
    tcop_points: [11]
---

# Choosing technology

<p class="lead">How to decide whether to reuse, buy or build - and how to avoid being stuck with the choice.</p>

## GR-TECH-01 Look for something to reuse first {#gr-tech-01}

<span class="rfc rfc--must">Must</span> Before buying or building, check the [technology capability catalogue](../handrail/technology-capabilities.md) and cross-government components for something that already meets the need.

**Why:** Duplicate capabilities multiply cost, security risk and support effort.

**How to meet it:** Record in your ADR which strategic options you considered and why they did or did not fit. If a strategic option is close but not quite right, talk to the owning platform team before building around it.

## GR-TECH-02 Buy commodity, build differentiating {#gr-tech-02}

<span class="rfc rfc--should">Should</span> Buy or use SaaS for commodity needs (email, HR, finance, CRM, document management). Build only where the capability is specific to Defra's mission and no product fits without heavy customisation.

**Why:** Heavily customised products combine the cost of building with the constraints of buying.

**How to meet it:** If you are configuring more than you are using out of the box, stop and reconsider. Prefer configuration over customisation; avoid modifying vendor code.

## GR-TECH-03 Plan your exit before you enter {#gr-tech-03}

<span class="rfc rfc--should">Should</span> Any new product, platform or significant supplier dependency has a documented exit plan covering data export in open formats, contract terms and an estimate of switching cost.

**Why:** Lock-in is sometimes a sensible trade-off, but it must be a deliberate one.

**How to meet it:** Include an exit section in your ADR or business case. Make sure contracts give Defra ownership of its data and the right to export it.

## GR-TECH-04 Assess SaaS before you adopt it {#gr-tech-04}

<span class="rfc rfc--must">Must</span> SaaS and third-party hosted products are assessed for security, data protection, data location, accessibility and integration before contract.

**Why:** Supply chain risk is one of the biggest sources of security incidents in government.

**How to meet it:** Use the [Secure by Design](../security/secure-by-design.md) supplier assurance activities, complete a DPIA if personal data is involved and confirm the product supports single sign-on with Microsoft Entra ID for staff ([GR-IAM-02](identity-and-access.md#gr-iam-02)).

## GR-TECH-05 Prefer open standards and portable technology {#gr-tech-05}

<span class="rfc rfc--should">Should</span> Choose products and components that use [open standards](https://www.gov.uk/government/publications/open-standards-principles) and can be run on more than one provider.

**Why:** Portability keeps our options open and our commercial position strong.

## GR-TECH-06 Get spend approval early {#gr-tech-06}

<span class="rfc rfc--must">Must</span> Spend that falls under the [government digital and technology spend control](https://www.gov.uk/service-manual/agile-delivery/spend-controls-check-if-you-need-approval-to-spend-money-on-a-service) is discussed with the architecture team before procurement starts.

**Why:** Architecture questions raised at the end of a procurement are expensive to answer.
