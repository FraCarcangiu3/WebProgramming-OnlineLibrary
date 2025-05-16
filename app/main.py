#BY ARTIS FROM ARTIS

# Punto di ingresso principale dell'applicazione FastAPI
# Configura il server, i router e il ciclo di vita dell'applicazione

# Import delle librerie e dipendenze necessarie
from fastapi import FastAPI  # Il framework FastAPI
from routers import books, frontend  # I router dell'applicazione
from fastapi.staticfiles import StaticFiles  # Per servire file statici (CSS, JS, immagini)
from data.db import init_database  # Funzione per inizializzare il database
from contextlib import asynccontextmanager  # Per gestire il ciclo di vita asincrono

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Funzione di gestione del ciclo di vita dell'applicazione.
    Viene eseguita all'avvio e alla chiusura dell'applicazione.
    
    Questo pattern permette di:
    - Inizializzare risorse prima che l'app cominci a rispondere alle richieste
    - Liberare risorse quando l'app si chiude
    - Gestire connessioni a database, code di messaggi, ecc.
    
    Args:
        app: L'istanza FastAPI dell'applicazione
    """
    # Codice eseguito all'avvio dell'applicazione
    print("Initializing database...")
    
    # Inizializza il database (crea tabelle e dati di esempio se necessario)
    # Questa funzione è definita in data/db.py
    init_database()
    
    print("Database initialized successfully!")
    
    # Yield per far proseguire l'applicazione con la gestione delle richieste
    yield
    
    # Codice eseguito alla chiusura dell'applicazione
    # Qui potresti chiudere connessioni, liberare risorse, ecc.
    print("Shutting down application...")


# Crea l'istanza dell'applicazione FastAPI con il gestore del ciclo di vita
app = FastAPI(lifespan=lifespan)

# Registra i router dell'applicazione con i rispettivi tag per la documentazione
app.include_router(books.router, tags=["Books"])  # Router per le API dei libri
app.include_router(frontend.router, tags=["Frontend"])  # Router per le pagine frontend

# Monta la cartella "static" per servire file statici
# Questo rende disponibili i file CSS, JavaScript e immagini
# all'URL /static/... per il browser
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Questo blocco viene eseguito solo quando il file viene eseguito direttamente
# (non quando viene importato da un altro modulo)
if __name__ == "__main__":
    # Importa uvicorn per avviare il server ASGI
    import uvicorn
    
    # Avvia il server con l'app FastAPI
    # reload=True abilita il ricaricamento automatico quando i file vengono modificati
    # Utile durante lo sviluppo per vedere le modifiche senza riavviare manualmente
    uvicorn.run(app, reload=True)