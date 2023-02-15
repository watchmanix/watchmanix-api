import secrets
import subprocess

import typer
from rich import print as rich_print

app = typer.Typer()
# app.add_typer()


@app.callback()
def callback():
    """
    Awesome Portal Gun
    """


@app.command(name="dev")
def cli_dev(
    host: str = typer.Option(default="127.0.0.1", help="Bind socket to this host."),
    port: str = typer.Option(default="8000", help="Bind socket to this port."),
    reload: bool = typer.Option(default=True, help="Bind socket to this port."),
):
    """Run dev server"""
    rich_print(
        ":rocket: [bold yellow]Attention![/bold yellow] [green]Launched dev server![/green]",
        sep="\n",
    )
    subprocess.run(
        [
            "uvicorn",
            "src.main:app",
            "--host",
            host,
            "--port",
            port,
            "--reload" if reload else "",
        ],
        capture_output=False,
        check=True,
    )


@app.command(name="gen_key")
def cli_generate_key(
    length: int = typer.Option(default=32, help="Number of characters in the key")
):
    """
    This script generates a secret key for your application
    """
    from rich.panel import Panel

    s = "abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)"
    key = "".join(secrets.choice(s) for i in range(length))
    rich_print(Panel(f"Your key, [red]{key}!", title="Hello :rocket:"))
