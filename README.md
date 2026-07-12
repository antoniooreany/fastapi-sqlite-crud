# FastAPI SQLite CRUD Example

A small but production-minded FastAPI project that demonstrates CRUD operations, JWT-based authentication, SQLite persistence, structured logging, automated tests, Docker support, and project documentation.

It combines a simple REST API with a lightweight frontend served by FastAPI and is organized to show clean backend structure, developer tooling, and reproducible local setup.

## Documentation

Detailed API documentation and architectural notes are available on the project documentation site:

- [Project documentation](https://antoniooreany.github.io/fastapi-sqlite-crud/)

## Features

- FastAPI-based REST API.
- SQLite database with SQLAlchemy ORM.
- JWT authentication for protected routes.
- Pydantic-based request and response schemas.
- Layered project structure with routers, services, CRUD helpers, and config.
- Structured logging and security-oriented audit logging.
- Pytest test suite.
- Docker and Docker Compose support.
- MkDocs-based project documentation.
- PowerShell helper script for generating a repository snapshot.

## Project structure

```text
fastapi-sqlite-crud/
├── .github/              # CI/CD workflows
├── alembic/              # Database migrations
├── app/                  # Backend source code
│   ├── routers/          # API route modules
│   ├── auth.py           # Authentication helpers
│   ├── config.py         # App configuration
│   ├── crud.py           # Data access helpers
│   ├── database.py       # DB engine and session setup
│   ├── logging_utils.py  # Logging configuration
│   ├── main.py           # FastAPI application entry point
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   └── services.py       # Service-layer logic
├── docs/                 # Documentation files
├── logs/                 # Runtime log output (ignored)
├── output/               # Generated snapshot/report output (ignored)
├── scripts/              # Helper scripts
├── static/               # Frontend files
├── tests/                # Test suite
├── .gitignore            # Git ignored files
├── Dockerfile            # Docker build instructions
├── docker-compose.yml    # Docker orchestration
├── mkdocs.yml            # MkDocs configuration
├── README.md             # Project documentation
└── requirements.txt      # Project dependencies
```

## Tech stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest
- Docker
- MkDocs
- PowerShell

## Local setup

### 1. Create a virtual environment

#### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
uvicorn app.main:app --reload
```

By default, open:

- `http://127.0.0.1:8000/` — frontend
- `http://127.0.0.1:8000/docs` — Swagger UI
- `http://127.0.0.1:8000/redoc` — ReDoc

## Running tests

The project includes automated tests for API behavior and application logic.

Run the test suite from the project root:

```bash
pytest
```

For more detailed output:

```bash
pytest -v
```

## Security features

This project includes several security-focused practices appropriate for a backend portfolio project:

- **Authentication:** OAuth2-style login flow with JWT access tokens.
- **Password protection:** Passwords are stored as hashes, not plain text.
- **Access control:** Protected routes require authenticated users.
- **Request traceability:** Each request can be associated with request-level identifiers for easier debugging and log correlation.
- **Audit logging:** Authentication attempts and sensitive actions can be captured in logs for review.
- **Structured logging:** JSON-style or structured application logs improve observability and troubleshooting.

## Logging and observability

The application is designed with operational visibility in mind:

- structured log records;
- request-aware logging patterns;
- security-relevant event logging;
- support for runtime log files in a dedicated `logs/` directory.

Generated runtime logs should not be committed to Git and are intended for local development or deployment diagnostics.

## Project snapshot script

The repository includes a PowerShell helper script:

```powershell
.\scripts\project_snapshot.ps1
```

This script generates a Markdown snapshot of the current repository state at:

```text
output/project_snapshot.md
```

The snapshot is intended to help with code review, onboarding, project inspection, and portfolio presentation. It gives a fast technical overview of the working tree without manually opening multiple files.

The generated snapshot currently includes:

- the current Git branch;
- `git status` output;
- recent local commits;
- discovered files inside `app/`;
- discovered files inside `tests/`;
- local Python version;
- local pytest version.

### Example usage

```powershell
.\scripts\project_snapshot.ps1
notepad .\output\project_snapshot.md
```

### Why it exists

This script is useful when:

- preparing a concise repository overview for review;
- documenting the current local state before making larger changes;
- quickly sharing project structure and environment details;
- creating lightweight development snapshots without adding heavy tooling.

The `output/` directory is intended for generated artifacts and should remain untracked unless there is a specific reason to commit generated output.

## Database and migrations

The project uses SQLite for local persistence and includes Alembic for schema migrations.

If migrations are configured and needed, typical commands are:

```bash
alembic upgrade head
```

To create a new migration revision:

```bash
alembic revision --autogenerate -m "describe change"
```

## Run with Docker

To build and start the project with Docker Compose:

```bash
docker-compose up --build
```

Then open:

- `http://127.0.0.1:8000/` — frontend
- `http://127.0.0.1:8000/docs` — Swagger UI

## Development notes

A few practical repository conventions are worth keeping in mind:

- `logs/` contains runtime log files and should stay out of version control.
- `output/` contains generated snapshot or report artifacts and is typically ignored.
- `scripts/` contains helper utilities for local development and inspection.
- `tests/` should continue to grow alongside new features and fixes.

## Why this project is useful

This repository is small enough to understand quickly, but structured enough to demonstrate backend engineering habits that go beyond a minimal CRUD demo:

- separation of concerns;
- authentication and protected endpoints;
- typing and validation;
- logging and observability;
- testing and reproducibility;
- documentation and developer tooling.

That makes it a stronger portfolio project than a single-file API example.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.