import sqlite3

connessione = sqlite3.connect("dipendenti.db")
cursor = connessione.cursor()

id_dipendente = int(input("ID del dipendente da modificare: "))
nuovo_stipendio = float(input("Nuovo stipendio: "))
cursor.execute(
    "UPDATE dipendenti SET stipendio = ? WHERE id = ?",
    (nuovo_stipendio, id_dipendente)
)


connessione.commit()

print("Dipendente modificato con successo!")
connessione.close()

