from typing import TYPE_CHECKING

from sqlalchemy import REAL
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base

if TYPE_CHECKING:
    from room.models import Room


class Hotel(Base):
    name: Mapped[str]
    country: Mapped[str]
    city: Mapped[str]
    rooms_quantity: Mapped[int]
    rating: Mapped[float] = mapped_column(
        REAL(precision=1), default=0, server_default="0"
    )

    rooms: Mapped[list["Room"]] = relationship(back_populates="hotel")
