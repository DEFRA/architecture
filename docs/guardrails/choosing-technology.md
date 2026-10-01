---
principles: [GR-PRIN-03, GR-PRIN-01]
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

<span class="rfc rfc--must">Must</span> Any new product, platform or significant supplier dependency has a documented exit plan covering data export in open formats, contract terms and an estimate of switching cost.

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
