from pydantic import BaseModel


class TemplateAdd(BaseModel):
    template: str
    event_id: int