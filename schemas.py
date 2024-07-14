from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    name: str
    email: str
    contact_number: str


class UpdateUserSchema(BaseModel):
    name: str | None = None
    email: str | None = None
    contact_number: str | None


class LibraryCreateSchema(BaseModel):
    user_id: int
    book_name: str
    author: str
    department: str
    price: float


class LibraryUpdateSchema(BaseModel):
    book_name: str | None = None
    author: str | None = None
    department: str | None = None
    price: float | None = None


class LibrarySchema(BaseModel):
    user: UserCreateSchema
    books: LibraryCreateSchema
