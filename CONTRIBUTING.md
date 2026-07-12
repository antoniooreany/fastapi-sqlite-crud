# Contributing

Thank you for contributing to this project.

This guide describes the repository workflow, local setup, testing expectations, and branch conventions used for ongoing development.

## Branching model

This project uses a lightweight Git Flow-style approach:

- `main` contains stable, release-ready code.
- `develop` is the integration branch for upcoming work.
- `gh-pages` is reserved for the published documentation site.

All day-to-day work should be done in short-lived branches created from `develop`.

Supported naming patterns:

- `feature/<name>` — new features and enhancements
- `fix/<name>` — bug fixes and small corrections
- `docs/<name>` — documentation-only updates

Examples:

- `feature/jwt-auth`
- `fix/ci-pip-audit`
- `docs/changelog-and-meta`

## Development flow

### 1. Sync `develop`

Before starting work, update your local integration branch:

```bash
git checkout develop
git pull origin develop
```

### 2. Create a topic branch

Create a focused working branch from `develop`:

```bash
git checkout -b feature/your-change
```

Use a branch name that clearly describes the task.

## Making changes

Keep changes scoped to a single purpose when possible. Avoid mixing unrelated refactoring, documentation updates, and functional work in the same branch unless they belong to the same change set.

### Commit style

Use short, clear commit messages. Conventional-style prefixes are preferred:

- `feat:`
- `fix:`
- `docs:`
- `test:`
- `refactor:`
- `chore:`
- `ci:`

Examples:

```text
feat: add JWT auth helpers
fix: correct CI pip-audit behavior
docs: expand README and changelog
test: improve item endpoint coverage
```

### Push your branch

```bash
git push origin feature/your-change
```

## Pull requests

Open Pull Requests against `develop` for normal project work.

A good Pull Request should include:

- a clear summary of the change;
- the reason for the change;
- testing notes;
- any documentation updates if behavior changed.

Small follow-up commits during review are fine. Push additional commits to the same branch and the Pull Request will update automatically, which matches the standard GitHub contribution workflow. [web:1251]

## Merge and cleanup

When CI passes and the Pull Request is approved or accepted, merge the branch into `develop`.

After merge, delete the topic branch locally and on GitHub to keep the repository tidy:

```bash
git branch -d feature/your-change
git push origin --delete feature/your-change
```

## Release flow

Releases are promoted from `develop` into `main`.

Typical release steps:

1. Ensure `develop` is stable and up to date.
2. Open a release Pull Request from `develop` to `main`.
3. Merge the release Pull Request after checks pass.
4. Pull the updated `main`.
5. Create and push a version tag.
6. Publish a GitHub Release from that tag.

Example:

```bash
git checkout main
git pull origin main
git tag -a v0.1.0 -m "FastAPI SQLite CRUD v0.1.0"
git push origin v0.1.0
```

## Local setup

### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Tests

Run the full test suite before opening a Pull Request:

```bash
pytest
```

Verbose mode:

```bash
pytest -v
```

If behavior changes, update or add tests as part of the same branch.

## Documentation

If a change affects setup, behavior, project structure, or release flow, update the relevant documentation:

- `README.md`
- `docs/`
- `CHANGELOG.md`
- `SECURITY.md` if security behavior or reporting expectations change

Documentation-only work may use `docs/<name>` branches.

## Repository conventions

A few repository-specific conventions apply:

- `logs/` contains runtime logs and should remain untracked.
- `output/` contains generated artifacts such as project snapshots and should usually remain untracked.
- `scripts/` contains local developer utilities and helper tooling.
- `gh-pages` is for published documentation output, not normal application development.

## Security reporting

If you discover a security issue, avoid publishing full exploit details in a public issue before the problem is reviewed.

See `SECURITY.md` for the project security policy and reporting guidance.