from pydantic import BaseModel

from src.services.base import BaseService
from src.schemas.templates import TemplateAdd, TemplatePatch


class TemplateService(BaseService):

    async def add_template(self, template: TemplateAdd):
        result = await self.db.templates.add_template(template)
        await self.db.commit()
        return result

    async def get_templates(self):
        return await self.db.templates.get_all()

    async def get_template(self, template_id: int):
        return await self.db.templates.get_template(template_id)

    async def edit_template(self, data: TemplatePatch, template_id: int):
        await self.db.templates.edit(template_id, data)
        await self.db.commit()

    async def edit_template_partially(
            self, data: TemplatePatch, template_id: int, exclude_unset: bool = False
    ):
        await self.db.templates.edit(data, exclude_unset=exclude_unset, id=template_id)
        await self.db.commit()

    async def delete_template(self, template_id: int):
        await self.db.templates.delete(id=template_id)
        await self.db.commit()




