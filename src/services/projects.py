from src.services.base import BaseService


class ProjectService(BaseService):

    async def create_project(self, name: str):
        project = await self.db.projects.create_project(name=name)
        await self.db.commit()
        return project