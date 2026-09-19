from pydantic import BaseModel, ConfigDict


class DeviceAdd(BaseModel):
    project_id: int
    user_id: int
    fcm_token: str

class DeviceDTO(DeviceAdd):
    id: int

    model_name = ConfigDict(from_attributes=True)