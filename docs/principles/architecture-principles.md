---
# Metadata for every guardrail on this page. See the contribution guide for the fields.
guardrail_defaults:
  status: endorsed
  owner: Architecture team
  automated_check: manual
  last_reviewed: 2026-10-01
  since_version: 0.1.0
---
# Architecture principles

<p class="lead">Defra's eight Strategic Architecture Principles. They make decisions consistent, reduce complexity and stop change fragmenting across services. Use them to govern technology change across Defra so that it supports Defra's strategic goals.</p>

The principles apply the [DDTS doctrine](doctrine.md) to technology change, and every guardrail puts one or more of them into practice - see [how they fit together](index.md). When a guardrail does not give you a direct answer, ask: *which option best fits these principles?*

| # | Principle | In short |
| --- | --- | --- |
| 1 | [Delivery-focused architecture](#gr-prin-01) | Architecture is a service to delivery teams |
| 2 | [Design for users](#gr-prin-02) | Intuitive, accessible, consistent solutions |
| 3 | [Maximise value, minimise waste](#gr-prin-03) | Reuse common capabilities; build less, deliver more |
| 4 | [Clean data, clear decisions](#gr-prin-04) | Data that is accurate, timely and accessible |
| 5 | [Connect and collaborate](#gr-prin-05) | Interoperable services, APIs and seamless data flows |
| 6 | [Secure today, safe tomorrow](#gr-prin-06) | Security proportionate to risk, built in from the start |
| 7 | [Empower to innovate](#gr-prin-07) | Safe spaces and tools to experiment |
| 8 | [Right tools, right place](#gr-prin-08) | Fit-for-purpose tools for every working context |

## GR-PRIN-01 Delivery-focused architecture {#gr-prin-01}

<span class="rfc rfc--principle">Principle</span> Architecture is a service to delivery teams. Architecture principles will support seamless delivery pipelines, enabling rapid, low-risk releases.

**Rationale:** The core purpose of these principles is to support Defra's ability to deliver value continuously and reliably. Without delivery-focused principles, architecture can become a bottleneck rather than a business enabler. Streamlining change with predictable, low-risk releases improves user satisfaction and business responsiveness.

**How to follow it:**

- Keep architectural governance lightweight and built into delivery workflows - automated guardrails over manual reviews.
- Give timely, context-aware guidance aligned with product and delivery cadences.
- Design services for observability so teams can learn quickly and roll back when needed.
- Invest in automation and standardised environments.
- Keep services loosely coupled to allow incremental changes and isolated deployments.

<!-- trace:principle GR-PRIN-01 -->

**See also:** [governance](../governance/index.md), the [decision check](../governance/decision-check.md), [software development](../guardrails/software-development.md), [hosting and platforms](../guardrails/hosting-and-platforms.md), [observability and operations](../guardrails/observability-and-operations.md).

## GR-PRIN-02 Design for users {#gr-prin-02}

<span class="rfc rfc--principle">Principle</span> Create intuitive, accessible, user-friendly and consistent solutions that simplify access and improve user experience.

**Rationale:** Technology should serve the needs of the people using it. Services that are not accessible or fail to meet users' needs introduce friction, reduce adoption and create inequality. Designing with empathy, grounded in research and aligned with accessibility standards, makes solutions inclusive, usable and effective. Use user-centred design methods from inception through delivery.

**How to follow it:**

- Use the common user interface standards and design templates agreed across Defra group, based on government (GDS) standards.
- Design every solution around the customer, colleague and partner experience, to meet agreed service levels.
- Assess off-the-shelf systems against Defra user interface standards to maximise compliance.
- Reuse existing processes for similar user-facing tasks across Defra and its arm's length bodies - issuing permits, managing customer cases - so they feel familiar to users.

<!-- trace:principle GR-PRIN-02 -->

**See also:** [front end and accessibility](../guardrails/front-end-and-accessibility.md), [identity and access](../guardrails/identity-and-access.md), the [Defra Digital Service Manual](https://digital.defra.gov.uk/service-manual).

## GR-PRIN-03 Maximise value, minimise waste {#gr-prin-03}

<span class="rfc rfc--principle">Principle</span> Focus on delivering greater value to customers and citizens through reuse of common capabilities and effective technology management.

**Rationale:** Architecture should guide Defra towards the most value with the least effort and risk. Reusing existing, compliant capabilities reduces duplication, gets services live faster and keeps them consistent and compliant. Minimising waste - of time, budget, technology and effort - supports strategic alignment, efficiency and sustainability. Architecture should help teams "build less and deliver more".

**How to follow it:**

- Evaluate and prioritise reuse of existing platforms, APIs, components and services before starting custom development.
- Maintain an up-to-date catalogue of approved, reusable capabilities - see [technology capabilities](../handrail/technology-capabilities.md).
- Make the health, compliance and ownership of reusable components visible, so teams can make informed reuse decisions.
- Include cost-benefit analysis in architectural decisions to find high-impact, low-effort options.
- Discourage one-off solutions and use patterns that minimise technical debt.
- Include reuse checks in architecture reviews, and require justification for duplicating a capability.

<!-- trace:principle GR-PRIN-03 -->

**See also:** [choosing technology](../guardrails/choosing-technology.md), the [handrail](../handrail/index.md), [hosting and platforms](../guardrails/hosting-and-platforms.md), [open source](../guardrails/open-source.md), [sustainability](../guardrails/sustainability.md).

## GR-PRIN-04 Clean data, clear decisions {#gr-prin-04}

<span class="rfc rfc--principle">Principle</span> Ensure data is clean, accurate, consistent, timely and accessible, using AI to enhance data quality, integration and insights.

**Rationale:** High-quality data is the foundation of good decisions and operational excellence. Inaccurate or unavailable data undermines trust, leads to poor outcomes and increases risk. Services must protect data integrity and accessibility so insight and action can be timely. AI and automation can improve data quality, streamline integration and generate deeper insight.

**How to follow it:**

- Set clear ownership, accountability and policies to maintain data quality standards.
- Automate detecting and correcting data errors at ingestion and throughout the data lifecycle.
- Align data definitions and formats across services and platforms.
- Design for timely data updates and low-latency access.
- Use AI for anomaly detection, predictive data quality, intelligent integration and richer analytics.
- Provide secure, scalable data platforms and APIs for easy, governed access.
- Treat data quality as a prerequisite for analytical and operational decisions.

<!-- trace:principle GR-PRIN-04 -->

**See also:** [data guardrails](../guardrails/data.md), [Defra on a page](../data/defra-on-a-page.md), [data standards](../data/data-standards.md), [artificial intelligence](../guardrails/ai.md).

## GR-PRIN-05 Connect and collaborate {#gr-prin-05}

<span class="rfc rfc--principle">Principle</span> Create a flexible, connected and interoperable ecosystem through integration, automation and AI, to give streamlined user journeys and seamless data flows.

**Rationale:** Defra relies on a network of systems, services and partner organisations. Services designed in isolation fragment journeys and duplicate effort. Services must be interoperable - able to exchange data, trigger actions and adapt across systems - using APIs, integration patterns, automation and orchestration, so Defra can scale and evolve as needs change.

**How to follow it:**

- Expose well-documented, secure, reusable APIs by default.
- Consider how each service fits into wider workflows, data flows and [business capabilities](../handrail/business-capabilities.md).
- Use industry standards to maximise compatibility and future-proofing.
- Invest in a robust integration platform for real-time and batch processing.
- Support event-driven architecture and intelligent automation.
- Enable single sign-on and consistent identity management across services.
- Share clean, consistent, context-rich data while respecting privacy, ethics and compliance.

<!-- trace:principle GR-PRIN-05 -->

**See also:** [APIs and integration](../guardrails/apis-and-integration.md), [identity and access](../guardrails/identity-and-access.md), [data guardrails](../guardrails/data.md).

## GR-PRIN-06 Secure today, safe tomorrow {#gr-prin-06}

<span class="rfc rfc--principle">Principle</span> Implement robust security measures to protect data and systems and maintain a secure environment.

**Rationale:** Security must be part of the architecture, not an afterthought. As threats become more sophisticated, building security in from the outset protects users, safeguards data and keeps Defra compliant. Secure-by-design approaches reduce vulnerabilities early, cut the cost of rework and build trust.

**How to follow it:**

- Manage security in proportion to risk - for example, balancing data security with the need to share data.
- Follow the Defra group Security (DgS) strategy and recommendations.
- Use role-based access control to manage access to system functions and data.

<!-- trace:principle GR-PRIN-06 -->

**See also:** [security guardrails](../guardrails/security.md), [Secure by Design in Defra](../security/secure-by-design.md), [threat modelling](../security/threat-modelling.md).

## GR-PRIN-07 Empower to innovate {#gr-prin-07}

<span class="rfc rfc--principle">Principle</span> Give the business the knowledge and tools to use its creativity to deliver innovative change.

**Rationale:** Innovation keeps Defra resilient and adaptive. It only happens when it is enabled by intentional structures, culture and support: people need the right tools, spaces to experiment and the knowledge to decide well. Architecture should guide technology exploration, lower barriers to experimentation and build innovation into delivery.

**How to follow it:**

- Provide reusable frameworks, playbooks and technology sandboxes for low-friction experimentation.
- Use lightweight governance and automated controls so teams can explore safely within defined boundaries.
- Promote communities of practice, design patterns and internal case studies.
- Encourage experimentation with emerging technologies (such as AI, low-code and digital twins) through pilots.
- Provide non-production environments where teams can test bold ideas safely.
- Bring architects, technologists and business units together to act on innovation opportunities aligned to outcomes.
- Track innovation by value, scalability and learning - not just technical novelty.

<!-- trace:principle GR-PRIN-07 -->

**See also:** [artificial intelligence](../guardrails/ai.md), the [decision check](../governance/decision-check.md), [open source and working in the open](../guardrails/open-source.md).

## GR-PRIN-08 Right tools, right place {#gr-prin-08}

<span class="rfc rfc--principle">Principle</span> Equip staff with the tools and devices they need to communicate and operate effectively in all conditions.

**Rationale:** One-size-fits-all solutions fail people working in laboratories, in the field or in remote areas with limited connectivity. Architecture must support flexible, secure, context-aware device strategies - rugged hardware, offline working, reliable connectivity - so staff can work productively and safely anywhere. Fit-for-purpose equipment directly affects service quality, resilience and user satisfaction.

**How to follow it:**

- Guide the procurement and support of devices suited to the user's context - rugged tablets for fieldwork, secure laptops for remote access, specialist laboratory equipment.
- Support offline-first working and resilient syncing where connectivity is unreliable or absent.
- Provide portable connectivity, mobile data access and satellite support where infrastructure is lacking.
- Extend security policies and controls to every device type and location, with remote updates, encryption and endpoint protection.
- Design IT support for diverse contexts: self-service, remote diagnostics and on-site support.
- Keep devices easy to replace or upgrade as needs change.

<!-- trace:principle GR-PRIN-08 -->

**See also:** [front end and accessibility](../guardrails/front-end-and-accessibility.md#gr-fe-05) (low bandwidth), [field work and inspection](../handrail/technology-capabilities.md#manufacturing-and-delivery), [staff identity](../guardrails/identity-and-access.md#gr-iam-02).

---

<small>Source: Defra Strategic Architecture Principles, owned by the Strategic Architecture team. Changes to these principles are approved by the [Technology Governance Board](../governance/tgb.md).</small>
