from datetime import date
from typing import TYPE_CHECKING

from database import Base
from sqlalchemy import Date, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from room.models import Room
    from user.models import User


class Booking(Base):
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_from: Mapped[date] = mapped_column(Date)
    date_to: Mapped[date] = mapped_column(Date)
    price: Mapped[float] = mapped_column(
        Float(precision=2), default=0, server_default="0"
    )

    user: Mapped["User"] = relationship(back_populates="booking")
    room: Mapped["Room"] = relationship(back_populates="booking")
