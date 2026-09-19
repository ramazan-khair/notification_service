import typing

from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database import Base


class Logg(Base):
    __tablename__ = "notification_logs"

    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    user_id: Mapped[int]
    status: Mapped[str]
    notification: Mapped[str]
    error: Mapped[str | None]
    sent_at: Mapped[datetime] = mapped_column(default=datetime.now)

