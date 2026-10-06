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
  GR-HOST-01:
    phases: [discovery, alpha, beta, live]
    lead_roles: [technical-architect]
    evidence: The service runs on the Core Delivery Platform, or an approved exception
    evidence_by_phase:
      discovery: Platform team engaged, and any hosting needs the Core Delivery Platform might not meet identified
      alpha: The design runs on the Core Delivery Platform, or an exception has been requested
      beta: The service runs on the Core Delivery Platform, or under an approved exception
      live: The service still runs on the platform, and any exception is reviewed before it expires
    service_standard_points: [11]
    tcop_points: [5, 8]
  GR-HOST-02:
    phases: [alpha, beta, live]
    lead_roles: [technical-architect]
    evidence: Hosting design showing a Defra-managed public cloud tenancy
    evidence_by_phase:
      alpha: Where the platform cannot be used, the hosting design uses a Defra-managed public cloud tenancy
      beta: The service runs in a Defra-managed public cloud tenancy
      live: No on-premises hosting introduced
    tcop_points: [5]
  GR-HOST-03:
    phases: [beta, live]
    lead_roles: [developer]
    evidence: Infrastructure, configuration and pipeline code in the repository, and drift detection results
    evidence_by_phase:
      beta: Infrastructure, configuration and pipelines defined as code in the repository, with no manual changes to production
      live: Drift detection running, and no manual changes to production in the change history
    service_standard_points: [14]
    sbd_principles: [10]
  GR-HOST-04:
    phases: [alpha, beta]
    lead_roles: [technical-architect, developer]
    evidence: Hosting design listing the managed services used
    tcop_points: [5]
  GR-HOST-05:
    phases: [alpha, beta, live]
    lead_roles: [developer]
    evidence: Environments created from the same code, and how lower environments avoid real personal data
  GR-HOST-06:
    phases: [alpha, beta, live]
    lead_roles: [technical-architect, security-architect]
    evidence: Data location confirmed for every data store and backup
    evidence_by_phase:
      alpha: Hosting design places every data store and backup in UK regions
      beta: Data location confirmed for every data store and backup as built
      live: Data location checked when new stores or services are added
  GR-HOST-07:
    phases: [alpha, beta, live]
    lead_roles: [technical-architect, product-manager]
    evidence: Agreed recovery time and recovery point objectives, a multi-zone design and the date of the last recovery test
    evidence_by_phase:
      alpha: Recovery time and recovery point objectives agreed with the service owner, and a design that meets them
      beta: Multi-zone design built, and recovery tested before go-live
      live: Recovery tested at least once a year, with the date of the last test
      significant-change: Recovery objectives and design checked for the change
    service_standard_points: [14]
---

# Hosting and platforms

<p class="lead">Where and how services run. Use the paved road so your team can focus on users rather than infrastructure.</p>

Technology capability [Enabling Platforms](../handrail/technology-capabilities.md#enabling-platforms): application hosting and delivery platform.

## GR-HOST-01 Use Defra's strategic delivery platform by default {#gr-host-01}

<span class="rfc rfc--must">Must</span> New digital services are hosted on the **Defra Core Delivery Platform (CDP)** unless an exception has been agreed.

**Why:** CDP provides secure-by-default hosting, CI/CD, observability, secrets management and protective monitoring once, for everyone. Each team that builds its own platform recreates this at its own cost and risk.

**How to meet it:** In discovery or alpha, work with the Delivery Architecture team to decide whether CDP is right for your service - the expectation is that it will be - and engage the platform team. If CDP cannot meet a requirement (for example specialist compute, a SaaS product or a legacy migration), raise an [exception](../governance/exceptions.md) early and tell the platform team - the gap may be something they should solve for everyone.

**In the Defra Digital Service Manual:** [Core Delivery Platform](https://digital.defra.gov.uk/architecture-and-software-development/core-delivery-platform). The manual says a service not on CDP is managed as an exception through the Delivery Architecture team's governance process; how that relates to exceptions on this site is [still being agreed](../governance/exceptions.md#exceptions-to-the-software-development-standards).

## GR-HOST-02 Public cloud first {#gr-host-02}

<span class="rfc rfc--should">Should</span> Where a service cannot use a strategic platform, it is hosted in a Defra-managed public cloud tenancy. New on-premises hosting is not permitted.

**Why:** Government [Cloud First policy](https://www.gov.uk/guidance/government-cloud-first-policy) and Defra's data centre exit.

## GR-HOST-03 Everything as code {#gr-host-03}

<span class="rfc rfc--should">Should</span> Infrastructure, configuration, pipelines and policies are defined as code, version-controlled and deployed through automated pipelines. No manual changes to production.

**Why:** Repeatable, reviewable, recoverable environments. Manual changes cause drift and incidents.

**How to meet it:** Use the platform's provided templates. Where you manage your own infrastructure, use a declarative tool such as Terraform and run drift detection.

## GR-HOST-04 Use managed services before self-managed {#gr-host-04}

<span class="rfc rfc--should">Should</span> Prefer managed cloud services (databases, queues, storage) over running your own on virtual machines.

**Why:** Managed services remove patching and much operational toil.

## GR-HOST-05 Consistent, disposable environments {#gr-host-05}

<span class="rfc rfc--should">Should</span> Have at least development, test and production environments, created from the same code, with production data never copied to lower environments unless anonymised.

## GR-HOST-06 Host data in the UK {#gr-host-06}

<span class="rfc rfc--should">Should</span> Data classified OFFICIAL is held in UK regions unless an assessed and approved exception exists.

**Why:** Data protection, sovereignty and Defra's information risk appetite.

## GR-HOST-07 Design for the resilience the service needs {#gr-host-07}

<span class="rfc rfc--should">Should</span> Agree recovery time and recovery point objectives with the service owner, design to them across availability zones, and test recovery at least once a year.

**Why:** Some Defra services, such as flood warnings and disease control, are critical during emergencies - exactly when infrastructure is under stress.
