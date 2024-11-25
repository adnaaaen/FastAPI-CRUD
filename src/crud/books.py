from sqlalchemy.orm import Session
from models import Book
from schemas import TBook, TBookUpdate
from utils import Crud, logger


class BookCrud(Crud):

    def create(self, db: Session, request: TBook) -> TBook:
        try:
            new = Book(**request.dict())
            db.add(new)
            db.commit()
            return new

        except Exception as e:
            db.rollback()
            logger.error(f"unexpected error occured {e}")


    def read(self, db: Session, id: int) -> TBook:
        try:
            result = db.query(Book).filter(Book.id == id).first()
            return result

        except Exception as e:
            db.rollback()
            logger.error(f"unexpected error occured {e}")


    def update(self, db: Session, id: int, request: TBookUpdate) -> None:

        try:
            # TODO:
            result = db.query(Book).filter(Book.id == id).first()

            # result.name = request.name if request.name is not None else result.name
            # result.author = request.name if request.name is not None else result.author
            # result.department = request.name if request.name is not None else result.department
            # result.price = request.name if request.name is not None else result.price
            # result.is_available = request.name if request.is_available is not None else result.is_available
            # result.update_at = datetime.now()



        pass
        

    def delete(self, db: Session, request: TBook) -> None:
        raise NotImplementedError



