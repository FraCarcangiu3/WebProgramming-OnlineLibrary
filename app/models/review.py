# === MODELLO DEI DATI PER UNA RECENSIONE ===

# Importiamo i componenti necessari per la validazione
from pydantic import BaseModel, Field  # BaseModel per definire modelli, Field per validazione
from typing import Annotated  # Per arricchire i tipi con metadati e validazione


# Definizione della classe Review che rappresenta una recensione/valutazione di un libro
class Review(BaseModel):
    # Campo 'review' che rappresenta la valutazione numerica:
    # - Può essere un intero da 1 a 5 (ge=1 significa >=1, le=5 significa <=5)
    # - Può essere None (nessuna valutazione)
    # - Il valore predefinito è None
    review: Annotated[int | None, Field(ge=1, le=5)] = None