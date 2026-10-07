<!-- https://defra.github.io/architecture/deliver/roles/delivery-manager/ | maturity: prototype | site version 0.3.0 | generated from deliver/roles/delivery-manager.md -->

# Delivery manager

<p class="lead">The guardrails a delivery manager leads, what to show in each phase, the patterns that help and when to work with an architect.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



You keep the team delivering and the governance light. You make sure evidence is gathered as the team goes, not at the end, and that the service is ready to run in live.

You lead **10 guardrails**, often with other roles. Leading means making sure the team meets them and can show it, not doing all the work. See them all in the <a href="../../../guardrails/library/#role=delivery-manager">guardrail library, filtered to your role</a>.

## Your guardrails, phase by phase

### Discovery

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-TECH-06](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-06) Get spend approval early | Must | Architecture team consulted before any procurement under spend control starts |
| [GR-PROD-02](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-02) Name the product owner and service owner | Should | Named product owner and service owner, recorded in the service catalogue |
| [GR-OPEN-05](https://defra.github.io/architecture/guardrails/open-source/#gr-open-05) Blog and show the thing | Could | Blog posts, show and tells or contributions to this site |

More on the [discovery page](https://defra.github.io/architecture/deliver/discovery/).

### Alpha

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-OPEN-01](https://defra.github.io/architecture/guardrails/open-source/#gr-open-01) Code in the open | Must | Code public in a Defra GitHub organisation from the first commit, or a recorded reason for keeping a repository private |
| [GR-DEV-02](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-02) All code in Defra source control | Must | All code, including prototypes and infrastructure code written by suppliers, in a Defra-owned GitHub organisation from the first commit |
| [GR-AI-07](https://defra.github.io/architecture/guardrails/ai/#gr-ai-07) Suppliers use AI coding assistants openly and safely | Should | Supplier's agreed list of AI coding assistants and how each runs within Defra-approved terms, the review process for generated code, and disclosure in pull requests or delivery reports |
| [GR-TECH-03](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) Plan your exit before you enter | Should | Draft exit plan for each new product, platform or significant supplier |
| [GR-PROD-02](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-02) Name the product owner and service owner | Should | Named product owner and service owner, recorded in the service catalogue |
| [GR-OPEN-05](https://defra.github.io/architecture/guardrails/open-source/#gr-open-05) Blog and show the thing | Could | Blog posts, show and tells or contributions to this site |

More on the [alpha page](https://defra.github.io/architecture/deliver/alpha/).

### Beta

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-OPS-05](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05) Be ready for live before you go live | Must | Before public beta, the support model, on-call arrangements, runbooks, incident process and live owner agreed, and the service catalogue entry made |
| [GR-OPEN-01](https://defra.github.io/architecture/guardrails/open-source/#gr-open-01) Code in the open | Must | Repositories public, or the reasons for keeping them private reviewed |
| [GR-SEC-06](https://defra.github.io/architecture/guardrails/security/#gr-sec-06) Test before go-live and after major change | Must | IT health check before go-live, and a remediation tracker |
| [GR-DEV-02](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-02) All code in Defra source control | Must | All source, infrastructure and pipeline code in the Defra GitHub organisation, with nothing held only by a supplier |
| [GR-AI-07](https://defra.github.io/architecture/guardrails/ai/#gr-ai-07) Suppliers use AI coding assistants openly and safely | Should | Supplier's agreed list of AI coding assistants and how each runs within Defra-approved terms, the review process for generated code, and disclosure in pull requests or delivery reports |
| [GR-TECH-03](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) Plan your exit before you enter | Should | Exit plan agreed, with contracts giving Defra its data and the right to export it in open formats |
| [GR-PROD-02](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-02) Name the product owner and service owner | Should | Named product owner and service owner, recorded in the service catalogue |
| [GR-OPEN-05](https://defra.github.io/architecture/guardrails/open-source/#gr-open-05) Blog and show the thing | Could | Blog posts, show and tells or contributions to this site |

More on the [beta page](https://defra.github.io/architecture/deliver/beta/).

### Live

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-OPS-05](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05) Be ready for live before you go live | Must | Runbooks and support arrangements tested and kept current |
| [GR-OPEN-01](https://defra.github.io/architecture/guardrails/open-source/#gr-open-01) Code in the open | Must | Repositories still public, or private for a recorded reason |
| [GR-SEC-06](https://defra.github.io/architecture/guardrails/security/#gr-sec-06) Test before go-live and after major change | Must | IT health check after significant change, with remediation tracked |
| [GR-DEV-02](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-02) All code in Defra source control | Must | All changes made in the Defra GitHub organisation |
| [GR-AI-07](https://defra.github.io/architecture/guardrails/ai/#gr-ai-07) Suppliers use AI coding assistants openly and safely | Should | Supplier's agreed list of AI coding assistants and how each runs within Defra-approved terms, the review process for generated code, and disclosure in pull requests or delivery reports |
| [GR-TECH-03](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) Plan your exit before you enter | Should | Exit plan reviewed at contract renewal, with switching cost estimated |
| [GR-OPS-06](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-06) Learn from incidents | Should | Post-incident reviews and the actions taken |
| [GR-PROD-02](https://defra.github.io/architecture/guardrails/products-and-platforms/#gr-prod-02) Name the product owner and service owner | Should | Named product owner and service owner, recorded in the service catalogue |
| [GR-OPEN-05](https://defra.github.io/architecture/guardrails/open-source/#gr-open-05) Blog and show the thing | Could | Blog posts, show and tells or contributions to this site |

More on the [live page](https://defra.github.io/architecture/deliver/live/).

### Significant change

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-SEC-06](https://defra.github.io/architecture/guardrails/security/#gr-sec-06) Test before go-live and after major change | Must | IT health check scoped and booked for the change where it is significant |
| [GR-TECH-06](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-06) Get spend approval early | Must | Architecture team consulted before new procurement for the change |
| [GR-OPS-05](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05) Be ready for live before you go live | Must | Runbooks and support arrangements updated before the change goes live |
| [GR-TECH-03](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) Plan your exit before you enter | Should | Exit plan updated for any new product or supplier |

More on the [significant change page](https://defra.github.io/architecture/deliver/significant-change/).

### Retire a service

| Guardrail | Level | What to show |
| --- | --- | --- |
| [GR-OPEN-01](https://defra.github.io/architecture/guardrails/open-source/#gr-open-01) Code in the open | Must | Repositories archived, not deleted, so the code and decisions stay available |
| [GR-TECH-03](https://defra.github.io/architecture/guardrails/choosing-technology/#gr-tech-03) Plan your exit before you enter | Should | Exit plan carried out - data exported in open formats and contracts ended |

More on the [retire a service page](https://defra.github.io/architecture/deliver/retire/).

## Patterns that help

No patterns yet. See the [patterns](https://defra.github.io/architecture/patterns/) section.

## Working with architects

- Book architecture and security conversations into the plan for each phase - see [Deliver a service](https://defra.github.io/architecture/deliver/).
- Use the evidence checklist for your phase before each assessment.
- Agree the support model and runbooks before public beta ([GR-OPS-05](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-05)).
- Make sure suppliers know the guardrails from mobilisation - see [delivery partners](https://defra.github.io/architecture/about/delivery-partners/).



