<!-- https://defra.github.io/architecture/nfrs/service-tiers/ | maturity: draft | site version 0.3.0 | generated from nfrs/service-tiers.md -->

# Service tiers

<p class="lead">Not every service needs the same level of availability and support. A service tier sets proportionate targets, so critical services get the resilience they need and smaller services are not over-engineered.</p>

!!! warning "Draft - to be confirmed"
    Parts of this page, such as names, timings and thresholds, are still being confirmed by the architecture team. Use it as a guide, and check with your solution design authority before relying on the detail.



## Choosing a tier

Agree the tier with the service owner in discovery, and review it at each phase. Ask:

1. Could a failure put people, animals, plants or the environment at risk?
1. Does the service support a statutory duty or legal deadline?
1. How much money flows through it, and what happens if payments are late?
1. How many users depend on it, and is there another channel they could use?
1. Would an outage be reported in the media or raised in Parliament?


If the answer to either of the first two questions is yes, the service is probably **T1 Critical** or **T2 Important**. If in doubt, ask your [solution design authority](https://defra.github.io/architecture/governance/solution-design-authorities/).

## The tiers

| | **T1 Critical** | **T2 Important** | **T3 Standard** | **T4 Low** |
| --- | --- | --- | --- | --- |
| **When to use it** | Failure puts life, animal or plant health, the environment or national infrastructure at risk, or stops a statutory duty with no workaround. | Failure causes significant harm to users, revenue or reputation, but a short outage can be managed with a workaround. | Failure is an inconvenience. Users can wait or use another channel until the service returns. | Short-lived, experimental or low-use services where failure has little impact. |
| **Examples** | Flood warnings, animal disease control, payments at statutory deadlines | Licensing and permitting services, grant applications | Information services, most internal staff tools | Prototypes, private beta, internal reporting |
| **Availability** | 99.9% | 99.5% | 99% | Best effort |
| **Support hours** | 24 hours a day, 7 days a week | 7am to 8pm, Monday to Saturday | 8am to 6pm, Monday to Friday | 9am to 5pm, Monday to Friday |
| **Recovery time objective (RTO)** | 4 hours | 24 hours | 3 working days | 5 working days |
| **Recovery point objective (RPO)** | 15 minutes | 1 hour | 24 hours | 24 hours |
| **Disaster recovery test** | Every 6 months | Every year | Every year | Restore from backup tested once |


## What the tier changes

The tier sets the targets for the tiered requirements in the [NFR catalogue](https://defra.github.io/architecture/nfrs/catalogue/), such as availability, recovery time and alerting. Requirements without tier targets, such as accessibility and security testing, apply to every service whatever its tier.

A higher tier costs more to build and run. Choose the lowest tier that meets user and business needs, and record the choice in an [architecture decision record](https://defra.github.io/architecture/governance/architecture-decision-records/).

