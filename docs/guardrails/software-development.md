---
principles: [GR-PRIN-01, GR-PRIN-03]
# Metadata for every guardrail on this page. See the contribution guide for the fields.
guardrail_defaults:
  status: draft
  owner: Architecture team
  automated_check: manual
  last_reviewed: 2026-10-01
  since_version: 0.1.0
guardrails:
  GR-DEV-01:
    phases: [alpha]
    evidence: ADR recording the reason wherever the service uses a different stack
    service_standard_points: [11]
  GR-DEV-02:
    phases: [alpha, beta, live]
    evidence: All source code in a Defra-owned GitHub organisation from the first commit
    service_standard_points: [12]
  GR-DEV-03:
    phases: [alpha, beta, live]
    evidence: Branch protection on the main branch requiring a review and passing checks
    sbd_principles: [10]
  GR-DEV-04:
    phases: [alpha, beta, live]
    evidence: Pipeline definition in the repository and deployment history
    service_standard_points: [14]
    sbd_principles: [10]
  GR-DEV-05:
    phases: [alpha, beta, live]
    evidence: Test results from the pipeline at each level
  GR-DEV-06:
    phases: [alpha, beta, live]
    evidence: Dependabot or Renovate configuration and runtimes on supported versions
    automated_check: Dependabot or Renovate updates and software composition analysis in the pipeline
  GR-DEV-07:
    phases: [alpha, beta, live]
    evidence: Linting and formatting checks in the pipeline
    automated_check: Lint and format checks in the pipeline
  GR-DEV-08:
    phases: [alpha, beta, live]
    evidence: README explaining what the service does and how to run, test and deploy it, with links to its ADRs
  GR-DEV-09:
    phases: [discovery, alpha, beta, live]
    evidence: ADR log in the repository or linked from its README
    since_version: 0.2.0
---

# Software development

<p class="lead">How we write, test and ship code so that any Defra team, or any partner, can pick it up and run with it.</p>

!!! tip "Looking for detailed coding guidance?"
    These guardrails set the boundaries. The [Defra software development standards](https://defra.github.io/software-development-standards/) are the detailed, practical guide to languages, coding style, testing, source control, versioning and release - follow them for day-to-day engineering.

## GR-DEV-01 Use the supported languages and frameworks {#gr-dev-01}

<span class="rfc rfc--should">Should</span> Use Defra's supported stack for new services so that skills, libraries and support are shared.

| Use | Default | Also supported |
| --- | --- | --- |
| Web front ends and APIs | Node.js (current LTS) with hapi and Nunjucks, using GOV.UK Frontend | - |
| Back-end services | Node.js | .NET (current LTS), where a team or product already uses it |
| Data engineering and analysis | Python | R for analysis |
| Infrastructure | Terraform | Platform-provided templates |

**Why:** A small, well-supported set of technologies makes it easier to move people between teams, share components and support services for the long term.

**How to meet it:** Choosing something else is fine where it is clearly the right tool. Record the reason in an ADR, including how the service will be supported after the team moves on.

## GR-DEV-02 All code in Defra source control {#gr-dev-02}

<span class="rfc rfc--must">Must</span> All source code, including infrastructure and pipeline code written by suppliers, lives in a Defra-owned GitHub organisation from day one.

**Why:** Defra owns what it pays for and must be able to change supplier without losing code or history.

## GR-DEV-03 Protect the main branch {#gr-dev-03}

<span class="rfc rfc--must">Must</span> Main branches are protected: changes arrive through pull requests with at least one review and passing automated checks.

## GR-DEV-04 Continuous integration and delivery {#gr-dev-04}

<span class="rfc rfc--must">Must</span> Every change is built, tested, scanned and deployed by an automated pipeline. Releases to production are small, frequent and reversible.

## GR-DEV-05 Automated testing at the right levels {#gr-dev-05}

<span class="rfc rfc--should">Should</span> Use a balanced set of automated tests - unit, integration/contract, end-to-end journey, accessibility, performance and security - run in the pipeline.

## GR-DEV-06 Manage dependencies actively {#gr-dev-06}

<span class="rfc rfc--must">Must</span> Use automated dependency updates and software composition analysis, and keep runtimes on supported versions.

**Why:** Unpatched dependencies are one of the most common ways services are compromised.

## GR-DEV-07 Follow shared coding standards {#gr-dev-07}

<span class="rfc rfc--should">Should</span> Use automated linting and formatting, and follow the [Defra software development standards](https://defra.github.io/software-development-standards/), so code looks and behaves consistently across teams.

## GR-DEV-08 Document as you go {#gr-dev-08}

<span class="rfc rfc--should">Should</span> Each repository has a README explaining what it does, how to run it locally, how to test it and how to deploy it, and links to its ADRs.

## GR-DEV-09 Record significant decisions as ADRs {#gr-dev-09}

<span class="rfc rfc--should">Should</span> Record significant architecture decisions as [architecture decision records](../governance/architecture-decision-records.md) (ADRs), kept with the code or linked from the repository's README.

**Why:** the reasons behind a design are lost when people move on. ADRs let the next team, an assessor or a partner taking over the service understand what was decided and why, and change it safely.

**How to meet it:** keep ADRs in a `docs/adr` folder in the service repository, using the [ADR template](../governance/templates/adr.md). Write one when you make a decision that is hard to reverse, departs from a guardrail, or that someone will later ask "why did we do this?".
