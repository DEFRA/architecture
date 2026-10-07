<!-- https://defra.github.io/architecture/partners/contracting/ | maturity: published | site version 0.3.0 | generated from partners/contracting.md -->

# Contracting with this site

<p class="lead">How to reference the guardrails in a statement of requirements or statement of work, so buyers and suppliers share one clear, stable baseline.</p>

This page is for Defra commercial teams, delivery leads writing requirements, and suppliers bidding for or delivering Defra work.

<div id="tbc-1"></div>

!!! warning "To be confirmed"
    **TODO:** confirm with Defra commercial and legal teams that the model clauses on this page can be used in Defra contracts, and in which frameworks.

## Cite a fixed version

The site changes often. A contract should point to a **fixed version**, so both sides know exactly what applied when the contract was signed.

Each release of the site is:

- numbered using [semantic versioning](https://semver.org/), for example `0.2.0`
- tagged in the [repository](https://github.com/DEFRA/architecture/tags), for example as `v0.3.0`
- published as a [GitHub release](https://github.com/DEFRA/architecture/releases) with a PDF of every guardrail attached, as an archived copy
- listed in [what's new](https://defra.github.io/architecture/about/changelog/)

Cite it like this:

> Defra architecture guardrails, version 0.3.0, as published at https://github.com/DEFRA/architecture/releases/tag/v0.3.0, including the archived PDF attached to that release.

Version 0.2.0 was released before the site moved to the DEFRA GitHub organisation. It stays at <https://github.com/howellsr/architecture/releases/tag/v0.2.0>, so contracts that cite it remain valid.

Guardrail ids, such as `GR-HOST-01`, never change meaning and are never reused. A guardrail that is no longer needed is marked **deprecated** and points to its replacement, so a reference in an older contract can always be traced.

## Versioning policy

| Change | Example | Version change |
| --- | --- | --- |
| A new Must, a Should raised to a Must, or a Must made stricter | Adding a Must for supplier AI use | **Major** (from 1.0.0 onwards); minor while the site is in alpha (0.x) |
| A Must deprecated or relaxed | Removing a requirement that no longer applies | Major (from 1.0.0); minor in alpha |
| A new Should or Could, new guidance or a new page | A new pattern | Minor |
| Clearer wording that does not change what is required, fixed links | Typo fixes | Patch |

While the site is in **alpha** (versions `0.x`), anything may change between releases. Contracts should cite the version in force at signature, and agree how later versions are adopted.

## Notice period for new Musts

New or stricter Must guardrails do not apply to existing contracts automatically. They apply from the version a contract cites, or from a later version both parties agree to adopt.

<div id="tbc-2"></div>

!!! warning "To be confirmed"
    **TODO:** the notice period Defra gives before a new Must applies to new work, and how it is communicated to suppliers.

## Model clauses

Use or adapt these in a statement of requirements or statement of work. Text in square brackets is for you to complete.

### 1. Guardrails

> The Supplier shall meet every Must guardrail in the Defra architecture guardrails, version [X.Y.Z] (Annex A), unless the Authority has approved an exception through the published [exception process](https://defra.github.io/architecture/governance/exceptions/). Where the Supplier departs from a Should guardrail, it shall record the reason in an architecture decision record and share it with the Authority's solution design authority.

### 2. Non-functional requirements for the service tier

> The Service is service tier [T1 / T2 / T3 / T4], as defined in the Defra [service tiers](https://defra.github.io/architecture/nfrs/service-tiers/), version [X.Y.Z]. The Supplier shall meet the targets for that tier in the Defra [NFR catalogue](https://defra.github.io/architecture/nfrs/catalogue/), version [X.Y.Z], and evidence them through automated testing before each release to production.

### 3. Code and repositories

> All source code, infrastructure code, pipeline definitions and documentation shall be held in a Defra-owned GitHub organisation from the first commit ([GR-DEV-02](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-02)), public unless the Authority agrees a recorded reason ([GR-OPEN-01](https://defra.github.io/architecture/guardrails/open-source/#gr-open-01)), and licensed as required by [GR-OPEN-02](https://defra.github.io/architecture/guardrails/open-source/#gr-open-02). The Authority owns all code and intellectual property created under this contract.

### 4. Architecture decision records

> The Supplier shall record significant architecture decisions as architecture decision records in the service repository ([GR-DEV-09](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-09)), using the Authority's [ADR template](https://defra.github.io/architecture/governance/templates/adr/), from the start of the engagement.

### 5. Secure by Design

> The Supplier shall carry out the [Secure by Design](https://defra.github.io/architecture/security/secure-by-design/) activities for each phase, and provide and keep current the threat model ([GR-SEC-02](https://defra.github.io/architecture/guardrails/security/#gr-sec-02)), security risk records ([GR-SEC-09](https://defra.github.io/architecture/guardrails/security/#gr-sec-09)) and IT health check remediation ([GR-SEC-06](https://defra.github.io/architecture/guardrails/security/#gr-sec-06)). The Supplier shall support the Authority's named risk owner.

### 6. AI coding assistants

> The Supplier shall use AI coding assistants on the Authority's work only as set out in [GR-AI-07](https://defra.github.io/architecture/guardrails/ai/#gr-ai-07), and only tools that meet [GR-AI-02](https://defra.github.io/architecture/guardrails/ai/#gr-ai-02).

### 7. Exit and handover

> The Supplier shall maintain an exit plan ([GR-TECH-03](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03)) and, at the end of the contract or on request, hand over the Service so that it meets the Authority's [handover definition of done](https://defra.github.io/architecture/partners/handover-and-exit/). The Supplier shall co-operate with any incoming supplier during transition.

## Annex A: Must guardrails

Generated from the guardrails on this site. For a contract, use the PDF attached to the release you cite rather than this live list.

There are **29** Must guardrails.

| Guardrail | Requirement | Evidence | Since |
| --- | --- | --- | --- |
| <a href="../../guardrails/ai/#gr-ai-02">GR-AI-02</a> Use approved AI services and tenancies | Services you build run their AI in Defra's cloud tenancies or under approved enterprise agreements. When anyone uses an AI tool, they put Defra data into it only as the using data with AI rules in the AI digital toolkit allow - for example, never OFFICIAL-SENSITIVE or personal data in a public consumer tool. | List of the AI services the service uses and the Defra tenancy or enterprise agreement each runs under | 0.1.0 |
| <a href="../../guardrails/ai/#gr-ai-03">GR-AI-03</a> Keep a human accountable | Decisions with legal or significant effects on people or organisations - such as licensing, enforcement or payments - have meaningful human oversight, and the ability to challenge. | Design of the human oversight and challenge route, tested with users | 0.1.0 |
| <a href="../../guardrails/ai/#gr-ai-04">GR-AI-04</a> Be transparent | Publish an Algorithmic Transparency Recording Standard record for algorithmic tools that meet its scope, and tell users when they are interacting with AI. | Link to the published Algorithmic Transparency Recording Standard record and the AI notice shown to users | 0.1.0 |
| <a href="../../guardrails/apis-and-integration/#gr-api-07">GR-API-07</a> Secure every API | All APIs authenticate callers (OAuth 2.0 / OpenID Connect or mutual TLS), authorise every request, validate input and apply rate limiting. No API is "internal so it's safe". | Authentication and authorisation design, rate limits and input validation, covered by security testing | 0.1.0 |
| <a href="../../guardrails/choosing-technology/#gr-tech-01">GR-TECH-01</a> Look for something to reuse first | Before buying or building, check the technology capability catalogue and cross-government components for something that already meets the need. | ADR listing the reuse options considered from the technology capability catalogue and cross-government components | 0.1.0 |
| <a href="../../guardrails/choosing-technology/#gr-tech-04">GR-TECH-04</a> Assess SaaS before you adopt it | SaaS and third-party hosted products are assessed for security, data protection, data location, accessibility and integration before contract. | Supplier security assessment, DPIA where personal data is involved, data location, accessibility and single sign-on confirmed before contract | 0.1.0 |
| <a href="../../guardrails/choosing-technology/#gr-tech-06">GR-TECH-06</a> Get spend approval early | Spend that falls under the government digital and technology spend control is discussed with the architecture team before procurement starts. | Record of the conversation with the architecture team before procurement started | 0.1.0 |
| <a href="../../guardrails/data/#gr-data-06">GR-DATA-06</a> Protect personal data by design | Complete a data protection impact assessment (DPIA) before processing personal data, minimise what you collect, and apply retention and deletion automatically. | Approved DPIA, and retention and deletion built into the service | 0.1.0 |
| <a href="../../guardrails/data/#gr-data-09">GR-DATA-09</a> Retain and dispose of records properly | Apply Defra's retention schedules. Records of permanent value are identified for transfer to The National Archives. | Retention schedule applied and records of permanent value identified | 0.1.0 |
| <a href="../../guardrails/front-end-and-accessibility/#gr-fe-01">GR-FE-01</a> Meet WCAG 2.2 AA | Public and staff-facing services meet WCAG 2.2 level AA, are tested with assistive technology and publish an accessibility statement. | Accessibility audit, assistive technology testing results and a published accessibility statement | 0.1.0 |
| <a href="../../guardrails/front-end-and-accessibility/#gr-fe-02">GR-FE-02</a> Use the GOV.UK Design System | Public-facing services use GOV.UK Frontend and patterns. Staff-facing services should use them too. | The service uses GOV.UK Frontend and design decisions record where it departs from the patterns | 0.1.0 |
| <a href="../../guardrails/front-end-and-accessibility/#gr-fe-06">GR-FE-06</a> Support Welsh where required | Services used in Wales meet the Welsh Language Standards where they apply. Design for translation from the start. | Assessment of whether the Welsh Language Standards apply and translated content where they do | 0.1.0 |
| <a href="../../guardrails/hosting-and-platforms/#gr-host-01">GR-HOST-01</a> Use Defra's strategic delivery platform by default | New digital services are hosted on the Defra Core Delivery Platform (CDP) unless an exception has been agreed. | The service runs on the Core Delivery Platform, or an approved exception | 0.1.0 |
| <a href="../../guardrails/identity-and-access/#gr-iam-01">GR-IAM-01</a> Use the strategic customer identity services | Services for citizens, farmers and businesses use Defra Customer Identity (Defra ID), which uses GOV.UK One Login and Government Gateway as identity providers, for authentication. Services do not build their own sign-in. See Defra Customer Identity in the Defra Digital Service Manual. | Integration with Defra Customer Identity and the agreed level of identity assurance | 0.1.0 |
| <a href="../../guardrails/identity-and-access/#gr-iam-02">GR-IAM-02</a> Staff sign in with Microsoft Entra ID | Staff-facing services and products, including SaaS, use single sign-on through Microsoft Entra ID with multi-factor authentication. No local staff accounts. | Single sign-on through Microsoft Entra ID with multi-factor authentication and no local staff accounts | 0.1.0 |
| <a href="../../guardrails/identity-and-access/#gr-iam-03">GR-IAM-03</a> Authorise on least privilege | Users, services and pipelines get only the permissions they need, granted through roles or groups, and reviewed regularly. | Role and group model and a record of access reviews | 0.1.0 |
| <a href="../../guardrails/identity-and-access/#gr-iam-05">GR-IAM-05</a> No secrets in code | Secrets, keys and credentials are held in a managed secrets store, rotated, and never committed to source control. Use workload identity in preference to long-lived keys. | Secrets held in a managed store with rotation and secret scanning enabled | 0.1.0 |
| <a href="../../guardrails/identity-and-access/#gr-iam-06">GR-IAM-06</a> Privileged access is controlled and audited | Production and administrative access is just-in-time, uses phishing-resistant MFA, and is logged to the security operations centre. | Just-in-time privileged access with phishing-resistant MFA and logs reaching the security operations centre | 0.1.0 |
| <a href="../../guardrails/observability-and-operations/#gr-ops-05">GR-OPS-05</a> Be ready for live before you go live | Before public beta, agree the support model, on-call arrangements, runbooks, incident process and who owns the service in live. Register the service in the service catalogue. | Support model, on-call arrangements, runbooks, incident process, named live owner and service catalogue entry | 0.1.0 |
| <a href="../../guardrails/open-source/#gr-open-01">GR-OPEN-01</a> Code in the open | New source code is public from the start, in a Defra GitHub organisation, unless there is a recorded reason to keep a specific repository private (for example fraud rules or unannounced policy). | Public repository in a Defra GitHub organisation, or a recorded reason for keeping it private | 0.1.0 |
| <a href="../../guardrails/security/#gr-sec-01">GR-SEC-01</a> Follow Secure by Design | Every new service and significant change follows the Secure by Design activities, with a named risk owner, from discovery onward. | Named risk owner and the Secure by Design activities completed for the phase | 0.1.0 |
| <a href="../../guardrails/security/#gr-sec-02">GR-SEC-02</a> Keep a current threat model | Each service has a threat model, created by the team in alpha and revisited at every significant change and at least annually. | Current, dated threat model, reviewed at the last significant change and at least annually | 0.1.0 |
| <a href="../../guardrails/security/#gr-sec-03">GR-SEC-03</a> Classify information | Identify the government security classification and data types the service handles, and design controls to match. | Security classification and data types recorded with the controls that match them | 0.1.0 |
| <a href="../../guardrails/security/#gr-sec-04">GR-SEC-04</a> Encrypt in transit and at rest | Use TLS 1.2 or higher for all traffic, internal and external, and encrypt data at rest using platform-managed or customer-managed keys. | TLS configuration and encryption at rest settings for every data store | 0.1.0 |
| <a href="../../guardrails/security/#gr-sec-05">GR-SEC-05</a> Scan continuously and fix quickly | Run static analysis, dependency, container and infrastructure scanning in the pipeline. Fix critical vulnerabilities within 14 days and high within 30 days, or record a risk decision. | Pipeline scanning results and the time taken to fix critical and high vulnerabilities | 0.1.0 |
| <a href="../../guardrails/security/#gr-sec-06">GR-SEC-06</a> Test before go-live and after major change | Commission an independent IT health check (penetration test) proportionate to risk before go-live and after significant change, and track remediation. | IT health check report and remediation tracker | 0.1.0 |
| <a href="../../guardrails/security/#gr-sec-07">GR-SEC-07</a> Log for detection and response | Send security-relevant events (authentication, authorisation failures, administrative actions, data exports) to the security operations centre. See GR-OPS-01. | Security-relevant events reaching the security operations centre | 0.1.0 |
| <a href="../../guardrails/security/#gr-sec-09">GR-SEC-09</a> Manage risk explicitly | Where a control cannot be met, record the risk and get it accepted by the right owner through the security exception process. Accepted risks are time-limited. | Risk register entries with an owner and an expiry date for every accepted risk | 0.1.0 |
| <a href="../../guardrails/software-development/#gr-dev-02">GR-DEV-02</a> All code in Defra source control | All source code, including infrastructure and pipeline code written by suppliers, lives in a Defra-owned GitHub organisation from day one. | All source code in a Defra-owned GitHub organisation from the first commit | 0.1.0 |


