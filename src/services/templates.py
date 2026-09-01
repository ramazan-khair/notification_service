from src.services.base import BaseService
from src.shemas.templates import TemplateAdd


class TemplateService(BaseService):
    async def create_template(self, data: TemplateAdd):
        template = self.db.templates.add(data)
        await self.db.commit()
        return template