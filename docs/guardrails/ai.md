---
applicability: tbc
principles: [GR-PRIN-07, GR-PRIN-04]
# Metadata for every guardrail on this page. See the contribution guide for the fields.
guardrail_defaults:
  status: draft
  owner: Architecture team
  automated_check: manual
  last_reviewed: 2026-10-01
  since_version: 0.1.0
guardrails:
  GR-AI-01:
    phases: [discovery, alpha]
    lead_roles: [product-manager, service-designer]
    evidence: ADR recording the AI options considered and why they were or were not used
    service_standard_points: [11]
  GR-AI-02:
    phases: [discovery, alpha, beta, live]
    lead_roles: [technical-architect, security-architect]
    evidence: List of the AI services the service uses and the Defra tenancy or enterprise agreement each runs under
    evidence_by_phase:
      discovery: Any AI services you are exploring identified, with the Defra tenancy or enterprise agreement they would run under
      alpha: AI services chosen for the design, each confirmed as running in a Defra tenancy or under an approved agreement
      beta: The AI services in the built service run only in approved tenancies, shown in the hosting design and configuration
      live: List of AI services in use, reviewed when services or agreements change
    service_standard_points: [9]
    tcop_points: [6, 7]
    sbd_principles: [2]
  GR-AI-03:
    phases: [alpha, beta, live]
    lead_roles: [service-designer, user-researcher]
    evidence: Design of the human oversight and challenge route, tested with users
    evidence_by_phase:
      alpha: Design of the human oversight and challenge route for decisions with significant effects, tested with users in prototypes
      beta: Human review and challenge built into the service and tested with users and staff
      live: Records of human review, challenges raised and their outcomes, reviewed regularly
  GR-AI-04:
    phases: [beta, live]
    lead_roles: [content-designer, interaction-designer]
    evidence: Link to the published Algorithmic Transparency Recording Standard record and the AI notice shown to users
    evidence_by_phase:
      beta: Draft Algorithmic Transparency Recording Standard record, and the notice telling users about AI tested with them
      live: Link to the published Algorithmic Transparency Recording Standard record, kept current
  GR-AI-05:
    phases: [alpha, beta, live]
    lead_roles: [data-architect, security-architect]
    evidence: Model evaluation results for accuracy, bias and safety, live monitoring, and a threat model that covers AI-specific threats
    evidence_by_phase:
      alpha: Evaluation plan for accuracy, bias and safety, and AI-specific threats in the threat model
      beta: Evaluation results for accuracy, bias and safety before release, and mitigations for AI threats tested
      live: Monitoring of model performance and drift in live, with evaluation repeated when the model or data changes
    service_standard_points: [9]
    sbd_principles: [3, 9]
  GR-AI-06:
    phases: [discovery, alpha]
    lead_roles: [technical-architect]
    evidence: Technical Design Authority review outcome recorded in the ADR
    evidence_by_phase:
      discovery: Novel or generative AI use in decision making identified, and a conversation with the Technical Design Authority booked
      alpha: Technical Design Authority review outcome recorded in the ADR
      significant-change: Technical Design Authority review of any new AI use introduced by the change
  GR-AI-07:
    phases: [alpha, beta, live]
    lead_roles: [delivery-manager, developer]
    evidence: "Supplier's agreed list of AI coding assistants and how each runs within Defra-approved terms, the review process for generated code, and disclosure in pull requests or delivery reports"
    since_version: 0.2.0
    sbd_principles: [2, 10]
  GR-AI-08:
    phases: [alpha, beta, live]
    lead_roles: [technical-architect, security-architect]
    evidence: List of each agent's tools and permissions, granted to the agent's own identity and reviewed
    evidence_by_phase:
      alpha: Each agent's tools and permissions listed in the design, with a workload identity for the agent
      beta: Agent permissions configured as designed and tested, including that the agent cannot reach tools it should not
      live: Agent permissions reviewed regularly, as for a privileged user
    since_version: 0.2.0
    sbd_principles: [7]
  GR-AI-09:
    phases: [alpha, beta, live]
    lead_roles: [service-designer, technical-architect]
    evidence: Design showing which agent actions need human approval, and tests proving they cannot happen without it
    evidence_by_phase:
      alpha: Agent actions classified, and the actions that need human approval identified in the design
      beta: Approval enforced in the tool layer, with tests showing the agent cannot act without it
      live: Approval records reviewed, and the classification updated when the agent gains new tools
    since_version: 0.2.0
    sbd_principles: [4]
  GR-AI-10:
    phases: [beta, live]
    lead_roles: [developer, security-architect]
    evidence: Audit records of agent inputs, tool calls, approvals and outcomes, sent to security monitoring
    evidence_by_phase:
      beta: Audit records of agent inputs, tool calls, approvals and outcomes produced and sent to security monitoring
      live: Audit records retained and reviewed, and used to investigate any problem
    since_version: 0.2.0
    sbd_principles: [5]
  GR-AI-11:
    phases: [alpha, beta, live]
    lead_roles: [security-architect, developer]
    evidence: Threat model covering prompt injection through every input the agent reads, with tested mitigations
    evidence_by_phase:
      alpha: Threat model covering prompt injection through every input the agent reads
      beta: Prompt injection mitigations tested, including attempts to misuse tools and leak data
      live: Prompt injection defences re-tested when inputs, tools or models change
    since_version: 0.2.0
    sbd_principles: [3, 8]
---

# Artificial intelligence

<p class="lead">AI can help Defra do more with less - from classifying species in images to drafting responses. These guardrails help teams use it safely, lawfully and transparently.</p>

Applies the DDTS doctrine [assume AI until proven otherwise](../principles/doctrine.md#ddts-05), and builds on the [AI Playbook for the UK Government](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government).

For practical guidance - which tools teams use, what data you can put into them, keeping data safe, working with AI agents and reporting an AI incident - use the [AI digital toolkit](https://digital.defra.gov.uk/ai-toolkit) in the Defra Digital Service Manual, run by the AI Capability and Enablement (AICE) team. Contact details for AICE are on the toolkit's home page. These guardrails set the architecture boundaries; the toolkit tells you how. Technology capability [TC20 Artificial intelligence and machine learning](../handrail/technology-capabilities.md#tc20).

## GR-AI-01 Consider AI first {#gr-ai-01}

<span class="rfc rfc--should">Should</span> When designing a service or process, actively explore whether AI can improve quality, productivity, user experience or outcomes before choosing a traditional approach, and record the reasoning either way.

**Why:** the DDTS doctrine says [assume AI until proven otherwise](../principles/doctrine.md#ddts-05). That does not mean AI everywhere; it means deliberately considering the opportunity before dismissing it.

**How to meet it:** in discovery and alpha, look for repetitive tasks, triage, summarising, classification or decision support that AI could help with. Note in your ADR what you considered and why you did or did not use AI.

**In the AI digital toolkit:** start with [check if AI is right for your idea](https://digital.defra.gov.uk/ai-toolkit/triage/question-1), five questions about the problem, users, data, benefits and what you have tried.

## GR-AI-02 Use approved AI services and tenancies {#gr-ai-02}

<span class="rfc rfc--must">Must</span> Services you build run their AI in Defra's cloud tenancies or under approved enterprise agreements. When anyone uses an AI tool, they put Defra data into it only as the [using data with AI](https://digital.defra.gov.uk/ai-toolkit/guidance/using-data-with-ai) rules in the AI digital toolkit allow - for example, never OFFICIAL-SENSITIVE or personal data in a public consumer tool.

**In the AI digital toolkit:** [choosing a tool](https://digital.defra.gov.uk/ai-toolkit/guidance/choosing-a-tool) and [keeping data safe](https://digital.defra.gov.uk/ai-toolkit/guidance/keeping-data-safe).

## GR-AI-03 Keep a human accountable {#gr-ai-03}

<span class="rfc rfc--must">Must</span> Decisions with legal or significant effects on people or organisations - such as licensing, enforcement or payments - have meaningful human oversight, and the ability to challenge.

## GR-AI-04 Be transparent {#gr-ai-04}

<span class="rfc rfc--must">Must</span> Publish an [Algorithmic Transparency Recording Standard](https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub) record for algorithmic tools that meet its scope, and tell users when they are interacting with AI.

## GR-AI-05 Evaluate, monitor and threat model {#gr-ai-05}

<span class="rfc rfc--should">Should</span> Evaluate models for accuracy, bias and safety before release, monitor them in live, and include AI-specific threats (prompt injection, data leakage, model abuse) in your [threat model](../security/threat-modelling.md).

!!! tip "Cross-government AI tools"
    OCTO's [AI technology enablement](https://architecture.cddo.cabinetoffice.gov.uk/psai-tech/index.html) resources include an AI risk management toolkit, an AI assurance questionnaire, the public sector AI governance operating model and a service assessment questions navigator. Use them to evidence [GR-AI-03](#gr-ai-03), [GR-AI-04](#gr-ai-04) and [GR-AI-05](#gr-ai-05).

## GR-AI-06 Talk to the TDA about novel use {#gr-ai-06}

<span class="rfc rfc--should">Should</span> Novel uses of AI, and any use of generative AI in decision making, are reviewed by the [Technical Design Authority](../governance/tda.md).

## GR-AI-07 Suppliers use AI coding assistants openly and safely {#gr-ai-07}

<span class="rfc rfc--should">Should</span> Delivery partners who use AI coding assistants on Defra work agree which tools they use with Defra, use them only under terms that meet [GR-AI-02](#gr-ai-02), have a person review every change before it is merged, and say in pull requests or delivery reports where AI did significant work.

**Why:** AI coding assistants can speed up delivery, but they can also leak code, secrets or data to a third party, bring in code with unclear licences, and produce plausible but wrong code. Defra owns the code it pays for and must be able to trust it.

**How to meet it:**

- Follow [choosing a tool](https://digital.defra.gov.uk/ai-toolkit/guidance/choosing-a-tool) and [using data with AI](https://digital.defra.gov.uk/ai-toolkit/guidance/using-data-with-ai) in the AI digital toolkit: what matters is the data you put in, and privacy settings must be on.
- Tell the Defra engagement lead which tools you use at [mobilisation](../partners/mobilisation.md), and record them in the repository.
- Follow [AI security](https://digital.defra.gov.uk/ai-toolkit/guidance/security) in the AI digital toolkit: AI-written code clears the same Defra security gates as any other code.
- Never put secrets into prompts.
- Review AI-generated code with the same care as any other code ([GR-DEV-03](software-development.md#gr-dev-03)), including licences of any suggested code.

This guardrail is a **draft** proposal. Comment on it by [opening an issue](https://github.com/DEFRA/architecture/issues).

## Agentic AI

AI agents do more than answer questions: they plan steps and take actions through tools, such as updating records, sending messages or calling APIs. That makes them useful, and it makes mistakes and attacks more costly. For how to build agents in Defra - identity, connecting tools, evaluations and tracing, and which platforms are ready - see [working with AI agents](https://digital.defra.gov.uk/ai-toolkit/guidance/working-with-agents) in the AI digital toolkit, and talk to AICE before you choose a platform. These draft guardrails come from the [guardrail backlog](../about/roadmap.md#guardrail-backlog) and apply on top of [GR-AI-02](#gr-ai-02) to [GR-AI-06](#gr-ai-06).

## GR-AI-08 Give agents the least privilege they need {#gr-ai-08}

<span class="rfc rfc--should">Should</span> AI agents act under their own identity, with access only to the tools, data and actions their task needs, and never with a person's full permissions.

**Why:** an agent can be tricked, or can be wrong. Limiting what it can reach limits the damage ([GR-IAM-03](identity-and-access.md#gr-iam-03)).

**How to meet it:** list each agent's tools and permissions, grant them to a workload identity for the agent, and review them as you would a privileged user's.

**In the AI digital toolkit:** [working with AI agents](https://digital.defra.gov.uk/ai-toolkit/guidance/working-with-agents).

## GR-AI-09 Get human approval for consequential actions {#gr-ai-09}

<span class="rfc rfc--should">Should</span> An agent does not take an action with legal, financial or significant effects on people, or one that cannot easily be undone, without approval from an accountable person.

**Why:** [GR-AI-03](#gr-ai-03) keeps a human accountable for decisions. Agents act faster than people can notice, so approval has to be designed in, not assumed.

**How to meet it:** classify the agent's actions in alpha. Enforce approval in the tool layer, not only in the prompt, and test that the agent cannot bypass it.

**In the AI digital toolkit:** [working with AI agents](https://digital.defra.gov.uk/ai-toolkit/guidance/working-with-agents).

## GR-AI-10 Keep an audit trail of what agents do {#gr-ai-10}

<span class="rfc rfc--should">Should</span> Record what each agent was asked, what it read, which tools it called with what inputs, who approved what, and the outcome - and send security-relevant events to security monitoring.

**Why:** without a full record, nobody can explain, challenge or reverse what an agent did.

**How to meet it:** log at the tool layer with correlation ids ([GR-OPS-02](observability-and-operations.md#gr-ops-02)), and keep records for as long as the decisions they support.

**In the AI digital toolkit:** [working with AI agents](https://digital.defra.gov.uk/ai-toolkit/guidance/working-with-agents).

## GR-AI-11 Defend agents against prompt injection {#gr-ai-11}

<span class="rfc rfc--should">Should</span> Treat everything an agent reads - documents, emails, web pages, tool results - as untrusted input that may try to change its instructions, and design controls that hold even if it does.

**Why:** prompt injection is the most common way to make an agent misuse its tools or leak data.

**How to meet it:** include injection through every input in your [threat model](../security/threat-modelling.md) ([GR-AI-05](#gr-ai-05)), separate untrusted content from instructions, restrict tools as in GR-AI-08 and require approval as in GR-AI-09.

**In the AI digital toolkit:** [working with AI agents](https://digital.defra.gov.uk/ai-toolkit/guidance/working-with-agents).
