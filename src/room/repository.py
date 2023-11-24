from src.base_repository import BaseRepository
from src.room.models import Room


class RoomRepository(BaseRepository[Room]):
    model = Room
