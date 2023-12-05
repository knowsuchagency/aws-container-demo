from mangum import Mangum

from app import app as asgi_app
from utilities import get_current_weather

app = Mangum(asgi_app, lifespan="off")


def handler(event, context):
    if event.get("requestContext", {}).get("http", {}):
        # this means the AWS Lambda was invoked via its own URL
        return app(event, context)

    assert "location" in event, "location is required"

    return get_current_weather(event["location"])
