import click
import rich

from utilities import get_current_weather


@click.command(name="weather")
@click.argument("location")
def cli(location: str):
    """Get the weather for a location."""
    rich.print(get_current_weather(location))
