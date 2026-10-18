from fastapi import FastAPI, HTTPException
import database
import sqlite3
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
    try:
        dipendenti =database.mostra_dipendenti()
    except sqlite3.Error as errore:
        raise HTTPException(
            status_code=500,
            detail="Errore durante il recupero dei dipendenti"
        ) from errore
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
    try:
        id_dipendente = database.inserisci_dipendente(
            dipendente.nome,
            dipendente.eta,
            dipendente.stipendio
        )
    except sqlite3.Error as errore:
        raise HTTPException(
            status_code=500,
            detail="Errore durante il salvataggio del dipendente"
        ) from errore

    return {"id": id_dipendente, "nome": dipendente.nome, "eta": dipendente.eta, "stipendio": dipendente.stipendio}

@app.get("/dipendenti/stipendio_medio")
def trova_stipendio_medio():
    try:
        stipendio_medio = database.trova_stipendio_medio()
    except sqlite3.Error as errore:
        raise HTTPException(
            status_code=500,
            detail="Errore durante il calcolo dello stipendio medio"
        ) from errore
    if stipendio_medio is None:
        return {"stipendio_medio": "dipendenti non presenti"}
    return {"stipendio_medio": float(f"{stipendio_medio:.2f}")}

@app.get("/dipendenti/cerca", response_model=list[DipendenteResponse])
def cerca_dipendente(nome: str):
    try:
        dipendenti = database.cerca_dipendente(nome)
    except sqlite3.Error as errore:
        raise HTTPException(
            status_code=500,
            detail="Errore durante la ricerca del dipendente"
        ) from errore
    
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
    try:
        dipendente = database.cerca_dipendente_id(id_dipendente)
    except sqlite3.Error as errore:
        raise HTTPException(
            status_code=500,
            detail="Errore durante la ricerca del dipendente"
        ) from errore
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
    try:
        dipendente = database.elimina_dipendente(id_dipendente)
    except sqlite3.Error as errore:
        raise HTTPException(
            status_code=500,
            detail="Errore durante l'eliminazione del dipendente"
        ) from errore
    if not dipendente:
        raise HTTPException(
            status_code=404,
            detail="Dipendente non trovato"
        )

@app.put("/dipendenti/{id_dipendente}")
def modifica_dipendente(id_dipendente: int, dipendente: Dipendente):
    try:
        dipendente_esistente = database.cerca_dipendente_id(id_dipendente)
    except sqlite3.Error as errore:
        raise HTTPException(
            status_code=500,
            detail="Errore durante la ricerca del dipendente"
        ) from errore    
    if not dipendente_esistente:
        raise HTTPException(
            status_code=404,
            detail="Dipendente non trovato"
        )
    try:
        dipendente_modificato = database.modifica_dipendente(id_dipendente, dipendente.nome, dipendente.eta, dipendente.stipendio)
    except sqlite3.Error as errore:
        raise HTTPException(
            status_code=500,
            detail="Errore durante la modifica del dipendente"
        ) from errore
    if not dipendente_modificato:
        raise HTTPException(
            status_code=404,
            detail="Dipendente non trovato"
        )
    return {"id": id_dipendente, "nome": dipendente.nome, "eta": dipendente.eta, "stipendio": dipendente.stipendio}