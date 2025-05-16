"""
Router per la gestione dei libri nell'API.
Questo modulo contiene tutte le rotte per eseguire operazioni CRUD sui libri 
(Create, Read, Update, Delete).
"""

# Import delle librerie e dipendenze necessarie
from fastapi import APIRouter, HTTPException, Path, Form  # Componenti FastAPI per la creazione delle API
from models.review import Review  # Modello per le recensioni
from typing import Annotated  # Per migliorare la tipizzazione
from models.book import Book, BookPublic, BookCreate  # Modelli per i libri
from data.db import SessionDep  # Dipendenza per l'accesso al database
from sqlmodel import select  # Funzione per costruire query SQL


# Creazione del router con prefisso "/books" per tutti gli endpoint
router = APIRouter(prefix="/books")


@router.get("/")
def get_all_books(
        session: SessionDep,  # Iniezione della sessione di database
        sort: bool = False  # Parametro di query opzionale per ordinare i libri
) -> list[BookPublic]:  # Il tipo di ritorno è una lista di oggetti BookPublic
    """Returns the list of available books."""
    # Crea una query SELECT per ottenere tutti i libri dalla tabella 'book'
    statement = select(Book)
    # Esegue la query e converte il risultato in una lista di oggetti Book
    books = session.exec(statement).all()
    
    if sort:
        # Se il parametro sort è True, ordina i libri per valore di review
        # key=lambda book: book.review definisce la chiave di ordinamento
        return sorted(books, key=lambda book: book.review)
    else:
        # Altrimenti, restituisce i libri nell'ordine originale
        return books


@router.post("/")
def add_book(book: BookCreate, session: SessionDep):
    """Adds a new book."""
    # Converte il modello BookCreate in un oggetto Book per il database
    # model_validate garantisce che tutti i dati rispettino i vincoli definiti nel modello
    validated_book = Book.model_validate(book)
    
    # Aggiunge il nuovo libro alla sessione di database (staging)
    session.add(validated_book)
    
    # Salva le modifiche nel database (commit)
    # Questo assegna anche un ID al nuovo libro
    session.commit()
    
    # Restituisce un messaggio di conferma
    return "Book successfully added."


@router.post("_form/")
def add_book_from_form(
        book: Annotated[BookCreate, Form()],  # Ottiene i dati dal form HTML
        session: SessionDep,  # Iniezione della sessione di database
):
    """Adds a new book"""
    # Simile a add_book, ma riceve i dati da un form HTML invece che da JSON
    validated_book = Book.model_validate(book)
    
    # Aggiunge il libro alla sessione
    session.add(validated_book)
    
    # Salva le modifiche nel database
    session.commit()
    
    # Restituisce un messaggio di conferma
    return "Book successfully added."


@router.delete("/")
def delete_all_books(session: SessionDep):
    """Deletes all books."""
    # Crea una query SELECT per ottenere tutti i libri
    statement = select(Book)
    
    # Esegue la query con .delete() che elimina tutti i record selezionati
    # Questa è un'operazione più efficiente rispetto a eliminare i libri uno per uno
    session.exec(statement).delete()
    
    # Salva le modifiche nel database
    session.commit()
    
    # Restituisce un messaggio di conferma
    return "All books successfully deleted"


@router.delete("/{id}")
def delete_book(
        session: SessionDep,  # Iniezione della sessione di database
        id: Annotated[int, Path(description="The ID of the book to delete")]  # ID del libro come parametro di percorso
):
    """Deletes the book with the given ID."""
    # Ottiene il libro con l'ID specificato dal database
    # session.get è un metodo che cerca un oggetto per chiave primaria
    book = session.get(Book, id)
    
    # Se il libro non esiste, solleva un'eccezione 404 Not Found
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Elimina il libro dalla sessione
    session.delete(book)
    
    # Salva le modifiche nel database
    session.commit()
    
    # Restituisce un messaggio di conferma
    return "Book successfully deleted"


@router.get("/{id}")
def get_book_by_id(
        session: SessionDep,  # Iniezione della sessione di database
        id: Annotated[int, Path(description="The ID of the book to get")]  # ID del libro come parametro di percorso
) -> BookPublic:  # Il tipo di ritorno è un oggetto BookPublic
    """Returns the book with the given id."""
    # Ottiene il libro con l'ID specificato
    book = session.get(Book, id)
    
    # Se il libro non esiste, solleva un'eccezione 404 Not Found
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Restituisce il libro (viene automaticamente convertito in BookPublic)
    return book


@router.post("/{id}/review")
def add_review(
        session: SessionDep,  # Iniezione della sessione di database
        id: Annotated[int, Path(description="The ID of the book to which add the review")],  # ID del libro
        review: Review  # Oggetto Review dal corpo della richiesta
):
    """Adds a review to the book with the given ID."""
    # Ottiene il libro con l'ID specificato
    book = session.get(Book, id)
    
    # Se il libro non esiste, solleva un'eccezione 404 Not Found
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Aggiorna il campo review del libro con il valore dalla richiesta
    book.review = review.review
    
    # Salva le modifiche nel database
    # Non è necessario chiamare session.add() perché l'oggetto book
    # è già stato caricato dalla sessione
    session.commit()
    
    # Restituisce un messaggio di conferma
    return "Review successfully added"


@router.put("/{id}")
def update_book(
        session: SessionDep,  # Iniezione della sessione di database
        id: Annotated[int, Path(description="The ID of the book to update")],  # ID del libro
        new_book: BookCreate  # Nuovi dati del libro dal corpo della richiesta
):
    """Updates the book with the given ID."""
    # Ottiene il libro esistente con l'ID specificato
    book = session.get(Book, id)
    
    # Se il libro non esiste, solleva un'eccezione 404 Not Found
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Aggiorna i campi del libro con i nuovi valori
    # Nota: in un'applicazione più grande, potresti usare un approccio più scalabile
    # come book.model_copy(update=new_book.model_dump()) o un ciclo for sui campi
    book.title = new_book.title
    book.author = new_book.author
    book.review = new_book.review
    
    # Salva le modifiche nel database
    # Non è necessario chiamare session.add() perché l'oggetto book
    # è già stato caricato dalla sessione
    session.commit()
    
    # Restituisce un messaggio di conferma
    return "Book successfully updated"