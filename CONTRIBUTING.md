# Contributing

Thank you for helping improve the Defra architecture site. Defra staff and delivery partners are equally welcome.

The full guide - repository layout, how to add a guardrail, NFR or capability, writing style and the checks that run - is on the site: **<https://defra.github.io/architecture/contribute/>** (source: [`docs/contribute/index.md`](docs/contribute/index.md)).

Quick start:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
pytest                 # content checks
mkdocs serve           # preview at http://127.0.0.1:8000
mkdocs build --strict  # the same build CI runs
```

## Where things live

- **Guidance** lives in this repository, under `docs/`, and is published to the site. It never goes in the GitHub wiki.
- **Changes** are made through pull requests.
- **Mistakes, suggestions and backlog items** are tracked as issues; the roadmap's GitHub Project shows what is planned and in progress.
- **Questions and early ideas** go in Discussions.
- **How to do the job and who to contact** belong in the [Defra Digital Service Manual](https://digital.defra.gov.uk/), not here.

See [where things live](https://defra.github.io/architecture/contribute/where-things-live/) for the full picture.

This is a public repository. Never commit secrets, internal hostnames, personal data or detailed security weaknesses.
