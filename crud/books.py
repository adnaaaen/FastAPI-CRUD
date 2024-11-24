from sqlalchemy.orm import Session
from models import Book
from schemas import TBook, TBookUpdate


class BookCrud:

    def create(self, request: TBook, db: Session) -> TBook:
        try:
            new = Book(**request)
            db.add(new)
            db.commit()
            return new
        except Exception:
            # TODO: add logging

    def read(self) -> None:
        raise NotImplementedError

    def delete(self) -> None:
        raise NotImplementedError

    def update(self) -> None:
        raise NotImplementedError

