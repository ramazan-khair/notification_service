from src.models.templates import Template, TemplateChannel
from src.models.users import User
from src.repositories.mappers.base import DataMapper
from src.schemas.templates import TemplateDTO, TemplateChannelDTO
from src.schemas.users import UserDTO


class TemplateDataMapper(DataMapper):
    model = Template
    schema = TemplateDTO

class TemplateChannelDataMapper(DataMapper):
    model = TemplateChannel
    schema = TemplateChannelDTO

class UserDataMapper(DataMapper):
    model = User
    schema = UserDTO