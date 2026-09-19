from src.schemas.contacts import ContactDTO, ContactAdd
from src.services.base import BaseService


class ContactService(BaseService):

    async def add_contact(self, data: ContactAdd):
        contact = await self.db.contacts.add(data)
        await self.db.commit()
        return contact