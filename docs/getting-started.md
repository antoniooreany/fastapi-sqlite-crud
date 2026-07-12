# Getting Started

This guide shows how to run the project locally for development and testing.

## Prerequisites

Make sure you have the following installed:

- Python 3.10+
- Git
- Optional: Docker and Docker Compose

## Clone the repository

```bash
git clone https://github.com/antoniooreany/fastapi-sqlite-crud.git
cd fastapi-sqlite-crud
```

## Create a virtual environment

### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the application

```bash
uvicorn app.main:app --reload
```

When the server starts, open:

- `http://127.0.0.1:8000/` — frontend
- `http://127.0.0.1:8000/docs` — Swagger UI
- `http://127.0.0.1:8000/redoc` — ReDoc

## Run tests

```bash
pytest
```

Verbose output:

```bash
pytest -v
```

## Run with Docker

```bash
docker-compose up --build
```

## Build and deploy documentation

Build docs locally:

```bash
mkdocs build
```

Serve docs locally:

```bash
mkdocs serve
```

Deploy docs to GitHub Pages:

```bash
mkdocs gh-deploy
```
