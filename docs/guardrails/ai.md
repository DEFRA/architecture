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
    evidence: ADR recording the AI options considered and why they were or were not used
    service_standard_points: [11]
  GR-AI-02:
    phases: [discovery, alpha, beta, live]
    evidence: List of the AI services the service uses and the Defra tenancy or enterprise agreement each runs under
    service_standard_points: [9]
    tcop_points: [6, 7]
    sbd_principles: [2]
  GR-AI-03:
    phases: [alpha, beta, live]
    evidence: Design of the human oversight and challenge route, tested with users
  GR-AI-04:
    phases: [beta, live]
    evidence: Link to the published Algorithmic Transparency Recording Standard record and the AI notice shown to users
  GR-AI-05:
    phases: [alpha, beta, live]
    evidence: Model evaluation results for accuracy, bias and safety, live monitoring, and a threat model that covers AI-specific threats
    service_standard_points: [9]
    sbd_principles: [3, 9]
  GR-AI-06:
    phases: [discovery, alpha]
    evidence: Technical Design Authority review outcome recorded in the ADR
  GR-AI-07:
    phases: [alpha, beta, live]
    evidence: "Supplier's agreed list of AI coding assistants and how each runs within Defra-approved terms, the review process for generated code, and disclosure in pull requests or delivery reports"
    since_version: 0.2.0
    sbd_principles: [2, 10]
  GR-AI-08:
    phases: [alpha, beta, live]
    evidence: List of each agent's tools and permissions, granted to the agent's own identity and reviewed
    since_version: 0.2.0
    sbd_principles: [7]
  GR-AI-09:
    phases: [alpha, beta, live]
    evidence: Design showing which agent actions need human approval, and tests proving they cannot happen without it
    since_version: 0.2.0
    sbd_principles: [4]
  GR-AI-10:
    phases: [beta, live]
    evidence: Audit records of agent inputs, tool calls, approvals and outcomes, sent to security monitoring
    since_version: 0.2.0
    sbd_principles: [5]
  GR-AI-11:
    phases: [alpha, beta, live]
    evidence: Threat model covering prompt injection through every input the agent reads, with tested mitigations
    since_version: 0.2.0
    sbd_principles: [3, 8]
---

# Artificial intelligence

<p class="lead">AI can help Defra do more with less - from classifying species in images to drafting responses. These guardrails help teams use it safely, lawfully and transparently.</p>

Applies the DDTS doctrine [assume AI until proven otherwise](../principles/doctrine.md#ddts-05), and builds on the [AI Playbook for the UK Government](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government). Technology capability [TC20 Artificial intelligence and machine learning](../handrail/technology-capabilities.md#tc20).

## GR-AI-01 Consider AI first {#gr-ai-01}

<span class="rfc rfc--should">Should</span> When designing a service or process, actively explore whether AI can improve quality, productivity, user experience or outcomes before choosing a traditional approach, and record the reasoning either way.

**Why:** the DDTS doctrine says [assume AI until proven otherwise](../principles/doctrine.md#ddts-05). That does not mean AI everywhere; it means deliberately considering the opportunity before dismissing it.

**How to meet it:** in discovery and alpha, look for repetitive tasks, triage, summarising, classification or decision support that AI could help with. Note in your ADR what you considered and why you did or did not use AI.

## GR-AI-02 Use approved AI services and tenancies {#gr-ai-02}

<span class="rfc rfc--must">Must</span> Use AI services provisioned within Defra's cloud tenancies or approved enterprise agreements. Do not put Defra data into consumer AI tools.

## GR-AI-03 Keep a human accountable {#gr-ai-03}

<span class="rfc rfc--must">Must</span> Decisions with legal or significant effects on people or organisations - such as licensing, enforcement or payments - have meaningful human oversight, and the ability to challenge.

## GR-AI-04 Be transparent {#gr-ai-04}

<span class="rfc rfc--must">Must</span> Publish an [Algorithmic Transparency Recording Standard](https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub) record for algorithmic tools that meet its scope, and tell users when they are interacting with AI.

## GR-AI-05 Evaluate, monitor and threat model {#gr-ai-05}

<span class="rfc rfc--must">Must</span> Evaluate models for accuracy, bias and safety before release, monitor them in live, and include AI-specific threats (prompt injection, data leakage, model abuse) in your [threat model](../security/threat-modelling.md).

!!! tip "Cross-government AI tools"
    OCTO's [AI technology enablement](https://architecture.cddo.cabinetoffice.gov.uk/psai-tech/index.html) resources include an AI risk management toolkit, an AI assurance questionnaire, the public sector AI governance operating model and a service assessment questions navigator. Use them to evidence [GR-AI-03](#gr-ai-03), [GR-AI-04](#gr-ai-04) and [GR-AI-05](#gr-ai-05).

## GR-AI-06 Talk to the TDA about novel use {#gr-ai-06}

<span class="rfc rfc--must">Must</span> Novel uses of AI, and any use of generative AI in decision making, are reviewed by the [Technical Design Authority](../governance/tda.md).

## GR-AI-07 Suppliers use AI coding assistants openly and safely {#gr-ai-07}

<span class="rfc rfc--should">Should</span> Delivery partners who use AI coding assistants on Defra work agree which tools they use with Defra, use them only under terms that meet [GR-AI-02](#gr-ai-02), have a person review every change before it is merged, and say in pull requests or delivery reports where AI did significant work.

**Why:** AI coding assistants can speed up delivery, but they can also leak code, secrets or data to a third party, bring in code with unclear licences, and produce plausible but wrong code. Defra owns the code it pays for and must be able to trust it.

**How to meet it:**

- Agree the tools and their configuration with the Defra engagement lead at [mobilisation](../partners/mobilisation.md), and record them in the repository.
- Use only enterprise versions that do not keep or train on Defra code or prompts, and turn off public code suggestions where the tool allows it.
- Never put secrets, personal data or OFFICIAL-SENSITIVE information into prompts.
- Review AI-generated code with the same care as any other code ([GR-DEV-03](software-development.md#gr-dev-03)), including licences of any suggested code.

This guardrail is a **draft** proposal. Comment on it by [opening an issue](https://github.com/howellsr/architecture/issues).

## Agentic AI

AI agents do more than answer questions: they plan steps and take actions through tools, such as updating records, sending messages or calling APIs. That makes them useful, and it makes mistakes and attacks more costly. These draft guardrails come from the [guardrail backlog](../about/roadmap.md#guardrail-backlog) and apply on top of [GR-AI-02](#gr-ai-02) to [GR-AI-06](#gr-ai-06).

## GR-AI-08 Give agents the least privilege they need {#gr-ai-08}

<span class="rfc rfc--must">Must</span> AI agents act under their own identity, with access only to the tools, data and actions their task needs, and never with a person's full permissions.

**Why:** an agent can be tricked or can simply be wrong. Limiting what it can reach limits the damage ([GR-IAM-03](identity-and-access.md#gr-iam-03)).

**How to meet it:** list each agent's tools and permissions, grant them to a workload identity for the agent, and review them as you would a privileged user's.

## GR-AI-09 Get human approval for consequential actions {#gr-ai-09}

<span class="rfc rfc--must">Must</span> An agent does not take an action with legal, financial or significant effects on people, or one that cannot easily be undone, without approval from an accountable person.

**Why:** [GR-AI-03](#gr-ai-03) keeps a human accountable for decisions. Agents act faster than people can notice, so approval has to be designed in, not assumed.

**How to meet it:** classify the agent's actions in alpha. Enforce approval in the tool layer, not only in the prompt, and test that the agent cannot bypass it.

## GR-AI-10 Keep an audit trail of what agents do {#gr-ai-10}

<span class="rfc rfc--must">Must</span> Record what each agent was asked, what it read, which tools it called with what inputs, who approved what, and the outcome - and send security-relevant events to security monitoring.

**Why:** without a full record, nobody can explain, challenge or reverse what an agent did.

**How to meet it:** log at the tool layer with correlation ids ([GR-OPS-02](observability-and-operations.md#gr-ops-02)), and keep records for as long as the decisions they support.

## GR-AI-11 Defend agents against prompt injection {#gr-ai-11}

<span class="rfc rfc--must">Must</span> Treat everything an agent reads - documents, emails, web pages, tool results - as untrusted input that may try to change its instructions, and design controls that hold even if it does.

**Why:** prompt injection is the most common way to make an agent misuse its tools or leak data.

**How to meet it:** include injection through every input in your [threat model](../security/threat-modelling.md) ([GR-AI-05](#gr-ai-05)), separate untrusted content from instructions, restrict tools as in GR-AI-08 and require approval as in GR-AI-09.
