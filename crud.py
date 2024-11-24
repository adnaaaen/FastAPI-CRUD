from models import User, Book 

from schemas import (
    UserCreateSchema,
    UpdateUserSchema,
    LibraryUpdateSchema,
    LibraryCreateSchema,
)
from sqlalchemy.orm import Session


# user crud
def list_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreateSchema):
    new_user = User(
        name=user.name, email=user.email, contact_number=user.contact_number
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def update_user_by_id(db: Session, user_id, user: UpdateUserSchema):
    user_by_id = db.query(User).filter(User.id == user_id).first()
    if user_id:
        user_by_id.name = user.name if user.name else ...
        user_by_id.email = user.email if user.email else ...
        user_by_id.contact_number = user.contact_number if user.contact_number else ...

        db.commit()
        db.refresh(user_by_id)
    return user_by_id


def delete_by_id(db: Session, user_id: int):
    user_by_id = db.query(User).filter(User.id == user_id).first()
    db.delete(user_by_id) if user_by_id else ...
    db.commit()
    return user_by_id


# library crud
def create_book_by_user(db: Session, book_data: LibraryCreateSchema):
    new_book = Book(
        user_id=book_data.user_id,
        book_name=book_data.book_name,
        author=book_data.author,
        department=book_data.department,
        price=book_data.price,
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def get_all_book(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()


def get_book_by_id(db: Session, book_id: int):
    response = db.query(Book).filter(Book.book_id).first()
    return response


def delete_book(db: Session, book_id: int):
    response = (
        db.query(Book).filter(Book.book_id == book_id).first()
    )
    if response:
        db.delete(response)
        db.commit()
    return response


def update_book(db: Session, book_id: int, updated_book: LibraryCreateSchema):
    data = db.query(Book).filter(Book.book_id == book_id).first()
    if data:
        data.book_name = updated_book.book_name
        data.author = updated_book.author
        data.department = updated_book.department
        data.price = updated_book.price
    db.commit()
    db.refresh(data)
    return data
