import pytest
import api
from fastapi.testclient import TestClient

client = TestClient(api.app)
@pytest.fixture
def database_test(tmp_path, monkeypatch):
    percorso_database = tmp_path / "test.db"
    monkeypatch.setattr(api.database, "PERCORSO_DATABASE", str(percorso_database))
    api.database.inizializzazione_database()

@pytest.fixture
def dipendenti_test(database_test):
    api.database.inserisci_dipendente("Mario", 30, 2500)
    api.database.inserisci_dipendente("Anna", 28, 2200)

def test_get_dipendenti(dipendenti_test):
    response = client.get("/dipendenti")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_dipendente(dipendenti_test):
    response = client.get("/dipendenti/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_dipendente_non_esistente(dipendenti_test):
    response = client.get("/dipendenti/999")
    assert response.status_code == 404

def test_crea_dipendente(dipendenti_test):
    response = client.post("/dipendenti", json={
        "nome": "Test",
        "eta": 30,
        "stipendio": 3000.0
    })
    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["id"], int)
    assert response.json()["eta"] == 30
    assert response.json()["stipendio"] == 3000.0
    assert response.json()["nome"] == "Test"

def test_crea_dipendente_dati_non_validi():
    response = client.post("/dipendenti", json={
        "nome": "Test",
        "eta": "ciao",
        "stipendio": 3000
    })
    assert response.status_code == 422

def test_modifica_dipendente(dipendenti_test):
    response = client.put("/dipendenti/1", json={
        "nome": "Mario Modificato",
        "eta": 40,
        "stipendio": 3500
    })
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["eta"] == 40
    assert response.json()["stipendio"] == 3500
    assert response.json()["nome"] == "Mario Modificato"

def test_modifica_dipendente_non_esistente(dipendenti_test):
    response = client.put("/dipendenti/999", json={
        "nome": "Mario Modificato",
        "eta": 40,
        "stipendio": 3500
    })
    assert response.status_code == 404

def test_elimina_dipendente(dipendenti_test):
    response = client.delete("/dipendenti/1")

    assert response.status_code == 204

def test_elimina_dipendente_non_esistente(dipendenti_test):
    response = client.delete("/dipendenti/999")
    
    assert response.status_code == 404

def test_cerca_dipendente(dipendenti_test):
    response = client.get("/dipendenti/cerca?nome=Mario")
    risultato = response.json()
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert risultato[0]["nome"] == "Mario"

def test_cerca_dipendente_non_trovato(dipendenti_test):
    response = client.get("/dipendenti/cerca?nome=NonEsistente")
    
    assert response.status_code == 404

def test_crea_dipendente_eta_negativa():
    response = client.post("/dipendenti", json={
        "nome": "Test",
        "eta": -5,
        "stipendio": 3000
    })
    assert response.status_code == 422

def test_crea_dipendente_stipendio_negativo():
    response = client.post("/dipendenti", json={
        "nome": "Test",
        "eta": 30,
        "stipendio": -1000
    })
    assert response.status_code == 422

def test_crea_dipendente_nome_vuoto_con_spazi():
    response = client.post("/dipendenti", json={
        "nome": "  ",
        "eta": 30,
        "stipendio": 1000
    })
    assert response.status_code == 422