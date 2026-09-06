from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database import Base
from src.models.templates import TemplateChannel
from src.models.users import User


class NotificationLog(Base):
    __tablename__ = "notification_logs"

    template_channel_id: Mapped[int] = mapped_column(ForeignKey("template_channels.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    status: Mapped[str]
    notification: Mapped[str]
    error: Mapped[str | None]
    sent_at: Mapped[datetime] = mapped_column(default=datetime.now)

    user: Mapped["User"] = relationship(back_populates="logs")
    template_channel: Mapped["TemplateChannel"] = relationship(back_populates="logs")
