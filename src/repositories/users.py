from src.models.users import User
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import UserDataMapper


class UsersRepository(BaseRepository):
    model = User
    mapper = UserDataMapper