from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from db import Base

if TYPE_CHECKING:
    from booking.models import Booking


class User(Base):
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    email: Mapped[str]
    password: Mapped[str]

    booking: Mapped["Booking"] = relationship(back_populates="user")
