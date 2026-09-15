# MAIN
import validazione
import database1

scelta = 0

while scelta != 8:

    print("1. Mostra dipendenti")
    print("2. Cerca dipendente")
    print("3. Trova stipendio massimo")
    print("4. Aggiungi dipendente")
    print("5. Elimina dipendente")
    print("6. Modifica dipendente")
    print("7. Mostra stipendio medio")
    print("8. Esci")

    
    scelta = validazione.validazione_scelta()

    if scelta == 1 :
        dipendenti = database1.mostra_dipendenti()
        for dipendente in dipendenti:
            print(f"ID: {dipendente[0]}, Nome: {dipendente[1]}, Età: {dipendente[2]}, Stipendio: {dipendente[3]:.2f} €")
    elif scelta == 2 :
        nome_richiesto = validazione.validazione_nome()
        risultato = database1.cerca_dipendente(nome_richiesto)
        if risultato is None:
            print("dipendente non trovato")
        else :
            print(f"ID: {risultato[0]}, Nome: {risultato[1]}, Età: {risultato[2]}, Stipendio: {risultato[3]:.2f} €")
    elif scelta == 3 :
        max_stip = database1.trova_massimo()
        print(f"L'utente con lo stipendio più alto è ID: {max_stip[0]}, Nome: {max_stip[1]}, Età: {max_stip[2]}, Stipendio: {max_stip[3]:.2f} €")
    elif scelta == 4 :
        nome = validazione.validazione_nome()
        eta = validazione.validazione_eta()
        stipendio = validazione.validazione_stipendio()
        database1.inserisci_dipendente(nome, eta, stipendio)
        print(f"dipendente {nome} aggiunto con successo")
    elif scelta == 5 :
        id_dipendente = validazione.validazione_id()
        risultato = database1.elimina_dipendente(id_dipendente)
        if risultato is False:
            print("dipendente non trovato")
        else:
            print(f"Dipendente ID {id_dipendente} eliminato con successo")
    elif scelta == 6 :
        while True:
            id_dipendente = validazione.validazione_id()
            if database1.cerca_dipendente_id(id_dipendente) is None:
                print("L'id inserito non è presente. Riprova.")
            else:
                break
        nuovo_nome = validazione.validazione_nome()
        nuova_eta = validazione.validazione_eta()
        nuovo_stipendio = validazione.validazione_stipendio()
        database1.modifica_dipendente(id_dipendente, nuovo_nome, nuova_eta, nuovo_stipendio)
        print(f"ID: {id_dipendente} modificato con successo")
    elif scelta == 7 :
        media_stipendi = database1.trova_stipendio_medio()
        print(f"Lo stipendio medio dei dipendenti è: {media_stipendi:.2f}")
