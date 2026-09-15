import sqlite3

connessione = sqlite3.connect("dipendenti.db")

cursor = connessione.cursor()

cursor.execute("SELECT * FROM dipendenti WHERE stipendio > 500 ORDER BY stipendio DESC")

risultati = cursor.fetchall()

for dipendente in risultati:
    print(dipendente)

connessione.close()