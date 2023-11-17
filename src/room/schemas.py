from pydantic import BaseModel


class RoomSchema(BaseModel):
    hotel_id: int
    name: str
    description: str | None
    price: int
    quantity: int
