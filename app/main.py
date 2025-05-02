#BY ARTIS FROM ARTIS

from fastapi import FastAPI
from routers import books, frontend
from fastapi.staticfiles import StaticFiles



app = FastAPI()
app.include_router(books.router, tags=["Books"])
app.include_router(frontend.router, tags=["Frontend"])

# Monta la cartella "static" per servire file statici (CSS, JavaScript, immagini)
app.mount("/static", StaticFiles(directory="app/static"), name="static")








# Questo blocco viene eseguito solo quando il file viene eseguito direttamente
# (non quando viene importato da un altro modulo)
if __name__ == "__main__":
    # Uvicorn è un server ASGI (Asynchronous Server Gateway Interface) per applicazioni Python
    import uvicorn
    # Avvia il server con l'app FastAPI
    # Il parametro reload=True permette il ricaricamento automatico quando i file vengono modificati
    # (utile durante lo sviluppo)
    uvicorn.run(app, reload=True)