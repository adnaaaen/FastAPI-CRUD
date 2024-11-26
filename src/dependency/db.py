from sqlalchemy.orm import declarative_base, sessionmaker, Session
from typing import Any
from sqlalchemy import create_engine
from .config import settings

engine = create_engine(url=settings.DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)


def get_db() -> Any:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
