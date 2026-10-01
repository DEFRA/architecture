---
title: Check a decision
hide:
  - toc
---

# Check a decision

<p class="lead">Seven questions to find out whether your team can make a decision itself, needs targeted advice, or should take it to a design authority. It takes about two minutes and gives you a draft decision record to keep.</p>

<div class="dc" data-decision-check markdown>

<div class="dc-links" hidden markdown>
[TGB](tgb.md){ data-route="tgb" }
[TDA](tda.md){ data-route="tda" }
[SDA](solution-design-authorities.md){ data-route="sda" }
[Triage](triage.md){ data-route="advice" }
[ADRs](architecture-decision-records.md){ data-route="team" }
[Library](../guardrails/library.md){ data-route="library" }
</div>

<section class="dc-step" aria-labelledby="dc-step-1">
<p class="dc-step__label">Step 1 of 3</p>
<h2 id="dc-step-1">Describe the decision</h2>
<div class="dc-fields">
<label class="dc-field dc-field--wide" for="dc-title"><span>Decision</span><input id="dc-title" type="text" placeholder="e.g. Use a managed event streaming service for permit notifications"></label>
<label class="dc-field" for="dc-team"><span>Team or service</span><input id="dc-team" type="text" placeholder="e.g. Waste permits"></label>
<label class="dc-field dc-field--wide" for="dc-context"><span>Context <small>(optional)</small></span><textarea id="dc-context" rows="3" placeholder="What problem are you solving, and what constraints apply?"></textarea></label>
</div>
</section>

<section class="dc-step" aria-labelledby="dc-step-2">
<p class="dc-step__label">Step 2 of 3</p>
<h2 id="dc-step-2">Test it against the guardrails</h2>
<p>Answer every question. <strong>Yes</strong> means a boundary is crossed. <strong>Unsure</strong> means you should ask an architect about that point.</p>
<div class="dc-progress" aria-hidden="true"><span></span></div>
<p class="dc-counter" aria-live="polite">0 of 7 answered</p>
<div class="dc-questions"></div>
</section>

<section class="dc-step" aria-labelledby="dc-step-3">
<p class="dc-step__label">Step 3 of 3</p>
<h2 id="dc-step-3">See your route and keep a record</h2>
<p class="dc-waiting">Your route appears here once every question has an answer.</p>
<div class="dc-result" hidden aria-live="polite"></div>
<div class="dc-record" hidden>
<label for="dc-record-text"><strong>Draft decision record</strong> - paste this into <code>docs/adr/</code> in your repository and finish it.</label>
<textarea id="dc-record-text" rows="16" spellcheck="false"></textarea>
<p class="dc-actions"><button type="button" class="md-button md-button--primary dc-copy">Copy record</button> <button type="button" class="md-button dc-reset">Start again</button> <span class="dc-copy-status" aria-live="polite"></span></p>
</div>
</section>

</div>

!!! note "A guide, not an approval"
    The check suggests a route from your answers. It does not approve anything, and nothing you type leaves your browser. If the result surprises you, [read how triage works](triage.md) or ask an architect.
