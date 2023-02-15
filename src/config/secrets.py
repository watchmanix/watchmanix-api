import os

from pydantic import BaseModel, Field

from .database import DatabaseSettings


class SecretsSettings(BaseModel):
    DEBUG: str = os.getenv("DEBUG", "DEBUG")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "SECRET_KEY")

    allowed_host_env: str = os.getenv("ALLOWED_HOSTS", "ALLOWED_HOSTS")
    cors_allow_origins_env: str = os.getenv("CORS_ALLOW_ORIGINS", "CORS_ALLOW_ORIGINS")

    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    db: DatabaseSettings = DatabaseSettings()

    @property
    def ALLOWED_HOSTS(self):
        return self.allowed_host_env.split(",")

    @property
    def CORS_ALLOW_ORIGINS(self):
        list_hosts = self.cors_allow_origins_env.split(",")
        return [f"http://{address}" for address in list_hosts]
