<!-- https://defra.github.io/architecture/deliver/checklists/alpha/ | maturity: prototype | site version 0.3.0 | generated from deliver/checklists/alpha.md -->

# Alpha evidence checklist

<p class="lead">The architecture evidence for alpha, as a checklist you can work through or print. Built from the guardrail metadata each time the site is published.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



Tick what you have, link to where it lives, and bring it to your solution design authority or assessment. Where you cannot meet a Must, record the approved [exception](https://defra.github.io/architecture/governance/exceptions/).

<p class="dl-print"><button type="button" class="md-button" data-print>Print this checklist</button></p>

## Artefacts

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-1"><label for="ck-1"><strong>Architecture decision record (ADR) log</strong> - Record hosting, identity, integration and data decisions.</label></li>
<li><input type="checkbox" id="ck-2"><label for="ck-2"><strong>C4 system context diagram</strong> - Confirm the context.</label></li>
<li><input type="checkbox" id="ck-3"><label for="ck-3"><strong>C4 container diagram</strong> - Draw the containers for the options you are testing.</label></li>
<li><input type="checkbox" id="ck-4"><label for="ck-4"><strong>Threat model</strong> - Run the first collaborative threat model.</label></li>
<li><input type="checkbox" id="ck-5"><label for="ck-5"><strong>Data protection impact assessment (DPIA)</strong> - Complete the DPIA if you process personal data.</label></li>
<li><input type="checkbox" id="ck-6"><label for="ck-6"><strong>Service tier</strong> - Agree the tier with the service owner.</label></li>
<li><input type="checkbox" id="ck-7"><label for="ck-7"><strong>Non-functional requirements (NFRs)</strong> - Choose NFRs from the catalogue for your tier.</label></li>
<li><input type="checkbox" id="ck-8"><label for="ck-8"><strong>Exit plan</strong> - Draft an exit plan for each new product or supplier.</label></li>
</ul>

## Must guardrails

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-9"><label for="ck-9"><a href="../../../guardrails/ai/#gr-ai-02">GR-AI-02</a> <strong>Use approved AI services and tenancies</strong> - AI services chosen for the design, each confirmed as running in a Defra tenancy or under an approved agreement</label></li>
<li><input type="checkbox" id="ck-10"><label for="ck-10"><a href="../../../guardrails/ai/#gr-ai-03">GR-AI-03</a> <strong>Keep a human accountable</strong> - Design of the human oversight and challenge route for decisions with significant effects, tested with users in prototypes</label></li>
<li><input type="checkbox" id="ck-11"><label for="ck-11"><a href="../../../guardrails/apis-and-integration/#gr-api-07">GR-API-07</a> <strong>Secure every API</strong> - Authentication, authorisation, input validation and rate limiting designed for each API</label></li>
<li><input type="checkbox" id="ck-12"><label for="ck-12"><a href="../../../guardrails/choosing-technology/#gr-tech-01">GR-TECH-01</a> <strong>Look for something to reuse first</strong> - ADR recording the reuse options considered and why they did or did not fit</label></li>
<li><input type="checkbox" id="ck-13"><label for="ck-13"><a href="../../../guardrails/choosing-technology/#gr-tech-04">GR-TECH-04</a> <strong>Assess SaaS before you adopt it</strong> - Security, data protection, data location, accessibility and single sign-on assessed before contract</label></li>
<li><input type="checkbox" id="ck-14"><label for="ck-14"><a href="../../../guardrails/data/#gr-data-06">GR-DATA-06</a> <strong>Protect personal data by design</strong> - Draft DPIA, with data minimisation and retention designed in</label></li>
<li><input type="checkbox" id="ck-15"><label for="ck-15"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-01">GR-FE-01</a> <strong>Meet WCAG 2.2 AA</strong> - Prototypes built with accessible components, and a plan for an accessibility audit and assistive technology testing</label></li>
<li><input type="checkbox" id="ck-16"><label for="ck-16"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-02">GR-FE-02</a> <strong>Use the GOV.UK Design System</strong> - Prototypes built with the GOV.UK Design System, with departures recorded and researched</label></li>
<li><input type="checkbox" id="ck-17"><label for="ck-17"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-06">GR-FE-06</a> <strong>Support Welsh where required</strong> - Whether the Welsh Language Standards apply decided, and the service designed for translation</label></li>
<li><input type="checkbox" id="ck-18"><label for="ck-18"><a href="../../../guardrails/hosting-and-platforms/#gr-host-01">GR-HOST-01</a> <strong>Use Defra&#x27;s strategic delivery platform by default</strong> - The design runs on the Core Delivery Platform, or an exception has been requested</label></li>
<li><input type="checkbox" id="ck-19"><label for="ck-19"><a href="../../../guardrails/identity-and-access/#gr-iam-01">GR-IAM-01</a> <strong>Use the strategic customer identity services</strong> - Sign-in designed with Defra Customer Identity, and tested with users</label></li>
<li><input type="checkbox" id="ck-20"><label for="ck-20"><a href="../../../guardrails/identity-and-access/#gr-iam-05">GR-IAM-05</a> <strong>No secrets in code</strong> - Secret scanning on from the first commit, and secrets held in a managed store from the start</label></li>
<li><input type="checkbox" id="ck-21"><label for="ck-21"><a href="../../../guardrails/open-source/#gr-open-01">GR-OPEN-01</a> <strong>Code in the open</strong> - Code public in a Defra GitHub organisation from the first commit, or a recorded reason for keeping a repository private</label></li>
<li><input type="checkbox" id="ck-22"><label for="ck-22"><a href="../../../guardrails/security/#gr-sec-01">GR-SEC-01</a> <strong>Follow Secure by Design</strong> - Secure by Design activities for alpha completed, including security requirements in the backlog</label></li>
<li><input type="checkbox" id="ck-23"><label for="ck-23"><a href="../../../guardrails/security/#gr-sec-02">GR-SEC-02</a> <strong>Keep a current threat model</strong> - First threat model, created by the team</label></li>
<li><input type="checkbox" id="ck-24"><label for="ck-24"><a href="../../../guardrails/security/#gr-sec-03">GR-SEC-03</a> <strong>Classify information</strong> - Controls in the design that match the classification</label></li>
<li><input type="checkbox" id="ck-25"><label for="ck-25"><a href="../../../guardrails/security/#gr-sec-09">GR-SEC-09</a> <strong>Manage risk explicitly</strong> - Risks from controls that cannot be met recorded, with an owner</label></li>
<li><input type="checkbox" id="ck-26"><label for="ck-26"><a href="../../../guardrails/software-development/#gr-dev-02">GR-DEV-02</a> <strong>All code in Defra source control</strong> - All code, including prototypes and infrastructure code written by suppliers, in a Defra-owned GitHub organisation from the first commit</label></li>
</ul>

## Should guardrails

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-27"><label for="ck-27"><a href="../../../guardrails/ai/#gr-ai-01">GR-AI-01</a> <strong>Consider AI first</strong> - ADR recording the AI options considered and why they were or were not used</label></li>
<li><input type="checkbox" id="ck-28"><label for="ck-28"><a href="../../../guardrails/ai/#gr-ai-05">GR-AI-05</a> <strong>Evaluate, monitor and threat model</strong> - Evaluation plan for accuracy, bias and safety, and AI-specific threats in the threat model</label></li>
<li><input type="checkbox" id="ck-29"><label for="ck-29"><a href="../../../guardrails/ai/#gr-ai-06">GR-AI-06</a> <strong>Talk to the TDA about novel use</strong> - Technical Design Authority review outcome recorded in the ADR</label></li>
<li><input type="checkbox" id="ck-30"><label for="ck-30"><a href="../../../guardrails/ai/#gr-ai-07">GR-AI-07</a> <strong>Suppliers use AI coding assistants openly and safely</strong> - Supplier&#x27;s agreed list of AI coding assistants and how each runs within Defra-approved terms, the review process for generated code, and disclosure in pull requests or delivery reports</label></li>
<li><input type="checkbox" id="ck-31"><label for="ck-31"><a href="../../../guardrails/ai/#gr-ai-08">GR-AI-08</a> <strong>Give agents the least privilege they need</strong> - Each agent&#x27;s tools and permissions listed in the design, with a workload identity for the agent</label></li>
<li><input type="checkbox" id="ck-32"><label for="ck-32"><a href="../../../guardrails/ai/#gr-ai-09">GR-AI-09</a> <strong>Get human approval for consequential actions</strong> - Agent actions classified, and the actions that need human approval identified in the design</label></li>
<li><input type="checkbox" id="ck-33"><label for="ck-33"><a href="../../../guardrails/ai/#gr-ai-11">GR-AI-11</a> <strong>Defend agents against prompt injection</strong> - Threat model covering prompt injection through every input the agent reads</label></li>
<li><input type="checkbox" id="ck-34"><label for="ck-34"><a href="../../../guardrails/apis-and-integration/#gr-api-01">GR-API-01</a> <strong>API first</strong> - API specification written before or alongside the user interface</label></li>
<li><input type="checkbox" id="ck-35"><label for="ck-35"><a href="../../../guardrails/apis-and-integration/#gr-api-02">GR-API-02</a> <strong>Describe APIs with open specifications</strong> - Draft OpenAPI 3 or AsyncAPI documents for the interfaces you are prototyping</label></li>
<li><input type="checkbox" id="ck-36"><label for="ck-36"><a href="../../../guardrails/apis-and-integration/#gr-api-03">GR-API-03</a> <strong>Follow government API standards</strong> - API design reviewed against the GDS API technical and data standards</label></li>
<li><input type="checkbox" id="ck-37"><label for="ck-37"><a href="../../../guardrails/apis-and-integration/#gr-api-05">GR-API-05</a> <strong>No integration through shared databases</strong> - Container diagram showing integration only through APIs, events or governed data products</label></li>
<li><input type="checkbox" id="ck-38"><label for="ck-38"><a href="../../../guardrails/apis-and-integration/#gr-api-06">GR-API-06</a> <strong>Use events for change notifications</strong> - Event and message definitions described in AsyncAPI</label></li>
<li><input type="checkbox" id="ck-39"><label for="ck-39"><a href="../../../guardrails/choosing-technology/#gr-tech-02">GR-TECH-02</a> <strong>Buy commodity, build differentiating</strong> - Buy or build options appraisal in the ADR or business case</label></li>
<li><input type="checkbox" id="ck-40"><label for="ck-40"><a href="../../../guardrails/choosing-technology/#gr-tech-03">GR-TECH-03</a> <strong>Plan your exit before you enter</strong> - Draft exit plan for each new product, platform or significant supplier</label></li>
<li><input type="checkbox" id="ck-41"><label for="ck-41"><a href="../../../guardrails/choosing-technology/#gr-tech-05">GR-TECH-05</a> <strong>Prefer open standards and portable technology</strong> - ADR noting the open standards used and how portable the choice is</label></li>
<li><input type="checkbox" id="ck-42"><label for="ck-42"><a href="../../../guardrails/data/#gr-data-01">GR-DATA-01</a> <strong>Every data set has an owner</strong> - Each data set the service will create or hold identified, with a proposed information asset owner</label></li>
<li><input type="checkbox" id="ck-43"><label for="ck-43"><a href="../../../guardrails/data/#gr-data-02">GR-DATA-02</a> <strong>Use authoritative sources</strong> - Data flow diagram naming the authoritative source for each shared entity, and how any copies are refreshed</label></li>
<li><input type="checkbox" id="ck-44"><label for="ck-44"><a href="../../../guardrails/data/#gr-data-03">GR-DATA-03</a> <strong>Use agreed data standards and identifiers</strong> - Data model using the agreed data standards and identifiers</label></li>
<li><input type="checkbox" id="ck-45"><label for="ck-45"><a href="../../../guardrails/data/#gr-data-04">GR-DATA-04</a> <strong>Collect once, share safely</strong> - Journey design showing users are not asked for information Defra already holds, and data sharing agreements where required</label></li>
<li><input type="checkbox" id="ck-46"><label for="ck-46"><a href="../../../guardrails/data/#gr-data-10">GR-DATA-10</a> <strong>Handle research data safely</strong> - The same for alpha research, with DPIA screening done for the research and any new research tool assessed</label></li>
<li><input type="checkbox" id="ck-47"><label for="ck-47"><a href="../../../guardrails/data/#gr-data-11">GR-DATA-11</a> <strong>No real personal data in prototypes</strong> - Prototypes and research materials use made-up data, including data a participant types in during a session</label></li>
<li><input type="checkbox" id="ck-48"><label for="ck-48"><a href="../../../guardrails/digital-first/#gr-dig-01">GR-DIG-01</a> <strong>Challenge paper and manual processes</strong> - Discovery findings showing paper, email and manual steps in the current process and how the new design removes or justifies each one</label></li>
<li><input type="checkbox" id="ck-49"><label for="ck-49"><a href="../../../guardrails/digital-first/#gr-dig-02">GR-DIG-02</a> <strong>Design across organisational boundaries</strong> - A map of the whole service, including the parts other teams and organisations deliver, and agreed hand-offs between them</label></li>
<li><input type="checkbox" id="ck-50"><label for="ck-50"><a href="../../../guardrails/digital-first/#gr-dig-03">GR-DIG-03</a> <strong>Provide assisted digital and offline routes</strong> - Assisted digital and offline routes designed and tested with users who need them</label></li>
<li><input type="checkbox" id="ck-51"><label for="ck-51"><a href="../../../guardrails/field-working-and-devices/#gr-field-01">GR-FIELD-01</a> <strong>Choose devices that suit the job</strong> - User research on the working environment, and the device choice recorded in an ADR</label></li>
<li><input type="checkbox" id="ck-52"><label for="ck-52"><a href="../../../guardrails/field-working-and-devices/#gr-field-02">GR-FIELD-02</a> <strong>Design field tools to work offline</strong> - Field journeys tested with no connection, including sync after reconnecting and conflict handling</label></li>
<li><input type="checkbox" id="ck-53"><label for="ck-53"><a href="../../../guardrails/field-working-and-devices/#gr-field-03">GR-FIELD-03</a> <strong>Manage and secure every device</strong> - Device management approach agreed for the devices the service will use</label></li>
<li><input type="checkbox" id="ck-54"><label for="ck-54"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-03">GR-FE-03</a> <strong>Progressive enhancement</strong> - Core journeys tested with JavaScript turned off</label></li>
<li><input type="checkbox" id="ck-55"><label for="ck-55"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-04">GR-FE-04</a> <strong>Consider forms platforms first</strong> - ADR noting whether the forms capability was considered</label></li>
<li><input type="checkbox" id="ck-56"><label for="ck-56"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-05">GR-FE-05</a> <strong>Design for low bandwidth and rural users</strong> - Page weight budget, save-progress design and testing on slow connections</label></li>
<li><input type="checkbox" id="ck-57"><label for="ck-57"><a href="../../../guardrails/front-end-and-accessibility/#gr-fe-07">GR-FE-07</a> <strong>Tell users what is happening when things fail or are slow</strong> - Each dependency that can fail or be slow identified with the developers, and what users see in each case designed and tested in the prototype</label></li>
<li><input type="checkbox" id="ck-58"><label for="ck-58"><a href="../../../guardrails/hosting-and-platforms/#gr-host-02">GR-HOST-02</a> <strong>Public cloud first</strong> - Where the platform cannot be used, the hosting design uses a Defra-managed public cloud tenancy</label></li>
<li><input type="checkbox" id="ck-59"><label for="ck-59"><a href="../../../guardrails/hosting-and-platforms/#gr-host-04">GR-HOST-04</a> <strong>Use managed services before self-managed</strong> - Hosting design listing the managed services used</label></li>
<li><input type="checkbox" id="ck-60"><label for="ck-60"><a href="../../../guardrails/hosting-and-platforms/#gr-host-05">GR-HOST-05</a> <strong>Consistent, disposable environments</strong> - Environments created from the same code, and how lower environments avoid real personal data</label></li>
<li><input type="checkbox" id="ck-61"><label for="ck-61"><a href="../../../guardrails/hosting-and-platforms/#gr-host-06">GR-HOST-06</a> <strong>Host data in the UK</strong> - Hosting design places every data store and backup in UK regions</label></li>
<li><input type="checkbox" id="ck-62"><label for="ck-62"><a href="../../../guardrails/hosting-and-platforms/#gr-host-07">GR-HOST-07</a> <strong>Design for the resilience the service needs</strong> - Recovery time and recovery point objectives agreed with the service owner, and a design that meets them</label></li>
<li><input type="checkbox" id="ck-63"><label for="ck-63"><a href="../../../guardrails/identity-and-access/#gr-iam-04">GR-IAM-04</a> <strong>Separate authentication from authorisation</strong> - Authorisation rules written down and covered by automated tests</label></li>
<li><input type="checkbox" id="ck-64"><label for="ck-64"><a href="../../../guardrails/open-source/#gr-open-02">GR-OPEN-02</a> <strong>Licence clearly</strong> - LICENCE file in every repository from the start</label></li>
<li><input type="checkbox" id="ck-65"><label for="ck-65"><a href="../../../guardrails/open-source/#gr-open-03">GR-OPEN-03</a> <strong>Publish safely</strong> - Secret scanning and push protection on for every repository from the first commit</label></li>
<li><input type="checkbox" id="ck-66"><label for="ck-66"><a href="../../../guardrails/open-source/#gr-open-04">GR-OPEN-04</a> <strong>Reuse and contribute back</strong> - Reuse and upstream contributions noted in ADRs and pull requests</label></li>
<li><input type="checkbox" id="ck-67"><label for="ck-67"><a href="../../../guardrails/products-and-platforms/#gr-prod-01">GR-PROD-01</a> <strong>Fund and run products, not projects</strong> - A named, long-lived team responsible for the product, with a roadmap beyond the current funding period</label></li>
<li><input type="checkbox" id="ck-68"><label for="ck-68"><a href="../../../guardrails/products-and-platforms/#gr-prod-02">GR-PROD-02</a> <strong>Name the product owner and service owner</strong> - Named product owner and service owner, recorded in the service catalogue</label></li>
<li><input type="checkbox" id="ck-69"><label for="ck-69"><a href="../../../guardrails/products-and-platforms/#gr-prod-03">GR-PROD-03</a> <strong>Contribute to platforms rather than working around them</strong> - Requests and contributions raised with platform teams, and ADRs where the team worked around a platform</label></li>
<li><input type="checkbox" id="ck-70"><label for="ck-70"><a href="../../../guardrails/security/#gr-sec-08">GR-SEC-08</a> <strong>Protect the supply chain</strong> - Security assessment of suppliers and third-party products in the design</label></li>
<li><input type="checkbox" id="ck-71"><label for="ck-71"><a href="../../../guardrails/software-development/#gr-dev-01">GR-DEV-01</a> <strong>Use the supported languages and frameworks</strong> - ADR recording the reason wherever the service uses a different stack</label></li>
<li><input type="checkbox" id="ck-72"><label for="ck-72"><a href="../../../guardrails/software-development/#gr-dev-03">GR-DEV-03</a> <strong>Protect the main branch</strong> - Main branch protected from the start, with changes through reviewed pull requests</label></li>
<li><input type="checkbox" id="ck-73"><label for="ck-73"><a href="../../../guardrails/software-development/#gr-dev-05">GR-DEV-05</a> <strong>Automated testing at the right levels</strong> - Test results from the pipeline at each level</label></li>
<li><input type="checkbox" id="ck-74"><label for="ck-74"><a href="../../../guardrails/software-development/#gr-dev-07">GR-DEV-07</a> <strong>Follow shared coding standards</strong> - Linting and formatting checks in the pipeline</label></li>
<li><input type="checkbox" id="ck-75"><label for="ck-75"><a href="../../../guardrails/software-development/#gr-dev-08">GR-DEV-08</a> <strong>Document as you go</strong> - README explaining what the service does and how to run, test and deploy it, with links to its ADRs</label></li>
<li><input type="checkbox" id="ck-76"><label for="ck-76"><a href="../../../guardrails/software-development/#gr-dev-09">GR-DEV-09</a> <strong>Record significant decisions as ADRs</strong> - ADR log in the repository or linked from its README</label></li>
<li><input type="checkbox" id="ck-77"><label for="ck-77"><a href="../../../guardrails/sustainability/#gr-sus-01">GR-SUS-01</a> <strong>Consider sustainability in design decisions</strong> - Environmental impact recorded in ADRs for hosting and technology choices</label></li>
<li><input type="checkbox" id="ck-78"><label for="ck-78"><a href="../../../guardrails/sustainability/#gr-sus-04">GR-SUS-04</a> <strong>Keep data and pages lean</strong> - Data retention settings and page weight measurements</label></li>
</ul>

## Could guardrails

<ul class="dl-checklist">
<li><input type="checkbox" id="ck-79"><label for="ck-79"><a href="../../../guardrails/field-working-and-devices/#gr-field-04">GR-FIELD-04</a> <strong>Check connectivity before you design</strong> - Connectivity in the places the service will be used checked, and the approach recorded</label></li>
<li><input type="checkbox" id="ck-80"><label for="ck-80"><a href="../../../guardrails/open-source/#gr-open-05">GR-OPEN-05</a> <strong>Blog and show the thing</strong> - Blog posts, show and tells or contributions to this site</label></li>
<li><input type="checkbox" id="ck-81"><label for="ck-81"><a href="../../../guardrails/sustainability/#gr-sus-03">GR-SUS-03</a> <strong>Choose lower-carbon regions and services</strong> - Region and service choice recorded with its carbon intensity</label></li>
</ul>

## Sign-off

| Detail | Answer |
| --- | --- |
| Service | |
| Completed by | |
| Date | |
| Solution design authority | |
| Exceptions or departures (guardrail ids) | |

Read more on the [alpha page](https://defra.github.io/architecture/deliver/alpha/).


