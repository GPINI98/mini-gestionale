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

def inserisci_dipendente(nome, eta, stipendio):
    cursor.execute(
        "INSERT INTO dipendenti (nome, eta, stipendio) VALUES (?, ?, ?)",
        (nome, eta, stipendio)
    )
    connessione.commit()
    if cursor.rowcount == 0:
        print("Errore nell'inserimento del dipendente.")
    else:
        print("Dipendente inserito con successo!")

# nome = input("Nome: ")
# eta = int(input("Età: "))
# stipendio = float(input("Stipendio: "))

# # INSERISCI DIPENDENTE NEL DATABASE
# cursor.execute(
#     "INSERT INTO dipendenti (nome, eta, stipendio) VALUES (?, ?, ?)",
#     (nome, eta, stipendio)
# )
# if cursor.rowcount == 0:
#     print("Errore nell'inserimento del dipendente.")
# else:
#     print("Dipendente inserito con successo!")
connessione.commit()

# MOSTRA DIPENDENTI NEL DATABASE
def mostra_dipendenti():
    cursor.execute("SELECT * FROM dipendenti ORDER BY stipendio DESC")
    risultati = cursor.fetchall()
    for dipendente in risultati:
        print(dipendente)
# cursor.execute("SELECT * FROM dipendenti ORDER BY stipendio DESC")
# risultati = cursor.fetchall()
# for dipendente in risultati:
#     print(dipendente)

# MODIFICA DIPENDENTE NEL DATABASE
def modifica_dipendente(id_dipendente, nuovo_stipendio):
    cursor.execute(
        "UPDATE dipendenti SET stipendio = ? WHERE id = ?",
        (nuovo_stipendio, id_dipendente)
    )
    if cursor.rowcount == 0:
        print("Nessun dipendente trovato con l'ID specificato.")
    else:
        print("Dipendente modificato con successo!")
    connessione.commit()
# id_dipendente = int(input("ID del dipendente da modificare: "))
# nuovo_stipendio = float(input("Nuovo stipendio: "))
# cursor.execute(
#     "UPDATE dipendenti SET stipendio = ? WHERE id = ?",
#     (nuovo_stipendio, id_dipendente)
# )
# if cursor.rowcount == 0:
#     print("Nessun dipendente trovato con l'ID specificato.")
# else:
#     print("Dipendente modificato con successo!")
connessione.commit()

# ELIMINA DIPENDENTE DAL DATABASE
def elimina_dipendente(id_dipendente):
    cursor.execute(
        "DELETE FROM dipendenti WHERE id = ?",
        (id_dipendente,)
    )
    if cursor.rowcount == 0:
        print("Nessun dipendente trovato con l'ID specificato.")
    else:
        print("Dipendente eliminato con successo!")
    connessione.commit()
# id_dipendente = int(input("ID del dipendente da eliminare: "))
# cursor.execute(
#     "DELETE FROM dipendenti WHERE id = ?",
#     (id_dipendente,)
# )
# if cursor.rowcount == 0:
#     print("Nessun dipendente trovato con l'ID specificato.")
# else:
#     print("Dipendente eliminato con successo!")
connessione.commit()

connessione.close()