# === MODELLO DEI DATI PER UN LIBRO ===
"""
Questo modulo definisce i modelli di dati per i libri nel database.
Utilizza SQLModel che combina le funzionalità di SQLAlchemy ORM e Pydantic,
permettendo la definizione di modelli per il database con validazione dei dati.
"""

from sqlmodel import Field, SQLModel  # Importa le classi principali di SQLModel
from typing import Annotated  # Per arricchire i tipi con metadati di validazione

class BookBase(SQLModel):  # Classe base per tutti i modelli di libri
    """
    Classe base che definisce i campi comuni per tutti i modelli di libri.
    Questa è una classe astratta che non viene direttamente mappata a una tabella nel database.
    """
    title: str  # Campo obbligatorio per il titolo del libro
    author: str  # Campo obbligatorio per l'autore del libro
    # Campo opzionale per la recensione (valutazione) con validazione:
    # - Può essere un intero da 1 a 5 (inclusivi) o None
    # - Field(ge=1, le=5) imposta i vincoli "greater equal than 1" e "less equal than 5"
    # - Il valore predefinito è None (nessuna recensione)
    review: Annotated[int | None, Field(ge=1, le=5)] = None


class Book(BookBase, table=True):  # Modello per la tabella del database
    """
    Modello principale che rappresenta la tabella 'book' nel database.
    Eredita tutti i campi da BookBase e aggiunge l'ID come chiave primaria.
    L'opzione table=True indica a SQLModel di creare una tabella per questo modello.
    """
    # Campo ID come chiave primaria:
    # - default=None fa sì che il valore venga generato automaticamente se non specificato
    # - primary_key=True lo definisce come chiave primaria della tabella
    id: int = Field(default=None, primary_key=True)


class BookCreate(BookBase):  # Modello per la creazione di un libro
    """
    Modello utilizzato per la validazione dei dati durante la creazione di un nuovo libro.
    Non include l'ID perché viene generato automaticamente dal database.
    Eredita tutti i campi da BookBase senza aggiungerne di nuovi.
    """
    pass


class BookPublic(BookBase):  # Modello per l'output pubblico
    """
    Modello utilizzato per restituire i dati dei libri nelle risposte API.
    Include l'ID insieme a tutti i campi ereditati da BookBase.
    A differenza di Book, questo modello non è mappato a una tabella nel database.
    """
    id: int  # L'ID è obbligatorio per i libri esistenti che vengono restituiti all'utente