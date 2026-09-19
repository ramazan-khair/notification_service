from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped

from src.database import Base


class Device(Base):
    __tablename__ = "devices"

    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    user_id: Mapped[int]
    fcm_token: Mapped[str]

    __table_args__ = (UniqueConstraint("project_id", "user_id", name="uq_project_user"),)