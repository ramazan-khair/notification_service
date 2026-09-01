from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.services.templates import TemplateService
from src.shemas.templates import TemplateAdd

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("")
async def create_template(db: DBDep, data: TemplateAdd):
    template = await TemplateService(db).create_template(data)
    return {"status": "OK", "data": template}