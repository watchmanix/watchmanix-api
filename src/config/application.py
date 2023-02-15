from pydantic import BaseModel


class AppSettings(BaseModel):
    title: str = "Watchmanix API"
    version: str = "0.1.0"
    description: str = "Watchmanix API Description coming soon"
