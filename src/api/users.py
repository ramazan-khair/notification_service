from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.services.schedules import ScheduleService
from src.shemas.schedules import ScheduleAdd

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/schedule/{user_id}")
async def set_schedule(
        db: DBDep,
        user_id: int,
        data: ScheduleAdd
):
    await ScheduleService(db).set_schedule(user_id, data)
    return {"status": "OK"}