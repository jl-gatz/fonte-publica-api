from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Fonte Pública API"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"
    DATABASE_URL: str = "sqlite+pysqlite:///:memory:"
    SQL_ECHO: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
