---
principles: [GR-PRIN-03, GR-PRIN-01]
---

# Hosting and platforms

<p class="lead">Where and how services run. Use the paved road so your team can focus on users rather than infrastructure.</p>

Technology capability [TC21 Application hosting and delivery platform](../handrail/technology-capabilities.md#tc21).

## GR-HOST-01 Use Defra's strategic delivery platform by default {#gr-host-01}

<span class="rfc rfc--must">Must</span> New digital services are hosted on the **Defra Core Delivery Platform (CDP)** unless an exception has been agreed.

**Why:** CDP provides secure-by-default hosting, CI/CD, observability, secrets management and protective monitoring once, for everyone. Each team that builds its own platform recreates this at its own cost and risk.

**How to meet it:** Engage the platform team during discovery or alpha. If CDP cannot meet a requirement (for example specialist compute, a SaaS product or a legacy migration), raise an [exception](../governance/exceptions.md) early and tell the platform team - the gap may be something they should solve for everyone.

## GR-HOST-02 Public cloud first {#gr-host-02}

<span class="rfc rfc--must">Must</span> Where a service cannot use a strategic platform, it is hosted in a Defra-managed public cloud tenancy. New on-premises hosting is not permitted.

**Why:** Government [Cloud First policy](https://www.gov.uk/guidance/government-cloud-first-policy) and Defra's data centre exit.

## GR-HOST-03 Everything as code {#gr-host-03}

<span class="rfc rfc--must">Must</span> Infrastructure, configuration, pipelines and policies are defined as code, version-controlled and deployed through automated pipelines. No manual changes to production.

**Why:** Repeatable, reviewable, recoverable environments. Manual changes cause drift and incidents.

**How to meet it:** Use the platform's provided templates. Where you manage your own infrastructure, use a declarative tool such as Terraform and run drift detection.

## GR-HOST-04 Use managed services before self-managed {#gr-host-04}

<span class="rfc rfc--should">Should</span> Prefer managed cloud services (databases, queues, storage) over running your own on virtual machines.

**Why:** Managed services remove patching and much operational toil.

## GR-HOST-05 Consistent, disposable environments {#gr-host-05}

<span class="rfc rfc--should">Should</span> Have at least development, test and production environments, created from the same code, with production data never copied to lower environments unless anonymised.

## GR-HOST-06 Host data in the UK {#gr-host-06}

<span class="rfc rfc--must">Must</span> Data classified OFFICIAL is held in UK regions unless an assessed and approved exception exists.

**Why:** Data protection, sovereignty and Defra's information risk appetite.

## GR-HOST-07 Design for the resilience the service needs {#gr-host-07}

<span class="rfc rfc--must">Must</span> Agree recovery time and recovery point objectives with the service owner, design to them across availability zones, and test recovery at least once a year.

**Why:** Some Defra services, such as flood warnings and disease control, are critical during emergencies - exactly when infrastructure is under stress.
