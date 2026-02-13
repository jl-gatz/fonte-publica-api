from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base declarativa única para todos os models ORM.

    - Centraliza o metadata
    - Compatível com SQLAlchemy 2.0
    - Base para Alembic e testes
    """

    pass
