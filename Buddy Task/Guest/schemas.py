from pydantic import BaseModel

class GuestSchema(BaseModel):
    guest_id: int | None = None
    guest_name: str
    guest_number: int
    guest_status: str = "Active"

    class Config:
        from_attribute = True
