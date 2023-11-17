from pydantic import BaseModel


class HotelSchema(BaseModel):
    id: int  # noqa: A003
    name: str
    country: str
    city: str
    rooms_quantity: int
    rating: float
