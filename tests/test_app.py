from http import HTTPStatus

from fastapi.testclient import TestClient  # type: ignore

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (Organização do teste)

    response = client.get("/")  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {"message": "Olá mundo!"}  # Assert
