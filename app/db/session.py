from typing import Annotated, Generator

from fastapi import Depends
from sqlalchemy.orm import Session, sessionmaker

from app.db import engine
from app.db.engine import get_engine

engine = get_engine()  # noqa: F811

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DbSession = Annotated[Session, Depends(get_db)]
