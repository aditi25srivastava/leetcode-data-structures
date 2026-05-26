from pathlib import Path
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    app_name: str = "NeuroSync AI"
    environment: str = "development"
    ai_provider: str = Field("openai", env="AI_PROVIDER")
    openai_api_key: str = Field("", env="OPENAI_API_KEY")
    openai_api_base: str = Field("https://api.openai.com", env="OPENAI_API_BASE")
    openrouter_api_key: str = Field("", env="OPENROUTER_API_KEY")
    openrouter_api_base: str = Field("https://openrouter.ai/v1", env="OPENROUTER_API_BASE")
    mongo_uri: str = Field("mongodb://localhost:27017", env="MONGO_URI")
    auth_username: str = Field("pilot", env="AUTH_USERNAME")
    auth_password: str = Field("portfolio", env="AUTH_PASSWORD")
    auth_token_secret: str = Field("super-secret-token", env="AUTH_TOKEN_SECRET")
    frontend_url: str = Field("http://localhost:3000", env="FRONTEND_URL")
    backend_url: str = Field("http://localhost:8000", env="BACKEND_URL")

    class Config:
        env_file = Path(__file__).resolve().parents[2] / ".env"
        env_file_encoding = "utf-8"


settings = Settings()
