import logging
from pathlib import Path

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from models import Weather
from utilities import get_current_weather, get_icon

app = FastAPI()
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


@app.post("/weather", response_class=HTMLResponse)
def render_weather_html(request: Request, location: str = Form(...)):
    weather = get_current_weather(location)
    icon = None
    try:
        description = weather["weatherDesc"][0]["value"]
        icon = get_icon(description)["bs_icon"]
    except Exception as e:
        logging.exception(e)
    return templates.TemplateResponse(
        "partials/weather.html",
        context={"request": request, "icon": icon, **weather},
    )


@app.get("/weather")
def get_weather(location: str) -> Weather:
    return get_current_weather(location)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
