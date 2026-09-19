import hashlib
import logging
import secrets

from asyncpg import UniqueViolationError
from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError


from src.models.projects import Project
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import ProjectDataMapper
from src.schemas.projects import ProjectResponse


class ProjectsRepository(BaseRepository):
    model = Project
    mapper = ProjectDataMapper

    @staticmethod
    def generate_api_key() -> str:
        return secrets.token_urlsafe(32)

    @staticmethod
    def hash_api_key(api_key: str) -> str:
        return hashlib.sha256(
            api_key.encode("utf-8")
        ).hexdigest()

    async def create_project(self, name: str):
        try:
            api_key = self.generate_api_key()
            data_1 = {"name": name, "api_key": self.hash_api_key(api_key)}
            add_data_stmt = insert(Project).values(**data_1).returning(Project)
            result = await self.session.execute(add_data_stmt)
            model = result.scalars().one()
            data_2 = {
                id: model.id,
                name: model.name,
                api_key: api_key
            }
            project_response = ProjectResponse(**data_2)
            return project_response
        except IntegrityError as ex:
            logging.exception(f"Не удалось добавить данные в БД, входные данные={name}")
            if isinstance(ex.orig.__cause__, UniqueViolationError):
                raise ObjectAlreadyExistsException from ex
            else:
                logging.exception(
                    f"Незнакомая ошибка: не удалось добавить данные в БД, входные данные={name}"
                )
                raise ex