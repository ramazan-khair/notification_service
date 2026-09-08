from src.models.templates import Template, TemplateChannel
from src.repositories.mappers.base import DataMapper
from src.schemas.templates import TemplateDTO, TemplateChannelDTO


class TemplateDataMapper(DataMapper):
    model = Template
    schema = TemplateDTO

class TemplateChannelDataMapper(DataMapper):
    model = TemplateChannel
    schema = TemplateChannelDTO