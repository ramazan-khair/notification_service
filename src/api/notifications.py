from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.services.notifications import NotificationService
from src.services.users import UserService

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.post("")
async def send_notification(db: DBDep, user_id: int, template_channel_id: int,  data: dict[str, str]):
    await NotificationService(db).send_notification(user_id, template_channel_id, data)
    return {"status": "OK"}




