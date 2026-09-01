from src.models.templates import TemplatesOrm
from src.repositories.base import BaseRepository


class TemplatesRepository(BaseRepository):
    model = TemplatesOrm

