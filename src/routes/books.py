from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.dependency.db import get_db
from src.schemas import TBook, TBookIn, TBookUpdate
from src.crud import BooksCrud

router = APIRouter()


@router.post("/books", response_model=TBook)
async def create_book(request: TBookIn, db: Session = Depends(get_db)):
    new_book = await BooksCrud.create(db=db, request=request)
    return new_book


@router.get("/books/{id}", response_model=TBook)
async def get_book(id: int, db: Session = Depends(get_db)) -> Any:
    book = await BooksCrud.read(db=db, id=id)
    return book


@router.patch("/books/{id}", response_model=TBook)
async def update_book(
    id: int, request: TBookUpdate, db: Session = Depends(get_db)
) -> Any:
    updated_book = await BooksCrud.update(id=id, db=db, request=request)
    return updated_book


@router.delete("/books/{id}", response_model=TBook)
async def delete_book(id: int, db: Session = Depends(get_db)):
    delete_status = await BooksCrud.delete(db=db, id=id)
    return delete_status
