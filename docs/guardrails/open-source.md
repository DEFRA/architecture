---
principles: [GR-PRIN-03, GR-PRIN-07]
# Metadata for every guardrail on this page. See the contribution guide for the fields.
guardrail_defaults:
  status: draft
  owner: Architecture team
  automated_check: manual
  last_reviewed: 2026-10-01
  since_version: 0.1.0
guardrails:
  GR-OPEN-01:
    phases: [discovery, alpha, beta, live]
    evidence: Public repository in a Defra GitHub organisation, or a recorded reason for keeping it private
    service_standard_points: [12]
    tcop_points: [3]
  GR-OPEN-02:
    phases: [alpha, beta, live]
    evidence: LICENCE file with the Open Government Licence or MIT licence in every repository
    service_standard_points: [12]
    tcop_points: [3]
  GR-OPEN-03:
    phases: [alpha, beta, live]
    evidence: Secret scanning and push protection enabled on every repository
    automated_check: GitHub secret scanning with push protection
    service_standard_points: [12]
    tcop_points: [3, 6]
    sbd_principles: [7]
  GR-OPEN-04:
    phases: [alpha, beta, live]
    evidence: Reuse and upstream contributions noted in ADRs and pull requests
    service_standard_points: [13]
    tcop_points: [3, 8]
  GR-OPEN-05:
    phases: [discovery, alpha, beta, live]
    evidence: Blog posts, show and tells or contributions to this site
    tcop_points: [8]
---

# Open source and working in the open

<p class="lead">We code in the open and share what we learn. It improves quality, makes reuse easy and lets partners see how we work before they work with us.</p>

Relates to Service Standard point 12 and TCoP point 3.

## GR-OPEN-01 Code in the open {#gr-open-01}

<span class="rfc rfc--must">Must</span> New source code is public from the start, in a Defra GitHub organisation, unless there is a recorded reason to keep a specific repository private (for example fraud rules or unannounced policy).

**Why:** [Service Standard point 12](https://www.gov.uk/service-manual/service-standard/point-12-make-new-source-code-open). Openness also makes teams more careful about secrets and quality.

## GR-OPEN-02 Licence clearly {#gr-open-02}

<span class="rfc rfc--must">Must</span> Code is released under the [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) or the MIT licence, with a LICENCE file in every repository.

## GR-OPEN-03 Publish safely {#gr-open-03}

<span class="rfc rfc--must">Must</span> Enable secret scanning and push protection on every repository. Keep secrets, credentials and sensitive configuration out of code.

## GR-OPEN-04 Reuse and contribute back {#gr-open-04}

<span class="rfc rfc--should">Should</span> Use and improve existing open source and Defra components rather than forking or rewriting. Contribute fixes back upstream.

## GR-OPEN-05 Blog and show the thing {#gr-open-05}

<span class="rfc rfc--could">Could</span> Share what you learn on the [Defra Digital blog](https://defradigital.blog.gov.uk/), at show and tells, and in this repository.
