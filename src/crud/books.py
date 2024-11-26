from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models import Book
from src.schemas import TBookIn, TBookUpdate, TBook
from src.utils import BaseCrud, logger


class BookCrud(BaseCrud):

    async def create(self, db: Session, request: TBookIn) -> TBook | None:
        try:
            db_book = Book(**request.dict())
            db.add(db_book)
            db.commit()
            return db_book
        except SQLAlchemyError as s:
            db.rollback()
            logger.error(f"DataBase Error occurred when create book, {s}")
            return None
        except Exception as e:
            logger.error(f"unexpected error occurred {e}")
            return None

    async def read(self, db: Session, id: int) -> TBook | None:
        try:
            result = db.query(Book).filter(Book.id == id).first()
            return result if result else None
        except SQLAlchemyError as s:
            db.rollback()
            logger.error(f"DataBase Error occurred when read book with ID: {id}, {s}")
            return None
        except Exception as e:
            logger.error(f"unexpected error occurred {e}")
            return None

    async def update(self, db: Session, id: int, request: TBookUpdate) -> TBook | None:
        try:
            result = db.query(Book).filter(Book.id == id).first()
            if result:
                for key, value in request.dict(exclude_none=True).items():
                    setattr(result, key, value)
                db.commit()
                return result
            return None
        except SQLAlchemyError as s:
            db.rollback()
            logger.error(f"DataBase Error occurred when update book with ID: {id}, {s}")
            return None
        except Exception as e:
            logger.error(f"unexpected error occurred {e}")
            return None

    async def delete(self, db: Session, id: int) -> bool:
        try:
            db_book = db.query(Book).filter(Book.id == id).first()
            if db_book is None:
                return False
            db.delete(db_book)
            db.commit()
            return True
        except SQLAlchemyError as s:
            db.rollback()
            logger.error(f"DataBase Error occurred when delete book with ID: {id}, {s}")
            return False
        except Exception as e:
            logger.error(f"unexpected error occurred {e}")
            return False
