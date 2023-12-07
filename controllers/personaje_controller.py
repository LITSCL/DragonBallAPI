from fastapi import HTTPException

from config.database import DataBase
from models.personaje import Personaje
from schemas.personaje_schema import objeto_schema, lista_schema

class PersonajeController:
    __db: object = DataBase().get_conexion()
    __query: object = None
    
    async def get_personajes(self, limite: int = None) -> list:
        if (limite == None):
            self.__query = self.__db.personaje.find()
            resultado: list = lista_schema(self.__query)
        else:
            self.__query = self.__db.personaje.find().limit(limite)
            resultado: list = lista_schema(self.__query)
        return resultado