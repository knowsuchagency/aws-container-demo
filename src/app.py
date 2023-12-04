#!/usr/bin/env python3
import logging
import os
import re
from pathlib import Path
import subprocess as sp

import click
import httpx
import rich
from litestar import Litestar, get, post, Request
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.response import Template
from litestar.template import TemplateConfig
from mangum import Mangum

from models import Weather

os.environ["LITESTAR_WARN_IMPLICIT_SYNC_TO_THREAD"] = "0"

logging.getLogger("httpx").setLevel(logging.WARNING)


def get_current_weather(location: str) -> Weather:
    url = f"https://wttr.in/{location}?format=j1"
    response = httpx.get(url)
    response.raise_for_status()
    return response.json()["current_condition"][0]


@post("/forecast")
async def render_forecast(request: Request) -> Template:
    body = (await request.body()).decode()
    location = re.search(r"location=(\w+)", body).group(1)
    return Template(
        "partials/forecast.html",
        context=get_current_weather(location),
    )


@get("/weather")
def weather(location: str) -> Weather:
    return get_current_weather(location)


@get("/")
def index() -> Template:
    return Template("index.html")


app = Litestar(
    route_handlers=[index, weather, render_forecast],
    template_config=TemplateConfig(
        directory=Path(__file__).parent / "templates",
        engine=JinjaTemplateEngine,
    ),
)

lambda_handler = Mangum(app.asgi_handler, lifespan="off")


@click.command(name="weather")
@click.argument("location")
def cli(location: str):
    """Get the weather for a location."""
    result = get_current_weather(location)
    rich.print(result)


if __name__ == "__main__":
    if os.getenv("AWS_LAMBDA_FUNCTION_NAME"):
        sp.run(["/lambda-entrypoint.sh", "app.lambda_handler"])
    else:
        cli()
