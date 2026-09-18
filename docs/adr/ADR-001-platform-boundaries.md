# ADR-001: Platform boundaries and application discovery

## Decision

Use a Python package under `src/core` for shared execution infrastructure and discover applications from `src/applications/*/manifest.yaml`. Application-specific behavior stays outside core.

## Rationale

This keeps application count from increasing core branching complexity and allows app3+ onboarding through artifacts rather than core edits. `pytest-bdd` provides the Cucumber-style feature and step model without introducing a second language runtime.

## Consequences

Applications must implement the contracts exposed by core. Dependency injection is explicit scenario composition because it makes mutable scenario state local and testable. External providers remain explicit integration points and require deployment configuration.
