from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.utils import BaseCrud
from src.schemas import TUser, TUserIn, TUserUpdate
from src.models import User
from src.utils import logger

class UserCrud(BaseCrud):

    async def create(self, db: Session, request: TUserIn) -> TUser | None:
        try:
            db_user = User(**request.dict())
            db.add(db_user)
            db.commit()
            return db_user
        except SQLAlchemyError as s:
            db.rollback()
            logger.error(f"DataBase Error occurred when create user, {s}")
            return None
        except Exception as e:
            logger.error(f"unexpected error occurred {e}")
            return None

    async def read(self, db: Session, id: int) -> TUser | None:
        try:
            result = db.query(User).filter(User.id == id).first()
            return result if result else None
        except SQLAlchemyError as s:
            db.rollback()
            logger.error(f"DataBase Error occurred when read user with ID: {id}, {s}")
            return None
        except Exception as e:
            logger.error(f"unexpected error occurred {e}")
            return None

    async def update(self, db: Session, id: int, request: TUserUpdate) -> TUser | None:
        try:
            result = db.query(User).filter(User.id == id).first()
            if result:
                for key, value in request.dict(exclude_none=True).items():
                    setattr(result, key, value)
                db.commit()
                return result
            return None
        except SQLAlchemyError as s:
            db.rollback()
            logger.error(f"DataBase Error occurred when update user with ID: {id}, {s}")
            return None
        except Exception as e:
            logger.error(f"unexpected error occurred {e}")
            return None

    async def delete(self, db: Session, id: int) -> bool:
        try:
            db_user = db.query(User).filter(User.id == id).first()
            if db_user is None:
                return False
            db.delete(db_user)
            db.commit()
            return True
        except SQLAlchemyError as s:
            db.rollback()
            logger.error(f"DataBase Error occurred when delete user with ID: {id}, {s}")
            return False
        except Exception as e:
            logger.error(f"unexpected error occurred {e}")
            return False
