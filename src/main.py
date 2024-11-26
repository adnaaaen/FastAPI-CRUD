from src.dependency.db import Base, engine
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.routes import books, users

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Library Management")

@app.get("/")
def doc_redirect() -> RedirectResponse:
    return RedirectResponse("/docs")

app.include_router(books.router, prefix="/api", tags=["Book"])
# app.include_router(users.router, prefix="/api")


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
