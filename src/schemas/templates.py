from pydantic import BaseModel, HttpUrl, ConfigDict


class TemplateAdd(BaseModel):
    name: str
    channels: list[TemplateChannelAdd]

class TemplateChannelAdd(BaseModel):
    channel: str
    subject: str | None = None
    body: str

class TemplateDTO(TemplateAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)

class TemplatePatch(BaseModel):
    name: str | None = None
    channels: list[TemplateChannelAdd] | None = None



