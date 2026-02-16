from http import HTTPStatus
from unittest.mock import MagicMock, patch

import pytest
from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

from app.db.dependencies import get_db

app = FastAPI()


def test_get_db_yields_session_and_closes():
    fake_session = MagicMock()

    with patch("app.db.dependencies.SessionLocal", return_value=fake_session):
        generator = get_db()

        # executa até o yield
        db = next(generator)

        assert db == fake_session
        fake_session.close.assert_not_called()

        # força execução do finally
        with pytest.raises(StopIteration):
            next(generator)

        fake_session.close.assert_called_once()


@app.get("/")
def route(db=Depends(get_db)):
    return {"ok": True}


def test_dependency_with_fastapi():
    fake_session = MagicMock()

    with patch("app.db.dependencies.SessionLocal", return_value=fake_session):
        client = TestClient(app)
        response = client.get("/")

        assert response.status_code == HTTPStatus.OK
        fake_session.close.assert_called_once()
