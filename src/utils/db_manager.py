from src.repositories.contacts import ContactsRepository
from src.repositories.loggs import LoggsRepository
from src.repositories.projects import ProjectsRepository
from src.repositories.templates import TemplatesRepository, TemplateChannelsRepository
from src.repositories.devices import DevicesRepository


class DBManager:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.templates = TemplatesRepository(self.session)
        self.templatechannels = TemplateChannelsRepository(self.session)
        self.loggs = LoggsRepository(self.session)
        self.projects = ProjectsRepository(self.session)
        self.contacts = ContactsRepository(self.session)
        self.devices = DevicesRepository(self.session)

        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()