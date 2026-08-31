import config

dipendenti = [
    {"nome": "Marco", "eta": 32, "stipendio": 2200},
    {"nome": "Luca", "eta": 25, "stipendio": 1800},
    {"nome": "Anna", "eta": 41, "stipendio": 2500},
    {"nome": "Paolo", "eta": 29, "stipendio": 1950}
]
    
scelta = 0

while scelta != 6:

    print("1. Mostra dipendenti")
    print("2. Cerca dipendente")
    print("3. Trova stipendio massimo")
    print("4. Chiama aggiungi dipendente")
    print("5. Elimina dipendente")
    print("6. Esci")

    scelta = int(input("Scegli un'opzione: "))

    if scelta == 1 :
        config.mostra_dipendenti(dipendenti)
    elif scelta == 2 :
        nome_richiesto = input("che nome devo cercare?")
        risultato = config.cerca_dipendente(dipendenti, nome_richiesto)
        if risultato is None:
            print("dipendente non trovato")
        else :
            print(risultato)
    elif scelta == 3 :
        max_stip = config.trova_massimo(dipendenti)
        print(max_stip)
    elif scelta == 4 :
        nome = input("Inserisci il nome: ")
        eta = int(input("Inserisci l'età: "))
        stipendio = int(input("Inserisci lo stipendio: "))        
        config.aggiungi_dipendente(dipendenti, nome, eta, stipendio)
    elif scelta == 5 :
        config.elimina_dipendente(dipendenti)
        
        
