# FastAPI SQLite CRUD Example

Simple REST API built with FastAPI, SQLAlchemy and SQLite, plus a tiny frontend served by FastAPI.

## Features

- GET `/items/`
- GET `/items/{id}`
- POST `/items/`
- PATCH `/items/{id}`
- DELETE `/items/{id}`

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

## Run with Docker

```bash
docker-compose up --build
```

Open:
- `http://127.0.0.1:8000/` — frontend
- `http://127.0.0.1:8000/docs` — Swagger UI
