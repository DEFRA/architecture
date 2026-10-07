<!-- https://defra.github.io/architecture/deliver/checklists/discovery/ | maturity: prototype | site version 0.3.0 | generated from deliver/checklists/discovery.md -->

# Discovery evidence checklist

<p class="lead">The architecture evidence for discovery, as a checklist you can work through or print. Built from the guardrail metadata each time the site is published.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



Tick what you have, link to where it lives, and bring it to your solution design authority or assessment. Where you cannot meet a Must, record the approved [exception](https://defra.github.io/architecture/governance/exceptions/).

<p class="dl-print"><button type="button" class="md-button" data-print>Print this checklist</button></p>

## Artefacts

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-1"><label for="ck-1"><strong>Architecture decision record (ADR) log</strong> - Start the log. Record the reuse options you considered.</label></li>
<li><input type="checkbox" id="ck-2"><label for="ck-2"><strong>C4 system context diagram</strong> - Sketch the context - users, Defra systems and partners involved.</label></li>
<li><input type="checkbox" id="ck-3"><label for="ck-3"><strong>Service tier</strong> - Propose a tier with the service owner.</label></li>
<li><input type="checkbox" id="ck-4"><label for="ck-4"><strong>Data protection impact assessment (DPIA)</strong> - Screen for personal data and decide whether you need a full DPIA.</label></li>
</ul>

## Must guardrails

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-5"><label for="ck-5"><a href="../../../guardrails/ai/#gr-ai-02">GR-AI-02</a> <strong>Use approved AI services and tenancies</strong> - Any AI services you are exploring identified, with the Defra tenancy or enterprise agreement they would run under</label></li>
<li><input type="checkbox" id="ck-6"><label for="ck-6"><a href="../../../guardrails/choosing-technology/#gr-tech-01">GR-TECH-01</a> <strong>Look for something to reuse first</strong> - Existing Defra and cross-government options for the need identified from the technology capability catalogue</label></li>
<li><input type="checkbox" id="ck-7"><label for="ck-7"><a href="../../../guardrails/choosing-technology/#gr-tech-04">GR-TECH-04</a> <strong>Assess SaaS before you adopt it</strong> - SaaS and third-party products under consideration listed, with the assessments they will need</label></li>
<li><input type="checkbox" id="ck-8"><label for="ck-8"><a href="../../../guardrails/choosing-technology/#gr-tech-06">GR-TECH-06</a> <strong>Get spend approval early</strong> - Architecture team consulted before any procurement under spend control starts</label></li>
<li><input type="checkbox" id="ck-9"><label for="ck-9"><a href="../../../guardrails/data/#gr-data-06">GR-DATA-06</a> <strong>Protect personal data by design</strong> - DPIA screening completed, showing whether personal data is involved</label></li>
<li><input type="checkbox" id="ck-10"><label for="ck-10"><a href="../../../guardrails/hosting-and-platforms/#gr-host-01">GR-HOST-01</a> <strong>Use Defra&#x27;s strategic delivery platform by default</strong> - Platform team engaged, and any hosting needs the Core Delivery Platform might not meet identified</label></li>
<li><input type="checkbox" id="ck-11"><label for="ck-11"><a href="../../../guardrails/identity-and-access/#gr-iam-01">GR-IAM-01</a> <strong>Use the strategic customer identity services</strong> - Identity team engaged about the level of identity assurance needed and how users act for organisations</label></li>
<li><input type="checkbox" id="ck-12"><label for="ck-12"><a href="../../../guardrails/security/#gr-sec-01">GR-SEC-01</a> <strong>Follow Secure by Design</strong> - Named risk owner, and the information and threats the service is likely to face identified</label></li>
<li><input type="checkbox" id="ck-13"><label for="ck-13"><a href="../../../guardrails/security/#gr-sec-03">GR-SEC-03</a> <strong>Classify information</strong> - Security classification and the types of data the service will handle identified</label></li>
</ul>

## Should guardrails

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-14"><label for="ck-14"><a href="../../../guardrails/ai/#gr-ai-01">GR-AI-01</a> <strong>Consider AI first</strong> - ADR recording the AI options considered and why they were or were not used</label></li>
<li><input type="checkbox" id="ck-15"><label for="ck-15"><a href="../../../guardrails/ai/#gr-ai-06">GR-AI-06</a> <strong>Talk to the TDA about novel use</strong> - Novel or generative AI use in decision making identified, and a conversation with the Technical Design Authority booked</label></li>
<li><input type="checkbox" id="ck-16"><label for="ck-16"><a href="../../../guardrails/choosing-technology/#gr-tech-02">GR-TECH-02</a> <strong>Buy commodity, build differentiating</strong> - Buy or build options appraisal in the ADR or business case</label></li>
<li><input type="checkbox" id="ck-17"><label for="ck-17"><a href="../../../guardrails/data/#gr-data-02">GR-DATA-02</a> <strong>Use authoritative sources</strong> - Shared entities the service needs identified, with their authoritative sources</label></li>
<li><input type="checkbox" id="ck-18"><label for="ck-18"><a href="../../../guardrails/data/#gr-data-10">GR-DATA-10</a> <strong>Handle research data safely</strong> - Consent forms and privacy notice in use, recordings and notes stored only in approved places, and a deletion date set</label></li>
<li><input type="checkbox" id="ck-19"><label for="ck-19"><a href="../../../guardrails/data/#gr-data-11">GR-DATA-11</a> <strong>No real personal data in prototypes</strong> - Any prototype uses made-up data</label></li>
<li><input type="checkbox" id="ck-20"><label for="ck-20"><a href="../../../guardrails/digital-first/#gr-dig-01">GR-DIG-01</a> <strong>Challenge paper and manual processes</strong> - Discovery findings showing paper, email and manual steps in the current process and how the new design removes or justifies each one</label></li>
<li><input type="checkbox" id="ck-21"><label for="ck-21"><a href="../../../guardrails/digital-first/#gr-dig-02">GR-DIG-02</a> <strong>Design across organisational boundaries</strong> - A map of the whole service, including the parts other teams and organisations deliver, and agreed hand-offs between them</label></li>
<li><input type="checkbox" id="ck-22"><label for="ck-22"><a href="../../../guardrails/field-working-and-devices/#gr-field-01">GR-FIELD-01</a> <strong>Choose devices that suit the job</strong> - User research on the working environment, and the device choice recorded in an ADR</label></li>
<li><input type="checkbox" id="ck-23"><label for="ck-23"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-04">GR-FE-04</a> <strong>Consider forms platforms first</strong> - ADR noting whether the forms capability was considered</label></li>
<li><input type="checkbox" id="ck-24"><label for="ck-24"><a href="../../../guardrails/products-and-platforms/#gr-prod-02">GR-PROD-02</a> <strong>Name the product owner and service owner</strong> - Named product owner and service owner, recorded in the service catalogue</label></li>
<li><input type="checkbox" id="ck-25"><label for="ck-25"><a href="../../../guardrails/software-development/#gr-dev-09">GR-DEV-09</a> <strong>Record significant decisions as ADRs</strong> - ADR log in the repository or linked from its README</label></li>
<li><input type="checkbox" id="ck-26"><label for="ck-26"><a href="../../../guardrails/sustainability/#gr-sus-01">GR-SUS-01</a> <strong>Consider sustainability in design decisions</strong> - Environmental impact recorded in ADRs for hosting and technology choices</label></li>
</ul>

## Could guardrails

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-27"><label for="ck-27"><a href="../../../guardrails/field-working-and-devices/#gr-field-04">GR-FIELD-04</a> <strong>Check connectivity before you design</strong> - Connectivity in the places the service will be used checked, and the approach recorded</label></li>
<li><input type="checkbox" id="ck-28"><label for="ck-28"><a href="../../../guardrails/open-source/#gr-open-05">GR-OPEN-05</a> <strong>Blog and show the thing</strong> - Blog posts, show and tells or contributions to this site</label></li>
</ul>

## Sign-off

| Detail | Answer |
| --- | --- |
| Service | |
| Completed by | |
| Date | |
| Solution design authority | |
| Exceptions or departures (guardrail ids) | |

Read more on the [discovery page](https://defra.github.io/architecture/deliver/discovery/).


