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
