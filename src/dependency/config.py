from pydantic_settings import BaseSettings
from pathlib import Path
import os

PROJECT_DIR = Path(__name__).resolve().parent


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///database.db"  # if no URL provided

    class Config:
        env_file = os.path.join(PROJECT_DIR, ".env")


settings = Settings()
