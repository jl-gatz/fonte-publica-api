from http import HTTPStatus


def teste_simples(client):
    response = client.get("/")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "Not Found"}
