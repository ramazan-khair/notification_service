from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


class NotificationSend(BaseModel):
    template_channel_id: int
    user_id: int
    data: dict[str, str]

class NotifcationLogAdd(BaseModel):
    user_id: int
    status: str
    notification: str
    error: str | None = None
    sent_at: datetime | None = None

class NotificationLogDTO(NotifcationLogAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)





