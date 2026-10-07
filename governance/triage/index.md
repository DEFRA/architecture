<!-- https://defra.github.io/architecture/governance/triage/ | maturity: published | site version 0.3.0 | generated from governance/triage.md -->

# Which route do I take?

<p class="lead">Answer five questions to find the lightest governance route that fits your work.</p>

!!! tip "Prefer an interactive version?"
    The [decision check](https://defra.github.io/architecture/governance/decision-check/) walks you through these questions, suggests a route and drafts a decision record for you.

```mermaid
flowchart TD
    accTitle: Governance triage decision tree
    accDescr: Changes to strategy or strategic platforms go to the Technology Governance Board. Exceptions to Must guardrails, and novel or cross-cutting work, go to the Technical Design Authority. Departures from Should guardrails, phase gates and significant changes go to the solution design authority. Everything else is self-assured and recorded in an ADR.
    A([Start]) --> Q1{"Does it change Defra<br/>technology strategy, or<br/>create or retire a<br/>strategic platform?"}
    Q1 -->|Yes| TGB["Technology<br/>Governance Board"]
    Q1 -->|No| Q2{"Do you need an exception<br/>to a <b>Must</b> guardrail?"}
    Q2 -->|Yes| TDA["Technical Design<br/>Authority"]
    Q2 -->|No| Q3{"Is it novel for Defra, or<br/>does it affect services<br/>beyond your own?"}
    Q3 -->|Yes| TDA
    Q3 -->|No| Q4{"Do you depart from a<br/><b>Should</b> guardrail or a<br/>strategic capability?"}
    Q4 -->|Yes| SDA["Solution design<br/>authority"]
    Q4 -->|No| Q5{"Is it a phase gate<br/>or significant change?"}
    Q5 -->|Yes| SDA
    Q5 -->|No| SELF["Self-assure and<br/>record an ADR"]
```

## The questions in more detail

### 1. Does it change strategy or a strategic platform?

Examples: adopting a new cloud provider, introducing a new strategic platform, changing a Must guardrail, retiring a capability used across Defra. These go to the [Technology Governance Board](https://defra.github.io/architecture/governance/tgb/), normally after review by the TDA.

### 2. Do you need an exception to a Must guardrail?

Examples: hosting outside the Core Delivery Platform, building your own sign-in, keeping code private. Go to the [Technical Design Authority](https://defra.github.io/architecture/governance/tda/) via the [exception process](https://defra.github.io/architecture/governance/exceptions/).

### 3. Is it novel or cross-cutting?

**Novel** means Defra has not done it before: a new technology, a new integration pattern, a first use of generative AI in a service. **Cross-cutting** means other services, teams or arm's length bodies will depend on it or be affected by it: a new shared API, a change to a shared data set, a new identity integration pattern. Go to the [TDA](https://defra.github.io/architecture/governance/tda/).

### 4. Do you depart from a Should guardrail or strategic capability?

Record your reasoning in an [ADR](https://defra.github.io/architecture/governance/architecture-decision-records/) and agree it with your [solution design authority](https://defra.github.io/architecture/governance/solution-design-authorities/).

### 5. Is it a phase gate or significant change?

Share your architecture, ADR log and threat model with your SDA ahead of alpha, beta and live assessments, and before significant changes.

### Otherwise - self-assure

Use the [10-minute self-assurance checklist](https://defra.github.io/architecture/guardrails/#self-assure-in-10-minutes), record significant decisions as ADRs, and carry on.

## Not sure?

Ask. The architecture team runs drop-in sessions for teams and delivery partners and will tell you the right route - usually in a single conversation. See [the architecture team](https://defra.github.io/architecture/about/team/).

