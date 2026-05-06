import requests
from config_api import URL_API

PET_ID = 9999

def test_criar_pet():
    payload = {
        "id": PET_ID,
        "name": "Rex",
        "status": "available",
        "photoUrls": ["https://exemplo.com/rex.jpg"]
    }
    r = requests.post(f"{URL_API}/pet", json=payload)
    assert r.status_code == 200
    assert r.json()["id"] == PET_ID
    assert r.json()["name"] == "Rex"

def test_buscar_pet_por_id():
    r = requests.get(f"{URL_API}/pet/{PET_ID}")
    assert r.status_code == 200
    assert r.json()["id"] == PET_ID

def test_buscar_pet_por_status():
    r = requests.get(f"{URL_API}/pet/findByStatus", params={"status": "available"})
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    assert any(p["status"] == "available" for p in r.json())

def test_atualizar_pet():
    payload = {
        "id": PET_ID,
        "name": "Toby Fox",
        "status": "pending",
        "photoUrls": ["https://undertale.wiki/images/Trophy_sprite_Bronze.png?cb=ile637&h=thumb.php&f=Trophy_sprite_Bronze.png"]
    }
    r = requests.put(f"{URL_API}/pet", json=payload)
    assert r.status_code == 200
    assert r.json()["name"] == "Toby Fox"
    assert r.json()["status"] == "pending"

def test_deletar_pet():
    r = requests.delete(f"{URL_API}/pet/{PET_ID}")
    assert r.status_code == 200

def test_buscar_pet_deletado_retorna_404():
    r = requests.get(f"{URL_API}/pet/{PET_ID}")
    assert r.status_code == 404