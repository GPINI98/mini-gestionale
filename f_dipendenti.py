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
        if dipendente_max is None or dipendente_max ['stipendio'] < dipendente ['stipendio']:
            dipendente_max = dipendente
    return dipendente_max

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
