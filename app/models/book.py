# === MODELLO DEI DATI PER UN LIBRO ===

# Importiamo BaseModel da pydantic che ci permette di definire modelli di dati
# e Field che consente di aggiungere vincoli e metadati ai campi
from pydantic import BaseModel, Field
# Importiamo Annotated che permette di aggiungere informazioni aggiuntive ai tipi
from typing import Annotated

# Definizione della classe Book che rappresenta un libro nel nostro sistema
class Book(BaseModel):
    # Identificativo numerico univoco del libro
    id: int
    # Titolo del libro
    title: str
    # Autore del libro
    author: str
    # Recensione del libro, che può essere:
    # - Un numero intero da 1 a 5 (ge=1 significa >=1, le=5 significa <=5)
    # - None (nessuna recensione ancora presente)
    # Il valore predefinito è None
    review: Annotated[int|None, Field(ge=1, le=5)] = None




