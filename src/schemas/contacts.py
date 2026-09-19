from pydantic import BaseModel, ConfigDict


class ContactAdd(BaseModel):
    project_id: int
    user_id: int
    email: str | None = None
    sms: int | None = None
    tg_chat_id: int | None = None

class ContactDTO(ContactAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)