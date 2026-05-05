import requests

from config import BASE_URL;

def test_criar_usuario_com_sucesso():
    payload = {
        "id": 6767,
        "username": "joao_qa",
        "firstName": "Joao",
        "lastName": "Rabelo",
        "email": "joao@email.com",
        "password": "123",
        "phone": "99999999",
        "userStatus": 0
    }

    response = requests.post(f"{BASE_URL}/user", json=payload)

    assert response.status_code == 200  
    assert response.json()["message"] == "6767" 

def test_fazer_login_usuario():
    params = {
        "username": "joao_qa",
        "password": "123"
    }

    response = requests.get(f"{BASE_URL}/user/login", params=params)

    assert response.status_code == 200
    assert "logged in user session" in response.json()["message"] 