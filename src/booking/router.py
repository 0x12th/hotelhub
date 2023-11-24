from fastapi import APIRouter

from src.booking.repository import BookingRepository
from src.booking.schemas import BookingSchema

booking_router = APIRouter(prefix="/bookings", tags=["Bookings"])


@booking_router.get("")
async def get_bookings() -> list[BookingSchema]:
    return await BookingRepository.get_all()
