---
principles: [GR-PRIN-01, GR-PRIN-03]
applicability: tbc
guardrail_defaults:
  status: draft
  owner: Architecture team
  automated_check: manual
  last_reviewed: 2026-10-01
  since_version: 0.2.0
guardrails:
  GR-PROD-01:
    phases: [alpha, beta, live]
    evidence: A named, long-lived team responsible for the product, with a roadmap beyond the current funding period
    service_standard_points: [6]
  GR-PROD-02:
    phases: [discovery, alpha, beta, live]
    evidence: Named product owner and service owner, recorded in the service catalogue
    service_standard_points: [6]
  GR-PROD-03:
    phases: [alpha, beta, live]
    evidence: Requests and contributions raised with platform teams, and ADRs where the team worked around a platform
    service_standard_points: [13]
    tcop_points: [8]
  GR-PROD-04:
    phases: [live]
    evidence: Product lifecycle stage recorded, with a retirement plan for products being replaced
    tcop_points: [11]
---

# Products and platforms

<p class="lead">Defra builds and runs technology as long-lived products on shared platforms, not as one-off projects. These draft guardrails describe what that means for teams.</p>

Applies the DDTS doctrine [platforms before projects](../principles/doctrine.md#ddts-01).

!!! info "Draft guardrails"
    These guardrails are new drafts from the [guardrail backlog](../about/roadmap.md#guardrail-backlog). Comment on them by [opening an issue](https://github.com/howellsr/architecture/issues).

## GR-PROD-01 Fund and run products, not projects {#gr-prod-01}

<span class="rfc rfc--should">Should</span> Build and run digital services as products, owned by a long-lived team that keeps improving them, rather than as projects that end at go-live.

**Why:** services are used for years. When the team that built a service disbands at launch, knowledge is lost, technical debt grows and the service slowly fails its users.

**How to meet it:** plan funding and team continuity beyond go-live from the start. If a project model is unavoidable, agree before go-live which product team will own the service in live ([GR-OPS-05](observability-and-operations.md#gr-ops-05)).

## GR-PROD-02 Name the product owner and service owner {#gr-prod-02}

<span class="rfc rfc--should">Should</span> Every product has a named product owner, and every service a named service owner, who are accountable for it throughout its life.

**Why:** decisions about priorities, risk and retirement need someone with the authority to make them.

**How to meet it:** record both in the service catalogue and in the repository README, and keep them current when people move on.

## GR-PROD-03 Contribute to platforms rather than working around them {#gr-prod-03}

<span class="rfc rfc--should">Should</span> When a shared platform does not meet a need, raise it with the platform team and contribute to fixing it, rather than building a local workaround.

**Why:** every workaround becomes something else to secure, support and eventually remove, and other teams have the same need.

**How to meet it:** talk to the platform team first. If you must work around a gap to meet a deadline, record it in an ADR with a plan to move back on to the platform.

## GR-PROD-04 Plan for the end of a product's life {#gr-prod-04}

<span class="rfc rfc--should">Should</span> Know where each product is in its lifecycle - growing, stable, being replaced or retiring - and plan its retirement as deliberately as its launch.

**Why:** products that linger after they are replaced keep costing money and carrying risk.

**How to meet it:** record the lifecycle stage in the service catalogue, and follow [retire a service](../deliver/retire.md) when the time comes.
