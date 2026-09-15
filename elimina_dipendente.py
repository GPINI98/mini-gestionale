import sqlite3

connessione = sqlite3.connect("dipendenti.db")
cursor = connessione.cursor()

id_dipendente = int(input("ID del dipendente da eliminare: "))
cursor.execute(
    "DELETE FROM dipendenti WHERE id = ?",
    (id_dipendente,)
)


connessione.commit()
if cursor.rowcount == 0:
    print("Nessun dipendente trovato con l'ID specificato.")
else:
    print("Dipendente eliminato con successo!")
connessione.close()

