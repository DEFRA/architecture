# Contribute

<p class="lead">This site is built in the open and improves when the people who use it change it. Defra staff and delivery partners are equally welcome to contribute.</p>

## Ways to contribute

- **Spotted a mistake or something unclear?** Select **Edit this page** (the pencil icon at the top of each page) to propose a change on GitHub.
- **Have a question or an idea?** [Open an issue](https://github.com/DEFRA/architecture/issues).
- **Want to change a guardrail?** Open a pull request explaining what and why. See [how guardrails change](../guardrails/index.md#how-guardrails-change).
- **Improving the capability model?** Edit the YAML in [`capabilities/`](https://github.com/DEFRA/architecture/tree/main/capabilities). The site build checks your change.

## Writing style

We follow the [GOV.UK style guide](https://www.gov.uk/guidance/style-guide). In short:

- plain English, short sentences, active voice
- write for a busy delivery team: lead with what they need to do
- explain *why*, not just *what*
- name capabilities and products consistently with the [handrail](../handrail/index.md)
- avoid acronyms, or explain them the first time

## Guardrail format

Each guardrail has:

- a stable id - `GR-<AREA>-<NN>` - which is never reused
- a heading anchor matching the id, for example `{#gr-host-01}`
- a level: <span class="rfc rfc--must">Must</span>, <span class="rfc rfc--should">Should</span> or <span class="rfc rfc--could">Could</span>
- **Why** - the rationale
- **How to meet it** - practical, ideally self-service, steps

## Running the site locally

You need Python 3.10 or later.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Then open <http://127.0.0.1:8000>. Pages reload as you edit.

Before opening a pull request, check the site builds cleanly:

```bash
mkdocs build --strict
```

The same check runs automatically on every pull request. Merges to `main` are published to [defra.github.io/architecture](https://defra.github.io/architecture/).

## What not to publish

This is a public repository. Do not include:

- secrets, credentials, internal hostnames or IP addresses
- detailed security vulnerabilities or threat model detail for live services
- personal information, other than names of people who have agreed to be named
- commercially sensitive information
