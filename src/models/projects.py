from sqlalchemy.orm import Mapped

from src.database import Base


class Project(Base):
    __tablename__ = "projects"

    name: Mapped[str]
    hash_api_key: Mapped[str]
