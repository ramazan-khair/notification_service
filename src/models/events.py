from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database import Base


class EventsOrm(Base):
    __tablename__ = "events"

    event: Mapped[str] = mapped_column(unique=True)
    template_id: Mapped[int] = mapped_column(ForeignKey("templates.id"))

    channels: Mapped[list["ChannelsOrm"]] = relationship(
        back_populates="events",
        secondary="event_channels"
    )


class Event_Channels(Base):
    __tablename__ = "event_channels"
    
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))
    channel_id: Mapped[int] = mapped_column(ForeignKey("channels.id"))

