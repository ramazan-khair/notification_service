from pydantic import BaseModel


class ScheduleAdd(BaseModel):
    user_id: int
    event_id: int
    days: list[str]
    time: str

