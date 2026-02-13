from http import HTTPStatus

from fastapi.testclient import TestClient


def test_list_records_empty(client: TestClient):
    response = client.get("api/v1/records")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == []
