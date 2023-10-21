from typing import TYPE_CHECKING

from database import Base
from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from booking.models import Booking
    from hotel.models import Hotel


class Room(Base):
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"))
    name: Mapped[str]
    description: Mapped[str | None] = mapped_column(String(250))
    price: Mapped[float] = mapped_column(
        Float(precision=2), default=0, server_default="0"
    )
    country: Mapped[str]
    city: Mapped[str]
    rooms_quantity: Mapped[int]
    quantity: Mapped[int]
    rating: Mapped[float] = mapped_column(
        Float(precision=1), default=0, server_default="0"
    )

    hotel: Mapped["Hotel"] = relationship(back_populates="rooms")
    booking: Mapped["Booking"] = relationship(back_populates="room")
