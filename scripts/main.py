import os


def run_dev():
    """
    This command starts the application in development mode
    """
    os.system("rm -rf ./src/*.sqlite3")
    os.system("cat ./backup.sql | sqlite3 ./src/db.sqlite3")
    os.system("fastapi-cli dev")
