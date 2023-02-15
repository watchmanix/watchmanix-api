from functools import lru_cache

from pydantic import BaseSettings

from .application import AppSettings
from .secrets import SecretsSettings


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    secrets: SecretsSettings = SecretsSettings()

    class Config:
        env_file = ".env"
        env_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """Get Base Settings and append in cache."""
    return Settings()
