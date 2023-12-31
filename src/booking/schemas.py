from datetime import date

from pydantic import BaseModel


class BookingSchema(BaseModel):
    id: int
    user_id: int
    room_id: int
    date_from: date
    date_to: date
    price: int
