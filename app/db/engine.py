from sqlalchemy import create_engine

from app.core.config import settings


def get_engine(database_url: str | None = None):
    return create_engine(
        database_url or settings.DATABASE_URL,
        echo=settings.SQL_ECHO,
        pool_pre_ping=True,
    )
