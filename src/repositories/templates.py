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



""""
    async def get_template(self, template_id: int):
        query = (
            select(Template)
            .where(Template.id == template_id)
            .options(
                selectinload(Template.channels)
            )
        )
        result = await self.session.execute(query)
        template = result.scalars().one()
        return self.mapper.map_to_domain_entity(template)
"""
#async def add(self, data: TemplateAdd):
#    query_1 = insert(Template).values(name=data.name).returning(Template)
#    result_1 = await self.session.execute(query_1)
#    template = result_1.scalars().one()
#    dicts = [i.model_dump() for i in data.channels]
#    for i in dicts:
#        i["template_id"] = template.id
#    query_2 = insert(TemplateChannel).values(dicts).returning(TemplateChannel)
#    result_2 = await self.session.execute(query_2)
#    return self.mapper.map_to_domain_entity(template)
