from src.models.contacts import Contact
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import ContactDataMapper


class ContactsRepository(BaseRepository):
    model = Contact
    mapper = ContactDataMapper