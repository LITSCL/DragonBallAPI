from fastapi import APIRouter
from typing import List

from models.personaje import Personaje
from controllers.personaje_controller import PersonajeController

pc: PersonajeController = PersonajeController()

router: object = APIRouter()

router.add_api_route("/api/personaje/get-personajes", pc.get_personajes, methods = ["GET"], response_model = List[Personaje], tags = ["modelo_personaje"])
router.add_api_route("/api/personaje/get-personajes/{limite}", pc.get_personajes, methods = ["GET"], response_model = List[Personaje], tags = ["modelo_personaje"])

rutas_personaje: object = router