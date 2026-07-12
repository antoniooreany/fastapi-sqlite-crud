# Architecture

The project uses a layered FastAPI structure that separates routing, schemas, persistence, and service logic. This keeps the codebase easier to test, extend, and explain.

## High-level layout

```text
app/
├── routers/          # API route modules
├── auth.py           # Authentication helpers and token logic
├── config.py         # Application settings
├── crud.py           # Data access helpers
├── database.py       # Engine and session management
├── logging_utils.py  # Logging configuration
├── main.py           # FastAPI application entry point
├── models.py         # SQLAlchemy ORM models
├── schemas.py        # Pydantic request/response schemas
└── services.py       # Service-layer business logic
```

## Layer responsibilities

### `main.py`

Creates the FastAPI application, registers middleware and routers, and exposes the application entry point used by Uvicorn.

### `routers/`

Defines HTTP endpoints and request/response behavior. Routers should stay thin and delegate business logic to lower layers when possible.

### `schemas.py`

Contains Pydantic models for request validation and response serialization. This keeps API contracts explicit and helps separate transport models from database models.

### `models.py`

Defines SQLAlchemy ORM models used for persistence in SQLite.

### `crud.py`

Encapsulates common database operations such as create, read, update, and delete.

### `services.py`

Provides a place for business rules and orchestration logic that should not live directly in routes.

### `auth.py`

Handles authentication utilities such as password verification, hashing, token creation, and user authentication flow.

### `database.py`

Creates the SQLAlchemy engine and session dependency used by the application.

### `logging_utils.py`

Supports structured and security-aware logging so important runtime and auth events can be traced more clearly.

## Why this structure works

This structure is appropriate for a small-to-medium backend project because it avoids putting all logic into one file while remaining simple enough to follow quickly. For portfolio purposes, it also makes architectural decisions visible to reviewers.
