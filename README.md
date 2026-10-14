# Mini Gestionale Dipendenti

## Funzionalità

- Visualizzazione, ricerca e gestione dei dipendenti
- Inserimento, modifica ed eliminazione dei dipendenti
- Ricerca del dipendente con lo stipendio più alto
- Calcolo dello stipendio medio
- Validazione degli input e dei dati ricevuti dall'API
- Gestione degli errori HTTP
- Test automatici delle funzioni e degli endpoint REST

## Tecnologie

- Python
- SQLite e SQL
- FastAPI
- Uvicorn
- Pytest
- Git e GitHub

## Installazione 

Per installare le dipendenze:
python -m pip install -r requirements.txt

## Avvio

Per eseguire il programma:
python main.py

## Test

Per eseguire i test automatici:
python -m pytest

## API REST

Per eseguire le API REST:
python -m uvicorn api:app --reload

## FastAPI 

Per visualizzare e provare gli endpoint tramite FastAPI aprire sul browser:
http://127.0.0.1:8000/docs


## Obiettivo

Il progetto è stato realizzato per mettere in pratica i principali concetti della programmazione Python, l'interazione con un database relazionale, lo sviluppo di API REST e la verifica del codice tramite test automatici.

## Struttura del progetto

- main.py → gestisce il menu principale e richiama le funzioni del programma.
- database.py → gestisce il database SQLite e le operazioni sui dipendenti.
- validazione.py → gestisce la validazione degli input inseriti dall'utente.
- api.py → espone le funzionalità tramite API REST.
- tests/ → contiene i test automatici per verificare il corretto funzionamento del programma.
