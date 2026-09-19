from datetime import datetime

from pydantic import BaseModel, ConfigDict


class LoggAdd(BaseModel):
    user_id: int
    status: str
    notification: str
    error: str | None = None
    sent_at: datetime | None = None

class LoggDTO(LoggAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)





