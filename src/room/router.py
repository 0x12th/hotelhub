from fastapi import APIRouter

from room.repository import RoomRepository
from room.schemas import RoomSchema

room_router = APIRouter(prefix="/rooms", tags=["Rooms"])


@room_router.get("")
async def get_rooms() -> list[RoomSchema]:
    return await RoomRepository.get_all()
