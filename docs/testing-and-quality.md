# Testing and Quality

The project includes several practices intended to make the codebase easier to validate and maintain.

## Testing

Automated tests are executed with Pytest:

```bash
pytest
```

Use verbose mode when needed:

```bash
pytest -v
```

## Quality practices

- Typed request and response schemas with Pydantic.
- Layered backend organization for clarity and maintainability.
- JWT authentication for protected routes.
- Structured logging for debugging and operational visibility.
- Docker support for reproducible local setup.
- MkDocs documentation for onboarding and review.

## Git workflow

This repository uses a simple long-lived branch model:

- `main` — stable, release-ready branch.
- `develop` — integration branch for ongoing work.
- `gh-pages` — documentation deployment branch.

Short-lived branches are created from `develop`:

- `feature/<name>`
- `fix/<name>`
- `docs/<name>`

Normal work is merged into `develop` through Pull Requests. Release-ready changes are then promoted from `develop` to `main`.
