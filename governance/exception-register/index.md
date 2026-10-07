<!-- https://defra.github.io/architecture/governance/exception-register/ | maturity: published | site version 0.3.0 | generated from governance/exception-register.md -->

# Exception register

<p class="lead">Approved exceptions to guardrails: which guardrail, for which service, who owns it and when it ends. Publishing them shows where guardrails do not fit, and keeps exceptions time-limited.</p>

Exceptions are approved through the [exception process](https://defra.github.io/architecture/governance/exceptions/). Every exception has an owner and an expiry date. The [guardrails health](https://defra.github.io/architecture/governance/guardrails-health/) page shows trends, such as guardrails that keep needing exceptions.

<div id="tbc-1"></div>

!!! warning "To be confirmed"
    **TODO:** whether Defra will publish its exception register in the open, which exceptions are recorded here (for example Must guardrails only), and how security exceptions are kept out of the public register.

The register never includes security vulnerabilities or anything else that would help an attacker - only the guardrail, the service, the owner and the dates. Security risk acceptances follow the [security exception process](https://defra.github.io/architecture/security/managing-exceptions/) and are not published.

No exceptions have been recorded in the published register yet.


The register is maintained in [`registers/exceptions.yaml`](https://github.com/DEFRA/architecture/blob/main/registers/exceptions.yaml). Add an approved exception there by pull request.

