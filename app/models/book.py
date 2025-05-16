# === MODELLO DEI DATI PER UN LIBRO ===

from sqlmodel import Field, SQLModel
from typing import Annotated

class BookBase(SQLModel): #funzione per le post
    title: str
    author: str
    review: Annotated[int | None, Field(ge=1, le=5)] = None


class Book(BookBase, table=True): #modello per la tabella del database
    id: int = Field(default=None, primary_key=True)


class BookCreate(BookBase): #model per la creazione di un libro 
    pass

class BookPublic(BookBase):
    id: int