from typing import List

from models.personaje import Personaje

def schema(personaje: Personaje) -> dict:
    return {
        "id": str(personaje["_id"]),
        "nombre": personaje["nombre"],
        "raza": personaje["raza"],
        "genero": personaje["genero"],
        "biografia": personaje["biografia"],
        "ataque": personaje["ataque"],
        "imagen": personaje["imagen"]
    }

def objeto_schema(personaje: Personaje) -> dict:
    return schema(personaje)
    
def lista_schema(personajes: List[Personaje]) -> list:
    return [schema(personaje) for personaje in personajes]