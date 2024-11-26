from sqlalchemy import Column, VARCHAR, INTEGER, BOOLEAN, DATETIME
from src.dependency.db import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50), index=True)
    email = Column(VARCHAR(50), index=True, unique=True)
    contact_number = Column(VARCHAR(10), unique=True)
    is_active = Column(BOOLEAN, default=True)
    created_at = Column(DATETIME, default=datetime.now())
    updated_at = Column(DATETIME, default=datetime.now())
