from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from src.database import Base


class LoggsOrm(Base):
    __tablename__ = "loggs"

    to_whom: Mapped[int] = mapped_column(ForeignKey("users.id"))
    content: Mapped[str]
    created_at: Mapped[datetime]
    is_sent: Mapped[bool]