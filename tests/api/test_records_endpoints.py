from http import HTTPStatus

from fastapi.testclient import TestClient


def test_list_records_empty(client: TestClient):
    response = client.get("api/v1/records")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == []


def test_create_records(client: TestClient):
    payload = {
        "type": "document",
        "title": "Lei de Acesso à Informação",
        "summary": "Lei que regula o acesso a informações públicas",
        "source": {
            "name": "Planalto",
            "method": "download",
            "url": "https://www.planalto.gov.br",
        },
        "collected_at": "2024-06-01T12:00:00Z",
        "status": "published",
        "version": 1,
        "hash": "testhash123",
        "attributes": {"tema": "transparência"},
    }

    response = client.post("api/v1/records/", json=payload)
    assert response.status_code == HTTPStatus.CREATED
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["source"]["name"] == payload["source"]["name"]
    assert data["version"] == payload["version"]
