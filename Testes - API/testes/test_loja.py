import requests
from config import BASE_URL

ORDER_ID = 1001

def test_consultar_inventario():
    r = requests.get(f"{BASE_URL}/store/inventory")
    assert r.status_code == 200
    assert isinstance(r.json(), dict)

def test_criar_pedido():
    payload = {
        "id": ORDER_ID,
        "petId": 9999,
        "quantity": 1,
        "status": "placed",
        "complete": False
    }
    r = requests.post(f"{BASE_URL}/store/order", json=payload)
    assert r.status_code == 200
    assert r.json()["id"] == ORDER_ID
    assert r.json()["status"] == "placed"

def test_buscar_pedido_por_id():
    r = requests.get(f"{BASE_URL}/store/order/{ORDER_ID}")
    assert r.status_code == 200
    assert r.json()["id"] == ORDER_ID
    assert r.json()["petId"] == 9999

def test_deletar_pedido():
    r = requests.delete(f"{BASE_URL}/store/order/{ORDER_ID}")
    assert r.status_code == 200

def test_buscar_pedido_deletado_retorna_404():
    r = requests.get(f"{BASE_URL}/store/order/{ORDER_ID}")
    assert r.status_code == 404