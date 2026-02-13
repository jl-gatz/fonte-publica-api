from typing import Annotated, Generator

from fastapi import Depends
from sqlalchemy.orm import Session, sessionmaker

SessionLocal = sessionmaker(
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
