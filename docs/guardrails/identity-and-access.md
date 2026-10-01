---
principles: [GR-PRIN-05, GR-PRIN-06]
---

# Identity and access

<p class="lead">Who users are and what they are allowed to do. Getting this right once, centrally, is safer and simpler for everyone.</p>

Technology capabilities [TC01 Customer identity and access](../handrail/technology-capabilities.md#tc01) and [TC02 Staff identity and access](../handrail/technology-capabilities.md#tc02).

## GR-IAM-01 Use the strategic customer identity services {#gr-iam-01}

<span class="rfc rfc--must">Must</span> Services for citizens, farmers and businesses use **Defra Identity (Defra ID)** and/or **GOV.UK One Login** for authentication. Services do not build their own sign-in.

**Why:** Users get one account across Defra services, we manage relationships between people and organisations (including agents) once, and we avoid storing credentials.

**How to meet it:** Talk to the identity team in discovery about the level of identity assurance you need and how the service will represent organisations and agents.

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
