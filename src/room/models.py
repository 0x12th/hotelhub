from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base

if TYPE_CHECKING:
    from booking.models import Booking
    from hotel.models import Hotel


class Room(Base):
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"))
    name: Mapped[str]
    description: Mapped[str | None] = mapped_column(String(250))
    price: Mapped[int] = mapped_column(default=0, server_default="0")
    quantity: Mapped[int]

    hotel: Mapped["Hotel"] = relationship(back_populates="rooms")
    booking: Mapped["Booking"] = relationship(back_populates="room")
