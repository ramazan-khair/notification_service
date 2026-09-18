from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.templates import TemplateAdd, TemplatePatch
from src.services.templates import TemplateService

router = APIRouter(prefix="/template", tags=["template"])


@router.get("")
async def get_templates(db: DBDep):
    return await TemplateService(db).get_templates()

@router.post("")
async def create_template(db: DBDep, template_data: TemplateAdd):
    template = await TemplateService(db).add_template(template_data)
    return {"status": "OK", "data": template}

@router.get("/{template_id}")
async def get_template(db: DBDep ,template_id: int):
    return await TemplateService(db).get_template(template_id)

@router.patch("/{template_id}")
async def edit_template(template_id: int, template_data: TemplatePatch, db: DBDep):
    await TemplateService(db).edit_template(template_data, template_id)
    return {"status": "OK"}

@router.delete("/{template_id}")
async def delete_template(template_id: int, db: DBDep):
    await TemplateService(db).delete_template(template_id)
    return {"status": "OK"}


