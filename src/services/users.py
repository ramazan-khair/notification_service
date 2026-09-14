from src.services.base import BaseService


class UserService(BaseService):

    async def get_user(self, user_id: int):
        return self.db.users.get_one(id=user_id)