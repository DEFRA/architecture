---
status: draft
---

# Service tiers

<p class="lead">Not every service needs the same level of availability and support. A service tier sets proportionate targets, so critical services get the resilience they need and smaller services are not over-engineered.</p>

## Choosing a tier

Agree the tier with the service owner in discovery, and review it at each phase. Ask:

<!-- nfrs:tier-questions -->

If the answer to either of the first two questions is yes, the service is probably **T1 Critical** or **T2 Important**. If in doubt, ask your [solution design authority](../governance/solution-design-authorities.md).

## The tiers

<!-- nfrs:tiers -->

## What the tier changes

The tier sets the targets for the tiered requirements in the [NFR catalogue](catalogue.md), such as availability, recovery time and alerting. Requirements without tier targets, such as accessibility and security testing, apply to every service whatever its tier.

A higher tier costs more to build and run. Choose the lowest tier that meets user and business needs, and record the choice in an [architecture decision record](../governance/architecture-decision-records.md).
