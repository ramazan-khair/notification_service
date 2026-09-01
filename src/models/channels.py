from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database import Base


class ChannelsOrm(Base):
    __tablename__ = "channels"

    channel: Mapped[str] = mapped_column(unique=True)

    events: Mapped[list["EventsOrm"]] = relationship(
        back_populates="channels",
        secondary="event_channels"
    )