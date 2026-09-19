from src.models.devices import Device
from src.models.loggs import Logg
from src.models.projects import Project
from src.models.templates import Template, TemplateChannel
from src.models.contacts import Contact
from src.repositories.mappers.base import DataMapper
from src.schemas.contacts import ContactDTO
from src.schemas.devices import DeviceDTO
from src.schemas.loggs import LoggDTO
from src.schemas.projects import ProjectDTO
from src.schemas.templates import TemplateDTO, TemplateChannelDTO


class TemplateDataMapper(DataMapper):
    model = Template
    schema = TemplateDTO

class TemplateChannelDataMapper(DataMapper):
    model = TemplateChannel
    schema = TemplateChannelDTO

class ProjectDataMapper(DataMapper):
    model = Project
    schema = ProjectDTO

class LoggDataMapper(DataMapper):
    model = Logg
    schema = LoggDTO

class ContactDataMapper(DataMapper):
    model = Contact
    schema = ContactDTO

class DeviceDataMapper(DataMapper):
    model = Device
    schema = DeviceDTO