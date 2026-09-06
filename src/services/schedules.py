from src.services.base import BaseService
from src.schemas.schedules import ScheduleAdd


class ScheduleService(BaseService):
    async def set_schedule(self, data: ScheduleAdd):
        await self.db.sсhedules.add(data)
        await self.db.commit()

