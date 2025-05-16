"""
Questo modulo gestisce la configurazione, l'inizializzazione e l'accesso al database SQLite.
Utilizza SQLModel per definire le strutture delle tabelle e gestire le operazioni sul database.
"""

# Import delle librerie necessarie
from sqlmodel import create_engine, SQLModel, Session  # SQLModel per l'ORM, create_engine per configurare la connessione, Session per gestire le transazioni
from typing import Annotated  # Per la dependency injection tipizzata
from fastapi import Depends  # Per l'iniezione delle dipendenze in FastAPI
from faker import Faker  # Libreria per generare dati fittizi realistici
import os  # Per operazioni sul filesystem
from models.book import Book  # Importa il modello Book definito in models/book.py


# Configurazione del database SQLite
sqlite_file_name = "app/data/database.db"  # Percorso del file del database
sqlite_url = f"sqlite:///{sqlite_file_name}"  # URL di connessione SQLAlchemy per SQLite
connect_args = {"check_same_thread": False}  # Permette l'accesso al database da thread diversi (necessario per FastAPI)
# Creazione dell'engine di database - il cuore della connessione al DB
# echo=True fa sì che le query SQL vengano stampate nella console (utile per debug)
engine = create_engine(sqlite_url, connect_args=connect_args,
                       echo=True)


def init_database():
    """
    Inizializza il database: crea le tabelle se non esistono e popola il DB con dati fittizi se è vuoto.
    Questa funzione viene chiamata all'avvio dell'applicazione dal gestore del ciclo di vita in main.py.
    """
    # Verifica se il file del database esiste già
    ds_exists = os.path.isfile(sqlite_file_name)
    # Crea tutte le tabelle definite nei modelli SQLModel (in questo caso, la tabella 'book')
    # Questo non sovrascrive le tabelle esistenti
    SQLModel.metadata.create_all(engine)
    
    # Se il database non esisteva prima, popolalo con dati di esempio
    if not ds_exists:
        # Crea un'istanza di Faker con locale italiano per generare dati realistici
        f = Faker("it_IT")
        # Apre una sessione di database per eseguire operazioni
        with Session(engine) as session:
            # Crea 10 libri di esempio
            for i in range(10):
                # Crea un nuovo oggetto Book con dati casuali
                book = Book(
                    title=f.sentence(nb_words=5),  # Genera una frase casuale come titolo
                    author=f.name(),  # Genera un nome casuale come autore
                    review=f.pyint(1, 5)  # Genera un numero intero casuale tra 1 e 5 come recensione
                )
                # Aggiunge il libro alla sessione (fase di staging)
                session.add(book)
            # Conferma tutte le modifiche e le salva nel database (fase di commit)
            session.commit()


def get_session():
    """
    Generator function per fornire una sessione di database.
    Usata come dependency injection nelle rotte FastAPI.
    Il pattern 'yield' garantisce che la sessione venga chiusa correttamente
    anche in caso di eccezioni durante la gestione della richiesta.
    """
    # Crea una nuova sessione utilizzando il context manager
    with Session(engine) as session:
        # Restituisce la sessione alla funzione che la richiede
        yield session
        # Quando la funzione che utilizza la sessione termina,
        # l'esecuzione riprende qui e la sessione viene chiusa automaticamente


# Definizione di una dipendenza tipizzata per l'iniezione di Session nei router FastAPI
# Questo permette di utilizzare facilmente la sessione nelle funzioni di gestione delle rotte
SessionDep = Annotated[Session, Depends(get_session)]