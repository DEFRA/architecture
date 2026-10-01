# Defra architecture

Source for the Defra architecture site at [https://defra.github.io/architecture](https://defra.github.io/architecture/): guardrails, the business-to-technology capability handrail, governance, and enterprise data and security architecture, for Defra product and platform teams and delivery partners.

## What is here

| Path | Contents |
| --- | --- |
| `docs/` | Site content in Markdown |
| `capabilities/` | Business and technology capability models (YAML) - the single source for the handrail |
| `hooks/capabilities.py` | MkDocs hook that validates the capability models, renders the capability map, catalogue and matrix, and publishes `capabilities.json` |
| `includes/` | Shared snippets such as abbreviations |
| `.github/workflows/ci.yml` | Strict build on every pull request; publish to GitHub Pages on merge to `main` |

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open http://127.0.0.1:8000. Run `mkdocs build --strict` before raising a pull request - broken links, missing anchors and an invalid capability model all fail the build.

## Contributing

Issues and pull requests are welcome from Defra staff and delivery partners. See the [contribution guide](https://defra.github.io/architecture/contribute/).

## Licence

THIS INFORMATION IS LICENSED UNDER THE CONDITIONS OF THE OPEN GOVERNMENT LICENCE found at:

<http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3>

The following attribution statement MUST be cited in your products and applications when using this information.

>Contains public sector information licensed under the Open Government license v3
