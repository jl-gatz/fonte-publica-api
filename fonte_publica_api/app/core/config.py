from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Fonte Pública API"
    API_V1_STR: str = "/v1"
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"


settings = Settings()
