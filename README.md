# FastAPI SQLite CRUD Example

Simple REST API built with FastAPI, SQLAlchemy and SQLite, plus a tiny frontend served by FastAPI.

## Documentation

Detailed API documentation and architectural information are available on our [project documentation site](https://antoniooreany.github.io/fastapi-sqlite-crud/).

## Project structure

```text
fastapi-sqlite-crud/
├── .github/      # CI/CD workflows
├── alembic/      # Database migrations
├── app/          # Backend source code
├── docs/         # Documentation files
├── static/       # Frontend files
├── tests/        # Test suite
├── .env          # Environment variables
├── .gitignore    # Git ignored files
├── Dockerfile    # Docker build instructions
├── docker-compose.yml # Docker orchestration
├── mkdocs.yml    # MkDocs configuration
├── README.md     # Project documentation
└── requirements.txt # Project dependencies
```

## Run

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## How to run tests

To ensure system reliability, we maintain a comprehensive test suite. To run the tests:

```bash
# Ensure you are in the project root and venv is activated
pytest
```

## Security features

This project adheres to high-security standards appropriate for mission-critical systems:

- **Authentication:** OAuth2 with JWT for secure user sessions.
- **Data Protection:** Passwords are hashed using robust cryptographic algorithms.
- **Traceability:**
  - **Request ID:** Every request is assigned a unique UUID for end-to-end tracing across all logs.
  - **Audit Logging:** Detailed security audit logs for authentication attempts (success/failure) and resource access (CRUD actions by specific users).
- **Hardened Logging:** Structured JSON logging with size-based rotation, capturing critical metadata (app version, environment, process ID, thread, line number).

## Run with Docker

```bash
docker-compose up --build
```

Open:
- `http://127.0.0.1:8000/` — frontend
- `http://127.0.0.1:8000/docs` — Swagger UI
