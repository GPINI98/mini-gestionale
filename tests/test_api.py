import pytest
import api
import sqlite3
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

def test_trova_stipendio_medio(dipendenti_test):
    response = client.get("/dipendenti/stipendio_medio")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

    assert "stipendio_medio" in response.json()
    assert response.json()["stipendio_medio"] == 2350.00

def test_trova_stipendio_medio_senza_dipendenti(database_test):
    response = client.get("/dipendenti/stipendio_medio")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "stipendio_medio" in response.json()
    assert response.json()["stipendio_medio"] == "dipendenti non presenti"

def test_crea_dipendente_errore_database(monkeypatch):
    def inserimento_con_errore(*args):
        raise sqlite3.OperationalError("Errore simulato")

#  sostituisce temporaneamente la funzione reale di inserimento
    monkeypatch.setattr(
        "api.database.inserisci_dipendente",
        inserimento_con_errore
    )

    client = TestClient(api.app)

    response = client.post(
        "/dipendenti",
        json={"nome": "Mario", "eta": 30, "stipendio": 1800}
    )

    assert response.status_code == 500
    assert response.json()["detail"] == "Errore durante il salvataggio del dipendente"

def test_cerca_dipendenti_errore_database(monkeypatch):
    def mostra_con_errore(*args):
        raise sqlite3.OperationalError("Errore simulato")

#  sostituisce temporaneamente la funzione reale di ricerca
    monkeypatch.setattr(
        "api.database.mostra_dipendenti",
        mostra_con_errore
    )

    client = TestClient(api.app)

    response = client.get(
        "/dipendenti"
    )

    assert response.status_code == 500
    assert response.json()["detail"] == "Errore durante il recupero dei dipendenti"

def test_cerca_dipendenti_stipendio_medio_errore_database(monkeypatch):
    def mostra_stipendio_medio_con_errore(*args):
        raise sqlite3.OperationalError("Errore simulato")

#  sostituisce temporaneamente la funzione reale di ricerca stipendio medio
    monkeypatch.setattr(
        "api.database.trova_stipendio_medio",
        mostra_stipendio_medio_con_errore
    )

    client = TestClient(api.app)

    response = client.get(
        "/dipendenti/stipendio_medio"
    )

    assert response.status_code == 500
    assert response.json()["detail"] == "Errore durante il calcolo dello stipendio medio"

def test_cerca_dipendente_errore_database(monkeypatch):
    def ricerca_con_errore(*args):
        raise sqlite3.OperationalError("Errore simulato")

#  sostituisce temporaneamente la funzione reale di ricerca
    monkeypatch.setattr(
        "api.database.cerca_dipendente",
        ricerca_con_errore
    )

    client = TestClient(api.app)

    response = client.get(
        "/dipendenti/cerca?nome=Mario"
    )

    assert response.status_code == 500
    assert response.json()["detail"] == "Errore durante la ricerca del dipendente"

def test_cerca_dipendente_id_errore_database(monkeypatch):
    def ricerca_id_con_errore(*args):
        raise sqlite3.OperationalError("Errore simulato")

#  sostituisce temporaneamente la funzione reale di ricerca
    monkeypatch.setattr(
        "api.database.cerca_dipendente_id",
        ricerca_id_con_errore
    )

    client = TestClient(api.app)

    response = client.get(
        "/dipendenti/1"
    )

    assert response.status_code == 500
    assert response.json()["detail"] == "Errore durante la ricerca del dipendente"

def test_modifica_dipendente_id_errore_database(monkeypatch):
    def modifica_con_errore(*args):
        raise sqlite3.OperationalError("Errore simulato")

#  sostituisce temporaneamente la funzione reale di modifica
    monkeypatch.setattr(
        "api.database.cerca_dipendente_id",
        lambda id_dipendente: (1, "Mario", 30, 2500)  # Simula un dipendente esistente
    )
    monkeypatch.setattr(
        "api.database.modifica_dipendente",
        modifica_con_errore
    )

    client = TestClient(api.app)

    response = client.put(
        "/dipendenti/1",
        json={"nome": "Andrea", "eta": 10, "stipendio": 1900}
    )

    assert response.status_code == 500
    assert response.json()["detail"] == "Errore durante la modifica del dipendente"

def test_elimina_dipendente_id_errore_database(monkeypatch):
    def elimina_con_errore(*args):
        raise sqlite3.OperationalError("Errore simulato")

#  sostituisce temporaneamente la funzione reale di eliminazione
    monkeypatch.setattr(
        "api.database.elimina_dipendente",
        elimina_con_errore
    )

    client = TestClient(api.app)

    response = client.delete(
        "/dipendenti/1",
    )

    assert response.status_code == 500
    assert response.json()["detail"] == "Errore durante l'eliminazione del dipendente"

def test_modifica_dipendente_non_trovato_database(monkeypatch):
    def modifica_non_trovato(*args):
        return False

#  sostituisce temporaneamente la funzione reale di modifica
    monkeypatch.setattr(
        "api.database.cerca_dipendente_id",
        lambda id_dipendente: (1, "Mario", 30, 2500)  # Simula un dipendente esistente
    )
    monkeypatch.setattr(
        "api.database.modifica_dipendente",
        modifica_non_trovato
    )

    client = TestClient(api.app)

    response = client.put(
        "/dipendenti/1",
        json={"nome": "Andrea", "eta": 10, "stipendio": 1900}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Dipendente non trovato"
