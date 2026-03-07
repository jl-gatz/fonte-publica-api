from sqlalchemy import create_engine

from app.core.config import get_settings

settings = get_settings()


def create_db_engine(database_url: str | None = None, echo: bool = False):
    return create_engine(
        settings.DATABASE_URL,
        echo=settings.SQL_ECHO,
        pool_pre_ping=True,
    )
