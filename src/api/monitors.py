from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic.schema import model_type_schema

from src.database import db
from src.queries.monitors import (
    delete_monitor_by_id,
    get_list_monitors,
    get_monitor_by_id,
    insert_monitor,
)
from src.schemas.monitors import MonitorInputSchema, MonitorOutputSchema

router = APIRouter(prefix="/monitors", tags=["Мониторы"])


@router.get("/")
async def monitor_list() -> list[MonitorOutputSchema]:
    monitors = await db.fetchall(get_list_monitors)
    if monitors:
        return [MonitorOutputSchema.parse_obj(monitor) for monitor in monitors]
    else:
        raise HTTPException(404)


@router.post("/")
async def monitor_add(input_monitor: MonitorInputSchema):
    monitor_id = await db.insert_and_return_id(
        insert_monitor,
        input_monitor.name,
    )
    monitor = await db.fetchone(get_monitor_by_id, monitor_id)
    if monitor:
        return MonitorOutputSchema(**monitor)
    else:
        raise HTTPException(404)


@router.get("/{monitor_id}")
async def monitor_by_id(monitor_id: int) -> MonitorOutputSchema:
    monitor = await db.fetchone(get_monitor_by_id, monitor_id)
    if monitor:
        return MonitorOutputSchema(**monitor)
    else:
        raise HTTPException(404)


@router.patch("/{monitor_id}")
async def update_monitor(
    monitor_id: int,
    input_monitor: MonitorInputSchema,
) -> MonitorOutputSchema:
    # TODO: Add PATCH monitor after update database
    monitor = await db.fetchone(get_monitor_by_id, monitor_id)
    print(input_monitor.dict(exclude_unset=True))
    if monitor:
        return MonitorOutputSchema(**monitor)
    else:
        raise HTTPException(404)


@router.delete("/{monitor_id}")
async def delete_monitor(monitor_id: int):
    monitor = await db.fetchone(get_monitor_by_id, monitor_id)
    if monitor:
        await db.execute(delete_monitor_by_id, monitor_id)
    else:
        raise HTTPException(404)
    return JSONResponse(dict(), status_code=status.HTTP_200_OK)
