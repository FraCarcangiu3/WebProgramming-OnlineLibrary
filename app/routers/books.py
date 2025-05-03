# === FILE PER LA GESTIONE DELLE API DEI LIBRI ===
# Questo file definisce tutte le rotte (endpoint) relative alla gestione dei libri
# con percorso base /books

# Importazioni per la gestione degli errori
from fastapi.exceptions import RequestValidationError
from requests import RequestException

# Importazioni dei modelli dati e dei "database"
from models.book import Book
from models.review import Review
from data.books import books

# Importazioni delle utility di FastAPI
# - APIRouter: Permette di organizzare le rotte in gruppi logici
# - HTTPException: Per generare errori HTTP significativi
# - Path: Per validare e documentare i parametri di percorso
from fastapi import APIRouter, HTTPException, Path, Form, Query
# ValidationError: Per gestire errori di validazione dei dati inviati
from pydantic import ValidationError
# Annotated: Per aggiungere metadati ai tipi (usato per documentazione e validazione)
from typing import Annotated

# === CONFIGURAZIONE DEL ROUTER ===
# Creazione del router per la gestione dei libri
# prefix="/books": Specifica che tutte le rotte definite avranno il prefisso /books
# (es. /books/, /books/1, ecc.)
router = APIRouter(prefix="/books")

# === DEFINIZIONE DELLE ROTTE (ENDPOINTS) ===

# --- GET: Ottieni tutti i libri ---
@router.get("/")
def get_all_books(
        sort: bool = False  # Parametro opzionale per ordinare i libri per recensione
) -> list[Book]:  # La funzione restituirà una lista di oggetti Book
    if sort:
        # Se il parametro sort è True, ordina i libri per valore della recensione
        # Utilizza una funzione di ordinamento che gestisce i valori None (ponendoli all'inizio)
        return sorted(books.values(), key=lambda book: book.review if book.review is not None else -1)

    # Altrimenti, restituisce tutti i libri senza ordinamento
    # Converte i valori del dizionario 'books' in una lista
    return list(books.values())

# --- GET: Ottieni un libro specifico tramite ID ---
@router.get("/{id}")  # {id} è un parametro di percorso (URL)
def get_book_by_id(id: Annotated[int, Path(description="L'ID del libro da cercare")]) -> Book:
    """
    Restituisce il libro con l'ID specificato
    """
    try:
        return books[id]  # Cerca il libro nel dizionario usando l'ID come chiave
    except KeyError:
        # Se il libro non esiste (chiave non trovata), genera un errore 404 (Not Found)
        raise HTTPException(status_code=404, detail="Libro non trovato")

# --- POST: Aggiungi una recensione a un libro esistente ---
@router.post("/{id}/review")
def add_review(
    id: Annotated[int, Path(description="L'ID del libro da recensire")],
    review: Review  # Questo parametro viene estratto automaticamente dal corpo della richiesta JSON
):
    """
    Aggiunge una recensione (valutazione da 1 a 5) al libro con l'ID specificato
    """
    try:
        # Aggiorna il campo review del libro con il valore fornito
        books[id].review = review.review
        return "Recensione aggiunta con successo"
    except KeyError:
        # Se il libro non esiste, genera un errore 404
        raise HTTPException(status_code=404, detail="Libro non trovato")

# --- POST: Aggiungi un nuovo libro ---
@router.post("/")
def add_book(book: Book):  # L'oggetto Book viene deserializzato automaticamente dal JSON
    """
    Aggiunge un nuovo libro alla collezione
    """
    # Verifica se esiste già un libro con lo stesso ID
    if book.id in books:
        # Se esiste, genera un errore 403 (Forbidden)
        raise HTTPException(status_code=403, detail="Esiste già un libro con questo ID")
    
    # Altrimenti, aggiunge il libro al dizionario
    books[book.id] = book
    return "Libro aggiunto con successo"

# --- PUT: Aggiorna un libro esistente ---
@router.put("/{id}")
def update_book(
    id: Annotated[int, Path(description="L'ID del libro da aggiornare")],
    book: Book  # Dati aggiornati del libro dal corpo della richiesta
):
    """
    Aggiorna i dati di un libro esistente
    """
    # Verifica se il libro esiste
    if not id in books:
        raise HTTPException(status_code=404, detail="Libro non trovato")
    
    # Aggiorna i dati del libro
    books[id] = book
    return "Libro aggiornato con successo"

# --- DELETE: Elimina tutti i libri ---
@router.delete("/")
def delete_all_book():
    """
    Elimina tutti i libri dalla collezione
    """
    books.clear()  # Svuota il dizionario
    return "Tutti i libri sono stati eliminati con successo"

# --- DELETE: Elimina un libro specifico ---
@router.delete("/{id}")
def delete_book(
    id: Annotated[int, Path(description="L'ID del libro da eliminare")]
):
    """
    Elimina il libro con l'ID specificato
    """
    try:
        del books[id]  # Elimina l'elemento dal dizionario
        return "Libro eliminato con successo"
    except KeyError:
        # Se il libro non esiste, genera un errore 404
        raise HTTPException(status_code=404, detail="Libro non trovato")



@router.post("books_form/")
def add_book_from_form(
    book: Annotated[Book, Form()]
    # Utilizza Form per estrarre i dati dal corpo della richiesta,
    # Form() è un helper di FastAPI che permette di estrarre i dati da un form HTML
):
    """
    Aggiunge un nuovo libro alla collezione
    """
    # Verifica se esiste già un libro con lo stesso ID
    if book.id in books:
        # Se esiste, genera un errore 403 (Forbidden)
        raise HTTPException(status_code=403, detail="Esiste già un libro con questo ID")

    # Altrimenti, aggiunge il libro al dizionario
    books[book.id] = book
    return "Libro aggiunto con successo"