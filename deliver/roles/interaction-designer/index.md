<!-- https://defra.github.io/architecture/deliver/roles/interaction-designer/ | maturity: prototype | site version 0.3.0 | generated from deliver/roles/interaction-designer.md -->

# Interaction designer

<p class="lead">The guardrails an interaction designer leads, what to show in each phase, the patterns that help and when to work with an architect.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



You design the screens and interactions. Accessibility, the GOV.UK Design System, offline working and what users see when something is slow or fails all depend on technical choices.

You lead **9 guardrails**, often with other roles. Leading means making sure the team meets them and can show it, not doing all the work. See them all in the <a href="../../../guardrails/library/#role=interaction-designer">guardrail library, filtered to your role</a>.

## Your guardrails, phase by phase

### Discovery

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-DATA-11](https://defra.github.io/architecture/guardrails/data/#gr-data-11) No real personal data in prototypes | Should | Any prototype uses made-up data |

More on the [discovery page](https://defra.github.io/architecture/deliver/discovery/).

### Alpha

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-FE-01](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-01) Meet WCAG 2.2 AA | Must | Prototypes built with accessible components, and a plan for an accessibility audit and assistive technology testing |
| [GR-FE-02](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-02) Use the GOV.UK Design System | Must | Prototypes built with the GOV.UK Design System, with departures recorded and researched |
| [GR-DATA-11](https://defra.github.io/architecture/guardrails/data/#gr-data-11) No real personal data in prototypes | Should | Prototypes and research materials use made-up data, including data a participant types in during a session |
| [GR-FIELD-02](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-02) Design field tools to work offline | Should | Field journeys tested with no connection, including sync after reconnecting and conflict handling |
| [GR-FE-03](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-03) Progressive enhancement | Should | Core journeys tested with JavaScript turned off |
| [GR-FE-07](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-07) Tell users what is happening when things fail or are slow | Should | Each dependency that can fail or be slow identified with the developers, and what users see in each case designed and tested in the prototype |
| [GR-SUS-04](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-04) Keep data and pages lean | Should | Data retention settings and page weight measurements |

More on the [alpha page](https://defra.github.io/architecture/deliver/alpha/).

### Beta

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-04](https://defra.github.io/architecture/guardrails/ai/#gr-ai-04) Be transparent | Must | Draft Algorithmic Transparency Recording Standard record, and the notice telling users about AI tested with them |
| [GR-FE-01](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-01) Meet WCAG 2.2 AA | Must | Accessibility audit and assistive technology testing completed, issues fixed, and an accessibility statement published |
| [GR-FE-02](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-02) Use the GOV.UK Design System | Must | The service uses GOV.UK Frontend, with design decisions recording any departures |
| [GR-DATA-11](https://defra.github.io/architecture/guardrails/data/#gr-data-11) No real personal data in prototypes | Should | Test and research environments use synthetic or anonymised data; any exception agreed through a DPIA |
| [GR-FIELD-02](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-02) Design field tools to work offline | Should | Field journeys tested with no connection, including sync after reconnecting and conflict handling |
| [GR-FE-03](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-03) Progressive enhancement | Should | Core journeys tested with JavaScript turned off |
| [GR-FE-07](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-07) Tell users what is happening when things fail or are slow | Should | The front end shows the designed content when a dependency fails or is slow, tested by switching dependencies off |
| [GR-OPS-04](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-04) Health checks and graceful degradation | Should | Health endpoints, timeout and retry settings, and a design for when dependencies fail |
| [GR-SUS-04](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-04) Keep data and pages lean | Should | Data retention settings and page weight measurements |

More on the [beta page](https://defra.github.io/architecture/deliver/beta/).

### Live

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-AI-04](https://defra.github.io/architecture/guardrails/ai/#gr-ai-04) Be transparent | Must | Link to the published Algorithmic Transparency Recording Standard record, kept current |
| [GR-FE-01](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-01) Meet WCAG 2.2 AA | Must | Accessibility statement kept current, and accessibility re-tested after significant change |
| [GR-FE-02](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-02) Use the GOV.UK Design System | Must | GOV.UK Frontend kept up to date |
| [GR-FIELD-02](https://defra.github.io/architecture/guardrails/field-working-and-devices/#gr-field-02) Design field tools to work offline | Should | Field journeys tested with no connection, including sync after reconnecting and conflict handling |
| [GR-FE-07](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-07) Tell users what is happening when things fail or are slow | Should | Failure and delay content kept accurate as dependencies and processing times change |
| [GR-OPS-04](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-04) Health checks and graceful degradation | Should | Health endpoints, timeout and retry settings, and a design for when dependencies fail |
| [GR-SUS-04](https://defra.github.io/architecture/guardrails/sustainability/#gr-sus-04) Keep data and pages lean | Should | Data retention settings and page weight measurements |

More on the [live page](https://defra.github.io/architecture/deliver/live/).

## Patterns that help

- [Asynchronous submission with an outbox](https://defra.github.io/architecture/patterns/async-submission/) - A user submits something that other systems must process, and you do not want those systems' availability to block the user.
- [Reading from an authoritative source](https://defra.github.io/architecture/patterns/authoritative-source/) - A service needs shared data - customers, organisations, holdings, locations or species - that another part of Defra owns.
- [File upload with malware scanning](https://defra.github.io/architecture/patterns/file-upload/) - Users upload documents or images, and the files must be scanned and stored safely before anyone opens them.

## Working with architects

- Prototype on the real platforms where a technical constraint changes the interaction, such as file upload or sign-in.
- Design what users see when a dependency fails, with the developers and an architect, before beta.



