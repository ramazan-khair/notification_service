from pydantic import BaseModel
from sqlalchemy import insert, select, update
from sqlalchemy.orm import selectinload

from src.models.templates import Template, TemplateChannel
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import TemplateDataMapper, TemplateChannelDataMapper
from src.schemas.templates import TemplateAdd, TemplateChannelAdd, TemplatePatch


class TemplateChannelsRepository(BaseRepository):
    model = TemplateChannel
    mapper = TemplateChannelDataMapper

class TemplatesRepository(BaseRepository):
    model = Template
    mapper = TemplateDataMapper

    async def add_template(self, data: TemplateAdd):
        template = Template(name=data.name)
        template.channels = [
            TemplateChannel(
                channel=item.channel,
                subject=item.subject,
                body=item.body
            )
            for item in data.channels
        ]
        self.session.add(template)
        await self.session.flush()
        return self.mapper.map_to_domain_entity(template)

    async def get_templates(self):
        return await self.get_all(
            options=(selectinload(Template.channels),)
        )

    async def get_template(self, template_id: int):
        return await self.get_one_orm(
            selectinload(Template.channels),
            id=template_id
        )

    async def edit(self, template_id: int, data: TemplatePatch) -> None:
        template = await self.get_template(template_id)
        if data.name:
            template.name = data.name
        if data.channels is not None:
            template.channels = [
                TemplateChannel(
                    channel=item.channel,
                    subject=item.subject,
                    body=item.body
                )
                for item in data.channels
            ]
        await self.session.flush()

    async def delete(self, template_id: int):
        template = await self.get_template(template_id)
        await self.session.delete(template)
        await self.session.flush()


