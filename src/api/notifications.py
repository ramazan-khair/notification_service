from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.services.notifications import NotificationService
from src.shemas.notifications import UserRegistered, PaymentSuccess, OrderShipped
from src.shemas.schedules import ScheduleAdd

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.post("/{event_id}")
async def send_notification(
        db: DBDep,
        event_id: int,
        data: UserRegistered | PaymentSuccess | OrderShipped
):
    notification = await NotificationService(db).send_notification(event_id, data)
    return {"status": "OK", "notification": notification}

@router.post("/{user_id}")
async def send_scheduled_notification(
        db: DBDep,
        user_id: int
):
    notification = await NotificationService(db).send_scheduled_notification(user_id)
    return {"status": "OK", "notification": notification}
