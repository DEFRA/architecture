# Software development

<p class="lead">How we write, test and ship code so that any Defra team, or any partner, can pick it up and run with it.</p>

Supports principles [GR-PRIN-07](principles.md#gr-prin-07) and [GR-PRIN-09](principles.md#gr-prin-09).

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

<span class="rfc rfc--should">Should</span> Use automated linting and formatting, and follow Defra's published coding standards, so code looks and behaves consistently across teams.

## GR-DEV-08 Document as you go {#gr-dev-08}

<span class="rfc rfc--should">Should</span> Each repository has a README explaining what it does, how to run it locally, how to test it and how to deploy it, and links to its ADRs.
