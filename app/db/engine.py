from sqlalchemy import create_engine


def create_db_engine(database_url: str | None = None, echo: bool = False):
    return create_engine(
        database_url,
        echo=echo,
        pool_pre_ping=True,
    )
