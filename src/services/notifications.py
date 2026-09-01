from pydantic import BaseModel

from src.services.base import BaseService
from jinja2 import Template


class NotificationService(BaseService):
    async def send_notification(self, event_id: int, data: BaseModel):
        template = self.db.templates.get_one(event_id=event_id)
        notification = Template(template.body).render(**data.model_dump())
        #send_notification.delay(notification)
        return notification

    async def send_scheduled_notification(self, user_id: int):
        schedule = await self.db.schedules.get_one(user_id=user_id)
        #send_scheduled_notification.delay(schedule)

