from src.base_repository import BaseRepository
from src.booking.models import Booking


class BookingRepository(BaseRepository[Booking]):
    model = Booking
