from fastapi import APIRouter

from src.room.repository import RoomRepository
from src.room.schemas import RoomSchema

room_router = APIRouter(prefix="/rooms", tags=["Rooms"])


@room_router.get("")
async def get_rooms() -> list[RoomSchema]:
    return await RoomRepository.get_all()
