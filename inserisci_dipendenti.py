import sqlite3

connessione = sqlite3.connect("dipendenti.db")
cursor = connessione.cursor()

nome = input("Nome: ")
eta = int(input("Età: "))
stipendio = float(input("Stipendio: "))

cursor.execute(
    "INSERT INTO dipendenti (nome, eta, stipendio) VALUES (?, ?, ?)",
    (nome, eta, stipendio)
)

connessione.commit()

print("Dipendente inserito con successo!")
connessione.close()

