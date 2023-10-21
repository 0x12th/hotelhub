from typing import TYPE_CHECKING

from database import Base
from sqlalchemy import Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from room.models import Room


class Hotel(Base):
    name: Mapped[str]
    country: Mapped[str]
    city: Mapped[str]
    rooms_quantity: Mapped[int]
    rating: Mapped[float] = mapped_column(
        Float(precision=1), default=0, server_default="0"
    )

    rooms: Mapped[list["Room"]] = relationship(back_populates="hotel")
