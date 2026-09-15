import sqlite3

connessione = sqlite3.connect("dipendenti.db")
cursor = connessione.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS dipendenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        eta INTEGER NOT NULL,
        stipendio REAL NOT NULL
    )
''')

# INSERISCI DIPENDENTE NEL DATABASE
def inserisci_dipendente(nome, eta, stipendio):
    cursor.execute(
        "INSERT INTO dipendenti (nome, eta, stipendio) VALUES (?, ?, ?)",
        (nome, eta, stipendio)
    )
    connessione.commit()

# CERCA DIPENDENTE NEL DATABASE
def cerca_dipendente(nome):
    cursor.execute(
        "SELECT * FROM dipendenti WHERE nome = ?",
        (nome,)
    )
    risultato = cursor.fetchone()
    return risultato

# CERCA DIPENDENTE ID NEL DATABASE
def cerca_dipendente_id(id_dipendente):
    cursor.execute(
        "SELECT * FROM dipendenti WHERE id = ?",
        (id_dipendente,)
    )
    risultato = cursor.fetchone()
    return risultato

# MOSTRA DIPENDENTI NEL DATABASE
def mostra_dipendenti():
    cursor.execute("SELECT * FROM dipendenti ORDER BY stipendio DESC")
    risultati = cursor.fetchall()
    return risultati

# MODIFICA DIPENDENTE NEL DATABASE
def modifica_dipendente(id_dipendente, nuovo_nome, nuova_eta, nuovo_stipendio):
    cursor.execute(
        "UPDATE dipendenti SET nome = ?, eta = ?, stipendio = ? WHERE id = ?",
        (nuovo_nome, nuova_eta, nuovo_stipendio, id_dipendente)
    )
    connessione.commit()

# ELIMINA DIPENDENTE DAL DATABASE
def elimina_dipendente(id_dipendente):
    cursor.execute(
        "DELETE FROM dipendenti WHERE id = ?",
        (id_dipendente,)
    )
    connessione.commit()
    if cursor.rowcount == 0:
        return False
    return True

# TROVA STIPENDIO MASSIMO NEL DATABASE
def trova_massimo():
    cursor.execute("SELECT * FROM dipendenti WHERE stipendio = (SELECT MAX(stipendio) FROM dipendenti)")
    risultato = cursor.fetchone()
    return risultato

# TROVA STIPENDIO MEDIO NEL DATABASE
def trova_stipendio_medio():
    cursor.execute("SELECT AVG(stipendio) FROM dipendenti")
    risultato = cursor.fetchone()
    return risultato[0]