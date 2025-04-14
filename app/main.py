#BY ARTIS FROM ARTIS

from fastapi import FastAPI
from routers import books

# === IMPORTAZIONE LIBRERIE PER IL FRONTEND ===
# HTMLResponse: Classe che rappresenta una risposta HTTP in formato HTML
from fastapi.responses import HTMLResponse
# Jinja2Templates: Sistema di template per generare pagine HTML dinamiche
from fastapi.templating import Jinja2Templates
# Request: Classe che rappresenta una richiesta HTTP inviata dal client
from fastapi import Request
# StaticFiles: Per servire file statici (CSS, JavaScript, immagini)
from fastapi.staticfiles import StaticFiles

# === CONFIGURAZIONE DELL'APPLICAZIONE ===
# Creazione dell'istanza principale dell'applicazione FastAPI
app = FastAPI()
# Aggiunta del router dedicato alla gestione dei libri
# Il parametro 'tags' serve per raggruppare le rotte nella documentazione
app.include_router(books.router, tags=["books"])

# === CONFIGURAZIONE FRONT-END ===
# Configurazione del sistema di template Jinja2, specificando la directory dove si trovano i file HTML
templates = Jinja2Templates(directory="app/templates")

# Configurazione per servire i file statici (CSS, JavaScript)
# Questo permette di accedere ai file nella directory "app/static" attraverso l'URL "/static"
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Definizione della rotta principale (homepage)
# Il decoratore @app.get specifica che questa funzione risponde alle richieste GET
# response_class=HTMLResponse indica che restituiremo una pagina HTML
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # Renderizza il template home.html, passando l'oggetto request come parametro
    # (necessario per Jinja2 per generare correttamente i link e i form)
    return templates.TemplateResponse(
        request=request, name="home.html"
    )

# Questo blocco viene eseguito solo quando il file viene eseguito direttamente
# (non quando viene importato da un altro modulo)
if __name__ == "__main__":
    # Uvicorn è un server ASGI (Asynchronous Server Gateway Interface) per applicazioni Python
    import uvicorn
    # Avvia il server con l'app FastAPI
    # Il parametro reload=True permette il ricaricamento automatico quando i file vengono modificati
    # (utile durante lo sviluppo)
    uvicorn.run(app, reload=True)