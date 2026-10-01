# Contributing

Thank you for helping improve the Defra architecture site. Defra staff and delivery partners are equally welcome.

The full guide - repository layout, how to add a guardrail, NFR or capability, writing style and the checks that run - is on the site: **<https://howellsr.github.io/architecture/contribute/>** (source: [`docs/contribute/index.md`](docs/contribute/index.md)).

Quick start:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
pytest                 # content checks
mkdocs serve           # preview at http://127.0.0.1:8000
mkdocs build --strict  # the same build CI runs
```

This is a public repository. Never commit secrets, internal hostnames, personal data or detailed security weaknesses.
