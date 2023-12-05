#!/usr/bin/env python3
import logging

import httpx

from models import Weather, WeatherIcon
from magentic import prompt

logging.getLogger("httpx").setLevel(logging.WARNING)


def get_current_weather(location: str) -> Weather:
    url = f"https://wttr.in/{location}?format=j1"
    response = httpx.get(url, timeout=10)
    response.raise_for_status()
    return response.json()["current_condition"][0]


@prompt(
    "Return the best VALID appropriate bootstrap icon for the given weather description: {description}"
)
def get_icon(description: str) -> WeatherIcon:
    ...
