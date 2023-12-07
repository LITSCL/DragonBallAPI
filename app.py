from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routes.personaje_route import rutas_personaje

app: object = FastAPI(
    title = "API REST",
    description = "Este proyecto tiene la finalidad de ser utilizado como API REST de consumo para cualquier otro proyecto",
    version = "1.0.0"
)

app.mount("/resources", StaticFiles(directory = "templates/resources"), name = "resources")

plantillas: object = Jinja2Templates(directory = "templates")

@app.get("/", response_class = HTMLResponse, tags = ["index"])
async def index(request: Request) -> object:
    return plantillas.TemplateResponse("index.html", {"request": request})

app.include_router(rutas_personaje)