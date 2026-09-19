from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base



class Contact(Base):
    __tablename__ = "contacts"

    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    user_id: Mapped[str]
    email: Mapped[str | None] = mapped_column(unique=True)
    sms: Mapped[str | None] = mapped_column(unique=True)
    tg_chat_id: Mapped[str | None] = mapped_column(unique=True)

    __table_args__ = (UniqueConstraint("project_id", "user_id", name="uq_project_user"),)


