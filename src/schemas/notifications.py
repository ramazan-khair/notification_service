from datetime import date

from pydantic import BaseModel


class NotificationSend(BaseModel):
    template_channel_id: int
    user_id: int
    data: dict[str, str]





