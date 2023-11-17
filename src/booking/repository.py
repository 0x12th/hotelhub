from base_repository import BaseRepository
from booking.models import Booking


class BookingRepository(BaseRepository[Booking]):
    model = Booking
