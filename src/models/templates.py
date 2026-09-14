from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database import Base



class Template(Base):
    __tablename__ = "templates"

    name: Mapped[str] = mapped_column(unique=True)

    channels: Mapped[list["TemplateChannel"]] = relationship(
        back_populates="template",
        cascade="all, delete-orphan"
    )

class TemplateChannel(Base):
    __tablename__ = "template_channels"

    template_id: Mapped[int] = mapped_column(ForeignKey("templates.id"))
    channel: Mapped[str]
    subject: Mapped[str | None]
    body: Mapped[str]

    template: Mapped["Template"] = relationship(back_populates="channels")


    __table_args__ = (UniqueConstraint("template_id", "channel", name="uq_template_id_channel"),)