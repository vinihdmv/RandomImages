from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests

app = FastAPI()

# Montar a pasta 'static' para servir arquivos CSS, JS, imagens etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar a pasta de templates (onde estão base.html, index.html)
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/random-animal-url", response_class=JSONResponse)
def get_random_animal_url():
    """Rota que obtém imagem aleatória de cachorro via Dog API."""
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    # A API retorna algo como {"message": "https://...", "status": "success"}
    data = response.json()                      

    return {"url": data["message"]}



