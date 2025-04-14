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
   - [Modelli dati (Pydantic)](#modelli-dati-appmodels)
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
- Come gestire i dati e la loro validazione
- Come creare un'interfaccia utente interattiva

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
- **Familiarità di base** con i concetti di programmazione

Non preoccuparti se non sei esperto in tutte queste tecnologie: questa guida è pensata per spiegare ogni passaggio in modo chiaro.

## Tecnologie utilizzate

In questo progetto utilizziamo diverse tecnologie, divise tra la parte server (backend) e la parte client (frontend).

### 🖥️ Back-end (lato server)

- **Python**: Un linguaggio di programmazione versatile e facile da imparare, popolare per lo sviluppo web.
  - *Perché lo usiamo?* Python è facile da leggere e scrivere, ha una sintassi chiara ed è perfetto per i principianti.

- **FastAPI**: Un framework moderno e veloce per la creazione di API web con Python.
  - *Perché lo usiamo?* FastAPI è facile da usare, veloce, e include automaticamente la documentazione delle API.

- **Pydantic**: Libreria per la validazione dei dati e la definizione di modelli.
  - *Perché lo usiamo?* Pydantic garantisce che i dati siano nel formato corretto, riducendo gli errori.

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
│   │   └── books.py         # "Database" di esempio con i libri
│   ├── models/
│   │   ├── book.py          # Modello per i libri
│   │   └── review.py        # Modello per le recensioni
│   ├── routers/
│   │   └── books.py         # Definizione delle API
│   ├── static/              # Directory per i file statici
│   │   ├── css/
│   │   │   └── style.css    # Stili CSS separati
│   │   └── js/
│   │       └── main.js      # Script JavaScript
│   ├── templates/
│   │   └── home.html        # Interfaccia utente (solo struttura HTML)
│   ├── __init__.py
│   └── main.py              # Punto di ingresso dell'applicazione
└── README.md                # Questa guida
```

Questa struttura segue un pattern comune per le applicazioni web:

- **app/**: La directory principale che contiene tutto il codice dell'applicazione
  - **data/**: Contiene i dati dell'applicazione (in un'applicazione reale, potrebbe essere sostituito da un database)
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

### Modelli dati (app/models/)

I modelli dati definiscono la struttura dei nostri oggetti e garantiscono che i dati siano validi. In Python, utilizziamo Pydantic per questo scopo.

#### ✏️ Passo 1: Definire il modello Book (app/models/book.py)
```python
from pydantic import BaseModel, Field
from typing import Annotated

class Book(BaseModel):
    id: int
    title: str
    author: str
    review: Annotated[int|None, Field(ge=1, le=5)] = None
```

Questo modello rappresenta un libro con:
- `id`: identificatore numerico univoco
- `title`: titolo del libro
- `author`: autore del libro
- `review`: recensione opzionale (da 1 a 5)

#### ✏️ Passo 2: Definire il modello Review (app/models/review.py)
```python
from pydantic import BaseModel, Field
from typing import Annotated

class Review(BaseModel):
    review: Annotated[int | None, Field(ge=1, le=5)] = None
```

Questo modello rappresenta una recensione con un valore da 1 a 5.

### Dati di esempio (app/data/books.py)

Per semplicità, usiamo un dizionario Python come "database" invece di un database reale:

```python
from models.book import Book

books = {
    0: Book(id=0, title="libro zero", author="autore zero", review=1),
    1: Book(id=1, title="libro uno", author="autore uno", review=2),
    2: Book(id=2, title="libro due", author="autore due", review=5),
}
```

### API (app/routers/books.py)

Le API definiscono le operazioni che possiamo eseguire sui nostri dati. In questo progetto, abbiamo implementato un set completo di API RESTful per la gestione dei libri.

#### 📋 Guida completa alle API implementate

| Operazione | Metodo HTTP | Endpoint | Descrizione | Esempio di utilizzo |
|------------|-------------|----------|------------|-------------------|
| Ottieni tutti i libri | GET | `/books` | Restituisce la lista di tutti i libri disponibili | `GET /books` |
| Ottieni tutti i libri (ordinati) | GET | `/books?sort=true` | Restituisce i libri ordinati per valutazione | `GET /books?sort=true` |
| Ottieni un libro specifico | GET | `/books/{id}` | Ottiene un libro specifico tramite il suo ID | `GET /books/1` |
| Aggiungi un nuovo libro | POST | `/books` | Crea un nuovo libro (richiede i dati del libro nel corpo della richiesta) | `POST /books` con JSON: `{"id": 3, "title": "Nuovo libro", "author": "Autore"}` |
| Aggiorna un libro | PUT | `/books/{id}` | Aggiorna i dati di un libro esistente | `PUT /books/1` con JSON: `{"id": 1, "title": "Titolo aggiornato", "author": "Autore"}` |
| Elimina un libro | DELETE | `/books/{id}` | Elimina un libro specifico | `DELETE /books/1` |
| Elimina tutti i libri | DELETE | `/books` | Elimina tutti i libri dal database | `DELETE /books` |
| Aggiungi una recensione | POST | `/books/{id}/review` | Aggiunge una valutazione (1-5) a un libro specifico | `POST /books/1/review` con JSON: `{"review": 5}` |

#### Implementazione dettagliata delle API

Ecco come sono implementate le API nel file `books.py`:

##### 1. Ottenere tutti i libri

```python
@router.get("/")
def get_all_books(sort: bool = False) -> list[Book]:
    if sort:
        # Ordina i libri per recensione se il parametro sort è true
        return sorted(books.values(), key=lambda book: book.review)
    
    # Altrimenti, restituisce tutti i libri senza ordinamento
    return list(books.values())
```

Questa API:
- Accetta un parametro opzionale `sort` (default: `false`)
- Se `sort=true`, ordina i libri in base al valore della recensione
- Restituisce la lista dei libri come array JSON

##### 2. Ottenere un libro specifico

```python
@router.get("/{id}")
def get_book_by_id(id: Annotated[int, Path(description="The ID of the book")]) -> Book:
    try:
        return books[id]
    except KeyError:
        # Se il libro non esiste, restituisce un errore 404
        raise HTTPException(status_code=404, detail="Book not found")
```

Questa API:
- Richiede un ID come parametro nel percorso URL
- Cerca il libro con l'ID specificato
- Se trova il libro, lo restituisce
- Se il libro non esiste, restituisce un errore 404

##### 3. Aggiungere una recensione

```python
@router.post("/{id}/review")
def add_review(
    id: Annotated[int, Path(description="The ID of the book")],
    review: Review
):
    try:
        books[id].review = review.review
        return "Review added successfully"
    except KeyError:
        raise HTTPException(status_code=404, detail="Libro non trovato")
```

Questa API:
- Richiede un ID come parametro nel percorso URL
- Accetta un oggetto Review nel corpo della richiesta
- Aggiorna la recensione del libro con l'ID specificato
- Restituisce un messaggio di successo o un errore 404 se il libro non esiste

##### 4. Aggiungere un nuovo libro

```python
@router.post("/")
def add_book(book: Book):
    if book.id in books:
        raise HTTPException(status_code=403, detail="Book ID already exists")
    books[book.id] = book
    return "Book added successfully"
```

Questa API:
- Accetta un oggetto Book nel corpo della richiesta
- Verifica se esiste già un libro con lo stesso ID
- Se l'ID è già in uso, restituisce un errore 403
- Altrimenti, aggiunge il libro e restituisce un messaggio di successo

##### 5. Aggiornare un libro esistente

```python
@router.put("/{id}")
def update_book(
    id: Annotated[int, Path(description="The ID of the book")],
    book: Book
):
    if not id in books:
        raise HTTPException(status_code=404, detail="Book not found")
    books[id] = book
    return "Book updated successfully"
```

Questa API:
- Richiede un ID come parametro nel percorso URL
- Accetta un oggetto Book nel corpo della richiesta
- Verifica se esiste un libro con l'ID specificato
- Se il libro esiste, lo aggiorna con i nuovi dati
- Altrimenti, restituisce un errore 404

##### 6. Eliminare tutti i libri

```python
@router.delete("/")
def delete_all_book():
    books.clear()
    return "All books deleted successfully"
```

Questa API:
- Elimina tutti i libri dal "database"
- Restituisce un messaggio di conferma

##### 7. Eliminare un libro specifico

```python
@router.delete("/{id}")
def delete_book(id: Annotated[int, Path(description="The ID of the book")]):
    try:
        del books[id]
        return "Book deleted successfully"
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found")
```

Questa API:
- Richiede un ID come parametro nel percorso URL
- Cerca di eliminare il libro con l'ID specificato
- Se il libro viene eliminato, restituisce un messaggio di successo
- Se il libro non esiste, restituisce un errore 404

### Punto di ingresso (app/main.py)

Il file main.py è il punto di ingresso dell'applicazione, ossia il file che viene eseguito per avviare il server.

#### ✏️ Passo 1: Creare il file main.py

```python
from fastapi import FastAPI
from routers import books
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(books.router, tags=["books"])

# Configurazione per servire i file statici (CSS, JavaScript)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, reload=True)
```

#### 📝 Spiegazione del codice

Questo file:
1. Crea un'applicazione FastAPI
2. Integra il router delle API dei libri
3. **Configura il sistema per servire i file statici** (CSS e JavaScript)
4. Configura il sistema di templating Jinja2 per servire la pagina HTML
5. Definisce una route per la pagina principale
6. Avvia il server quando il file viene eseguito direttamente

La linea `app.mount("/static", StaticFiles(directory="app/static"), name="static")` è fondamentale poiché permette di servire i file statici dalla cartella `app/static`, rendendoli accessibili tramite l'URL `/static` nel browser.

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
        <div class="contenitore">
            <h1>Libreria Online</h1>
            <p class="sottotitolo">Gestione del catalogo libri</p>
        </div>
    </header>

    <main class="contenitore">
        <!-- Contenuto dell'applicazione -->
        <!-- ... (tabella dei libri, form di modifica, ecc.) ... -->
    </main>

    <footer>
        <div class="contenitore">
            <p>© 2025 Libreria Online - Progetto realizzato da Francesco Carcangiu</p>
        </div>
    </footer>

    <!-- Collegamento al file JavaScript esterno -->
    <script src="/static/js/main.js"></script>
</body>
</html>
```

#### 📝 Elementi principali

La struttura HTML organizza l'interfaccia in:
- **Header**: Contiene il titolo dell'applicazione
- **Main**: La sezione principale che contiene:
  - Tabella per visualizzare i libri
  - Form per aggiungere/modificare libri
  - Form per aggiungere recensioni
- **Footer**: Contiene le informazioni sul copyright

### CSS (app/static/css/style.css)

CSS (Cascading Style Sheets) definisce l'aspetto visivo degli elementi HTML.

#### ✏️ Passo 1: Definire le variabili e il reset

```css
/* Definizione delle variabili CSS */
:root {
    --blu-principale: #3498db;   /* Colore primario per pulsanti e accenti */
    --blu-scuro: #2c3e50;        /* Colore secondario per header e titoli */
    --rosso: #e74c3c;            /* Colore per azioni pericolose (es. elimina) */
    --testo-colore: #333;        /* Colore del testo principale */
    --sfondo-chiaro: #f9f9f9;    /* Colore di sfondo della pagina */
    --bianco: #ffffff;           /* Colore bianco per elementi in primo piano */
    --ombra: 0 2px 8px rgba(0, 0, 0, 0.1);  /* Effetto ombra per elementi */
    --bordo-arrotondato: 8px;    /* Raggio per angoli arrotondati */
}

/* Reset degli stili di default del browser */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```

#### ✏️ Passo 2: Definire gli stili principali

```css
/* Stile del corpo della pagina */
body {
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.6;
    color: var(--testo-colore);
    background-color: var(--sfondo-chiaro);
    padding-bottom: 2rem;
}

/* Stile dell'intestazione */
header {
    background-color: var(--blu-scuro);
    color: var(--bianco);
    text-align: center;
    padding: 1.5rem 0;
    margin-bottom: 2rem;
    box-shadow: var(--ombra);
}
/* ... altri stili ... */
```

#### 📝 Vantaggi di un file CSS separato

- **Maggiore leggibilità**: il codice HTML è più pulito e focalizzato sulla struttura
- **Manutenibilità**: è più facile apportare modifiche all'aspetto dell'app
- **Caching**: i browser possono memorizzare il file CSS, migliorando le prestazioni
- **Riutilizzo**: gli stessi stili possono essere applicati a più pagine

### JavaScript (app/static/js/main.js)

JavaScript aggiunge interattività alla pagina web e comunica con il server.

#### ✏️ Passo 1: Configurare le variabili iniziali

```javascript
// API URLs
const API_URL = '/books';

// Elementi DOM
const sezioneLibri = document.getElementById('sezione-libri');
const sezioneFormLibro = document.getElementById('sezione-form-libro');
const sezioneFormRecensione = document.getElementById('sezione-form-recensione');
const listaLibri = document.getElementById('lista-libri');
// ... altre variabili ...

// Stato dell'applicazione
let staModificando = false;
let ordinamentoAttuale = false;
let valutazioneSelezionata = 0;

// Carica i libri all'avvio
document.addEventListener('DOMContentLoaded', () => {
    caricaLibri();
    impostaGestoriEventi();
});
```

#### ✏️ Passo 2: Implementare le funzioni principali

```javascript
// Funzione per caricare i libri dal server
async function caricaLibri() {
    try {
        const risposta = await fetch(`${API_URL}?sort=${ordinamentoAttuale}`);
        if (!risposta.ok) {
            throw new Error('Errore durante il caricamento dei libri');
        }
        const libri = await risposta.json();
        renderizzaLibri(libri);
    } catch (error) {
        mostraAvviso(error.message, 'errore');
    }
}

// ... altre funzioni ...
```

#### 📝 Funzionalità implementate in JavaScript

1. **Caricamento dei dati**: recupera i libri dal server utilizzando fetch API
2. **Manipolazione del DOM**: aggiorna dinamicamente l'interfaccia utente
3. **Gestione degli eventi**: risponde alle azioni dell'utente (clic, invio dei form)
4. **Comunicazione con il backend**: invia richieste HTTP al server
5. **Gestione degli errori**: mostra avvisi all'utente quando necessario

## Separazione delle preoccupazioni: Una best practice

Una delle migliori pratiche nello sviluppo web è la "separazione delle preoccupazioni" (Separation of Concerns, SoC). Scopriamo cos'è e perché è così importante per il tuo sviluppo come programmatore.

### 🤔 Cosa significa?

La separazione delle preoccupazioni è un principio di design che consiste nel dividere un'applicazione in parti distinte, ciascuna responsabile di un aspetto specifico:

1. **HTML** si occupa della struttura e del contenuto 
2. **CSS** si occupa dell'aspetto visivo e dello stile
3. **JavaScript** si occupa del comportamento e dell'interattività

### 🌟 Vantaggi di questa separazione

#### 1. Migliore organizzazione del codice
Ogni file ha uno scopo chiaro e ben definito, rendendo più facile navigare e comprendere il codice.

#### 2. Manutenibilità migliorata
È possibile modificare uno degli aspetti (ad esempio lo stile) senza dover toccare gli altri (struttura o comportamento).

#### 3. Collaborazione più efficiente
Diversi membri del team possono lavorare contemporaneamente su parti diverse dell'applicazione con meno conflitti.

#### 4. Riutilizzo del codice
Gli stili e gli script possono essere facilmente riutilizzati in più pagine.

#### 5. Prestazioni migliori
I browser possono memorizzare nella cache i file CSS e JavaScript, riducendo i tempi di caricamento per le visite successive.

### 🛠️ Implementazione nel nostro progetto

Nel nostro progetto, abbiamo separato:

- **app/templates/home.html**: contiene solo la struttura della pagina
- **app/static/css/style.css**: contiene tutte le regole di stile
- **app/static/js/main.js**: contiene tutta la logica e l'interattività

Per far funzionare questa organizzazione, abbiamo configurato FastAPI per servire i file statici con:

```python
app.mount("/static", StaticFiles(directory="app/static"), name="static")
```

E abbiamo aggiunto i riferimenti ai file esterni nell'HTML:

```html
<link rel="stylesheet" href="/static/css/style.css">
<script src="/static/js/main.js"></script>
```

### 📊 Confronto: Prima e dopo

**Prima**: tutto il codice (HTML, CSS, JavaScript) era in un unico file, rendendo difficile la manutenzione e la leggibilità.

**Dopo**: ogni linguaggio ha il suo file dedicato, rendendo il codice più organizzato, leggibile e manutenibile.

## API e comunicazione client-server

Un'applicazione web moderna è composta da due parti che comunicano tra loro: il client (frontend) e il server (backend). Vediamo come funziona questa comunicazione nella nostra applicazione.

### 🔄 Il ciclo di comunicazione

Ecco come funziona la comunicazione tra il front-end e il back-end:

1. **Richiesta**: L'utente esegue un'azione nell'interfaccia (ad esempio, clicca su "Aggiungi Libro")
2. **JavaScript** cattura l'evento e prepara una richiesta HTTP al server
3. **API Backend** riceve la richiesta, la elabora e accede ai dati
4. **Risposta**: Il server risponde con i dati richiesti o un messaggio di conferma
5. **Aggiornamento UI**: JavaScript riceve la risposta e aggiorna l'interfaccia utente

### 📡 Esempi di comunicazione client-server

#### Esempio 1: Caricamento dei libri

```javascript
// Nel file JavaScript (client)
async function caricaLibri() {
    const risposta = await fetch('/books?sort=' + ordinamentoAttuale);
    const libri = await risposta.json();
    renderizzaLibri(libri);
}
```

```python
# Nel file Python (server)
@router.get("/")
def get_all_books(sort: bool = False) -> list[Book]:
    if sort:
        return sorted(books.values(), key=lambda book: book.review)
    return list(books.values())
```

#### Esempio 2: Aggiungere un nuovo libro

```javascript
// Nel file JavaScript (client)
async function aggiungiLibro(datiLibro) {
    const risposta = await fetch('/books', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(datiLibro)
    });
    // Gestione della risposta...
}
```

```python
# Nel file Python (server)
@router.post("/")
def add_book(book: Book):
    if book.id in books:
        raise HTTPException(status_code=403, detail="Book ID already exists")
    books[book.id] = book
    return "Book added successfully"
```

### 🔍 Debugging della comunicazione

Quando sviluppi un'applicazione web, è utile conoscere gli strumenti per il debug della comunicazione client-server:

1. **Strumenti di sviluppo del browser** (F12): La scheda "Network" mostra tutte le richieste HTTP
2. **Console del browser**: Puoi vedere gli errori JavaScript e le risposte delle richieste
3. **Log del server**: Uvicorn mostra i log delle richieste e degli errori del server

## Come eseguire l'applicazione

Questa guida dettagliata ti aiuterà a configurare e avviare l'applicazione sul tuo computer.

### Prerequisiti di sistema

Prima di iniziare, assicurati di avere:

1. **Python 3.7 o superiore** installato sul tuo sistema.
   - Per verificare se Python è installato e quale versione: `python --version` o `python3 --version`
   - Se non è installato, scaricalo da [python.org](https://www.python.org/downloads/)

2. **pip** (il gestore dei pacchetti di Python)
   - Generalmente viene installato con Python
   - Per verificare: `pip --version` o `pip3 --version`

### Passo 1: Clonare o scaricare il progetto

Hai due opzioni:

- **Opzione 1**: Clona il repository se hai Git installato:
  ```bash
  git clone https://github.com/tuousername/lab2025.git
  cd lab2025
  ```

- **Opzione 2**: Scarica il progetto come file ZIP, estrailo e apri il terminale nella cartella estratta.

### Passo 2: Creare un ambiente virtuale (consigliato)

Un ambiente virtuale isola le dipendenze del progetto da quelle di sistema:

```bash
# Su Windows
python -m venv venv
venv\Scripts\activate

# Su macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Installare le dipendenze

Installa i pacchetti richiesti:

```bash
pip install fastapi uvicorn jinja2
```

Alternativamente, se esiste un file `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Passo 4: Avviare l'applicazione

```bash
# Dalla directory principale del progetto
python -m app.main
```

Dovresti vedere qualcosa di simile a:

```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### Passo 5: Aprire l'applicazione nel browser

Apri il tuo browser web e vai all'indirizzo:
```
http://localhost:8000
```

Dovresti vedere l'interfaccia della Libreria Online con l'elenco dei libri.

### Passo 6: Esplorare la documentazione delle API

FastAPI genera automaticamente una documentazione interattiva delle API. Puoi accedervi visitando:
```
http://localhost:8000/docs
```

Questa pagina ti permette di:
- Vedere tutte le API disponibili
- Leggere la documentazione di ogni API
- Testare le API direttamente dal browser

### Risoluzione dei problemi comuni

- **Errore "Port already in use"**: Un'altra applicazione sta già usando la porta 8000
  - Soluzione: Termina l'altra applicazione o modifica la porta in `main.py` aggiungendo `port=8001` a `uvicorn.run()`

- **ModuleNotFoundError**: Un modulo non è stato trovato
  - Soluzione: Verifica di aver installato tutte le dipendenze con `pip install fastapi uvicorn jinja2`
  
- **Errore 404 quando visiti una pagina**: L'URL potrebbe essere errato
  - Soluzione: Verifica l'URL o controlla i log del server per eventuali errori

- **Il server si avvia ma l'interfaccia non carica i libri**: Potrebbe esserci un problema con le chiamate API
  - Soluzione: Apri gli strumenti di sviluppo del browser (F12) e controlla la console per eventuali errori

## Esercizi proposti

Ecco alcuni esercizi per migliorare l'applicazione:

### 1. Miglioramenti UI/UX
   - Aggiungi una modalità tema scuro implementando un file CSS alternativo
   - Migliora l'aspetto mobile aggiungendo media queries al file CSS
   - Aggiungi animazioni per le transizioni usando CSS o librerie JavaScript

### 2. Organizzazione modulare del JavaScript
   - Dividi il file `main.js` in moduli più piccoli e specifici (es. `api.js`, `ui.js`, `validation.js`)
   - Implementa un sistema di gestione degli stati più avanzato
   - Utilizza pattern di design JavaScript come il Module Pattern o il Revealing Module Pattern

### 3. Ottimizzazione dei file statici
   - Implementa la minificazione dei file CSS e JavaScript
   - Aggiungi versioning ai file statici per gestire la cache del browser
   - Utilizza un preprocessore CSS (come SASS o LESS) per migliorare la manutenibilità

### 4. Funzionalità aggiuntive
   - Aggiungi la ricerca dei libri con evidenziazione dinamica dei risultati
   - Implementa categorie/generi per i libri
   - Aggiungi paginazione per la lista dei libri

### 5. Estensione dello stile
   - Crea un design system con variabili CSS e componenti riutilizzabili
   - Implementa diversi temi che l'utente può scegliere
   - Aggiungi effetti hover e transizioni più sofisticate

### 6. Persistenza dei dati
   - Sostituisci il "database" in-memory con SQLite
   - Aggiungi un database SQL più robusto come PostgreSQL
   - Implementa un ORM come SQLAlchemy

### 7. Autenticazione
   - Aggiungi un sistema di login
   - Implementa diversi ruoli (utente, admin)
   - Limita alcune operazioni solo agli utenti autenticati

### 8. Miglioramenti di accessibilità
   - Assicurati che l'applicazione sia accessibile seguendo le linee guida WCAG
   - Migliora l'uso delle etichette ARIA e della struttura semantica HTML
   - Implementa la navigazione da tastiera e il supporto per screen reader

Buon divertimento con la programmazione web!

---

Questo progetto è stato creato per il Laboratorio di Programmazione Web 2025.

© 2025 - Progetto realizzato da Francesco Carcangiu
