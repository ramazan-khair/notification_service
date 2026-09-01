from src.models.schedules import Schedule
from src.repositories.mappers.base import DataMapper
from src.shemas.schedules import ScheduleAdd


class ScheduleDataMapper(DataMapper):
    db_model = Schedule
    schema = ScheduleAdd