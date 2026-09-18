import typing

from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database import Base
if typing.TYPE_CHECKING:
    from src.models.templates import TemplateChannel
    from src.models.users import User


class NotificationLog(Base):
    __tablename__ = "notification_logs"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    status: Mapped[str]
    notification: Mapped[str]
    error: Mapped[str | None]
    sent_at: Mapped[datetime] = mapped_column(default=datetime.now)

    user: Mapped["User"] = relationship(back_populates="logs")
