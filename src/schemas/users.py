from pydantic import BaseModel

class TUser(BaseModel):
    id: str
    name: str
    email: str
    contact_no: str

class TUserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    contact_no: str | None = None

