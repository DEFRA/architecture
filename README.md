# Defra architecture

Source for the Defra architecture site at [https://howellsr.github.io/architecture](https://howellsr.github.io/architecture/): guardrails, the business-to-technology capability handrail, governance, and enterprise data and security architecture, for Defra product and platform teams and delivery partners.

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

## Publishing

The site is published with GitHub Pages at <https://howellsr.github.io/architecture/>.

- Every push to `main` runs `.github/workflows/ci.yml`, which builds the site with `mkdocs build --strict` and then runs `mkdocs gh-deploy` to push the built site to the `gh-pages` branch.
- GitHub Pages serves the `gh-pages` branch. One-off setup (repository admin): **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `gh-pages` / `(root)` → Save**.
- To republish without a code change, run the **ci** workflow manually from the **Actions** tab (**Run workflow** on `main`).
- Pull requests run the build only; they never publish.

If the site moves to another organisation or custom domain, update `site_url`, `repo_url` and `repo_name` in `mkdocs.yml` and the links in this README.

## Contributing

Issues and pull requests are welcome from Defra staff and delivery partners. See the [contribution guide](https://howellsr.github.io/architecture/contribute/).

## Licence

THIS INFORMATION IS LICENSED UNDER THE CONDITIONS OF THE OPEN GOVERNMENT LICENCE found at:

<http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3>

The following attribution statement MUST be cited in your products and applications when using this information.

>Contains public sector information licensed under the Open Government license v3
