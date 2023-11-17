from base_repository import BaseRepository
from room.models import Room


class RoomRepository(BaseRepository[Room]):
    model = Room
