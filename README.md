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
pytest tests/e2e -m "app1 and sanity"       # application sanity suite
pytest tests/e2e -m "app2 and regression"   # application regression suite
pytest tests/e2e -m "app1 and e2e"           # end-to-end suite
pytest tests/unit tests/architecture
python -m compileall -q src tests
ruff check .
pytest --alluredir=reports/allure
allure generate reports/allure -o reports/allure-html --clean
pip-audit
bandit -r src
```

The browser scenarios are opt-in through `RUN_BROWSER_TESTS=true`; framework tests do not require network access.

Features are organized per application under `features/<application>/smoke`,
`sanity`, `regression`, and `e2e`.

Locators are page-specific under `locators/<application>/<PageName>Locators.py`.
Each application also has one shared file: `App1CommonLocators.py` or
`App2CommonLocators.py` for selectors reused across that application's pages.
Legacy application locator modules re-export these classes for compatibility.
Test data is organized under `testData/`; see [testData/README.md](testData/README.md)
for the merge order and suite layout.

## Adding an application

Add only an application directory with a manifest, pages, business services, features, steps, and test data. Set `APP=app3`; no `src/core` edit is required. Application names are validated against discovered manifests.

## Runtime overrides

Workflow inputs or environment variables override `config/framework.yaml`:
`APP`, `ENVIRONMENT`, `BROWSER`, `SUITE`, `WORKERS`, and `RETRY_COUNT`.

## Readiness

The framework is **95% ready with Docker excluded**. Core code, application discovery, configuration, browser smoke tests, offline tests, security audit, reporting adapters, and CI/CD configuration are validated. Deployment still requires real secrets/targets, production SMTP, the first hosted CI run, and target-infrastructure scale benchmarks. See [docs/PRODUCTION_READINESS.md](docs/PRODUCTION_READINESS.md).
