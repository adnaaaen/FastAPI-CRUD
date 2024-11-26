from datetime import datetime
from pydantic import BaseModel


class TUserIn(BaseModel):
    name: str
    email: str
    contact_no: str


class TUserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    contact_no: str | None = None
    updated_at: datetime = datetime.now()


class TUser(TUserIn):
    id: int

    class Config:
        orm_mode = True
