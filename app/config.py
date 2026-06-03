from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = "sqlite:///./items.db"
    app_title: str = "FastAPI SQLite CRUD Example"
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
