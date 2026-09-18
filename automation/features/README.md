# Feature suites

Each application owns the same suite taxonomy:

- `smoke/`: fast critical checks
- `sanity/`: focused release confidence checks
- `regression/`: broad application regression checks
- `e2e/`: end-to-end business journeys

Run a suite with pytest markers, for example `pytest tests/e2e -m "app1 and sanity"`. External browser execution requires `RUN_BROWSER_TESTS=true`.
