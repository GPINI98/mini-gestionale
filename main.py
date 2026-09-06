# MAIN
import f_dipendenti
import validazione

dipendenti = [
    {"nome": "Marco", "eta": 32, "stipendio": 2200},
    {"nome": "Luca", "eta": 25, "stipendio": 1800},
    {"nome": "Anna", "eta": 41, "stipendio": 2500},
    {"nome": "Paolo", "eta": 29, "stipendio": 1950}
]
    
scelta = 0

while scelta != 7:

    print("1. Mostra dipendenti")
    print("2. Cerca dipendente")
    print("3. Trova stipendio massimo")
    print("4. Aggiungi dipendente")
    print("5. Elimina dipendente")
    print("6. Modifica dipendente")
    print("7. Esci")
    
    scelta = validazione.validazione_scelta()

    if scelta == 1 :
        f_dipendenti.mostra_dipendenti(dipendenti)
    elif scelta == 2 :
        nome_richiesto = validazione.validazione_nome()
        risultato = f_dipendenti.cerca_dipendente(dipendenti, nome_richiesto)
        if risultato is None:
            print("dipendente non trovato")
        else :
            print(risultato)
    elif scelta == 3 :
        max_stip = f_dipendenti.trova_massimo(dipendenti)
        print(max_stip)
    elif scelta == 4 :
        nome = validazione.validazione_nome()
        eta = validazione.validazione_eta()
        stipendio = validazione.validazione_stipendio()
        f_dipendenti.aggiungi_dipendente(dipendenti, nome, eta, stipendio)
        print(f"dipendente {nome} aggiunto con successo")
    elif scelta == 5 :
        nome = validazione.validazione_nome()
        risultato = f_dipendenti.elimina_dipendente(dipendenti, nome)
        if risultato is True:
            print(f"{nome} è stato eliminato")    
        else:
            print("dipendente non rilevato")    
    elif scelta == 6 :
        while True:
            nome = validazione.validazione_nome()
            if f_dipendenti.cerca_dipendente(dipendenti, nome) is None:
                print("Il nome inserito non è presente. Riprova.")
            else:
                break
        nuova_eta = validazione.validazione_eta()
        nuovo_stipendio = validazione.validazione_stipendio()
        f_dipendenti.modifica_dipendente(dipendenti, nome, nuova_eta, nuovo_stipendio)
        print(f"dipendente {nome} modificato con successo")

