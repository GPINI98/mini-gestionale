import validazione

def test_validazione_nome(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Mario")

    risultato = validazione.validazione_nome()
    assert risultato == "Mario"

def test_validazione_nome_vuoto(monkeypatch):
    input_simulato = iter(["", "Luigi"])

    monkeypatch.setattr("builtins.input", lambda _: next(input_simulato))

    risultato = validazione.validazione_nome()

    assert risultato == "Luigi"

def test_validazione_id(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "10")

    risultato = validazione.validazione_id()

    assert risultato == 10

def test_validazione_id_non_valido(monkeypatch):
    input_simulato = iter(["abc", "0", "-5", "10"])

    monkeypatch.setattr("builtins.input", lambda _: next(input_simulato))

    risultato = validazione.validazione_id()

    assert risultato == 10

def test_validazione_eta(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "30")

    risultato = validazione.validazione_eta()

    assert risultato == 30

def test_validazione_eta_non_valida(monkeypatch):
    input_simulato = iter(["abc", "0", "-10", "30"])

    monkeypatch.setattr("builtins.input", lambda _: next(input_simulato))

    risultato = validazione.validazione_eta()

    assert risultato == 30

def test_validazione_stipendio(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2500")

    risultato = validazione.validazione_stipendio()

    assert risultato == 2500

def test_validazione_stipendio_non_valido(monkeypatch):
    input_simulato = iter(["abc", "0", "-100", "2500"])

    monkeypatch.setattr("builtins.input", lambda _: next(input_simulato))

    risultato = validazione.validazione_stipendio()

    assert risultato == 2500

def test_validazione_scelta(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "5")

    risultato = validazione.validazione_scelta()

    assert risultato == 5

def test_validazione_scelta_non_valida(monkeypatch):
    input_simulato = iter(["abc", "0", "9", "5"])

    monkeypatch.setattr("builtins.input", lambda _: next(input_simulato))

    risultato = validazione.validazione_scelta()

    assert risultato == 5