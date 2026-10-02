---
applicability: tbc
principles: [GR-PRIN-05, GR-PRIN-06]
# Metadata for every guardrail on this page. See the contribution guide for the fields.
guardrail_defaults:
  status: draft
  owner: Architecture team
  automated_check: manual
  last_reviewed: 2026-10-01
  since_version: 0.1.0
guardrails:
  GR-IAM-01:
    phases: [discovery, alpha, beta, live]
    lead_roles: [technical-architect, service-designer]
    evidence: Integration with Defra Customer Identity and the agreed level of identity assurance
    evidence_by_phase:
      discovery: Identity team engaged about the level of identity assurance needed and how users act for organisations
      alpha: Sign-in designed with Defra Customer Identity, and tested with users
      beta: Integration with Defra Customer Identity built and tested
      live: No other sign-in introduced
    service_standard_points: [9, 13]
    tcop_points: [8]
  GR-IAM-02:
    phases: [beta, live]
    lead_roles: [technical-architect]
    evidence: Single sign-on through Microsoft Entra ID with multi-factor authentication and no local staff accounts
    evidence_by_phase:
      beta: Staff sign in through Microsoft Entra ID with multi-factor authentication, and there are no local staff accounts
      live: Staff access reviewed regularly through Entra ID groups
    service_standard_points: [9]
    tcop_points: [6]
  GR-IAM-03:
    phases: [beta, live]
    lead_roles: [security-architect, developer]
    evidence: Role and group model and a record of access reviews
    evidence_by_phase:
      beta: Role and group model built, with users, services and pipelines given only the permissions they need
      live: Record of regular access reviews
      retire: All access to the service's systems and data removed
    tcop_points: [6]
    sbd_principles: [7]
  GR-IAM-04:
    phases: [alpha, beta]
    lead_roles: [developer, technical-architect]
    evidence: Authorisation rules written down and covered by automated tests
  GR-IAM-05:
    phases: [alpha, beta, live]
    lead_roles: [developer]
    evidence: Secrets held in a managed store with rotation and secret scanning enabled
    evidence_by_phase:
      alpha: Secret scanning on from the first commit, and secrets held in a managed store from the start
      beta: All secrets in a managed store with rotation, using workload identity where possible
      live: Secrets rotated, and secret scanning alerts dealt with
      retire: Secrets, keys and credentials revoked
    automated_check: GitHub secret scanning with push protection
    tcop_points: [6]
    sbd_principles: [7]
  GR-IAM-06:
    phases: [beta, live]
    lead_roles: [security-architect]
    evidence: Just-in-time privileged access with phishing-resistant MFA and logs reaching the security operations centre
    evidence_by_phase:
      beta: Just-in-time privileged access with phishing-resistant MFA configured, and logged to the security operations centre
      live: Privileged access reviewed regularly
    sbd_principles: [5, 8]
---

# Identity and access

<p class="lead">Who users are and what they are allowed to do. Getting this right once, centrally, is safer and simpler for everyone.</p>

Technology capabilities [TC01 Customer identity and access](../handrail/technology-capabilities.md#tc01) and [TC02 Staff identity and access](../handrail/technology-capabilities.md#tc02).

## GR-IAM-01 Use the strategic customer identity services {#gr-iam-01}

<span class="rfc rfc--must">Must</span> Services for citizens, farmers and businesses use **Defra Customer Identity (Defra ID)**, which uses GOV.UK One Login and Government Gateway as identity providers, for authentication. Services do not build their own sign-in. See [Defra Customer Identity](https://digital.defra.gov.uk/architecture-and-software-development/defra-customer-identity) in the Defra Digital Service Manual.

**Why:** Users get one account across Defra services, we manage relationships between people and organisations (including agents) once, and we avoid storing credentials.

**How to meet it:** Talk to the Customer Identity team in discovery about the level of identity assurance you need and how the service will represent organisations and agents.

## GR-IAM-02 Staff sign in with Microsoft Entra ID {#gr-iam-02}

<span class="rfc rfc--must">Must</span> Staff-facing services and products, including SaaS, use single sign-on through Microsoft Entra ID with multi-factor authentication. No local staff accounts.

**Why:** Joiners, movers and leavers are handled in one place, and conditional access protects every product.

## GR-IAM-03 Authorise on least privilege {#gr-iam-03}

<span class="rfc rfc--must">Must</span> Users, services and pipelines get only the permissions they need, granted through roles or groups, and reviewed regularly.

## GR-IAM-04 Separate authentication from authorisation {#gr-iam-04}

<span class="rfc rfc--should">Should</span> Use the identity provider to establish who someone is; keep business authorisation rules (for example "can act for this holding") explicit, testable and in the right service.

## GR-IAM-05 No secrets in code {#gr-iam-05}

<span class="rfc rfc--must">Must</span> Secrets, keys and credentials are held in a managed secrets store, rotated, and never committed to source control. Use workload identity in preference to long-lived keys.

**How to meet it:** Enable secret scanning on every repository ([GR-OPEN-03](open-source.md#gr-open-03)).

## GR-IAM-06 Privileged access is controlled and audited {#gr-iam-06}

<span class="rfc rfc--must">Must</span> Production and administrative access is just-in-time, uses phishing-resistant MFA, and is logged to the security operations centre.
