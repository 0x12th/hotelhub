from fastapi import APIRouter

from src.hotel.repository import HotelRepository
from src.hotel.schemas import HotelSchema

hotel_router = APIRouter(prefix="/hotels", tags=["Hotels"])


@hotel_router.get("")
async def get_hotels() -> list[HotelSchema]:
    return await HotelRepository.get_all()
