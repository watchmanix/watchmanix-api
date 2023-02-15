from pydantic import BaseModel


class MonitorInputSchema(BaseModel):
    name: str


class MonitorOutputSchema(MonitorInputSchema):
    id: int

    class Config:
        orm_mode = True


class MonitorInputPatchSchema(BaseModel):
    name: str | None = None
