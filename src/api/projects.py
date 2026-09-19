from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.services.projects import ProjectService

router = APIRouter(prefix="/project", tags=["project"])


@router.post("")
async def create_project(db: DBDep, name: str):
    project = await ProjectService(db).create_project(name=name)
    return {"status": "OK", "data": project}
