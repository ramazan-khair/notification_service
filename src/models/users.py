from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.models.loggs import NotificationLog


class User(Base):
    __tablename__ = "users"

    name: Mapped[str]
    email: Mapped[str | None] = mapped_column(unique=True)
    phone: Mapped[str | None] = mapped_column(unique=True)
    telegram: Mapped[str | None] = mapped_column(unique=True)

    logs: Mapped[list["NotificationLog"]] = relationship(back_populates="user")
