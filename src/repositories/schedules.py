from src.models.schedules import Schedule
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import ScheduleDataMapper


class SchedulesRepository(BaseRepository):
    model = Schedule
    mapper = ScheduleDataMapper