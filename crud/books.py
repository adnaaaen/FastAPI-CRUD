from sqlalchemy.orm import Session
from models import Book
from schemas import TBook, TBookUpdate
from utils import Crud


class BookCrud(Crud):

    def create(self, db: Session, request: TBook) -> TBook:
        try:
            new = Book(**request.dict())
            db.add(new)
            db.commit()
            return new
        except Exception:
            # TODO: add logging

    def read(self, db: Session, id: int) -> TBook:
        return db.query(Book).filter(Book.id == id).all()

    def update(self, request: TBookUpdate, db: Session) -> None:
        

    def delete(self, request: TBook, db: Session) -> None:
        raise NotImplementedError



