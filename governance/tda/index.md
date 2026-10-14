<!-- https://defra.github.io/architecture/governance/tda/ | maturity: draft | site version 0.3.0 | generated from governance/tda.md -->

# Technical Design Authority (TDA)

<p class="lead">The TDA is Defra's technical decision-making authority. It agrees roadmaps, grants authority to solution design authorities, and reviews cross-cutting and novel work and exceptions to the guardrails. It is a peer review that helps teams get to a good design - not an exam.</p>

!!! warning "Draft - to be confirmed"
    Parts of this page, such as names, timings and thresholds, are still being confirmed by the architecture team. Use it as a guide, and check with your solution design authority before relying on the detail.



## When to come to the TDA

Use [which route do I take?](https://defra.github.io/architecture/governance/triage/). In short, come to the TDA when your work:

- is **novel** for Defra - new technology, pattern or use of AI
- is **cross-cutting** - other services, teams or arm's length bodies will depend on it or be affected by it
- needs an **exception to a Must guardrail**
- fills a **gap** in the [technology capabilities](https://defra.github.io/architecture/handrail/technology-capabilities/)
- is escalated by a [solution design authority](https://defra.github.io/architecture/governance/solution-design-authorities/)

Come **early**. The best time is the end of discovery or early alpha, when changing direction is cheap. You can come more than once.

## What the TDA does

- Reviews designs and gives clear, actionable outcomes
- Approves or declines time-limited exceptions to Must guardrails
- Identifies reuse opportunities between teams
- Feeds lessons into the guardrails and handrail
- Recommends items to the [TGB](https://defra.github.io/architecture/governance/tgb/)

## Membership

Chaired by the Chief Architect or a delegate, with enterprise, solution, data and security architects, platform representatives and, for relevant items, arm's length body architects. Delivery partners presenting on behalf of a Defra team are welcome to attend.

## How it works

| Step | What happens | Timing |
| --- | --- | --- |
| 1. Talk to us | An informal conversation with an architect to shape the submission | Any time |
| 2. Submit | Complete the [TDA submission template](https://defra.github.io/architecture/governance/templates/tda-submission/) and email it with any ADRs and diagrams - see [raise a decision for review](https://defra.github.io/architecture/governance/architecture-decision-records/#raise-a-decision-for-review) | 5 working days before the meeting |
| 3. Review | 30-minute slot: 10 minutes to present, 20 minutes discussion | Fortnightly |
| 4. Outcome | Recorded in the [architecture decision register](https://defra.github.io/architecture/governance/architecture-decision-records/#enterprise-decisions-in-the-architecture-decision-register) and shared within 3 working days | |

## Outcomes

| Outcome | Means |
| --- | --- |
| **Endorsed** | Proceed. |
| **Endorsed with conditions** | Proceed, meeting named conditions by a named date. |
| **Not endorsed** | Rework and come back. The TDA explains why and offers support. |
| **Escalated** | The decision needs the [TGB](https://defra.github.io/architecture/governance/tgb/). |

## What good looks like in a submission

- The **problem and outcome** in plain English, and the [business capabilities](https://defra.github.io/architecture/handrail/business-capabilities/) affected
- The **options considered**, including the strategic options from the handrail, and why you prefer one
- A **context diagram** and a container-level diagram (the [C4 model](https://c4model.com/) works well)
- Which **guardrails** you meet and which you do not
- **Risks**, including security (a current threat model) and data protection
- **What you need from the TDA** - a decision, advice or an exception

Short is better. Five pages is plenty.

