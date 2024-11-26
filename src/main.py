from sqlalchemy.orm import Session
from src.dependency.db import Base, engine, get_db
from fastapi import FastAPI, Depends
from src.schemas.books import TBookCreate, TBook
from src.crud import BooksCrud

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Library")


@app.post("/api/users", response_model=TBook)
async def create_user(request: TBookCreate, db: Session = Depends(get_db)):
    result = await BooksCrud.create(request=request, db=db)
    return result


# @app.patch("/api/users/{id}", response_model=TBook)
# async dedf


#
# @app.get("/api/users/list")
# async def list_all_users(
#     skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
# ):
#     response = crud.list_all_users(db, skip, limit)
#     return response if response else HTTPException(status_code=404)
#
#
# @app.post("/api/users/create")
# async def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
#     responds = crud.create_user(db, user)
#     return responds
#
#
# @app.get("/api/users/id/{user_id}")
# async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
#     responds = crud.get_user_by_id(db, user_id)
#     return responds if responds else HTTPException(status_code=404)
#
#
# @app.put("/api/users/books/update/{book_id}")
# async def update_book_by_id(
#     book_id: int, updated_book: LibraryUpdateSchema, db: Session = Depends((get_db))
# ):
#     responds = crud.update_book(db, book_id, updated_book)
#     return responds if responds else HTTPException(status_code=404)
#
#
# @app.delete("/api/users/books/delete/{book_id}")
# async def delete_book_by_id(book_id: int, db: Session = Depends(get_db)):
#     responds = crud.delete_book(db, book_id)
#     return responds if responds else HTTPException(status_code=202)
