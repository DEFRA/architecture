---
title: Defra architecture
template: home.html
hide:
  - navigation
  - toc
---

<h1 class="visually-hidden">Defra architecture</h1>

<section class="da-section" aria-labelledby="start" markdown>
<p class="da-kicker da-kicker--dark">Start here</p>
<h2 id="start" class="da-h2">What do you need to do?</h2>
<p class="da-intro">Pick the job in front of you. Each route takes you to the smallest useful set of guidance.</p>

<div class="da-routes" markdown>

<div class="da-route da-route--green" markdown>

<span class="da-route__tag">Decide</span>

### [Check a design decision](governance/decision-check.md){ .da-route__link }

Seven questions tell you whether your team can decide, needs advice, or should go to a design authority.

<span class="da-route__cta" aria-hidden="true">Start the check</span>

</div>

<div class="da-route da-route--blue" markdown>

<span class="da-route__tag">Build</span>

### [Find the guardrails](guardrails/library.md){ .da-route__link }

Search every Must, Should and Could by keyword, area or id, with the reason behind each one.

<span class="da-route__cta" aria-hidden="true">Open the library</span>

</div>

<div class="da-route da-route--amber" markdown>

<span class="da-route__tag">Reuse</span>

### [Find what already exists](handrail/technology-capabilities.md){ .da-route__link }

Identity, payments, hosting, geospatial and more. Check the strategic option before you buy or build.

<span class="da-route__cta" aria-hidden="true">Browse capabilities</span>

</div>

<div class="da-route da-route--lime" markdown>

<span class="da-route__tag">Engage</span>

### [Get architecture support](governance/index.md){ .da-route__link }

How the TGB, the TDA and solution design authorities work, what to bring and how quickly you get an answer.

<span class="da-route__cta" aria-hidden="true">See governance</span>

</div>

</div>
</section>

<section class="da-band" aria-labelledby="flow" markdown>
<div class="da-band__copy" markdown>
<p class="da-kicker">Light-touch governance</p>
<h2 id="flow" class="da-h2">Most decisions belong to the team.</h2>
<p>The closer a design stays to the guardrails and reuses what Defra already has, the lighter its governance. Boards look only at what is new, cross-cutting or outside the guardrails.</p>
[Check a decision](governance/decision-check.md){ .md-button .da-button-lime } [How triage works](governance/triage.md){ .md-button .da-button-ghost }
</div>
<ol class="da-flow">
<li><span>01</span><strong>Map</strong>Find the business capability your service supports</li>
<li><span>02</span><strong>Reuse</strong>Use the strategic technology options first</li>
<li><span>03</span><strong>Check</strong>Test the design against the guardrails</li>
<li><span>04</span><strong>Decide</strong>Your team, your SDA or the TDA, by risk</li>
<li><span>05</span><strong>Record</strong>Write an ADR in the open so others can reuse it</li>
</ol>
</section>

<section class="da-section" aria-labelledby="what" markdown>
<p class="da-kicker da-kicker--dark">The handrail</p>
<h2 id="what" class="da-h2">What Defra does</h2>
<p class="da-intro">Every service should trace back to one of these business capabilities. Select one to see the technology that enables it and what you can reuse.</p>

<!-- capabilities:business-map -->

</section>

<section class="da-section" aria-labelledby="areas" markdown>
<p class="da-kicker da-kicker--dark">Explore the architecture</p>
<h2 id="areas" class="da-h2">Connect business, data, applications and technology</h2>

<div class="da-areas" markdown>

<div class="da-area" markdown>
<span class="da-area__tag">Business</span>

- [Business capabilities](handrail/business-capabilities.md)
- [Capability mapping](handrail/capability-mapping.md)
- [Reference architectures](handrail/reference-architectures/index.md)

</div>

<div class="da-area" markdown>
<span class="da-area__tag">Data</span>

- [Defra on a page](data/defra-on-a-page.md)
- [Data standards](data/data-standards.md)
- [Data guardrails](guardrails/data.md)

</div>

<div class="da-area" markdown>
<span class="da-area__tag">Applications</span>

- [APIs and integration](guardrails/apis-and-integration.md)
- [Software development](guardrails/software-development.md)
- [Coding standards](https://defra.github.io/software-development-standards/){ .da-ext }

</div>

<div class="da-area" markdown>
<span class="da-area__tag">Technology</span>

- [Technology capabilities](handrail/technology-capabilities.md)
- [Hosting and platforms](guardrails/hosting-and-platforms.md)
- [Choosing technology](guardrails/choosing-technology.md)

</div>

<div class="da-area" markdown>
<span class="da-area__tag">Security</span>

- [Secure by Design](security/secure-by-design.md)
- [Threat modelling](security/threat-modelling.md)
- [Managing exceptions](security/managing-exceptions.md)

</div>

</div>
</section>

<section class="da-section da-split" aria-labelledby="elsewhere" markdown>
<div markdown>
<p class="da-kicker da-kicker--dark">Detailed guidance</p>
<h2 id="elsewhere" class="da-h2">Where the detail lives</h2>
<p class="da-intro">This site sets direction and boundaries. For hands-on practice, go to the source.</p>

<ul class="da-links">
<li><a href="https://defra.github.io/software-development-standards/"><strong>Defra software development standards</strong><span>Languages, coding, testing, source control and release practice</span></a></li>
<li><a href="https://digital.defra.gov.uk/service-manual"><strong>Defra Digital Service Manual</strong><span>How Defra designs, builds and assesses services</span></a></li>
<li><a href="https://www.gov.uk/service-manual/service-standard"><strong>Service Standard</strong><span>The 14 points every government service meets</span></a></li>
<li><a href="https://www.gov.uk/guidance/the-technology-code-of-practice"><strong>Technology Code of Practice</strong><span>How government designs, builds and buys technology</span></a></li>
<li><a href="https://www.security.gov.uk/policy-and-guidance/secure-by-design/"><strong>Secure by Design</strong><span>Government's approach to security in delivery</span></a></li>
</ul>
</div>
<div class="da-panel" markdown>
<p class="da-kicker da-kicker--dark">Working with us</p>
<h3>Delivery partners welcome</h3>
<p>Everything here is public, so you know what good looks like before you bid or start. Partners follow the same guardrails as Defra teams and can contribute to them.</p>
[What to expect from us, and what we expect from you](about/delivery-partners.md)
<h3>Help improve this site</h3>
<p>Spotted a gap or something wrong? <a href="https://github.com/howellsr/architecture/issues">Open an issue</a> or use the edit button on any page.</p>
[What's new](about/changelog.md)
</div>
</section>
