from pydantic import BaseModel

class TBook(BaseModel):
    id: str
    name: str
    author: str
    department: str
    price: float
    is_available: bool = True

class TBookUpdate(BaseModel):
    name : str | None = None
    author: str | None = None
    department: str | None = None
    price: float | None = None
    is_available: float | None = None
