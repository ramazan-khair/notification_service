from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.contacts import ContactAdd
from src.services.contacts import ContactService

router = APIRouter(prefix="/project", tags=["project"])


@router.post("")
async def add_contact(db: DBDep, data: ContactAdd):
    contact = await ContactService(db).add_contact(data)
    return {"status": "OK", "data": contact}