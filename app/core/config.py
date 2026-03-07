import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseAppSettings(BaseSettings):
    PROJECT_NAME: str = "Fonte Pública API"
    API_V1_STR: str = "/api/v1"

    VERSION: str = "1.0.0"
    BUILD_VERSION: str = "dev"
    COMMIT_HASH: str = "unknown"

    ENVIRONMENT: str

    DATABASE_URL: str
    SQL_ECHO: bool = False
    DEBUG: bool = False

    SERVICE_NAME: str = "farol-publico"
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        case_sensitive=True,
    )


class DevSettings(BaseAppSettings):
    ENVIRONMENT: str = "dev"
    DEBUG: bool = True
    SQL_ECHO: bool = True

    model_config = SettingsConfigDict(
        env_file=".env.dev",
        case_sensitive=True,
    )


class TestSettings(BaseAppSettings):
    ENVIRONMENT: str = "test"
    DEBUG: bool = False
    SQL_ECHO: bool = False

    model_config = SettingsConfigDict(
        env_file=".env.test",
        case_sensitive=True,
    )


class ProdSettings(BaseAppSettings):
    ENVIRONMENT: str = "prod"
    DEBUG: bool = False
    SQL_ECHO: bool = False

    model_config = SettingsConfigDict(
        env_file=".env.prod",
        case_sensitive=True,
    )


def _select_settings_class():
    env = os.getenv("ENVIRONMENT", "dev")

    if env == "prod":
        return ProdSettings
    if env == "test":
        return TestSettings
    return DevSettings


@lru_cache
def get_settings() -> BaseAppSettings:
    settings_class = _select_settings_class()
    return settings_class()
