from fastapi import FastAPI

from src.booking.router import booking_router
from src.hotel.router import hotel_router
from src.room.router import room_router
from src.user.router import user_router

app = FastAPI()

app.include_router(booking_router)
app.include_router(user_router)
app.include_router(room_router)
app.include_router(hotel_router)


@app.get("/")
async def main() -> str:
    return "Wellcome to HotelHub"
