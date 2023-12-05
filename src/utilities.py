#!/usr/bin/env python3
import logging

import httpx

from models import Weather

logging.getLogger("httpx").setLevel(logging.WARNING)


def get_current_weather(location: str) -> Weather:
    url = f"https://wttr.in/{location}?format=j1"
    response = httpx.get(url)
    response.raise_for_status()
    return response.json()["current_condition"][0]
