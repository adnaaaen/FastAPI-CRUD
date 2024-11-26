from sqlalchemy import Column, VARCHAR, INTEGER, BOOLEAN, FLOAT, DATETIME
from src.dependency.db import Base
from datetime import datetime


class Book(Base):
    __tablename__ = "books"

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(30), nullable=False, index=True)
    author = Column(VARCHAR(30), index=True, nullable=False)
    department = Column(VARCHAR(30), index=True, nullable=False)
    price = Column(FLOAT, nullable=False)
    is_available = Column(BOOLEAN, default=True)
    created_at = Column(DATETIME, default=datetime.now())
    updated_at = Column(DATETIME, default=datetime.now())
