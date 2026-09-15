import json

# DIPENDENTI 
# ################# MOSTRA DIPENDENTI
def mostra_dipendenti(dipendenti):
    for dipendente in dipendenti:
        print(f"{dipendente['nome']}, {dipendente['eta']} anni , {dipendente['stipendio']} euro")

# ################# CERCA DIPENDENTI
def cerca_dipendente(dipendenti, nome):
    for dipendente in dipendenti:
        if dipendente['nome'] == nome:
            return dipendente
    return None


# ################# MOSTRA MASSIMO STIPENDIO
def trova_massimo(dipendenti):
    dipendente_max = None
    for dipendente in dipendenti:
        if dipendente_max is None or dipendente_max['stipendio'] < dipendente ['stipendio']:
            dipendente_max = dipendente
    return dipendente_max

# ################# MOSTRA STIPENDIO MEDIO
def calcola_stipendio_medio(dipendenti):
    somma_stipendi = 0
    for dipendente in dipendenti:
        somma_stipendi += dipendente['stipendio']
    return somma_stipendi / len(dipendenti) if dipendenti else 0

# ################# AGGIUNGI DIPENDENTE
def aggiungi_dipendente(dipendenti, nome, eta, stipendio):
    nuovo_dipendente = {
        "nome" : nome,
        "eta" : eta,
        "stipendio" : stipendio
    }
    dipendenti.append(nuovo_dipendente)

# ################# ELIMINA DIPENDENTE
def elimina_dipendente(dipendenti, nome):
    dipendente = cerca_dipendente(dipendenti, nome) 
    if dipendente is None:
        return False
    dipendenti.remove(dipendente)
    return True

# ################# MODIFICA DIPENDENTE
def modifica_dipendente(dipendenti, nome, nuova_eta, nuovo_stipendio):
    dipendente_modifica = cerca_dipendente(dipendenti, nome)
    if dipendente_modifica is None:
        return False
    dipendente_modifica['eta'] = nuova_eta
    dipendente_modifica['stipendio'] = nuovo_stipendio
    return True
    
# ################# SALVA DIPENDENTI
def salva_dipendenti(dipendenti):
    with open("dipendenti.json", "w") as file:
        json.dump(dipendenti, file, indent=4)

# ################# CONTROLLO JSON

def controllo_json():
    try:
        with open("dipendenti.json", "r") as file:
            dipendenti = json.load(file)
    except FileNotFoundError:
        print("Il file dipendenti.json non è stato trovato. Creazione di un nuovo file.")
        dipendenti = []
        salva_dipendenti(dipendenti)
    except json.JSONDecodeError:
        print("Errore nel decodificare il file JSON. Creazione di un nuovo file.")
        dipendenti = []
        salva_dipendenti(dipendenti)
    return dipendenti

# ############## ANALIZZA DIPENDENTI
def analizza_dipendenti(dipendenti):
    if not dipendenti:
        return {
            "numero_dipendenti": 0,
            "stipendio_minimo": 0,
            "stipendio_massimo": 0,
            "stipendio_medio": 0,
            "sopra_media": []
        }
    numero_dipendenti = len(dipendenti)
    stipendio_minimo = min(dipendente['stipendio'] for dipendente in dipendenti)
    stipendio_massimo = max(dipendente['stipendio'] for dipendente in dipendenti)
    stipendio_medio = calcola_stipendio_medio(dipendenti)
    sopra_media = [dipendente for dipendente in dipendenti if dipendente['stipendio'] > stipendio_medio]
    
    risultato = {
        "numero_dipendenti": numero_dipendenti,
        "stipendio_minimo": stipendio_minimo,
        "stipendio_massimo": stipendio_massimo,
        "stipendio_medio": stipendio_medio,
        "sopra_media": sopra_media
    }
    return risultato
