from base_repository import BaseRepository
from hotel.models import Hotel


class HotelRepository(BaseRepository[Hotel]):
    model = Hotel
