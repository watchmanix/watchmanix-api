import subprocess

import typer

app = typer.Typer()


@app.command()
def dev(host: str, port: int, reload: bool):
    """
    This command starts the application in development mode
    """
    subprocess.run(
        [
            "uvicorn",
            "src.main:app",
            "--host",
            host,
            "--port",
            port,
            "--reload" if reload else "",
        ]
    )
