from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.services.notifications import NotificationService
from src.schemas.schedules import ScheduleAdd

router = APIRouter(prefix="/notifications", tags=["notifications"])




