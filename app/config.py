from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = "sqlite:///./items.db"
    app_title: str = "FastAPI SQLite CRUD Example"
    app_version: str = "1.5.0"  # Match the version in GEMINI.md
    environment: str = "development"
    secret_key: str = "supersecretkey"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    salt_used: str = "default_salt"  # Required by system prompt requirements
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
