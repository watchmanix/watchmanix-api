from fastapi import Depends, FastAPI

from src.api import monitors
from src.config import Settings, get_settings
from src.database import db

settings = get_settings()

app = FastAPI(
    title=settings.app.title,
    version=settings.app.version,
    description=settings.app.description,
    debug=bool(settings.secrets.DEBUG),
)

app.include_router(monitors.router)


@app.on_event("startup")
async def startup():
    print("startup")
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    print("shutdown")
    await db.close()


@app.get("/")
def home(settings: Settings = Depends(get_settings)):
    return {"hello": settings.secrets.db.URI}
