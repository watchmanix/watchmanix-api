from pathlib import Path

from pydantic import BaseModel


class DatabaseSettings(BaseModel):
    db_name: str = "db.sqlite3"

    @property
    def URI(self):
        path_to_file = Path() / "src" / self.db_name
        return path_to_file.absolute().__str__()
