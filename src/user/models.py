from typing import TYPE_CHECKING

from database import Base
from sqlalchemy.orm import Mapped, relationship

if TYPE_CHECKING:
    from booking.models import Booking


class User(Base):
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]

    booking: Mapped["Booking"] = relationship(back_populates="user")
