from database import Base, engine, SessionLocal
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
from schemas import (
    UserCreateSchema,
    UpdateUserSchema,
    LibraryCreateSchema,
    LibraryUpdateSchema,
)

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/users/list")
async def list_all_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    response = crud.list_all_users(db, skip, limit)
    return response if response else HTTPException(status_code=404)


@app.post("/api/users/create")
async def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    responds = crud.create_user(db, user)
    return responds


@app.get("/api/users/id/{user_id}")
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    responds = crud.get_user_by_id(db, user_id)
    return responds if responds else HTTPException(status_code=404)


@app.get("/api/users/books/list")
async def get_all_book(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    response = crud.get_all_book(db, skip, limit)
    return response if response else HTTPException(status_code=404)


@app.post("/api/users/books/create")
async def create_book(book: LibraryCreateSchema, db: Session = Depends(get_db)):
    return crud.create_book_by_user(db, book)


@app.put("/api/users/books/update/{book_id}")
async def update_book(
    book_id: int, updated_book: LibraryUpdateSchema, db: Session = Depends((get_db))
):
    responds = crud.update_book(db, book_id, updated_book)
    return responds if responds else HTTPException(status_code=404)


@app.delete("/api/users/books/delete/{user_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    responds = crud.delete_book(db, book_id)
    return responds if responds else HTTPException(status_code=202)


@app.put("/api/users/update/{user_id}")
async def update_user_by_id(
    user_id: int, updated_user: UpdateUserSchema, db: Session = Depends(get_db)
):
    user_by_id = crud.update_user_by_id(db, user_id, updated_user)
    return user_by_id if user_by_id else HTTPException(status_code=404)


@app.delete("/api/users/delete/{user_id}")
async def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    response = crud.delete_by_id(db, user_id)
    return response if response else HTTPException(status_code=400)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
