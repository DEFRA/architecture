# Sample ADRs: apply for a licence

<p class="lead">Three architecture decision records from the fictional apply for a licence service, written with the <a href="../../../governance/templates/adr/">ADR template</a>. Use them as examples of the level of detail we expect.</p>

!!! info "Fictional examples"
    These ADRs belong to an invented service. The reasoning is realistic, but they are not real Defra decisions.

## 0001. Host on the Core Delivery Platform {#adr-0001}

- Status: Accepted
- Date: 2026-04-14
- Deciders: tech lead, product manager, solution architect
- Decided by: team, shared with the solution design authority
- Business capabilities: BC05 Issue licences and permits
- Technology capabilities: TC21 Application hosting and delivery platform
- Guardrails: GR-HOST-01 (met), GR-TECH-01 (met), GR-HOST-03 (met)
- Advice sought from: platform team

### Context

The service needs hosting for a front end, an API, a database, object storage and a scanner, with CI/CD, secrets and monitoring. The team is new to Defra and wants to reach a private beta in six months.

### Options considered

**Option 1: Core Delivery Platform (strategic).** Pros: hosting, pipelines, secrets, observability and protective monitoring already provided and assured; templates for Node.js services. Cons: the team must learn the platform's conventions; file scanning needs confirming with the platform team.

**Option 2: our own cloud account.** Pros: full control. Cons: we would rebuild what the platform already provides, need an exception to GR-HOST-01, and carry the security and support burden ourselves.

### Decision

We will host on the Core Delivery Platform because it meets every hosting need we have found, keeps us inside the guardrails, and lets the team spend its time on users.

### Consequences

- We use the platform's templates for infrastructure and pipelines.
- We agreed with the platform team how file scanning will work (see the [file upload pattern](../file-upload.md)).
- If the service later needs something the platform does not offer, we will raise it with the platform team before building around it.

## 0002. Accept applications asynchronously with an outbox {#adr-0002}

- Status: Accepted
- Date: 2026-05-02
- Deciders: tech lead, solution architect, case management product owner
- Decided by: team, shared with the solution design authority
- Technology capabilities: TC08 Case and workflow management, TC22 API management and integration
- Guardrails: GR-API-05 (met), GR-API-06 (met), GR-API-02 (met), GR-OPS-04 (met)
- Advice sought from: case management team, platform team

### Context

Applications must reach case management. Case management has planned downtime most weekends and its API can take several seconds to respond. Users told us in research that losing a half-finished application is the thing that most puts them off online services.

### Options considered

**Option 1: call the case management API synchronously on submit.** Pros: simple; immediate case reference. Cons: users cannot submit when case management is down; slow responses in the journey.

**Option 2: write directly to the case management database.** Pros: fast. Cons: breaks GR-API-05 and couples us to their schema.

**Option 3: save the application and an outbox record together, and publish an event** ([asynchronous submission pattern](../async-submission.md)). Pros: users can always submit; case management processes at its own pace; other consumers can subscribe later. Cons: more moving parts; the case reference arrives later.

### Decision

We will use option 3. Users get our own application reference straight away, and an email with the case reference once case management has picked up the application.

### Consequences

- We describe the `application-submitted` event in AsyncAPI in our repository.
- Case management must handle duplicate events using the event id.
- We monitor the dead letter queue and alert on any message older than one hour.

## 0003. Use Defra ID and the authoritative relationships for agents {#adr-0003}

- Status: Accepted
- Date: 2026-05-20
- Deciders: tech lead, product manager, identity team representative
- Decided by: solution design authority
- Technology capabilities: TC01 Customer identity and access, TC17 Reference and master data
- Guardrails: GR-IAM-01 (met), GR-IAM-04 (met), GR-DATA-02 (met)
- Advice sought from: identity team, enterprise data architecture

### Context

About a third of applications are made by agents for landowners. Some agents act for more than 50 landowners. Agents must only see and apply for the landowners and holdings they act for.

### Options considered

**Option 1: Defra ID for sign-in, relationships from the authoritative source, authorisation in our API** ([acting on behalf pattern](../acting-on-behalf.md)). Pros: one sign-in across Defra services; relationships stay current; rules are explicit and testable. Cons: depends on the relationships source being available.

**Option 2: our own table of which agent acts for which landowner.** Pros: no dependency. Cons: duplicates data Defra already holds, drifts, and breaks GR-DATA-02.

### Decision

We will use option 1. If the relationships source is unavailable, users can carry on with applications already started but cannot start one for a new organisation.

### Consequences

- An authorisation module in the API checks every request against the organisation the user is acting for, with unit tests for each role.
- Authorisation refusals are logged as security events.
