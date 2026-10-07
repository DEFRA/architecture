<!-- https://defra.github.io/architecture/deliver/roles/content-designer/ | maturity: prototype | site version 0.3.0 | generated from deliver/roles/content-designer.md -->

# Content designer

<p class="lead">The guardrails a content designer leads, what to show in each phase, the patterns that help and when to work with an architect.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



You write what users read. Confirmation pages, status messages, error messages, Welsh content and telling users about AI depend on how the service works underneath.

You lead **3 guardrails**, often with other roles. Leading means making sure the team meets them and can show it, not doing all the work. See them all in the <a href="../../../guardrails/library/#role=content-designer">guardrail library, filtered to your role</a>.

## Your guardrails, phase by phase

### Alpha

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-FE-06](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-06) Support Welsh where required | Must | Whether the Welsh Language Standards apply decided, and the service designed for translation |
| [GR-FE-07](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-07) Tell users what is happening when things fail or are slow | Should | Each dependency that can fail or be slow identified with the developers, and what users see in each case designed and tested in the prototype |

More on the [alpha page](https://defra.github.io/architecture/deliver/alpha/).

### Beta

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-04](https://defra.github.io/architecture/guardrails/ai/#gr-ai-04) Be transparent | Must | Draft Algorithmic Transparency Recording Standard record, and the notice telling users about AI tested with them |
| [GR-FE-06](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-06) Support Welsh where required | Must | Welsh content and journeys built and tested where the standards apply |
| [GR-FE-07](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-07) Tell users what is happening when things fail or are slow | Should | The front end shows the designed content when a dependency fails or is slow, tested by switching dependencies off |

More on the [beta page](https://defra.github.io/architecture/deliver/beta/).

### Live

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-04](https://defra.github.io/architecture/guardrails/ai/#gr-ai-04) Be transparent | Must | Link to the published Algorithmic Transparency Recording Standard record, kept current |
| [GR-FE-06](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-06) Support Welsh where required | Must | Welsh content kept in step with English content |
| [GR-FE-07](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-07) Tell users what is happening when things fail or are slow | Should | Failure and delay content kept accurate as dependencies and processing times change |

More on the [live page](https://defra.github.io/architecture/deliver/live/).

## Patterns that help

No patterns yet. See the [patterns](https://defra.github.io/architecture/patterns/) section.

## Working with architects

- Ask how long processing really takes, and what can fail, before you write confirmation and status content.
- Plan Welsh content early if the Welsh Language Standards apply ([GR-FE-06](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-06)).



