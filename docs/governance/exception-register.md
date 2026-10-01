# Exception register

<p class="lead">Approved exceptions to guardrails: which guardrail, for which service, who owns it and when it ends. Publishing them shows where guardrails do not fit, and keeps exceptions time-limited.</p>

Exceptions are approved through the [exception process](exceptions.md). Every exception has an owner and an expiry date. The [guardrails health](guardrails-health.md) page shows trends, such as guardrails that keep needing exceptions.

!!! warning "To be confirmed"
    **TODO:** whether Defra will publish its exception register in the open, which exceptions are recorded here (for example Must guardrails only), and how security exceptions are kept out of the public register.

The register never includes security vulnerabilities or anything else that would help an attacker - only the guardrail, the service, the owner and the dates. Security risk acceptances follow the [security exception process](../security/managing-exceptions.md) and are not published.

<!-- registers:exceptions -->

The register is maintained in [`registers/exceptions.yaml`](https://github.com/howellsr/architecture/blob/main/registers/exceptions.yaml). Add an approved exception there by pull request.
