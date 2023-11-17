from fastapi import FastAPI

from booking.router import booking_router
from hotel.router import hotel_router
from room.router import room_router
from user.router import user_router

app = FastAPI()

app.include_router(booking_router)
app.include_router(user_router)
app.include_router(room_router)
app.include_router(hotel_router)


@app.get("/")
async def main() -> str:
    return "Wellcome to HotelHub"
