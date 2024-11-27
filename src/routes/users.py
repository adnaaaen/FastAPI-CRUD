from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.dependency.db import get_db
from src.schemas import TUser, TUserIn, TUserUpdate
from src.crud import UsersCrud

router = APIRouter()


@router.post("/users", response_model=TUser)
async def create_user(request: TUserIn, db: Session = Depends(get_db)):
    new_user = await UsersCrud.create(db=db, request=request)
    return new_user


@router.get("/users/{id}", response_model=TUser)
async def get_user(id: int, db: Session = Depends(get_db)) -> Any:
    user = await UsersCrud.read(db=db, id=id)
    return user


@router.patch("/users/{id}", response_model=TUser)
async def update_user(
    id: int, request: TUserUpdate, db: Session = Depends(get_db)
) -> Any:
    updated_user = await UsersCrud.update(id=id, db=db, request=request)
    return updated_user


@router.delete("/users/{id}", response_model=TUser)
async def delete_user(id: int, db: Session = Depends(get_db)):
    delete_status = await UsersCrud.delete(db=db, id=id)
    return delete_status
