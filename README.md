# Enterprise Playwright Python Platform

A production-oriented, application-extensible UI/API automation platform using Python, Playwright, pytest-bdd, and dependency injection by explicit composition.

## Architecture

`pytest` is the execution boundary. Configuration is loaded and validated before a scenario gets a browser context. Application manifests are discovered from `src/applications/*/manifest.yaml`; core code never imports an application module. Thin BDD step definitions call business services, business services coordinate page interfaces, and page objects contain only UI interactions.

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) and [docs/adr/ADR-001-platform-boundaries.md](docs/adr/ADR-001-platform-boundaries.md).

## Setup

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
playwright install --with-deps chromium
```

Copy `.env.example` to `.env` and provide environment-specific URLs or credentials through environment variables. Secrets are never read from committed YAML.

## Commands

```powershell
pytest                         # default suite
pytest -m smoke                # smoke suite
pytest tests/unit tests/architecture
python -m compileall -q src tests
ruff check .
pytest --alluredir=reports/allure
allure generate reports/allure -o reports/allure-html --clean
pip-audit
bandit -r src
```

The browser scenarios are opt-in through `RUN_BROWSER_TESTS=true`; framework tests do not require network access.

## Adding an application

Add only an application directory with a manifest, pages, business services, features, steps, and test data. Set `APP=app3`; no `src/core` edit is required. Application names are validated against discovered manifests.

## Runtime overrides

Workflow inputs or environment variables override `config/framework.yaml`:
`APP`, `ENVIRONMENT`, `BROWSER`, `SUITE`, `WORKERS`, and `RETRY_COUNT`.

## Readiness

The framework core, application discovery, configuration, browser smoke tests, and offline tests are validated. It is **not yet production ready** until dependency audit remediation, CI execution with repository secrets, target-environment authentication, and operational email/history/plugin integrations are completed. See [docs/PRODUCTION_READINESS.md](docs/PRODUCTION_READINESS.md).
