from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Fonte Pública API"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"

    VERSION: str = "1.0.0"
    BUILD_VERSION: str = "dev"
    COMMIT_HASH: str = "unknown"

    DATABASE_URL: str = "sqlite+pysqlite:///:memory:"
    SQL_ECHO: bool = False
    DEBUG: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
