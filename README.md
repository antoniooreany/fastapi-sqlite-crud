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
├── app/
├── static/
├── requirements.txt
└── README.md
```

## Run

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:
- `http://127.0.0.1:8000/` — frontend
- `http://127.0.0.1:8000/docs` — Swagger UI
