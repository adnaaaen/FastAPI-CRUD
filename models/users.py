from sqlalchemy import Column, VARCHAR, INTEGER, BOOLEAN
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50), index=True)
    email = Column(VARCHAR(50), index=True, unique=True)
    contact_number = Column(VARCHAR(10), unique=True)
    is_active = Column(BOOLEAN, default=True)
    
    def __str__(self) -> str:
        return f"{self.name} <{self.email}>" 

