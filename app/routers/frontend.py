"""
Router per le pagine frontend dell'applicazione.
Gestisce il rendering delle pagine HTML e l'interazione con il database per mostrare i dati nelle pagine.
"""

# Import delle librerie e dipendenze necessarie
from fastapi import APIRouter, Request  # Componenti FastAPI per il routing e l'accesso ai dati della richiesta
from fastapi.responses import HTMLResponse  # Per restituire risposte HTML
from fastapi.templating import Jinja2Templates  # Per il rendering dei template HTML
from data.db import SessionDep  # Dipendenza per l'accesso al database
from sqlmodel import select  # Funzione per costruire query SQL
from models.book import Book  # Modello per i libri


# Configurazione del sistema di template Jinja2
# Specifica la directory dove si trovano i file HTML
templates = Jinja2Templates(directory="app/templates")

# Creazione del router per le pagine frontend
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    """
    Gestisce la pagina principale dell'applicazione.
    Non interagisce con il database, ma restituisce un template HTML con testo statico.
    
    Args:
        request: L'oggetto Request di FastAPI, necessario per il rendering del template
        
    Returns:
        HTMLResponse: La pagina HTML renderizzata
    """
    # Dati di esempio da passare al template
    text = {
        "title": "Welcome to the library",
        "content": "Have you ever seen this place?"
    }
    
    # Renderizza il template 'home.html' passando l'oggetto request e i dati text come contesto
    return templates.TemplateResponse(
        request=request, name="home.html",
        context={"text": text}
    )

@router.get("/book_list", response_class=HTMLResponse)
def show_book_list(request: Request, session: SessionDep):
    """
    Mostra la lista dei libri presenti nel database.
    Interagisce con il database per ottenere tutti i libri e passarli al template.
    
    Args:
        request: L'oggetto Request di FastAPI
        session: Sessione del database, iniettata automaticamente da FastAPI
        
    Returns:
        HTMLResponse: La pagina HTML con la lista dei libri
    """
    # Crea una query SELECT per ottenere tutti i libri dal database
    statement = select(Book)
    
    # Esegue la query e converte il risultato in una lista di oggetti Book
    books = session.exec(statement).all()
    
    # Prepara il contesto con la lista dei libri da passare al template
    context = {"books": books}
    
    # Renderizza il template 'list.html' con i libri nel contesto
    return templates.TemplateResponse(
        request=request, name="list.html", context=context
    )


@router.get("/add_book", response_class=HTMLResponse)
def add_book_form(request: Request):
    """
    Mostra il form per aggiungere un nuovo libro.
    Non interagisce con il database, ma restituisce un template HTML con il form.
    Il form invia i dati alla rotta POST /books_form/ definita in books.py.
    
    Args:
        request: L'oggetto Request di FastAPI
        
    Returns:
        HTMLResponse: La pagina HTML con il form per aggiungere un libro
    """
    # Renderizza il template 'add.html' senza dati aggiuntivi nel contesto
    return templates.TemplateResponse(
        request=request, name="add.html"
    )