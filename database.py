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

cursor.execute(
    "INSERT INTO dipendenti (nome, eta, stipendio) VALUES (?, ?, ?)",
    ("Mario", 30, 2500)
)
cursor.execute(
    "INSERT INTO dipendenti (nome, eta, stipendio) VALUES (?, ?, ?)",
    ("Luca", 25, 500)
)
cursor.execute(
    "INSERT INTO dipendenti (nome, eta, stipendio) VALUES (?, ?, ?)",
    ("Anna", 41, 3500)
)
cursor.execute(
    "INSERT INTO dipendenti (nome, eta, stipendio) VALUES (?, ?, ?)",
    ("Paolo", 29, 1500)
)
connessione.commit()
connessione.close()