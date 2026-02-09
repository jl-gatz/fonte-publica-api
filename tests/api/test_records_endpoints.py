from http import HTTPStatus


def test_list_records_empty(client):
    response = client.get("api/v1/records")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == []
