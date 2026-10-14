<!-- https://defra.github.io/architecture/deliver/checklists/significant-change/ | maturity: prototype | site version 0.3.0 | generated from deliver/checklists/significant-change.md -->

# Significant change evidence checklist

<p class="lead">The architecture evidence for significant change, as a checklist you can work through or print. Built from the guardrail metadata each time the site is published.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



Tick what you have, link to where it lives, and bring it to your solution design authority or assessment. Where you cannot meet a Must, record the approved [exception](https://defra.github.io/architecture/governance/exceptions/).

<p class="dl-print"><button type="button" class="md-button" data-print>Print this checklist</button></p>

## Artefacts

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-1"><label for="ck-1"><strong>Architecture decision record (ADR) log</strong> - Record the change, the options and why.</label></li>
<li><input type="checkbox" id="ck-2"><label for="ck-2"><strong>C4 container diagram</strong> - Update it before you build.</label></li>
<li><input type="checkbox" id="ck-3"><label for="ck-3"><strong>Threat model</strong> - Revisit it for the change.</label></li>
<li><input type="checkbox" id="ck-4"><label for="ck-4"><strong>Data protection impact assessment (DPIA)</strong> - Update it if personal data processing changes.</label></li>
<li><input type="checkbox" id="ck-5"><label for="ck-5"><strong>Non-functional requirements (NFRs)</strong> - Check the change does not breach them, or agree new ones.</label></li>
<li><input type="checkbox" id="ck-6"><label for="ck-6"><strong>Exit plan</strong> - Update it if you add a product or supplier.</label></li>
<li><input type="checkbox" id="ck-7"><label for="ck-7"><strong>Runbooks and support model</strong> - Update them before the change goes live.</label></li>
</ul>

## Must guardrails

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-8"><label for="ck-8"><a href="../../../guardrails/security/#gr-sec-01">GR-SEC-01</a> <strong>Follow Secure by Design</strong> - Secure by Design activities repeated for the change, with the risk owner involved</label></li>
<li><input type="checkbox" id="ck-9"><label for="ck-9"><a href="../../../guardrails/security/#gr-sec-02">GR-SEC-02</a> <strong>Keep a current threat model</strong> - Threat model revisited for the change before it is built</label></li>
<li><input type="checkbox" id="ck-10"><label for="ck-10"><a href="../../../guardrails/security/#gr-sec-06">GR-SEC-06</a> <strong>Test before go-live and after major change</strong> - IT health check scoped and booked for the change where it is significant</label></li>
<li><input type="checkbox" id="ck-11"><label for="ck-11"><a href="../../../guardrails/data/#gr-data-06">GR-DATA-06</a> <strong>Protect personal data by design</strong> - DPIA updated for any change in how personal data is processed</label></li>
<li><input type="checkbox" id="ck-12"><label for="ck-12"><a href="../../../guardrails/choosing-technology/#gr-tech-01">GR-TECH-01</a> <strong>Look for something to reuse first</strong> - ADR showing reuse options considered for any new component</label></li>
<li><input type="checkbox" id="ck-13"><label for="ck-13"><a href="../../../guardrails/choosing-technology/#gr-tech-06">GR-TECH-06</a> <strong>Get spend approval early</strong> - Architecture team consulted before new procurement for the change</label></li>
<li><input type="checkbox" id="ck-14"><label for="ck-14"><a href="../../../guardrails/observability-and-operations/#gr-ops-05">GR-OPS-05</a> <strong>Be ready for live before you go live</strong> - Runbooks and support arrangements updated before the change goes live</label></li>
</ul>

## Should guardrails

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-15"><label for="ck-15"><a href="../../../guardrails/apis-and-integration/#gr-api-04">GR-API-04</a> <strong>Version and deprecate deliberately</strong> - Consumers told about breaking changes in advance, with a new version and a retirement date for the old one</label></li>
<li><input type="checkbox" id="ck-16"><label for="ck-16"><a href="../../../guardrails/software-development/#gr-dev-09">GR-DEV-09</a> <strong>Record significant decisions as ADRs</strong> - ADR log in the repository or linked from its README</label></li>
<li><input type="checkbox" id="ck-17"><label for="ck-17"><a href="../../../guardrails/choosing-technology/#gr-tech-03">GR-TECH-03</a> <strong>Plan your exit before you enter</strong> - Exit plan updated for any new product or supplier</label></li>
<li><input type="checkbox" id="ck-18"><label for="ck-18"><a href="../../../guardrails/ai/#gr-ai-06">GR-AI-06</a> <strong>Talk to the TDA about novel use</strong> - Technical Design Authority review of any new AI use introduced by the change</label></li>
<li><input type="checkbox" id="ck-19"><label for="ck-19"><a href="../../../guardrails/hosting-and-platforms/#gr-host-07">GR-HOST-07</a> <strong>Design for the resilience the service needs</strong> - Recovery objectives and design checked for the change</label></li>
</ul>

## Sign-off

| Detail | Answer |
| --- | --- |
| Service | |
| Completed by | |
| Date | |
| Solution design authority | |
| Exceptions or departures (guardrail ids) | |

Read more on the [significant change page](https://defra.github.io/architecture/deliver/significant-change/).


