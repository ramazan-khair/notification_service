from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    name: str
    email: str | None = None
    sms: str | None = None
    telegram: str | None = None
    push_token: str


class UserRequestAdd(UserBase):
    password: str


class UserAdd(UserBase):
    hashed_password: str


class UserDTO(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class UserWithHashedPassword(UserDTO):
    hashed_password: str