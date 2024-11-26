from pydantic import BaseModel
from datetime import datetime


class TBookIn(BaseModel):
    name: str
    author: str
    department: str
    price: float


class TBook(TBookIn):
    id: int
    is_available: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class TBookUpdate(BaseModel):
    name: str | None = None
    author: str | None = None
    department: str | None = None
    price: float | None = None
    is_available: bool | None = None
    updated_at: datetime = datetime.now()
