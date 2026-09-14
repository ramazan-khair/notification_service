from pydantic import BaseModel, ConfigDict


class UserAdd(BaseModel):
    name: str
    email: str | None = None
    sms: str | None = None
    telegram: str | None = None

class UserDTO(UserAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)