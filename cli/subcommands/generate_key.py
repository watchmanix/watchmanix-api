import secrets

import click

from scripts.cli.tools.output import Square


@click.command()
@click.option("--length", default=50, help="Number of characters in a string (key)")
def generate_key(length: int = 50):
    """
    This script generates a secret key for your application
    """
    s = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
    key = "".join(secrets.choice(s) for i in range(length))

    square = Square([key], color="blue")

    click.echo(click.style("\u2714 Your key has been generated", fg="green"))
    square.draw()
