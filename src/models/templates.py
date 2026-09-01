from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from src.database import Base


class Template(Base):
    __tablename__ = "templates"

    body: Mapped[str] = mapped_column(unique=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))