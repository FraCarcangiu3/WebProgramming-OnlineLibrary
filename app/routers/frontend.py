from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
# === IMPORTAZIONE LIBRERIE PER IL FRONTEND ===
# HTMLResponse: Classe che rappresenta una risposta HTTP in formato HTML
from fastapi.responses import HTMLResponse
# Jinja2Templates: Sistema di template per generare pagine HTML dinamiche
from fastapi.templating import Jinja2Templates
# Request: Classe che rappresenta una richiesta HTTP inviata dal client
from fastapi import Request
# StaticFiles: Per servire file statici (CSS, JavaScript, immagini)
from fastapi.staticfiles import StaticFiles


from data.books import books



router = APIRouter() # Creazione del router per la gestione delle rotte frontend
templates = Jinja2Templates(directory="app/templates") # Configurazione del motore di template Jinja2


# Configurazione per servire i file statici (CSS, JavaScript)
# Questo permette di accedere ai file nella directory "app/static" attraverso l'URL "/static"
router.mount("/static", StaticFiles(directory="app/static"), name="static")



@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    # Renderizza il template home.html, passando l'oggetto request come parametro
    # (necessario per Jinja2 per generare correttamente i link e i form)

    text = {
        "title": "Welcome to the Library Online",
        "content": "This is the home page of the Library Online application."
    }
    return templates.TemplateResponse(
        request=request, name="home.html",
        context={"text": text} # Passa il testo come variabile al template,
        # è un dizionario che ci aiuta anche per la sicurezza # (per evitare attacchi XSS, Cross-Site Scripting)
    )


@router.get("/book_list", response_class=HTMLResponse)
def show_book_list(request: Request):
    # Renderizza il template list.html, passando l'oggetto request come parametro
    context = {"books": list(books.values())} # Passa la lista dei libri come variabile al template
    return templates.TemplateResponse(
        request=request, name="list.html",
        context=context # Passa l'oggetto
    )

@router.get("/add_book", response_class=HTMLResponse)
def add_book_form(request: Request):
    # Renderizza il template add_book.html, passando l'oggetto request come parametro
    return templates.TemplateResponse(
        request=request, name="add.html",    )