# === DATI DI ESEMPIO PER I LIBRI ===

# Importiamo il modello Book definito nel file models/book.py
from models.book import Book

# Dizionario che simula un database di libri
# In un'applicazione reale, questi dati sarebbero archiviati in un database vero e proprio
# La chiave del dizionario è l'ID del libro, il valore è un'istanza della classe Book
books = {
    # Libro con ID 0, titolo "libro zero", autore "autore zero" e valutazione 1
    0: Book(id=0, title="libro zero", author="autore zero", review=1),
    # Libro con ID 1, titolo "libro uno", autore "autore uno" e valutazione 2
    1: Book(id=1, title="libro uno", author="autore uno", review=2),
    # Libro con ID 2, titolo "libro due", autore "autore due" e valutazione 5 (massima)
    2: Book(id=2, title="libro due", author="autore due", review=5),
}