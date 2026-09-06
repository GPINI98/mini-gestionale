# VALIDAZIONE
# FUNZIONE DI VALIDAZIONE NOME
def validazione_nome(): 
    while True:
        nome = input("Inserisci il nome: ")
        if nome == "" or nome.isspace():
            print("Il nome non può essere vuoto. Riprova.")
        else:
            break
    return nome

# FUNZIONE DI VALIDAZIONE ETA'
def validazione_eta():
    while True:
        try:
            eta = int(input("Inserisci l'età: "))
            if eta <= 0:
                print("L'età deve essere un numero positivo. Riprova.")
            else:
                break
        except ValueError:
            print("Devi inserire un numero valido per l'età.")
    return eta

# FUNZIONE DI VALIDAZIONE STIPENDIO
def validazione_stipendio():
    while True:
        try:
            stipendio = int(input("Inserisci lo stipendio: "))
            if stipendio <= 0:
                print("Lo stipendio deve essere un numero positivo. Riprova.")
            else:
                break
        except ValueError:
            print("Devi inserire un numero valido per lo stipendio.")
    return stipendio

def validazione_scelta():
    while True:
        try:
            scelta = int(input("Scegli un'opzione: "))
            if scelta < 1 or scelta > 7 :
                print("Scelta non valida, devi inserire un numero tra 1 e 7. Riprova.")
            else:
                break
        except ValueError:
            print("Devi inserire un numero valido.")
    return scelta
