
from src.models.loggs import Logg
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import LoggDataMapper


class LoggsRepository(BaseRepository):
    model = Logg
    mapper = LoggDataMapper
