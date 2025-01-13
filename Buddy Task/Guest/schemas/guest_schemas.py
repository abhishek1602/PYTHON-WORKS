from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum

class GuestStatus(str, Enum):
    pending = "pending"
    active = "active"
    inactive = "inactive"

class GuestBase(BaseModel):
    status: GuestStatus
    name: str
    email: EmailStr
    phone: str = Field(..., pattern=r"^\+?\d{10,15}$")
    address: str
    city: str
    state: str
    zip: str
    country: str

class GuestUpdate(BaseModel):
    status: Optional[GuestStatus] = None
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    country: Optional[str] = None

class GuestInfo(BaseModel):
    id: int
    status: GuestStatus
    name: str
    email: str
    phone: str
    address: str
    city: str
    state: str
    zip: str
    country: str
