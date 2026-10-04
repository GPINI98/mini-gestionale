import pytest
import database
import validazione

@pytest.fixture
def database_test(tmp_path):
    percorso_database = tmp_path / "test.db"

    return percorso_database

def test_modifica_dipendente(database_test, monkeypatch):
    monkeypatch.setattr(database, "PERCORSO_DATABASE", str(database_test))

    database.inizializzazione_database()
    database.inserisci_dipendente("Mario", 30, 2000)
    database.modifica_dipendente(1, "Mario", 40, 12000)

    risultato = database.cerca_dipendente("Mario")

    assert risultato is not None
    assert risultato[1] == "Mario"
    assert risultato[2] == 40
    assert risultato[3] == 12000

def test_elimina_dipendente(database_test, monkeypatch):
    monkeypatch.setattr(database, "PERCORSO_DATABASE", str(database_test))

    database.inizializzazione_database()
    database.inserisci_dipendente("Mario", 30, 2000)
    database.elimina_dipendente(1)

    risultato = database.cerca_dipendente("Mario")

    assert risultato is None

def test_elimina_dipendente_non_esistente(database_test, monkeypatch):
    monkeypatch.setattr(database, "PERCORSO_DATABASE", str(database_test))

    database.inizializzazione_database()
    database.inserisci_dipendente("Mario", 30, 2000)

    risultato = database.elimina_dipendente(999)

    assert risultato is False

def test_trova_stipendio_medio(database_test, monkeypatch):
    monkeypatch.setattr(database, "PERCORSO_DATABASE", str(database_test))

    database.inizializzazione_database()
    database.inserisci_dipendente("Mario", 30, 2000)
    database.inserisci_dipendente("Pippo", 20, 3000)

    risultato = database.trova_stipendio_medio()

    assert risultato == 2500

def test_inserisci_dipendente(database_test, monkeypatch):
    monkeypatch.setattr(database, "PERCORSO_DATABASE", str(database_test))

    database.inizializzazione_database()
    database.inserisci_dipendente("Luigi", 25, 2500)

    risultato = database.cerca_dipendente("Luigi")

    assert risultato is not None
    assert risultato[1] == "Luigi"
    assert risultato[2] == 25
    assert risultato[3] == 2500

def test_cerca_dipendente(database_test, monkeypatch):
    monkeypatch.setattr(database, "PERCORSO_DATABASE", str(database_test))

    database.inizializzazione_database()
    database.inserisci_dipendente("Anna", 28, 2200)

    risultato = database.cerca_dipendente("Anna")

    assert risultato is not None
    assert risultato[1] == "Anna"
    assert risultato[2] == 28
    assert risultato[3] == 2200

def test_cerca_dipendente_id(database_test, monkeypatch):
    monkeypatch.setattr(database, "PERCORSO_DATABASE", str(database_test))

    database.inizializzazione_database()
    database.inserisci_dipendente("Marco", 35, 2800)

    risultato = database.cerca_dipendente_id(1)

    assert risultato is not None
    assert risultato[0] == 1
    assert risultato[1] == "Marco"
    assert risultato[2] == 35
    assert risultato[3] == 2800

def test_mostra_dipendenti(database_test, monkeypatch):
    monkeypatch.setattr(database, "PERCORSO_DATABASE", str(database_test))

    database.inizializzazione_database()
    database.inserisci_dipendente("Luca", 30, 2000)
    database.inserisci_dipendente("Sara", 25, 3000)

    risultato = database.mostra_dipendenti()

    assert len(risultato) == 2
    assert risultato[0][1] == "Sara"
    assert risultato[0][2] == 25
    assert risultato[0][3] == 3000
    assert risultato[1][1] == "Luca"
    assert risultato[1][2] == 30
    assert risultato[1][3] == 2000

def test_mostra_dipendenti_database_vuoto(database_test, monkeypatch):
    monkeypatch.setattr(database, "PERCORSO_DATABASE", str(database_test))

    database.inizializzazione_database()

    risultato = database.mostra_dipendenti()

    assert risultato == []

def test_trova_massimo(database_test, monkeypatch):
    monkeypatch.setattr(database, "PERCORSO_DATABASE", str(database_test))

    database.inizializzazione_database()
    database.inserisci_dipendente("Mario", 30, 2000)
    database.inserisci_dipendente("Pippo", 20, 3000)

    risultato = database.trova_massimo()

    assert risultato is not None
    assert risultato[1] == "Pippo"
    assert risultato[2] == 20
    assert risultato[3] == 3000 

def test_trova_massimo_database_vuoto(database_test, monkeypatch):
    monkeypatch.setattr(database, "PERCORSO_DATABASE", str(database_test))

    database.inizializzazione_database()

    risultato = database.trova_massimo()

    assert risultato is None

