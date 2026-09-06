from src.models.templates import Template
from src.repositories.mappers.base import DataMapper
from src.schemas.templates import TemplateDTO


class TemplateDataMapper(DataMapper):
    model = Template
    schema = TemplateDTO