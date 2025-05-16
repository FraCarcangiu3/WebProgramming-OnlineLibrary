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
6. [Guida completa al database](#guida-completa-al-database)
   - [Concetti fondamentali dei database](#concetti-fondamentali-dei-database)
   - [SQLModel e SQLAlchemy](#sqlmodel-e-sqlalchemy)
   - [Creazione del database](#creazione-del-database)
   - [Operazioni CRUD sul database](#operazioni-crud-sul-database)
   - [Relazioni tra tabelle](#relazioni-tra-tabelle)
   - [Migrazioni del database](#migrazioni-del-database)

### Parte 2: Il Frontend (Client)
7. [Front-end: HTML, CSS e JavaScript](#front-end-con-html-css-e-javascript)
   - [HTML: La struttura](#html-apptemplateshomelhtml)
   - [CSS: Lo stile](#css-appstaticcssfilecss)
   - [JavaScript: Il comportamento](#javascript-appstaticjsmainjs)
8. [Separazione delle preoccupazioni](#separazione-delle-preoccupazioni-una-best-practice)

### Parte 3: Integrazione e Utilizzo
9. [API e comunicazione client-server](#api-e-comunicazione-client-server)
10. [Come eseguire l'applicazione](#come-eseguire-lapplicazione)
11. [Esercizi proposti](#esercizi-proposti)
12. [Guida alla risoluzione dei problemi comuni](#guida-alla-risoluzione-dei-problemi-comuni)

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

## Guida completa al database

Questa sezione fornisce una guida dettagliata su come implementare e utilizzare un database in un'applicazione web. Ti spiegheremo tutto ciò che devi sapere per creare la tua web app con database SQLite e SQLModel.

### Concetti fondamentali dei database

Prima di immergerci nei dettagli tecnici, è importante comprendere alcuni concetti fondamentali dei database:

#### 1. Cos'è un database?

Un database è un sistema organizzato per la memorizzazione, gestione e recupero di dati. Nel contesto delle applicazioni web, il database conserva le informazioni che l'applicazione utilizza (ad esempio, i libri nella nostra libreria online).

#### 2. Tipi di database

Esistono diversi tipi di database:
- **Database relazionali** (come SQLite, PostgreSQL, MySQL): organizzano i dati in tabelle con relazioni tra loro
- **Database NoSQL** (come MongoDB, Cassandra): offrono schemi più flessibili per dati non strutturati
- **Database in-memory** (come Redis): memorizzano i dati in RAM per accessi ad alta velocità

In questo progetto utilizziamo **SQLite**, un database relazionale leggero archiviato in un singolo file, ideale per applicazioni di piccole e medie dimensioni.

#### 3. Modelli di dati e ORM

Un **Object-Relational Mapping (ORM)** è una tecnica che collega il database all'applicazione tramite "modelli" che rappresentano le tabelle del database come classi. Questo semplifica l'interazione con il database utilizzando il linguaggio di programmazione invece di scrivere direttamente SQL.

In questo progetto utilizziamo **SQLModel**, un ORM che combina SQLAlchemy (per le operazioni database) e Pydantic (per la validazione dei dati).

### SQLModel e SQLAlchemy

SQLModel è una libreria che unisce il meglio di SQLAlchemy e Pydantic, fornendo:
- Validazione dei dati (tramite Pydantic)
- Mappatura oggetto-relazionale (tramite SQLAlchemy)
- Supporto per tipizzazione moderna in Python

#### Installazione

Per utilizzare SQLModel, devi installarlo con pip:

```bash
pip install sqlmodel
```

#### Componenti principali di SQLModel

1. **SQLModel**: La classe base per definire i modelli che diventano tabelle nel database
2. **Field**: Per definire campi con caratteristiche speciali (chiavi primarie, valori predefiniti, ecc.)
3. **Relationship**: Per definire relazioni tra diversi modelli
4. **Session**: Per eseguire operazioni sul database
5. **select**: Per creare query di selezione

### Creazione del database

Vediamo come implementare un database SQLite utilizzando SQLModel in un'applicazione FastAPI:

#### 1. Definizione dei modelli

I modelli rappresentano le tabelle del database. Ecco un esempio completo e commentato:

```python
# app/models/book.py
from sqlmodel import Field, SQLModel
from typing import Annotated, Optional, List

# Modello base con i campi comuni
class BookBase(SQLModel):
    title: str  # Campo obbligatorio per il titolo
    author: str  # Campo obbligatorio per l'autore
    # Campo opzionale per la recensione con validazione (tra 1 e 5)
    review: Annotated[Optional[int], Field(ge=1, le=5)] = None
    # Puoi aggiungere altri campi come:
    # year: Optional[int] = None
    # genre: Optional[str] = None

# Modello per la tabella del database (table=True lo rende una tabella)
class Book(BookBase, table=True):
    # Chiave primaria con auto-incremento (default=None)
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # Se volessimo aggiungere relazioni (ad esempio, con le recensioni):
    # reviews: List["Review"] = Relationship(back_populates="book")

# Modello per la creazione di nuovi libri (senza ID)
class BookCreate(BookBase):
    pass

# Modello per restituire i dati pubblicamente (con ID)
class BookPublic(BookBase):
    id: int
```

#### 2. Configurazione del database

La configurazione del database include la creazione del motore di database, le funzioni per le sessioni e l'inizializzazione:

```python
# app/data/db.py
from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends
import os
from models.book import Book

# Percorso del file database
sqlite_file_name = "app/data/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Opzioni di connessione (check_same_thread=False permette l'uso in applicazioni web)
connect_args = {"check_same_thread": False}

# Creazione del motore del database
# echo=True mostra le query SQL eseguite (utile per il debugging)
engine = create_engine(sqlite_url, connect_args=connect_args, echo=True)

# Funzione per inizializzare il database
def init_database():
    # Controlla se il file database esiste già
    ds_exists = os.path.isfile(sqlite_file_name)
    
    # Crea le tabelle dal modello
    SQLModel.metadata.create_all(engine)
    
    # Se il database non esisteva, popolalo con dati di esempio
    if not ds_exists:
        create_sample_data()

# Funzione per creare dati di esempio
def create_sample_data():
    # Puoi usare la libreria Faker per generare dati realistici
    from faker import Faker
    f = Faker("it_IT")
    
    with Session(engine) as session:
        for i in range(10):
            book = Book(
                title=f.sentence(nb_words=5), 
                author=f.name(),
                review=f.pyint(1, 5)
            )
            session.add(book)
        session.commit()

# Funzione per ottenere una sessione di database
def get_session():
    with Session(engine) as session:
        yield session  # Yield rende questa funzione un generatore usabile come dipendenza FastAPI

# Dependency injection per ottenere la sessione nelle API
SessionDep = Annotated[Session, Depends(get_session)]
```

#### 3. Integrazione con FastAPI

Per integrare il database con FastAPI, devi inizializzarlo all'avvio dell'applicazione:

```python
# app/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from data.db import init_database

# Gestore del ciclo di vita per inizializzare il database all'avvio
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Codice eseguito all'avvio dell'applicazione
    init_database()
    yield
    # Codice eseguito alla chiusura dell'applicazione (opzionale)
    # Qui potresti aggiungere operazioni di pulizia se necessario

# Crea l'applicazione FastAPI con il gestore del ciclo di vita
app = FastAPI(lifespan=lifespan)

# ... resto della configurazione dell'app ...
```

### Operazioni CRUD sul database

Le operazioni CRUD (Create, Read, Update, Delete) sono le operazioni fondamentali per interagire con un database. Vediamo come implementarle con SQLModel:

#### 1. Create (Creare)

```python
# In un router FastAPI (app/routers/books.py)
@router.post("/")
def add_book(book: BookCreate, session: SessionDep):
    """Aggiunge un nuovo libro al database."""
    # Converti il modello di creazione nel modello di database
    db_book = Book.model_validate(book)
    
    # Aggiungi alla sessione
    session.add(db_book)
    
    # Salva i cambiamenti nel database
    session.commit()
    
    # Aggiorna l'oggetto con i dati generati (come l'ID auto-incrementato)
    session.refresh(db_book)
    
    return db_book
```

#### 2. Read (Leggere)

```python
# Leggere tutti i record
@router.get("/")
def get_all_books(session: SessionDep, skip: int = 0, limit: int = 100):
    """Restituisce tutti i libri con paginazione opzionale."""
    # Costruisci una query di selezione
    statement = select(Book).offset(skip).limit(limit)
    
    # Esegui la query
    books = session.exec(statement).all()
    
    return books

# Leggere un record specifico
@router.get("/{book_id}")
def get_book(book_id: int, session: SessionDep):
    """Restituisce un libro specifico tramite ID."""
    # Ottieni il libro per ID
    book = session.get(Book, book_id)
    
    # Gestione del caso in cui il libro non esiste
    if not book:
        raise HTTPException(status_code=404, detail="Libro non trovato")
    
    return book

# Leggere con filtri
@router.get("/search/")
def search_books(
    session: SessionDep, 
    title: str = None, 
    author: str = None,
    min_review: int = None
):
    """Cerca libri con vari filtri."""
    statement = select(Book)
    
    # Aggiungi filtri alla query se specificati
    if title:
        statement = statement.where(Book.title.contains(title))
    if author:
        statement = statement.where(Book.author.contains(author))
    if min_review:
        statement = statement.where(Book.review >= min_review)
    
    books = session.exec(statement).all()
    return books
```

#### 3. Update (Aggiornare)

```python
@router.put("/{book_id}")
def update_book(
    book_id: int,
    book_update: BookCreate,
    session: SessionDep
):
    """Aggiorna un libro esistente."""
    # Ottieni il libro esistente
    db_book = session.get(Book, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Libro non trovato")
    
    # Aggiorna i campi con i nuovi valori
    # Ottieni i dati come dizionario, escludendo None
    book_data = book_update.model_dump(exclude_unset=True)
    
    # Aggiorna l'oggetto con i nuovi dati
    for key, value in book_data.items():
        setattr(db_book, key, value)
    
    # Salva i cambiamenti
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    
    return db_book
```

#### 4. Delete (Eliminare)

```python
@router.delete("/{book_id}")
def delete_book(book_id: int, session: SessionDep):
    """Elimina un libro dal database."""
    # Ottieni il libro
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Libro non trovato")
    
    # Elimina il libro
    session.delete(book)
    session.commit()
    
    return {"message": "Libro eliminato con successo"}
```

### Relazioni tra tabelle

Un aspetto potente dei database relazionali è la capacità di creare relazioni tra tabelle. Ecco come implementare relazioni uno-a-molti e molti-a-molti con SQLModel:

#### Relazione uno-a-molti (One-to-Many)

Ad esempio, un libro può avere molte recensioni (un libro : molte recensioni):

```python
# Modello Recensione
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    rating: int = Field(ge=1, le=5)
    
    # Chiave esterna che collega questa recensione a un libro
    book_id: int = Field(foreign_key="book.id")
    
    # Relazione con il libro (per accesso facile nel codice Python)
    book: "Book" = Relationship(back_populates="reviews")

# Aggiornamento del modello Libro per includere la relazione
class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # Relazione con le recensioni
    reviews: List[Review] = Relationship(back_populates="book")
```

#### Relazione molti-a-molti (Many-to-Many)

Ad esempio, libri e autori (un libro può avere più autori, un autore può scrivere più libri):

```python
# Tabella di associazione (per relazioni molti-a-molti)
class BookAuthorLink(SQLModel, table=True):
    book_id: Optional[int] = Field(
        default=None, foreign_key="book.id", primary_key=True
    )
    author_id: Optional[int] = Field(
        default=None, foreign_key="author.id", primary_key=True
    )

class Author(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    
    # Relazione molti-a-molti con libri
    books: List["Book"] = Relationship(
        back_populates="authors",
        link_model=BookAuthorLink
    )

class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # Relazione molti-a-molti con autori
    authors: List[Author] = Relationship(
        back_populates="books",
        link_model=BookAuthorLink
    )
```

### Migrazioni del database

Le migrazioni sono un modo per gestire i cambiamenti nello schema del database nel tempo. Sebbene SQLModel non abbia un sistema di migrazione integrato, puoi utilizzare Alembic (compatibile con SQLAlchemy) per gestire le migrazioni.

Ecco i passaggi di base per configurare Alembic:

#### 1. Installazione di Alembic

```bash
pip install alembic
```

#### 2. Inizializzazione di Alembic

```bash
alembic init migrations
```

#### 3. Configurazione di Alembic

Modifica il file `alembic.ini` per puntare al tuo database:

```ini
sqlalchemy.url = sqlite:///app/data/database.db
```

Modifica `migrations/env.py` per utilizzare i tuoi modelli SQLModel:

```python
from models.book import Book  # Importa tutti i tuoi modelli
from sqlmodel import SQLModel

# Aggiungi questa riga per target_metadata
target_metadata = SQLModel.metadata
```

#### 4. Creazione di una migrazione

```bash
alembic revision --autogenerate -m "Descrizione della modifica"
```

#### 5. Applicazione della migrazione

```bash
alembic upgrade head
```

### Esempio pratico completo

Supponiamo di voler creare una web app per una libreria con le seguenti funzionalità:
- Gestione di libri, autori e recensioni
- Ricerca di libri per titolo, autore o valutazione
- Visualizzazione dettagliata dei libri con tutte le recensioni

Ecco come implementare il database per questa applicazione:

#### 1. Modelli dati (app/models)

```python
# models/author.py
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List

class Author(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    bio: Optional[str] = None
    
    # Relazione con i libri
    books: List["Book"] = Relationship(back_populates="authors")

# models/book.py
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    year: Optional[int] = None
    genre: Optional[str] = None
    
    # Relazioni
    authors: List["Author"] = Relationship(back_populates="books")
    reviews: List["Review"] = Relationship(back_populates="book")

# models/review.py
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    rating: int = Field(ge=1, le=5)
    
    # Relazione con il libro
    book_id: int = Field(foreign_key="book.id")
    book: "Book" = Relationship(back_populates="reviews")
```

#### 2. Configurazione del database

```python
# data/db.py
from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends
import os

# Importa tutti i modelli per assicurarti che siano registrati
from models.book import Book
from models.author import Author
from models.review import Review

# Configurazione del database
sqlite_file_name = "app/data/library.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args, echo=True)

def init_database():
    os.makedirs(os.path.dirname(sqlite_file_name), exist_ok=True)
    ds_exists = os.path.isfile(sqlite_file_name)
    SQLModel.metadata.create_all(engine)
    
    if not ds_exists:
        create_sample_data()

def create_sample_data():
    with Session(engine) as session:
        # Crea autori
        author1 = Author(name="J.K. Rowling", bio="Autrice di Harry Potter")
        author2 = Author(name="George Orwell", bio="Autore di 1984")
        
        # Crea libri
        book1 = Book(title="Harry Potter", year=1997, genre="Fantasy")
        book2 = Book(title="1984", year=1949, genre="Distopia")
        
        # Collega libri e autori
        book1.authors.append(author1)
        book2.authors.append(author2)
        
        # Aggiungi al database
        session.add(author1)
        session.add(author2)
        session.add(book1)
        session.add(book2)
        
        # Aggiungi recensioni
        review1 = Review(text="Fantastico!", rating=5, book_id=1)
        review2 = Review(text="Un classico.", rating=4, book_id=2)
        
        session.add(review1)
        session.add(review2)
        
        session.commit()

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
```

#### 3. API per il database

```python
# routers/books.py
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select, Session
from typing import List

from models.book import Book
from models.review import Review
from data.db import SessionDep

router = APIRouter(prefix="/books")

@router.get("/", response_model=List[Book])
def get_books(
    session: SessionDep,
    skip: int = 0,
    limit: int = 100,
    title: str = None,
    genre: str = None,
    min_rating: float = None
):
    """Ottieni libri con filtri opzionali."""
    query = select(Book)
    
    if title:
        query = query.where(Book.title.contains(title))
    if genre:
        query = query.where(Book.genre == genre)
    if min_rating:
        # Query più complessa con sottoquery per rating medio
        # Questa è una semplificazione
        pass
    
    query = query.offset(skip).limit(limit)
    books = session.exec(query).all()
    return books

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int, session: SessionDep):
    """Ottieni dettagli di un libro specifico."""
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Libro non trovato")
    return book

@router.post("/", response_model=Book)
def create_book(book: Book, session: SessionDep):
    """Crea un nuovo libro."""
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

@router.post("/{book_id}/reviews/", response_model=Review)
def add_review(book_id: int, review: Review, session: SessionDep):
    """Aggiungi una recensione a un libro."""
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Libro non trovato")
    
    review.book_id = book_id
    session.add(review)
    session.commit()
    session.refresh(review)
    return review
```

### Consigli per la progettazione del database

1. **Pianifica prima lo schema**: Prima di iniziare a codificare, pianifica le tabelle e le relazioni tra loro.

2. **Normalizza i dati**: Dividi i dati in tabelle logiche per evitare la ridondanza.

3. **Usa chiavi primarie appropriate**: Ogni tabella dovrebbe avere una chiave primaria univoca.

4. **Considera gli indici**: Aggiungi indici ai campi frequentemente cercati per migliorare le prestazioni.

5. **Validazione a livello di modello**: Utilizza i vincoli di SQLModel per garantire la validità dei dati.

6. **Migrazioni per i cambiamenti**: Usa Alembic per gestire i cambiamenti nello schema nel tempo.

7. **Test con dati di esempio**: Crea dati di esempio realistici per testare l'applicazione.

### Conclusione

Con questa guida hai ora tutti gli strumenti necessari per implementare un database SQLite con SQLModel nella tua applicazione FastAPI. Puoi utilizzare questi concetti come base per costruire applicazioni web più complesse con database relazionali.

Ricorda che questa è solo l'inizio: man mano che l'applicazione cresce, potresti voler esplorare database più robusti come PostgreSQL o MySQL, implementare caching con Redis, o aggiungere funzionalità di ricerca avanzate con Elasticsearch.

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
