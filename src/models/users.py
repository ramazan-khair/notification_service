from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class User(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    telegram: Mapped[str] = mapped_column(unique=True)
    sms: Mapped[str] = mapped_column(unique=True)