from pydantic import BaseModel, ConfigDict


class ProjectAdd(BaseModel):
    name: str
    hash_api_key: str

class ProjectResponse(BaseModel):
    id: int
    name: str
    api_key: str

class ProjectDTO(BaseModel):
    id: int

    model_config = ConfigDict(from_attributes=True)