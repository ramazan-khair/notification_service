from src.models import NotificationLog
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import NotificationLogDataMapper


class NotificationLogsRepository(BaseRepository):
    model = NotificationLog
    mapper = NotificationLogDataMapper
