from typing import Generator

from sqlalchemy.orm import Session

from tests.db import TestingSessionLocal


def override_get_db() -> Generator[Session, None, None]:
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.rollback()
        db.close()


# Mover para o teste de endpoints,
# pois é específico para testes de integração com o banco de dados.
# app.dependency_overrides[get_db] = override_get_db
