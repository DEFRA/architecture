<!-- https://defra.github.io/architecture/deliver/checklists/retire/ | maturity: prototype | site version 0.3.0 | generated from deliver/checklists/retire.md -->

# Retirement evidence checklist

<p class="lead">The architecture evidence for retiring a service, as a checklist you can work through or print. Built from the guardrail metadata each time the site is published.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



Tick what you have, link to where it lives, and bring it to your solution design authority or assessment. Where you cannot meet a Must, record the approved [exception](https://defra.github.io/architecture/governance/exceptions/).

<p class="dl-print"><button type="button" class="md-button" data-print>Print this checklist</button></p>

## Artefacts

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-1"><label for="ck-1"><strong>Architecture decision record (ADR) log</strong> - Record the decision to retire and what replaces the service.</label></li>
<li><input type="checkbox" id="ck-2"><label for="ck-2"><strong>Exit plan</strong> - Carry it out - export data in open formats and end contracts.</label></li>
<li><input type="checkbox" id="ck-3"><label for="ck-3"><strong>Runbooks and support model</strong> - Write the decommissioning runbook and keep it with the archived code.</label></li>
<li><input type="checkbox" id="ck-4"><label for="ck-4"><strong>Data protection impact assessment (DPIA)</strong> - Confirm personal data is deleted or transferred lawfully.</label></li>
</ul>

## Must guardrails

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-5"><label for="ck-5"><a href="../../../guardrails/data/#gr-data-09">GR-DATA-09</a> <strong>Retain and dispose of records properly</strong> - Records kept, transferred to The National Archives or destroyed, as agreed with the information asset owner</label></li>
<li><input type="checkbox" id="ck-6"><label for="ck-6"><a href="../../../guardrails/data/#gr-data-06">GR-DATA-06</a> <strong>Protect personal data by design</strong> - Personal data deleted or transferred lawfully, as set out in the DPIA</label></li>
<li><input type="checkbox" id="ck-7"><label for="ck-7"><a href="../../../guardrails/identity-and-access/#gr-iam-03">GR-IAM-03</a> <strong>Authorise on least privilege</strong> - All access to the service&#x27;s systems and data removed</label></li>
<li><input type="checkbox" id="ck-8"><label for="ck-8"><a href="../../../guardrails/identity-and-access/#gr-iam-05">GR-IAM-05</a> <strong>No secrets in code</strong> - Secrets, keys and credentials revoked</label></li>
<li><input type="checkbox" id="ck-9"><label for="ck-9"><a href="../../../guardrails/open-source/#gr-open-01">GR-OPEN-01</a> <strong>Code in the open</strong> - Repositories archived, not deleted, so the code and decisions stay available</label></li>
</ul>

## Should guardrails

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-10"><label for="ck-10"><a href="../../../guardrails/data/#gr-data-01">GR-DATA-01</a> <strong>Every data set has an owner</strong> - Information asset register updated to show what happened to each data set</label></li>
<li><input type="checkbox" id="ck-11"><label for="ck-11"><a href="../../../guardrails/apis-and-integration/#gr-api-04">GR-API-04</a> <strong>Version and deprecate deliberately</strong> - Consumers told the retirement date in advance, and moved to a replacement</label></li>
<li><input type="checkbox" id="ck-12"><label for="ck-12"><a href="../../../guardrails/choosing-technology/#gr-tech-03">GR-TECH-03</a> <strong>Plan your exit before you enter</strong> - Exit plan carried out - data exported in open formats and contracts ended</label></li>
<li><input type="checkbox" id="ck-13"><label for="ck-13"><a href="../../../guardrails/sustainability/#gr-sus-02">GR-SUS-02</a> <strong>Right-size and switch off</strong> - Autoscaling and out-of-hours schedules for non-production environments</label></li>
</ul>

## Sign-off

| Detail | Answer |
| --- | --- |
| Service | |
| Completed by | |
| Date | |
| Solution design authority | |
| Exceptions or departures (guardrail ids) | |

Read more on the [retire a service page](https://defra.github.io/architecture/deliver/retire/).


