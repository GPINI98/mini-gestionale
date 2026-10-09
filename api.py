from fastapi import FastAPI, HTTPException
import database
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

class Dipendente(BaseModel):
    nome: str = Field(min_length=1)
    eta: int = Field(gt=0)
    stipendio: float = Field(gt=0)

    @field_validator("nome")
    @classmethod
    def nome_non_vuoto(cls, valore):
        if not valore.strip():
            raise ValueError("Il nome non può essere vuoto o contenere solo spazi")
        return valore

class DipendenteResponse(BaseModel):
    id: int
    nome: str = Field(min_length=1)
    eta: int = Field(gt=0)
    stipendio: float = Field(gt=0)

    @field_validator("nome")
    @classmethod
    def nome_non_vuoto(cls, valore):
        if not valore.strip():
            raise ValueError("Il nome non può essere vuoto o contenere solo spazi")
        return valore

@app.get("/dipendenti", response_model=list[DipendenteResponse]) 
def get_dipendenti():
    dipendenti =database.mostra_dipendenti()
    risultato = []
    for dipendente in dipendenti:
        risultato.append({
            "id": dipendente[0],
            "nome": dipendente[1],
            "eta": dipendente[2],
            "stipendio": dipendente[3]
        })
    return risultato

@app.post("/dipendenti", status_code=201, response_model=DipendenteResponse)
def crea_dipendente(dipendente: Dipendente):
    id_dipendente = database.inserisci_dipendente(dipendente.nome, dipendente.eta, dipendente.stipendio)
    return {"id": id_dipendente, "nome": dipendente.nome, "eta": dipendente.eta, "stipendio": dipendente.stipendio}

@app.get("/dipendenti/cerca", response_model=list[DipendenteResponse])
def cerca_dipendente(nome: str):
    dipendenti = database.cerca_dipendente(nome)
    if not dipendenti:
        raise HTTPException(
            status_code=404,
            detail="Dipendente non trovato"
        )
    risultato = []
    for dipendente in dipendenti:
        risultato.append({
            "id": dipendente[0],
            "nome": dipendente[1],
            "eta": dipendente[2],
            "stipendio": dipendente[3]
        })
    return risultato


@app.get("/dipendenti/{id_dipendente}", response_model=DipendenteResponse) 
def get_dipendente(id_dipendente: int):
    dipendente = database.cerca_dipendente_id(id_dipendente)
    if not dipendente:
        raise HTTPException(status_code=404, detail="Dipendente non trovato")
    return {
        "id": dipendente[0],
        "nome": dipendente[1],
        "eta": dipendente[2],
        "stipendio": dipendente[3]
    }

@app.delete("/dipendenti/{id_dipendente}", status_code=204)
def elimina_dipendente(id_dipendente: int):
    dipendente = database.elimina_dipendente(id_dipendente)
    if not dipendente:
        raise HTTPException(
            status_code=404,
            detail="Dipendente non trovato"
        )

@app.put("/dipendenti/{id_dipendente}")
def modifica_dipendente(id_dipendente: int, dipendente: Dipendente):
    dipendente_esistente = database.cerca_dipendente_id(id_dipendente)
    if not dipendente_esistente:
        raise HTTPException(
            status_code=404,
            detail="Dipendente non trovato"
        )
    database.modifica_dipendente(id_dipendente, dipendente.nome, dipendente.eta, dipendente.stipendio)
    return {"id": id_dipendente, "nome": dipendente.nome, "eta": dipendente.eta, "stipendio": dipendente.stipendio}

