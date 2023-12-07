from pydantic import BaseModel
from typing import Optional

class Personaje(BaseModel):
    id: Optional[str] = None
    nombre: str = None
    raza: str = None
    genero: str = None
    biografia: str = None
    ataque: int = None
    imagen: str = None