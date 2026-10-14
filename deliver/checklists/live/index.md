<!-- https://defra.github.io/architecture/deliver/checklists/live/ | maturity: prototype | site version 0.3.0 | generated from deliver/checklists/live.md -->

# Live evidence checklist

<p class="lead">The architecture evidence for live, as a checklist you can work through or print. Built from the guardrail metadata each time the site is published.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



Tick what you have, link to where it lives, and bring it to your solution design authority or assessment. Where you cannot meet a Must, record the approved [exception](https://defra.github.io/architecture/governance/exceptions/).

<p class="dl-print"><button type="button" class="md-button" data-print>Print this checklist</button></p>

## Artefacts

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-1"><label for="ck-1"><strong>Architecture decision record (ADR) log</strong> - Keep recording decisions. Supersede ADRs rather than deleting them.</label></li>
<li><input type="checkbox" id="ck-2"><label for="ck-2"><strong>C4 container diagram</strong> - Keep it current.</label></li>
<li><input type="checkbox" id="ck-3"><label for="ck-3"><strong>Threat model</strong> - Review it at least once a year.</label></li>
<li><input type="checkbox" id="ck-4"><label for="ck-4"><strong>Runbooks and support model</strong> - Test them and keep them current.</label></li>
<li><input type="checkbox" id="ck-5"><label for="ck-5"><strong>Exit plan</strong> - Review it at contract renewal.</label></li>
</ul>

## Must guardrails

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-6"><label for="ck-6"><a href="../../../guardrails/ai/#gr-ai-02">GR-AI-02</a> <strong>Use approved AI services and tenancies</strong> - List of AI services in use, reviewed when services or agreements change</label></li>
<li><input type="checkbox" id="ck-7"><label for="ck-7"><a href="../../../guardrails/ai/#gr-ai-03">GR-AI-03</a> <strong>Keep a human accountable</strong> - Records of human review, challenges raised and their outcomes, reviewed regularly</label></li>
<li><input type="checkbox" id="ck-8"><label for="ck-8"><a href="../../../guardrails/ai/#gr-ai-04">GR-AI-04</a> <strong>Be transparent</strong> - Link to the published Algorithmic Transparency Recording Standard record, kept current</label></li>
<li><input type="checkbox" id="ck-9"><label for="ck-9"><a href="../../../guardrails/apis-and-integration/#gr-api-07">GR-API-07</a> <strong>Secure every API</strong> - API access reviewed, and controls re-tested after significant change</label></li>
<li><input type="checkbox" id="ck-10"><label for="ck-10"><a href="../../../guardrails/data/#gr-data-06">GR-DATA-06</a> <strong>Protect personal data by design</strong> - DPIA reviewed when processing changes, and deletion running as designed</label></li>
<li><input type="checkbox" id="ck-11"><label for="ck-11"><a href="../../../guardrails/data/#gr-data-09">GR-DATA-09</a> <strong>Retain and dispose of records properly</strong> - Retention applied and records of permanent value identified for The National Archives</label></li>
<li><input type="checkbox" id="ck-12"><label for="ck-12"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-01">GR-FE-01</a> <strong>Meet WCAG 2.2 AA</strong> - Accessibility statement kept current, and accessibility re-tested after significant change</label></li>
<li><input type="checkbox" id="ck-13"><label for="ck-13"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-02">GR-FE-02</a> <strong>Use the GOV.UK Design System</strong> - GOV.UK Frontend kept up to date</label></li>
<li><input type="checkbox" id="ck-14"><label for="ck-14"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-06">GR-FE-06</a> <strong>Support Welsh where required</strong> - Welsh content kept in step with English content</label></li>
<li><input type="checkbox" id="ck-15"><label for="ck-15"><a href="../../../guardrails/hosting-and-platforms/#gr-host-01">GR-HOST-01</a> <strong>Use Defra&#x27;s strategic delivery platform by default</strong> - The service still runs on the platform, and any exception is reviewed before it expires</label></li>
<li><input type="checkbox" id="ck-16"><label for="ck-16"><a href="../../../guardrails/identity-and-access/#gr-iam-01">GR-IAM-01</a> <strong>Use the strategic customer identity services</strong> - No other sign-in introduced</label></li>
<li><input type="checkbox" id="ck-17"><label for="ck-17"><a href="../../../guardrails/identity-and-access/#gr-iam-02">GR-IAM-02</a> <strong>Staff sign in with Microsoft Entra ID</strong> - Staff access reviewed regularly through Entra ID groups</label></li>
<li><input type="checkbox" id="ck-18"><label for="ck-18"><a href="../../../guardrails/identity-and-access/#gr-iam-03">GR-IAM-03</a> <strong>Authorise on least privilege</strong> - Record of regular access reviews</label></li>
<li><input type="checkbox" id="ck-19"><label for="ck-19"><a href="../../../guardrails/identity-and-access/#gr-iam-05">GR-IAM-05</a> <strong>No secrets in code</strong> - Secrets rotated, and secret scanning alerts dealt with</label></li>
<li><input type="checkbox" id="ck-20"><label for="ck-20"><a href="../../../guardrails/identity-and-access/#gr-iam-06">GR-IAM-06</a> <strong>Privileged access is controlled and audited</strong> - Privileged access reviewed regularly</label></li>
<li><input type="checkbox" id="ck-21"><label for="ck-21"><a href="../../../guardrails/observability-and-operations/#gr-ops-05">GR-OPS-05</a> <strong>Be ready for live before you go live</strong> - Runbooks and support arrangements tested and kept current</label></li>
<li><input type="checkbox" id="ck-22"><label for="ck-22"><a href="../../../guardrails/open-source/#gr-open-01">GR-OPEN-01</a> <strong>Code in the open</strong> - Repositories still public, or private for a recorded reason</label></li>
<li><input type="checkbox" id="ck-23"><label for="ck-23"><a href="../../../guardrails/security/#gr-sec-01">GR-SEC-01</a> <strong>Follow Secure by Design</strong> - Secure by Design activities for live continuing, including monitoring and review</label></li>
<li><input type="checkbox" id="ck-24"><label for="ck-24"><a href="../../../guardrails/security/#gr-sec-02">GR-SEC-02</a> <strong>Keep a current threat model</strong> - Threat model reviewed at least once a year, with the date of the last review</label></li>
<li><input type="checkbox" id="ck-25"><label for="ck-25"><a href="../../../guardrails/security/#gr-sec-04">GR-SEC-04</a> <strong>Encrypt in transit and at rest</strong> - Encryption settings checked when new stores or connections are added</label></li>
<li><input type="checkbox" id="ck-26"><label for="ck-26"><a href="../../../guardrails/security/#gr-sec-05">GR-SEC-05</a> <strong>Scan continuously and fix quickly</strong> - Time taken to fix critical and high vulnerabilities, within 14 and 30 days, or a recorded risk decision</label></li>
<li><input type="checkbox" id="ck-27"><label for="ck-27"><a href="../../../guardrails/security/#gr-sec-06">GR-SEC-06</a> <strong>Test before go-live and after major change</strong> - IT health check after significant change, with remediation tracked</label></li>
<li><input type="checkbox" id="ck-28"><label for="ck-28"><a href="../../../guardrails/security/#gr-sec-07">GR-SEC-07</a> <strong>Log for detection and response</strong> - Security events reviewed and alerts acted on</label></li>
<li><input type="checkbox" id="ck-29"><label for="ck-29"><a href="../../../guardrails/security/#gr-sec-09">GR-SEC-09</a> <strong>Manage risk explicitly</strong> - Accepted risks reviewed before they expire</label></li>
<li><input type="checkbox" id="ck-30"><label for="ck-30"><a href="../../../guardrails/software-development/#gr-dev-02">GR-DEV-02</a> <strong>All code in Defra source control</strong> - All changes made in the Defra GitHub organisation</label></li>
</ul>

## Should guardrails

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-31"><label for="ck-31"><a href="../../../guardrails/ai/#gr-ai-05">GR-AI-05</a> <strong>Evaluate, monitor and threat model</strong> - Monitoring of model performance and drift in live, with evaluation repeated when the model or data changes</label></li>
<li><input type="checkbox" id="ck-32"><label for="ck-32"><a href="../../../guardrails/ai/#gr-ai-07">GR-AI-07</a> <strong>Suppliers use AI coding assistants openly and safely</strong> - Supplier&#x27;s agreed list of AI coding assistants and how each runs within Defra-approved terms, the review process for generated code, and disclosure in pull requests or delivery reports</label></li>
<li><input type="checkbox" id="ck-33"><label for="ck-33"><a href="../../../guardrails/ai/#gr-ai-08">GR-AI-08</a> <strong>Give agents the least privilege they need</strong> - Agent permissions reviewed regularly, as for a privileged user</label></li>
<li><input type="checkbox" id="ck-34"><label for="ck-34"><a href="../../../guardrails/ai/#gr-ai-09">GR-AI-09</a> <strong>Get human approval for consequential actions</strong> - Approval records reviewed, and the classification updated when the agent gains new tools</label></li>
<li><input type="checkbox" id="ck-35"><label for="ck-35"><a href="../../../guardrails/ai/#gr-ai-10">GR-AI-10</a> <strong>Keep an audit trail of what agents do</strong> - Audit records retained and reviewed, and used to investigate any problem</label></li>
<li><input type="checkbox" id="ck-36"><label for="ck-36"><a href="../../../guardrails/ai/#gr-ai-11">GR-AI-11</a> <strong>Defend agents against prompt injection</strong> - Prompt injection defences re-tested when inputs, tools or models change</label></li>
<li><input type="checkbox" id="ck-37"><label for="ck-37"><a href="../../../guardrails/apis-and-integration/#gr-api-02">GR-API-02</a> <strong>Describe APIs with open specifications</strong> - Specifications kept in step with every released change</label></li>
<li><input type="checkbox" id="ck-38"><label for="ck-38"><a href="../../../guardrails/apis-and-integration/#gr-api-03">GR-API-03</a> <strong>Follow government API standards</strong> - API design reviewed against the GDS API technical and data standards</label></li>
<li><input type="checkbox" id="ck-39"><label for="ck-39"><a href="../../../guardrails/apis-and-integration/#gr-api-04">GR-API-04</a> <strong>Version and deprecate deliberately</strong> - Deprecation notices sent to consumers and retirement dates published for old versions</label></li>
<li><input type="checkbox" id="ck-40"><label for="ck-40"><a href="../../../guardrails/apis-and-integration/#gr-api-05">GR-API-05</a> <strong>No integration through shared databases</strong> - Integrations reviewed when the service or its dependencies change</label></li>
<li><input type="checkbox" id="ck-41"><label for="ck-41"><a href="../../../guardrails/apis-and-integration/#gr-api-08">GR-API-08</a> <strong>Make APIs discoverable</strong> - Entry in the platform API catalogue</label></li>
<li><input type="checkbox" id="ck-42"><label for="ck-42"><a href="../../../guardrails/choosing-technology/#gr-tech-03">GR-TECH-03</a> <strong>Plan your exit before you enter</strong> - Exit plan reviewed at contract renewal, with switching cost estimated</label></li>
<li><input type="checkbox" id="ck-43"><label for="ck-43"><a href="../../../guardrails/data/#gr-data-01">GR-DATA-01</a> <strong>Every data set has an owner</strong> - Register entries and owners kept current</label></li>
<li><input type="checkbox" id="ck-44"><label for="ck-44"><a href="../../../guardrails/data/#gr-data-02">GR-DATA-02</a> <strong>Use authoritative sources</strong> - Copies and refresh arrangements reviewed when sources change</label></li>
<li><input type="checkbox" id="ck-45"><label for="ck-45"><a href="../../../guardrails/data/#gr-data-05">GR-DATA-05</a> <strong>Describe your data</strong> - Published metadata records in UK GEMINI or DCAT</label></li>
<li><input type="checkbox" id="ck-46"><label for="ck-46"><a href="../../../guardrails/data/#gr-data-07">GR-DATA-07</a> <strong>Open by default</strong> - Link to the published open data and its licence</label></li>
<li><input type="checkbox" id="ck-47"><label for="ck-47"><a href="../../../guardrails/data/#gr-data-08">GR-DATA-08</a> <strong>Manage data quality</strong> - Data quality measures and regular reports</label></li>
<li><input type="checkbox" id="ck-48"><label for="ck-48"><a href="../../../guardrails/data/#gr-data-10">GR-DATA-10</a> <strong>Handle research data safely</strong> - Research data handled the same way for ongoing research, and deletion checked</label></li>
<li><input type="checkbox" id="ck-49"><label for="ck-49"><a href="../../../guardrails/digital-first/#gr-dig-03">GR-DIG-03</a> <strong>Provide assisted digital and offline routes</strong> - Assisted digital and offline routes designed and tested with users who need them</label></li>
<li><input type="checkbox" id="ck-50"><label for="ck-50"><a href="../../../guardrails/field-working-and-devices/#gr-field-02">GR-FIELD-02</a> <strong>Design field tools to work offline</strong> - Field journeys tested with no connection, including sync after reconnecting and conflict handling</label></li>
<li><input type="checkbox" id="ck-51"><label for="ck-51"><a href="../../../guardrails/field-working-and-devices/#gr-field-03">GR-FIELD-03</a> <strong>Manage and secure every device</strong> - Device compliance monitored, and lost devices wiped</label></li>
<li><input type="checkbox" id="ck-52"><label for="ck-52"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-07">GR-FE-07</a> <strong>Tell users what is happening when things fail or are slow</strong> - Failure and delay content kept accurate as dependencies and processing times change</label></li>
<li><input type="checkbox" id="ck-53"><label for="ck-53"><a href="../../../guardrails/hosting-and-platforms/#gr-host-02">GR-HOST-02</a> <strong>Public cloud first</strong> - No on-premises hosting introduced</label></li>
<li><input type="checkbox" id="ck-54"><label for="ck-54"><a href="../../../guardrails/hosting-and-platforms/#gr-host-03">GR-HOST-03</a> <strong>Everything as code</strong> - Drift detection running, and no manual changes to production in the change history</label></li>
<li><input type="checkbox" id="ck-55"><label for="ck-55"><a href="../../../guardrails/hosting-and-platforms/#gr-host-05">GR-HOST-05</a> <strong>Consistent, disposable environments</strong> - Environments created from the same code, and how lower environments avoid real personal data</label></li>
<li><input type="checkbox" id="ck-56"><label for="ck-56"><a href="../../../guardrails/hosting-and-platforms/#gr-host-06">GR-HOST-06</a> <strong>Host data in the UK</strong> - Data location checked when new stores or services are added</label></li>
<li><input type="checkbox" id="ck-57"><label for="ck-57"><a href="../../../guardrails/hosting-and-platforms/#gr-host-07">GR-HOST-07</a> <strong>Design for the resilience the service needs</strong> - Recovery tested at least once a year, with the date of the last test</label></li>
<li><input type="checkbox" id="ck-58"><label for="ck-58"><a href="../../../guardrails/observability-and-operations/#gr-ops-01">GR-OPS-01</a> <strong>Use the platform&#x27;s observability tooling</strong> - Dashboards and alerts in use by the team that runs the service</label></li>
<li><input type="checkbox" id="ck-59"><label for="ck-59"><a href="../../../guardrails/observability-and-operations/#gr-ops-02">GR-OPS-02</a> <strong>Log in a structured, safe way</strong> - Logging reviewed when new data or features are added</label></li>
<li><input type="checkbox" id="ck-60"><label for="ck-60"><a href="../../../guardrails/observability-and-operations/#gr-ops-03">GR-OPS-03</a> <strong>Define and measure service levels</strong> - Agreed service level objectives with monitoring and alerts</label></li>
<li><input type="checkbox" id="ck-61"><label for="ck-61"><a href="../../../guardrails/observability-and-operations/#gr-ops-04">GR-OPS-04</a> <strong>Health checks and graceful degradation</strong> - Health endpoints, timeout and retry settings, and a design for when dependencies fail</label></li>
<li><input type="checkbox" id="ck-62"><label for="ck-62"><a href="../../../guardrails/observability-and-operations/#gr-ops-06">GR-OPS-06</a> <strong>Learn from incidents</strong> - Post-incident reviews and the actions taken</label></li>
<li><input type="checkbox" id="ck-63"><label for="ck-63"><a href="../../../guardrails/observability-and-operations/#gr-ops-07">GR-OPS-07</a> <strong>Measure performance and cost</strong> - Published key performance indicators and cost tags on cloud resources</label></li>
<li><input type="checkbox" id="ck-64"><label for="ck-64"><a href="../../../guardrails/open-source/#gr-open-02">GR-OPEN-02</a> <strong>Licence clearly</strong> - LICENCE file in every new repository</label></li>
<li><input type="checkbox" id="ck-65"><label for="ck-65"><a href="../../../guardrails/open-source/#gr-open-03">GR-OPEN-03</a> <strong>Publish safely</strong> - Secret scanning alerts dealt with promptly</label></li>
<li><input type="checkbox" id="ck-66"><label for="ck-66"><a href="../../../guardrails/open-source/#gr-open-04">GR-OPEN-04</a> <strong>Reuse and contribute back</strong> - Reuse and upstream contributions noted in ADRs and pull requests</label></li>
<li><input type="checkbox" id="ck-67"><label for="ck-67"><a href="../../../guardrails/products-and-platforms/#gr-prod-01">GR-PROD-01</a> <strong>Fund and run products, not projects</strong> - A named, long-lived team responsible for the product, with a roadmap beyond the current funding period</label></li>
<li><input type="checkbox" id="ck-68"><label for="ck-68"><a href="../../../guardrails/products-and-platforms/#gr-prod-02">GR-PROD-02</a> <strong>Name the product owner and service owner</strong> - Named product owner and service owner, recorded in the service catalogue</label></li>
<li><input type="checkbox" id="ck-69"><label for="ck-69"><a href="../../../guardrails/products-and-platforms/#gr-prod-03">GR-PROD-03</a> <strong>Contribute to platforms rather than working around them</strong> - Requests and contributions raised with platform teams, and ADRs where the team worked around a platform</label></li>
<li><input type="checkbox" id="ck-70"><label for="ck-70"><a href="../../../guardrails/products-and-platforms/#gr-prod-04">GR-PROD-04</a> <strong>Plan for the end of a product&#x27;s life</strong> - Product lifecycle stage recorded, with a retirement plan for products being replaced</label></li>
<li><input type="checkbox" id="ck-71"><label for="ck-71"><a href="../../../guardrails/security/#gr-sec-08">GR-SEC-08</a> <strong>Protect the supply chain</strong> - Software bill of materials kept current, and supplier assessments reviewed at renewal</label></li>
<li><input type="checkbox" id="ck-72"><label for="ck-72"><a href="../../../guardrails/software-development/#gr-dev-03">GR-DEV-03</a> <strong>Protect the main branch</strong> - Branch protection still in place on every repository</label></li>
<li><input type="checkbox" id="ck-73"><label for="ck-73"><a href="../../../guardrails/software-development/#gr-dev-04">GR-DEV-04</a> <strong>Continuous integration and delivery</strong> - Deployment history showing small, frequent, reversible releases</label></li>
<li><input type="checkbox" id="ck-74"><label for="ck-74"><a href="../../../guardrails/software-development/#gr-dev-05">GR-DEV-05</a> <strong>Automated testing at the right levels</strong> - Test results from the pipeline at each level</label></li>
<li><input type="checkbox" id="ck-75"><label for="ck-75"><a href="../../../guardrails/software-development/#gr-dev-06">GR-DEV-06</a> <strong>Manage dependencies actively</strong> - Dependency updates merged promptly and runtimes upgraded before they go out of support</label></li>
<li><input type="checkbox" id="ck-76"><label for="ck-76"><a href="../../../guardrails/software-development/#gr-dev-07">GR-DEV-07</a> <strong>Follow shared coding standards</strong> - Linting and formatting checks in the pipeline</label></li>
<li><input type="checkbox" id="ck-77"><label for="ck-77"><a href="../../../guardrails/software-development/#gr-dev-08">GR-DEV-08</a> <strong>Document as you go</strong> - README explaining what the service does and how to run, test and deploy it, with links to its ADRs</label></li>
<li><input type="checkbox" id="ck-78"><label for="ck-78"><a href="../../../guardrails/software-development/#gr-dev-09">GR-DEV-09</a> <strong>Record significant decisions as ADRs</strong> - ADR log in the repository or linked from its README</label></li>
<li><input type="checkbox" id="ck-79"><label for="ck-79"><a href="../../../guardrails/sustainability/#gr-sus-02">GR-SUS-02</a> <strong>Right-size and switch off</strong> - Autoscaling and out-of-hours schedules for non-production environments</label></li>
<li><input type="checkbox" id="ck-80"><label for="ck-80"><a href="../../../guardrails/sustainability/#gr-sus-04">GR-SUS-04</a> <strong>Keep data and pages lean</strong> - Data retention settings and page weight measurements</label></li>
</ul>

## Could guardrails

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-81"><label for="ck-81"><a href="../../../guardrails/open-source/#gr-open-05">GR-OPEN-05</a> <strong>Blog and show the thing</strong> - Blog posts, show and tells or contributions to this site</label></li>
<li><input type="checkbox" id="ck-82"><label for="ck-82"><a href="../../../guardrails/sustainability/#gr-sus-05">GR-SUS-05</a> <strong>Measure and report</strong> - Carbon footprint reported alongside cost</label></li>
</ul>

## Sign-off

| Detail | Answer |
| --- | --- |
| Service | |
| Completed by | |
| Date | |
| Solution design authority | |
| Exceptions or departures (guardrail ids) | |

Read more on the [live page](https://defra.github.io/architecture/deliver/live/).


