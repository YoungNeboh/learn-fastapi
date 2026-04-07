from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    # --- Project Info ---
    PROJECT_NAME: str = "Multi-Tenant Shopping API"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    # --- Database ---
    DATABASE_URL: str 

    # --- Security & Auth ---
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 1 week

    # --- Multi-Tenancy ---
    # The main domain of your app (e.g., "localhost" or "myapp.com")
    BASE_DOMAIN: str = "localhost" 

    # --- CORS ---
    # Domains allowed to talk to your API
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]

    model_config = SettingsConfigDict(
        env_file=".env", 
        case_sensitive=True, 
        extra="ignore"
    )

settings = Settings()