---
applicability: tbc
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
    phases: [alpha, beta, live]
    lead_roles: [developer, delivery-manager]
    evidence: Public repository in a Defra GitHub organisation, or a recorded reason for keeping it private
    evidence_by_phase:
      alpha: Code public in a Defra GitHub organisation from the first commit, or a recorded reason for keeping a repository private
      beta: Repositories public, or the reasons for keeping them private reviewed
      live: Repositories still public, or private for a recorded reason
      retire: Repositories archived, not deleted, so the code and decisions stay available
    service_standard_points: [12]
    tcop_points: [3]
  GR-OPEN-02:
    phases: [alpha, beta, live]
    lead_roles: [developer]
    evidence: LICENCE file with the Open Government Licence or MIT licence in every repository
    evidence_by_phase:
      alpha: LICENCE file in every repository from the start
      beta: LICENCE file with the Open Government Licence or MIT licence in every repository
      live: LICENCE file in every new repository
    automated_check: "Guardrail check (tools/guardrail-check): LICENCE file with the Open Government Licence or MIT"
    service_standard_points: [12]
    tcop_points: [3]
  GR-OPEN-03:
    phases: [alpha, beta, live]
    lead_roles: [developer, security-architect]
    evidence: Secret scanning and push protection enabled on every repository
    evidence_by_phase:
      alpha: Secret scanning and push protection on for every repository from the first commit
      beta: Secret scanning and push protection on for every repository
      live: Secret scanning alerts dealt with promptly
    automated_check: "Guardrail check (tools/guardrail-check): secret scanning and push protection turned on, with a token that can read security settings"
    service_standard_points: [12]
    tcop_points: [3, 6]
    sbd_principles: [7]
  GR-OPEN-04:
    phases: [alpha, beta, live]
    lead_roles: [developer]
    evidence: Reuse and upstream contributions noted in ADRs and pull requests
    service_standard_points: [13]
    tcop_points: [3, 8]
  GR-OPEN-05:
    phases: [discovery, alpha, beta, live]
    lead_roles: [delivery-manager]
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

<span class="rfc rfc--should">Should</span> Code is released under the [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) or the MIT licence, with a LICENCE file in every repository.

## GR-OPEN-03 Publish safely {#gr-open-03}

<span class="rfc rfc--should">Should</span> Enable secret scanning and push protection on every repository. Keep secrets, credentials and sensitive configuration out of code.

## GR-OPEN-04 Reuse and contribute back {#gr-open-04}

<span class="rfc rfc--should">Should</span> Use and improve existing open source and Defra components rather than forking or rewriting. Contribute fixes back upstream.

## GR-OPEN-05 Blog and show the thing {#gr-open-05}

<span class="rfc rfc--could">Could</span> Share what you learn on the [Defra Digital blog](https://defradigital.blog.gov.uk/), at show and tells, and in this repository.
