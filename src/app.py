from pathlib import Path

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from models import Weather
from utilities import get_current_weather

app = FastAPI()
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


@app.post("/render_weather", response_class=HTMLResponse)
def render_weather(request: Request, location: str = Form(...)):
    weather = get_current_weather(location)
    return templates.TemplateResponse(
        "partials/weather.html",
        context={"request": request, **weather},
    )


@app.get("/weather")
def get_weather(location: str) -> Weather:
    return get_current_weather(location)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
