from src.base_repository import BaseRepository
from src.hotel.models import Hotel


class HotelRepository(BaseRepository[Hotel]):
    model = Hotel
