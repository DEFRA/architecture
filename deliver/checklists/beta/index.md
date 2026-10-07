<!-- https://defra.github.io/architecture/deliver/checklists/beta/ | maturity: prototype | site version 0.3.0 | generated from deliver/checklists/beta.md -->

# Beta evidence checklist

<p class="lead">The architecture evidence for beta, as a checklist you can work through or print. Built from the guardrail metadata each time the site is published.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



Tick what you have, link to where it lives, and bring it to your solution design authority or assessment. Where you cannot meet a Must, record the approved [exception](https://defra.github.io/architecture/governance/exceptions/).

<p class="dl-print"><button type="button" class="md-button" data-print>Print this checklist</button></p>

## Artefacts

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-1"><label for="ck-1"><strong>Architecture decision record (ADR) log</strong> - Keep it current as the design changes.</label></li>
<li><input type="checkbox" id="ck-2"><label for="ck-2"><strong>C4 container diagram</strong> - Update it to match what you built.</label></li>
<li><input type="checkbox" id="ck-3"><label for="ck-3"><strong>Threat model</strong> - Review it as controls are built and tested.</label></li>
<li><input type="checkbox" id="ck-4"><label for="ck-4"><strong>Data protection impact assessment (DPIA)</strong> - Update it for anything that has changed.</label></li>
<li><input type="checkbox" id="ck-5"><label for="ck-5"><strong>Non-functional requirements (NFRs)</strong> - Test against them and record the results.</label></li>
<li><input type="checkbox" id="ck-6"><label for="ck-6"><strong>Exit plan</strong> - Confirm contracts give Defra its data and the right to export it.</label></li>
<li><input type="checkbox" id="ck-7"><label for="ck-7"><strong>Runbooks and support model</strong> - Write them and agree the support model before public beta.</label></li>
</ul>

## Must guardrails

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-8"><label for="ck-8"><a href="../../../guardrails/ai/#gr-ai-02">GR-AI-02</a> <strong>Use approved AI services and tenancies</strong> - The AI services in the built service run only in approved tenancies, shown in the hosting design and configuration</label></li>
<li><input type="checkbox" id="ck-9"><label for="ck-9"><a href="../../../guardrails/ai/#gr-ai-03">GR-AI-03</a> <strong>Keep a human accountable</strong> - Human review and challenge built into the service and tested with users and staff</label></li>
<li><input type="checkbox" id="ck-10"><label for="ck-10"><a href="../../../guardrails/ai/#gr-ai-04">GR-AI-04</a> <strong>Be transparent</strong> - Draft Algorithmic Transparency Recording Standard record, and the notice telling users about AI tested with them</label></li>
<li><input type="checkbox" id="ck-11"><label for="ck-11"><a href="../../../guardrails/apis-and-integration/#gr-api-07">GR-API-07</a> <strong>Secure every API</strong> - These controls built and covered by security testing</label></li>
<li><input type="checkbox" id="ck-12"><label for="ck-12"><a href="../../../guardrails/data/#gr-data-06">GR-DATA-06</a> <strong>Protect personal data by design</strong> - Approved DPIA, and retention and deletion built and tested</label></li>
<li><input type="checkbox" id="ck-13"><label for="ck-13"><a href="../../../guardrails/data/#gr-data-09">GR-DATA-09</a> <strong>Retain and dispose of records properly</strong> - Retention schedule identified for each type of record, and disposal built in</label></li>
<li><input type="checkbox" id="ck-14"><label for="ck-14"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-01">GR-FE-01</a> <strong>Meet WCAG 2.2 AA</strong> - Accessibility audit and assistive technology testing completed, issues fixed, and an accessibility statement published</label></li>
<li><input type="checkbox" id="ck-15"><label for="ck-15"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-02">GR-FE-02</a> <strong>Use the GOV.UK Design System</strong> - The service uses GOV.UK Frontend, with design decisions recording any departures</label></li>
<li><input type="checkbox" id="ck-16"><label for="ck-16"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-06">GR-FE-06</a> <strong>Support Welsh where required</strong> - Welsh content and journeys built and tested where the standards apply</label></li>
<li><input type="checkbox" id="ck-17"><label for="ck-17"><a href="../../../guardrails/hosting-and-platforms/#gr-host-01">GR-HOST-01</a> <strong>Use Defra&#x27;s strategic delivery platform by default</strong> - The service runs on the Core Delivery Platform, or under an approved exception</label></li>
<li><input type="checkbox" id="ck-18"><label for="ck-18"><a href="../../../guardrails/identity-and-access/#gr-iam-01">GR-IAM-01</a> <strong>Use the strategic customer identity services</strong> - Integration with Defra Customer Identity built and tested</label></li>
<li><input type="checkbox" id="ck-19"><label for="ck-19"><a href="../../../guardrails/identity-and-access/#gr-iam-02">GR-IAM-02</a> <strong>Staff sign in with Microsoft Entra ID</strong> - Staff sign in through Microsoft Entra ID with multi-factor authentication, and there are no local staff accounts</label></li>
<li><input type="checkbox" id="ck-20"><label for="ck-20"><a href="../../../guardrails/identity-and-access/#gr-iam-03">GR-IAM-03</a> <strong>Authorise on least privilege</strong> - Role and group model built, with users, services and pipelines given only the permissions they need</label></li>
<li><input type="checkbox" id="ck-21"><label for="ck-21"><a href="../../../guardrails/identity-and-access/#gr-iam-05">GR-IAM-05</a> <strong>No secrets in code</strong> - All secrets in a managed store with rotation, using workload identity where possible</label></li>
<li><input type="checkbox" id="ck-22"><label for="ck-22"><a href="../../../guardrails/identity-and-access/#gr-iam-06">GR-IAM-06</a> <strong>Privileged access is controlled and audited</strong> - Just-in-time privileged access with phishing-resistant MFA configured, and logged to the security operations centre</label></li>
<li><input type="checkbox" id="ck-23"><label for="ck-23"><a href="../../../guardrails/observability-and-operations/#gr-ops-05">GR-OPS-05</a> <strong>Be ready for live before you go live</strong> - Before public beta, the support model, on-call arrangements, runbooks, incident process and live owner agreed, and the service catalogue entry made</label></li>
<li><input type="checkbox" id="ck-24"><label for="ck-24"><a href="../../../guardrails/open-source/#gr-open-01">GR-OPEN-01</a> <strong>Code in the open</strong> - Repositories public, or the reasons for keeping them private reviewed</label></li>
<li><input type="checkbox" id="ck-25"><label for="ck-25"><a href="../../../guardrails/security/#gr-sec-01">GR-SEC-01</a> <strong>Follow Secure by Design</strong> - Secure by Design activities for beta completed, including controls built and tested</label></li>
<li><input type="checkbox" id="ck-26"><label for="ck-26"><a href="../../../guardrails/security/#gr-sec-02">GR-SEC-02</a> <strong>Keep a current threat model</strong> - Threat model updated as controls are built and tested</label></li>
<li><input type="checkbox" id="ck-27"><label for="ck-27"><a href="../../../guardrails/security/#gr-sec-04">GR-SEC-04</a> <strong>Encrypt in transit and at rest</strong> - TLS 1.2 or higher for all traffic and encryption at rest for every data store, confirmed as built</label></li>
<li><input type="checkbox" id="ck-28"><label for="ck-28"><a href="../../../guardrails/security/#gr-sec-05">GR-SEC-05</a> <strong>Scan continuously and fix quickly</strong> - Static analysis, dependency, container and infrastructure scanning running in the pipeline</label></li>
<li><input type="checkbox" id="ck-29"><label for="ck-29"><a href="../../../guardrails/security/#gr-sec-06">GR-SEC-06</a> <strong>Test before go-live and after major change</strong> - IT health check before go-live, and a remediation tracker</label></li>
<li><input type="checkbox" id="ck-30"><label for="ck-30"><a href="../../../guardrails/security/#gr-sec-07">GR-SEC-07</a> <strong>Log for detection and response</strong> - Authentication, authorisation failures, administrative actions and data exports sent to the security operations centre, and tested</label></li>
<li><input type="checkbox" id="ck-31"><label for="ck-31"><a href="../../../guardrails/security/#gr-sec-09">GR-SEC-09</a> <strong>Manage risk explicitly</strong> - Residual risks accepted by the right owner through the security exception process, each with an expiry date</label></li>
<li><input type="checkbox" id="ck-32"><label for="ck-32"><a href="../../../guardrails/software-development/#gr-dev-02">GR-DEV-02</a> <strong>All code in Defra source control</strong> - All source, infrastructure and pipeline code in the Defra GitHub organisation, with nothing held only by a supplier</label></li>
</ul>

## Should guardrails

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-33"><label for="ck-33"><a href="../../../guardrails/ai/#gr-ai-05">GR-AI-05</a> <strong>Evaluate, monitor and threat model</strong> - Evaluation results for accuracy, bias and safety before release, and mitigations for AI threats tested</label></li>
<li><input type="checkbox" id="ck-34"><label for="ck-34"><a href="../../../guardrails/ai/#gr-ai-07">GR-AI-07</a> <strong>Suppliers use AI coding assistants openly and safely</strong> - Supplier&#x27;s agreed list of AI coding assistants and how each runs within Defra-approved terms, the review process for generated code, and disclosure in pull requests or delivery reports</label></li>
<li><input type="checkbox" id="ck-35"><label for="ck-35"><a href="../../../guardrails/ai/#gr-ai-08">GR-AI-08</a> <strong>Give agents the least privilege they need</strong> - Agent permissions configured as designed and tested, including that the agent cannot reach tools it should not</label></li>
<li><input type="checkbox" id="ck-36"><label for="ck-36"><a href="../../../guardrails/ai/#gr-ai-09">GR-AI-09</a> <strong>Get human approval for consequential actions</strong> - Approval enforced in the tool layer, with tests showing the agent cannot act without it</label></li>
<li><input type="checkbox" id="ck-37"><label for="ck-37"><a href="../../../guardrails/ai/#gr-ai-10">GR-AI-10</a> <strong>Keep an audit trail of what agents do</strong> - Audit records of agent inputs, tool calls, approvals and outcomes produced and sent to security monitoring</label></li>
<li><input type="checkbox" id="ck-38"><label for="ck-38"><a href="../../../guardrails/ai/#gr-ai-11">GR-AI-11</a> <strong>Defend agents against prompt injection</strong> - Prompt injection mitigations tested, including attempts to misuse tools and leak data</label></li>
<li><input type="checkbox" id="ck-39"><label for="ck-39"><a href="../../../guardrails/apis-and-integration/#gr-api-01">GR-API-01</a> <strong>API first</strong> - API specification written before or alongside the user interface</label></li>
<li><input type="checkbox" id="ck-40"><label for="ck-40"><a href="../../../guardrails/apis-and-integration/#gr-api-02">GR-API-02</a> <strong>Describe APIs with open specifications</strong> - OpenAPI 3 or AsyncAPI documents in the repository, checked in the pipeline against the running API</label></li>
<li><input type="checkbox" id="ck-41"><label for="ck-41"><a href="../../../guardrails/apis-and-integration/#gr-api-03">GR-API-03</a> <strong>Follow government API standards</strong> - API design reviewed against the GDS API technical and data standards</label></li>
<li><input type="checkbox" id="ck-42"><label for="ck-42"><a href="../../../guardrails/apis-and-integration/#gr-api-04">GR-API-04</a> <strong>Version and deprecate deliberately</strong> - Versioning approach published for each API and event</label></li>
<li><input type="checkbox" id="ck-43"><label for="ck-43"><a href="../../../guardrails/apis-and-integration/#gr-api-05">GR-API-05</a> <strong>No integration through shared databases</strong> - Built integrations match the container diagram, with no access to another service&#x27;s database</label></li>
<li><input type="checkbox" id="ck-44"><label for="ck-44"><a href="../../../guardrails/apis-and-integration/#gr-api-06">GR-API-06</a> <strong>Use events for change notifications</strong> - Event and message definitions described in AsyncAPI</label></li>
<li><input type="checkbox" id="ck-45"><label for="ck-45"><a href="../../../guardrails/apis-and-integration/#gr-api-08">GR-API-08</a> <strong>Make APIs discoverable</strong> - Entry in the platform API catalogue</label></li>
<li><input type="checkbox" id="ck-46"><label for="ck-46"><a href="../../../guardrails/choosing-technology/#gr-tech-03">GR-TECH-03</a> <strong>Plan your exit before you enter</strong> - Exit plan agreed, with contracts giving Defra its data and the right to export it in open formats</label></li>
<li><input type="checkbox" id="ck-47"><label for="ck-47"><a href="../../../guardrails/data/#gr-data-01">GR-DATA-01</a> <strong>Every data set has an owner</strong> - Information asset register entries with a named owner for each data set</label></li>
<li><input type="checkbox" id="ck-48"><label for="ck-48"><a href="../../../guardrails/data/#gr-data-02">GR-DATA-02</a> <strong>Use authoritative sources</strong> - The service reads from the authoritative sources as designed, tested with the source owners</label></li>
<li><input type="checkbox" id="ck-49"><label for="ck-49"><a href="../../../guardrails/data/#gr-data-03">GR-DATA-03</a> <strong>Use agreed data standards and identifiers</strong> - Data stored and exchanged using the agreed standards, checked in testing</label></li>
<li><input type="checkbox" id="ck-50"><label for="ck-50"><a href="../../../guardrails/data/#gr-data-04">GR-DATA-04</a> <strong>Collect once, share safely</strong> - Journey design showing users are not asked for information Defra already holds, and data sharing agreements where required</label></li>
<li><input type="checkbox" id="ck-51"><label for="ck-51"><a href="../../../guardrails/data/#gr-data-05">GR-DATA-05</a> <strong>Describe your data</strong> - Published metadata records in UK GEMINI or DCAT</label></li>
<li><input type="checkbox" id="ck-52"><label for="ck-52"><a href="../../../guardrails/data/#gr-data-07">GR-DATA-07</a> <strong>Open by default</strong> - Link to the published open data and its licence</label></li>
<li><input type="checkbox" id="ck-53"><label for="ck-53"><a href="../../../guardrails/data/#gr-data-08">GR-DATA-08</a> <strong>Manage data quality</strong> - Data quality measures and regular reports</label></li>
<li><input type="checkbox" id="ck-54"><label for="ck-54"><a href="../../../guardrails/data/#gr-data-10">GR-DATA-10</a> <strong>Handle research data safely</strong> - Research data from earlier phases deleted on schedule, and the same controls for beta research</label></li>
<li><input type="checkbox" id="ck-55"><label for="ck-55"><a href="../../../guardrails/data/#gr-data-11">GR-DATA-11</a> <strong>No real personal data in prototypes</strong> - Test and research environments use synthetic or anonymised data; any exception agreed through a DPIA</label></li>
<li><input type="checkbox" id="ck-56"><label for="ck-56"><a href="../../../guardrails/digital-first/#gr-dig-02">GR-DIG-02</a> <strong>Design across organisational boundaries</strong> - A map of the whole service, including the parts other teams and organisations deliver, and agreed hand-offs between them</label></li>
<li><input type="checkbox" id="ck-57"><label for="ck-57"><a href="../../../guardrails/digital-first/#gr-dig-03">GR-DIG-03</a> <strong>Provide assisted digital and offline routes</strong> - Assisted digital and offline routes designed and tested with users who need them</label></li>
<li><input type="checkbox" id="ck-58"><label for="ck-58"><a href="../../../guardrails/field-working-and-devices/#gr-field-02">GR-FIELD-02</a> <strong>Design field tools to work offline</strong> - Field journeys tested with no connection, including sync after reconnecting and conflict handling</label></li>
<li><input type="checkbox" id="ck-59"><label for="ck-59"><a href="../../../guardrails/field-working-and-devices/#gr-field-03">GR-FIELD-03</a> <strong>Manage and secure every device</strong> - Devices enrolled in Defra device management, with encryption, patching, screen lock and remote wipe confirmed</label></li>
<li><input type="checkbox" id="ck-60"><label for="ck-60"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-03">GR-FE-03</a> <strong>Progressive enhancement</strong> - Core journeys tested with JavaScript turned off</label></li>
<li><input type="checkbox" id="ck-61"><label for="ck-61"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-05">GR-FE-05</a> <strong>Design for low bandwidth and rural users</strong> - Page weight budget, save-progress design and testing on slow connections</label></li>
<li><input type="checkbox" id="ck-62"><label for="ck-62"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-07">GR-FE-07</a> <strong>Tell users what is happening when things fail or are slow</strong> - The front end shows the designed content when a dependency fails or is slow, tested by switching dependencies off</label></li>
<li><input type="checkbox" id="ck-63"><label for="ck-63"><a href="../../../guardrails/hosting-and-platforms/#gr-host-02">GR-HOST-02</a> <strong>Public cloud first</strong> - The service runs in a Defra-managed public cloud tenancy</label></li>
<li><input type="checkbox" id="ck-64"><label for="ck-64"><a href="../../../guardrails/hosting-and-platforms/#gr-host-03">GR-HOST-03</a> <strong>Everything as code</strong> - Infrastructure, configuration and pipelines defined as code in the repository, with no manual changes to production</label></li>
<li><input type="checkbox" id="ck-65"><label for="ck-65"><a href="../../../guardrails/hosting-and-platforms/#gr-host-04">GR-HOST-04</a> <strong>Use managed services before self-managed</strong> - Hosting design listing the managed services used</label></li>
<li><input type="checkbox" id="ck-66"><label for="ck-66"><a href="../../../guardrails/hosting-and-platforms/#gr-host-05">GR-HOST-05</a> <strong>Consistent, disposable environments</strong> - Environments created from the same code, and how lower environments avoid real personal data</label></li>
<li><input type="checkbox" id="ck-67"><label for="ck-67"><a href="../../../guardrails/hosting-and-platforms/#gr-host-06">GR-HOST-06</a> <strong>Host data in the UK</strong> - Data location confirmed for every data store and backup as built</label></li>
<li><input type="checkbox" id="ck-68"><label for="ck-68"><a href="../../../guardrails/hosting-and-platforms/#gr-host-07">GR-HOST-07</a> <strong>Design for the resilience the service needs</strong> - Multi-zone design built, and recovery tested before go-live</label></li>
<li><input type="checkbox" id="ck-69"><label for="ck-69"><a href="../../../guardrails/identity-and-access/#gr-iam-04">GR-IAM-04</a> <strong>Separate authentication from authorisation</strong> - Authorisation rules written down and covered by automated tests</label></li>
<li><input type="checkbox" id="ck-70"><label for="ck-70"><a href="../../../guardrails/observability-and-operations/#gr-ops-01">GR-OPS-01</a> <strong>Use the platform&#x27;s observability tooling</strong> - Logs, metrics and traces reaching the platform&#x27;s observability tooling, and security events reaching the security operations centre</label></li>
<li><input type="checkbox" id="ck-71"><label for="ck-71"><a href="../../../guardrails/observability-and-operations/#gr-ops-02">GR-OPS-02</a> <strong>Log in a structured, safe way</strong> - Structured logs with correlation identifiers, tested to show no secrets or unnecessary personal data are logged</label></li>
<li><input type="checkbox" id="ck-72"><label for="ck-72"><a href="../../../guardrails/observability-and-operations/#gr-ops-03">GR-OPS-03</a> <strong>Define and measure service levels</strong> - Agreed service level objectives with monitoring and alerts</label></li>
<li><input type="checkbox" id="ck-73"><label for="ck-73"><a href="../../../guardrails/observability-and-operations/#gr-ops-04">GR-OPS-04</a> <strong>Health checks and graceful degradation</strong> - Health endpoints, timeout and retry settings, and a design for when dependencies fail</label></li>
<li><input type="checkbox" id="ck-74"><label for="ck-74"><a href="../../../guardrails/observability-and-operations/#gr-ops-07">GR-OPS-07</a> <strong>Measure performance and cost</strong> - Published key performance indicators and cost tags on cloud resources</label></li>
<li><input type="checkbox" id="ck-75"><label for="ck-75"><a href="../../../guardrails/open-source/#gr-open-02">GR-OPEN-02</a> <strong>Licence clearly</strong> - LICENCE file with the Open Government Licence or MIT licence in every repository</label></li>
<li><input type="checkbox" id="ck-76"><label for="ck-76"><a href="../../../guardrails/open-source/#gr-open-03">GR-OPEN-03</a> <strong>Publish safely</strong> - Secret scanning and push protection on for every repository</label></li>
<li><input type="checkbox" id="ck-77"><label for="ck-77"><a href="../../../guardrails/open-source/#gr-open-04">GR-OPEN-04</a> <strong>Reuse and contribute back</strong> - Reuse and upstream contributions noted in ADRs and pull requests</label></li>
<li><input type="checkbox" id="ck-78"><label for="ck-78"><a href="../../../guardrails/products-and-platforms/#gr-prod-01">GR-PROD-01</a> <strong>Fund and run products, not projects</strong> - A named, long-lived team responsible for the product, with a roadmap beyond the current funding period</label></li>
<li><input type="checkbox" id="ck-79"><label for="ck-79"><a href="../../../guardrails/products-and-platforms/#gr-prod-02">GR-PROD-02</a> <strong>Name the product owner and service owner</strong> - Named product owner and service owner, recorded in the service catalogue</label></li>
<li><input type="checkbox" id="ck-80"><label for="ck-80"><a href="../../../guardrails/products-and-platforms/#gr-prod-03">GR-PROD-03</a> <strong>Contribute to platforms rather than working around them</strong> - Requests and contributions raised with platform teams, and ADRs where the team worked around a platform</label></li>
<li><input type="checkbox" id="ck-81"><label for="ck-81"><a href="../../../guardrails/security/#gr-sec-08">GR-SEC-08</a> <strong>Protect the supply chain</strong> - Dependencies pinned and verified, and a software bill of materials produced in the pipeline</label></li>
<li><input type="checkbox" id="ck-82"><label for="ck-82"><a href="../../../guardrails/software-development/#gr-dev-03">GR-DEV-03</a> <strong>Protect the main branch</strong> - Branch protection requiring at least one review and passing checks</label></li>
<li><input type="checkbox" id="ck-83"><label for="ck-83"><a href="../../../guardrails/software-development/#gr-dev-04">GR-DEV-04</a> <strong>Continuous integration and delivery</strong> - Every change built, tested, scanned and deployed by an automated pipeline, with rollback tested</label></li>
<li><input type="checkbox" id="ck-84"><label for="ck-84"><a href="../../../guardrails/software-development/#gr-dev-05">GR-DEV-05</a> <strong>Automated testing at the right levels</strong> - Test results from the pipeline at each level</label></li>
<li><input type="checkbox" id="ck-85"><label for="ck-85"><a href="../../../guardrails/software-development/#gr-dev-06">GR-DEV-06</a> <strong>Manage dependencies actively</strong> - Dependabot or Renovate configured, software composition analysis in the pipeline, and runtimes on supported versions</label></li>
<li><input type="checkbox" id="ck-86"><label for="ck-86"><a href="../../../guardrails/software-development/#gr-dev-07">GR-DEV-07</a> <strong>Follow shared coding standards</strong> - Linting and formatting checks in the pipeline</label></li>
<li><input type="checkbox" id="ck-87"><label for="ck-87"><a href="../../../guardrails/software-development/#gr-dev-08">GR-DEV-08</a> <strong>Document as you go</strong> - README explaining what the service does and how to run, test and deploy it, with links to its ADRs</label></li>
<li><input type="checkbox" id="ck-88"><label for="ck-88"><a href="../../../guardrails/software-development/#gr-dev-09">GR-DEV-09</a> <strong>Record significant decisions as ADRs</strong> - ADR log in the repository or linked from its README</label></li>
<li><input type="checkbox" id="ck-89"><label for="ck-89"><a href="../../../guardrails/sustainability/#gr-sus-02">GR-SUS-02</a> <strong>Right-size and switch off</strong> - Autoscaling and out-of-hours schedules for non-production environments</label></li>
<li><input type="checkbox" id="ck-90"><label for="ck-90"><a href="../../../guardrails/sustainability/#gr-sus-04">GR-SUS-04</a> <strong>Keep data and pages lean</strong> - Data retention settings and page weight measurements</label></li>
</ul>

## Could guardrails

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-91"><label for="ck-91"><a href="../../../guardrails/open-source/#gr-open-05">GR-OPEN-05</a> <strong>Blog and show the thing</strong> - Blog posts, show and tells or contributions to this site</label></li>
</ul>

## Sign-off

| Detail | Answer |
| --- | --- |
| Service | |
| Completed by | |
| Date | |
| Solution design authority | |
| Exceptions or departures (guardrail ids) | |

Read more on the [beta page](https://defra.github.io/architecture/deliver/beta/).


