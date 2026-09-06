# MAIN
import f_dipendenti

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
    
    while True:
        try:
            scelta = int(input("Scegli un'opzione: "))
            if scelta < 1 or scelta > 7 :
                print("Scelta non valida, devi inserire un numero tra 1 e 7. Riprova.")
            else:
                break
        except ValueError:
            print("Devi inserire un numero valido.")

    if scelta == 1 :
        f_dipendenti.mostra_dipendenti(dipendenti)
    elif scelta == 2 :
        nome_richiesto = input("che nome devo cercare?")
        risultato = f_dipendenti.cerca_dipendente(dipendenti, nome_richiesto)
        if risultato is None:
            print("dipendente non trovato")
        else :
            print(risultato)
    elif scelta == 3 :
        max_stip = f_dipendenti.trova_massimo(dipendenti)
        print(max_stip)
    elif scelta == 4 :
        while True:
            nome = input("Inserisci il nome: ")
            if nome == "" or nome.isspace():
                print("Il nome non può essere vuoto. Riprova.")
            elif f_dipendenti.cerca_dipendente(dipendenti, nome) is not None:
                print("Il nome inserito è già presente. Riprova.")
            else:
                break
        while True: 
            try:
                eta = int(input("Inserisci l'età: "))
                if eta <= 0:
                    print("L'età deve essere un numero positivo. Riprova.")
                else:
                    break
            except ValueError:
                print("Devi inserire un numero valido per l'età.")
        while True:
            try:
                stipendio = int(input("Inserisci lo stipendio: "))
                if stipendio <= 0:
                    print("Lo stipendio deve essere un numero positivo. Riprova.")
                else:
                    break
            except ValueError:
                print("Devi inserire un numero valido per lo stipendio.")
        f_dipendenti.aggiungi_dipendente(dipendenti, nome, eta, stipendio)
        print(f"dipendente {nome} aggiunto con successo")
    elif scelta == 5 :
        while True:
            nome = input("che nome devo cercare?")
            if nome == "" or nome.isspace():
                print("Il nome non può essere vuoto. Riprova.")
            else:
                break
        risultato = f_dipendenti.elimina_dipendente(dipendenti, nome)
        if risultato is True:
            print(f"{nome} è stato eliminato")    
        else:
            print("dipendente non rilevato")    
    elif scelta == 6 :
            while True:
                nome = input("Inserisci il nome: ")
                if nome == "" or nome.isspace():
                    print("Il nome non può essere vuoto. Riprova.")
                elif f_dipendenti.cerca_dipendente(dipendenti, nome) is None:
                    print("Il nome inserito non è presente. Riprova.")
                else:
                    break
            while True: 
                try:
                    nuova_eta = int(input("Inserisci l'età: "))
                    if nuova_eta <= 0:
                        print("L'età deve essere un numero positivo. Riprova.")
                    else:
                        break
                except ValueError:
                    print("Devi inserire un numero valido per l'età.")
            while True:
                try:
                    nuovo_stipendio = int(input("Inserisci lo stipendio: "))
                    if nuovo_stipendio <= 0:
                        print("Lo stipendio deve essere un numero positivo. Riprova.")
                    else:
                        break
                except ValueError:
                    print("Devi inserire un numero valido per lo stipendio.")
            f_dipendenti.modifica_dipendente(dipendenti, nome, nuova_eta, nuovo_stipendio)
            print(f"dipendente {nome} modificato con successo")

