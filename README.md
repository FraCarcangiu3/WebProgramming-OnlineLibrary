# Laboratorio di Programmazione Web - Libreria Online: Guida Passo dopo Passo

Benvenuto al corso introduttivo di Programmazione Web! 📚 Questa guida completa ti insegnerà come costruire da zero un'applicazione web per gestire una libreria online. Il progetto è pensato appositamente per principianti che vogliono imparare le basi dello sviluppo web moderno.

## Indice dei contenuti

### Introduzione
1. [Introduzione e obiettivi](#introduzione-e-obiettivi)
2. [Prerequisiti](#prerequisiti)
3. [Tecnologie utilizzate](#tecnologie-utilizzate)
4. [Struttura del progetto](#struttura-del-progetto)

### Parte 1: Il Backend (Server)
5. [Back-end con FastAPI](#back-end-con-fastapi)
   - [Modelli dati (SQLModel)](#modelli-dati-sqlmodel)
   - [Database SQLite](#database-sqlite)
   - [API RESTful](#api-approutersbookspy)
   - [Punto di ingresso](#punto-di-ingresso-appmainpy)

### Parte 2: Il Frontend (Client)
6. [Front-end: HTML, CSS e JavaScript](#front-end-con-html-css-e-javascript)
   - [HTML: La struttura](#html-apptemplateshomelhtml)
   - [CSS: Lo stile](#css-appstaticcssfilecss)
   - [JavaScript: Il comportamento](#javascript-appstaticjsmainjs)
7. [Separazione delle preoccupazioni](#separazione-delle-preoccupazioni-una-best-practice)

### Parte 3: Integrazione e Utilizzo
8. [API e comunicazione client-server](#api-e-comunicazione-client-server)
9. [Come eseguire l'applicazione](#come-eseguire-lapplicazione)
10. [Esercizi proposti](#esercizi-proposti)
11. [Guida alla risoluzione dei problemi comuni](#guida-alla-risoluzione-dei-problemi-comuni)

## Introduzione e obiettivi

Questa applicazione è un esempio pratico di un'applicazione web full-stack che gestisce una collezione di libri. È pensata come strumento didattico per imparare i principi fondamentali dello sviluppo web.

### Cosa imparerai:

- Come strutturare un'applicazione web moderna
- Come creare API REST con FastAPI
- Come connettere un front-end a un back-end
- Come implementare le operazioni CRUD (Create, Read, Update, Delete)
- Come gestire i dati e la loro validazione usando SQLModel
- Come creare un'interfaccia utente interattiva
- Come implementare un database SQLite persistente

### Funzionalità dell'applicazione:

- 📝 Visualizzare l'elenco dei libri
- ➕ Aggiungere nuovi libri
- 🔄 Modificare libri esistenti
- 🗑️ Eliminare libri
- ⭐ Aggiungere recensioni ai libri (da 1 a 5 stelle)
- 🔍 Ordinare i libri per valutazione

## Prerequisiti

Prima di iniziare, assicurati di avere:

- **Python 3.7 o superiore** installato
- **Un editor di codice** (come Visual Studio Code, PyCharm, o anche un semplice editor di testo)
- **Conoscenze di base** di HTML, CSS e JavaScript
- **Familiarità di base** con i concetti di programmazione e database

Non preoccuparti se non sei esperto in tutte queste tecnologie: questa guida è pensata per spiegare ogni passaggio in modo chiaro.

## Tecnologie utilizzate

In questo progetto utilizziamo diverse tecnologie, divise tra la parte server (backend) e la parte client (frontend).

### 🖥️ Back-end (lato server)

- **Python**: Un linguaggio di programmazione versatile e facile da imparare, popolare per lo sviluppo web.
  - *Perché lo usiamo?* Python è facile da leggere e scrivere, ha una sintassi chiara ed è perfetto per i principianti.

- **FastAPI**: Un framework moderno e veloce per la creazione di API web con Python.
  - *Perché lo usiamo?* FastAPI è facile da usare, veloce, e include automaticamente la documentazione delle API.

- **SQLModel**: Una libreria per interagire con database SQL attraverso modelli Python.
  - *Perché lo usiamo?* SQLModel combina la potenza di SQLAlchemy per le operazioni database con la semplicità di Pydantic per la validazione dei dati.

- **SQLite**: Un motore di database relazionale leggero.
  - *Perché lo usiamo?* SQLite è facile da configurare, non richiede un server separato e archivia i dati in un singolo file.

- **Faker**: Una libreria per generare dati realistici di esempio.
  - *Perché lo usiamo?* Faker ci permette di popolare il database con dati di prova realistici.

- **Uvicorn**: Un server ASGI (Asynchronous Server Gateway Interface) per eseguire l'applicazione FastAPI.
  - *Perché lo usiamo?* Uvicorn è veloce e facile da configurare per eseguire la nostra applicazione web.

### 🎨 Front-end (lato client)

- **HTML5**: Il linguaggio standard per creare pagine web.
  - *Perché lo usiamo?* HTML5 fornisce la struttura di base per la nostra interfaccia utente.

- **CSS3**: Il linguaggio usato per definire lo stile e l'aspetto delle pagine web.
  - *Perché lo usiamo?* CSS3 permette di creare un'interfaccia utente attraente e responsive.

- **JavaScript**: Il linguaggio di programmazione per rendere interattive le pagine web.
  - *Perché lo usiamo?* JavaScript ci permette di aggiungere interattività e comunicare con il server.

### 🔄 Architettura dell'applicazione

La nostra applicazione segue l'architettura **client-server**:
- Il **server** (back-end) gestisce i dati e fornisce API
- Il **client** (front-end) mostra l'interfaccia utente e interagisce con l'utente
- La comunicazione tra client e server avviene tramite **API REST**
- I dati sono memorizzati in un **database SQLite**

#### Cos'è un'API REST?

API REST (Representational State Transfer) è un'architettura per la creazione di servizi web. Ecco i concetti chiave:

1. **Risorse**: Nell'API, una risorsa è qualsiasi cosa a cui possiamo accedere tramite un URL (nel nostro caso, i libri).

2. **Metodi HTTP**: Utilizziamo diversi metodi HTTP per operare sulle risorse:
   - **GET**: Per ottenere dati (es. recuperare la lista dei libri)
   - **POST**: Per creare nuovi dati (es. aggiungere un nuovo libro)
   - **PUT**: Per aggiornare dati esistenti (es. modificare un libro)
   - **DELETE**: Per eliminare dati (es. rimuovere un libro)

3. **Formato JSON**: I dati vengono scambiati in formato JSON (JavaScript Object Notation), un formato leggero e facile da leggere.

## Struttura del progetto

```
lab2025/
├── app/
│   ├── data/
│   │   ├── db.py              # Configurazione del database SQLite
│   │   └── database.db        # File del database SQLite
│   ├── models/
│   │   ├── book.py            # Modello per i libri
│   │   └── review.py          # Modello per le recensioni
│   ├── routers/
│   │   ├── books.py           # Definizione delle API per i libri
│   │   └── frontend.py        # Gestione delle pagine frontend
│   ├── static/                # Directory per i file statici
│   │   ├── css/
│   │   │   └── style.css      # Stili CSS separati
│   │   └── js/
│   │       └── main.js        # Script JavaScript
│   ├── templates/
│   │   ├── home.html          # Pagina principale
│   │   └── list.html          # Pagina di elenco dei libri
│   ├── __init__.py
│   └── main.py                # Punto di ingresso dell'applicazione
├── requirements.txt           # Dipendenze del progetto
└── README.md                  # Questa guida
```

Questa struttura segue un pattern comune per le applicazioni web:

- **app/**: La directory principale che contiene tutto il codice dell'applicazione
  - **data/**: Contiene la configurazione del database e il file del database stesso
  - **models/**: Definisce la struttura dei dati utilizzati dall'applicazione
  - **routers/**: Contiene la logica delle API e delle rotte dell'applicazione
  - **static/**: Contiene i file statici (CSS, JavaScript, immagini)
    - **css/**: Contiene i fogli di stile CSS
    - **js/**: Contiene gli script JavaScript
  - **templates/**: Contiene i file HTML per l'interfaccia utente
  - **main.py**: Il punto di ingresso dell'applicazione che collega tutti i componenti

Questa organizzazione permette di:
- Separare chiaramente le diverse responsabilità del codice
- Mantenere il codice pulito e facile da navigare
- Facilitare la manutenzione e l'estensione dell'applicazione
- Seguire il principio di separazione delle preoccupazioni (HTML per la struttura, CSS per lo stile, JS per il comportamento)

## Back-end con FastAPI

In questa sezione, analizzeremo come costruire il "cervello" della nostra applicazione: il back-end. Il back-end è la parte del software che gira sul server e gestisce la logica dell'applicazione, l'accesso ai dati e le operazioni di base.

### Modelli dati (SQLModel)

I modelli dati definiscono la struttura dei nostri oggetti e garantiscono che i dati siano validi. In questo progetto, utilizziamo SQLModel che combina la validazione di Pydantic con le funzionalità ORM di SQLAlchemy.

#### ✏️ Passo 1: Definire i modelli dei libri (app/models/book.py)
```python
from sqlmodel import Field, SQLModel
from typing import Annotated

class BookBase(SQLModel): #classe base per definire i campi comuni
    title: str
    author: str
    review: Annotated[int | None, Field(ge=1, le=5)] = None

class Book(BookBase, table=True): #modello per la tabella del database
    id: int = Field(default=None, primary_key=True)

class BookCreate(BookBase): #modello per la creazione di un libro
    pass

class BookPublic(BookBase): #modello per esporre i dati pubblicamente
    id: int
```

Questo sistema di modelli implementa:
- Una classe base `BookBase` con i campi comuni
- Una classe `Book` per la definizione della tabella del database
- Una classe `BookCreate` per la creazione di nuovi libri (senza ID)
- Una classe `BookPublic` per esporre i dati pubblicamente (con ID)

#### ✏️ Passo 2: Definire il modello Review (app/models/review.py)
```python
from pydantic import BaseModel, Field
from typing import Annotated

class Review(BaseModel):
    review: Annotated[int | None, Field(ge=1, le=5)] = None
```

Questo modello rappresenta una recensione con un valore da 1 a 5.

### Database SQLite

Per archiviare i dati in modo persistente, utilizziamo SQLite, un database SQL leggero che memorizza i dati in un singolo file.

#### ✏️ Configurazione del database (app/data/db.py)
```python
from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends
from faker import Faker
import os
from models.book import Book

# Configurazione del database SQLite
sqlite_file_name = "app/data/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args, echo=True)

# Funzione per inizializzare il database
def init_database():
    ds_exists = os.path.isfile(sqlite_file_name)
    SQLModel.metadata.create_all(engine)
    if not ds_exists:
        # Generazione di dati di esempio con Faker
        f = Faker("it_IT")
        with Session(engine) as session:
            for i in range(10):
                book = Book(title=f.sentence(nb_words=5), author=f.name(),
                            review=f.pyint(1, 5))
                session.add(book)
            session.commit()

# Funzione per ottenere una sessione di database
def get_session():
    with Session(engine) as session:
        yield session

# Dependency injection per ottenere la sessione nelle API
SessionDep = Annotated[Session, Depends(get_session)]
```

Questo codice:
1. Configura la connessione al database SQLite
2. Definisce una funzione per inizializzare il database e creare dati di esempio
3. Crea una funzione per ottenere sessioni di database
4. Definisce una dependency injection per FastAPI

### API (app/routers/books.py)

Le API definiscono le operazioni che possiamo eseguire sui nostri dati. In questo progetto, abbiamo implementato un set completo di API RESTful per la gestione dei libri.

#### 📋 Guida completa alle API implementate

| Operazione | Metodo HTTP | Endpoint | Descrizione | Esempio di utilizzo |
|------------|-------------|----------|------------|-------------------|
| Ottieni tutti i libri | GET | `/books` | Restituisce la lista di tutti i libri disponibili | `GET /books` |
| Ottieni tutti i libri (ordinati) | GET | `/books?sort=true` | Restituisce i libri ordinati per valutazione | `GET /books?sort=true` |
| Ottieni un libro specifico | GET | `/books/{id}` | Ottiene un libro specifico tramite il suo ID | `GET /books/1` |
| Aggiungi un nuovo libro | POST | `/books` | Crea un nuovo libro (richiede i dati del libro nel corpo della richiesta) | `POST /books` con JSON: `{"title": "Nuovo libro", "author": "Autore"}` |
| Aggiungi un libro tramite form | POST | `/books_form/` | Aggiunge un libro tramite un form HTML | Form con campi per titolo e autore |
| Aggiorna un libro | PUT | `/books/{id}` | Aggiorna i dati di un libro esistente | `PUT /books/1` con JSON: `{"title": "Titolo aggiornato", "author": "Autore"}` |
| Elimina un libro | DELETE | `/books/{id}` | Elimina un libro specifico | `DELETE /books/1` |
| Aggiungi una recensione | POST | `/books/{id}/review` | Aggiunge una valutazione (1-5) a un libro specifico | `POST /books/1/review` con JSON: `{"review": 5}` |

#### Implementazione dettagliata delle API

Ecco come sono implementate le API nel file `books.py` usando SQLModel:

##### 1. Ottenere tutti i libri

```python
@router.get("/")
def get_all_books(
        session: SessionDep,
        sort: bool = False
) -> list[BookPublic]:
    """Returns the list of available books."""
    statement = select(Book)
    books = session.exec(statement).all()
    if sort:
        return sorted(books, key=lambda book: book.review)
    else:
        return books
```

Questa API:
- Utilizza la sessione del database iniettata tramite dependency injection
- Esegue una query SELECT per ottenere tutti i libri dal database
- Se `sort=true`, ordina i libri in base al valore della recensione
- Restituisce la lista dei libri come array JSON

##### 2. Aggiungere un nuovo libro

```python
@router.post("/")
def add_book(book: BookCreate, session: SessionDep):
    """Adds a new book."""
    validated_book = Book.model_validate(book)
    session.add(validated_book)
    session.commit()
    return "Book successfully added."
```

Questa API:
- Accetta un oggetto BookCreate nel corpo della richiesta
- Convalida i dati ricevuti
- Crea un nuovo record nel database
- Restituisce un messaggio di conferma

### Punto di ingresso (app/main.py)

Il file main.py è il punto di ingresso dell'applicazione, ossia il file che viene eseguito per avviare il server.

```python
from fastapi import FastAPI
from routers import books, frontend
from fastapi.staticfiles import StaticFiles
from data.db import init_database
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Funzione di gestione del ciclo di vita dell'applicazione.
    Inizializza il database quando l'app viene avviata.
    """
    init_database()
    yield
    
app = FastAPI(lifespan=lifespan)  # Crea un'istanza di FastAPI con la funzione di gestione del ciclo di vita
app.include_router(books.router, tags=["Books"])
app.include_router(frontend.router, tags=["Frontend"])

# Monta la cartella "static" per servire file statici (CSS, JavaScript, immagini)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Questo blocco viene eseguito solo quando il file viene eseguito direttamente
if __name__ == "__main__":
    # Uvicorn è un server ASGI (Asynchronous Server Gateway Interface) per applicazioni Python
    import uvicorn
    # Avvia il server con l'app FastAPI
    uvicorn.run(app, reload=True)
```

Questo file:
1. Crea un gestore del ciclo di vita dell'applicazione che inizializza il database
2. Crea un'applicazione FastAPI
3. Integra i router per le API dei libri e per il frontend
4. Configura il sistema per servire i file statici (CSS e JavaScript)
5. Avvia il server quando il file viene eseguito direttamente

## Front-end con HTML, CSS e JavaScript

Il frontend rappresenta la parte dell'applicazione con cui interagisce direttamente l'utente. In questa sezione esploreremo come costruire un'interfaccia utente intuitiva e reattiva utilizzando i tre linguaggi fondamentali del web.

### HTML (app/templates/home.html)

HTML (HyperText Markup Language) definisce la struttura e il contenuto della pagina web.

#### ✏️ Passo 1: Creare la struttura base

```html
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Libreria Online</title>
    
    <!-- Collegamento al foglio di stile esterno -->
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>Libreria Online</h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/book_list">Visualizza Libri</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <h2>{{ text.title }}</h2>
        <p>{{ text.content }}</p>
        
        <!-- Sezione per aggiungere un nuovo libro -->
        <section id="add-book">
            <h3>Aggiungi un nuovo libro</h3>
            <form id="book-form">
                <div class="form-group">
                    <label for="title">Titolo:</label>
                    <input type="text" id="title" name="title" required>
                </div>
                
                <div class="form-group">
                    <label for="author">Autore:</label>
                    <input type="text" id="author" name="author" required>
                </div>
                
                <div class="form-group">
                    <label for="review">Valutazione (1-5):</label>
                    <input type="number" id="review" name="review" min="1" max="5">
                </div>
                
                <button type="submit">Aggiungi libro</button>
            </form>
        </section>
        
        <!-- Sezione per visualizzare i libri (popolata da JavaScript) -->
        <section id="book-list">
            <h3>Libri disponibili</h3>
            <button id="sort-button">Ordina per valutazione</button>
            <div id="books-container"></div>
        </section>
    </main>
    
    <footer>
        <p>Laboratorio di Programmazione Web - Libreria Online</p>
    </footer>
    
    <!-- Collegamento allo script JavaScript -->
    <script src="/static/js/main.js"></script>
</body>
</html>
```

Questo HTML:
1. Crea un documento HTML5 con metadati appropriati
2. Collega un foglio di stile esterno e uno script JavaScript
3. Crea una struttura di base con header, main e footer
4. Include un modulo per aggiungere nuovi libri
5. Prepara una sezione per visualizzare i libri (che verrà popolata da JavaScript)
6. Utilizza template Jinja2 per inserire dati dinamici (`{{ text.title }}` e `{{ text.content }}`)

## Come eseguire l'applicazione

Per eseguire l'applicazione, segui questi passaggi:

1. **Installa le dipendenze**:
   ```bash
   pip install fastapi[standard] sqlmodel faker uvicorn
   ```
   Oppure usando il file requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

2. **Avvia l'applicazione**:
   ```bash
   python -m app.main
   ```

3. **Accedi all'applicazione**:
   - Apri il browser e vai a http://localhost:8000
   - Per la documentazione API automatica, vai a http://localhost:8000/docs

## Esercizi proposti

Per approfondire le conoscenze acquisite, ecco alcuni esercizi che puoi provare a implementare:

1. **Ricerca libri**: Aggiungi una funzionalità di ricerca per trovare libri per titolo o autore.
2. **Paginazione**: Implementa la paginazione per gestire grandi quantità di libri.
3. **Autenticazione**: Aggiungi un sistema di login per proteggere le operazioni di scrittura.
4. **Categorie**: Aggiungi supporto per categorizzare i libri (es. Fantascienza, Storia, etc.).
5. **Immagini**: Aggiungi supporto per caricare le copertine dei libri.
6. **Commenti**: Consenti agli utenti di lasciare commenti testuali oltre alle valutazioni numeriche.

## Guida alla risoluzione dei problemi comuni

### 🐛 Problema: L'applicazione non si avvia

**Possibili cause e soluzioni**:
- **Porte già in uso**: Se la porta 8000 è già in uso, puoi specificare una porta diversa: `uvicorn app.main:app --port 8001`
- **Dipendenze mancanti**: Assicurati di aver installato tutte le dipendenze con `pip install -r requirements.txt`
- **Percorso errato**: Esegui il comando dalla directory principale del progetto

### 🐛 Problema: Le richieste API falliscono

**Possibili cause e soluzioni**:
- **Formato dei dati errato**: Assicurati che le richieste POST e PUT utilizzino il corretto formato JSON
- **Validazione fallita**: Controlla i messaggi di errore, che includono informazioni sui problemi di validazione

### 🐛 Problema: Errori di importazione dei moduli

**Possibili cause e soluzioni**:
- **Struttura del progetto errata**: Assicurati che la struttura delle cartelle sia esattamente come quella descritta
- **Path di Python**: Esegui l'applicazione dalla directory principale per evitare problemi di path

### 🐛 Problema: Il database non viene creato

**Possibili cause e soluzioni**:
- **Permessi di file**: Assicurati di avere i permessi di scrittura nella directory app/data/
- **Percorso del file**: Verifica che il percorso del file database sia corretto nel file db.py

### 🐛 Problema: Il frontend non visualizza i dati

**Possibili cause e soluzioni**:
- **CORS**: Se sviluppi frontend e backend separatamente, potresti incontrare problemi di CORS
- **JavaScript**: Controlla la console del browser per eventuali errori JavaScript
- **Endpoint errati**: Verifica che gli URL delle API nel codice JavaScript corrispondano a quelli definiti nel backend

---

Questo progetto è stato creato per il Laboratorio di Programmazione Web 2025.

© 2025 - Progetto realizzato da Francesco Carcangiu
