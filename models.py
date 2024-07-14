from sqlalchemy import Column, VARCHAR, INTEGER, BOOLEAN, ForeignKey, FLOAT
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "user"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50), index=True)
    email = Column(VARCHAR(50), index=True, unique=True)
    contact_number = Column(VARCHAR(10), unique=True)
    is_active = Column(BOOLEAN, default=True)

    library = relationship("Library", back_populates="user")
    
    def __str__(self) -> str:
        return f"{self.name} <{self.email}>" 

class Library(Base):
    __tablename__ = "library"
    book_id = Column(INTEGER, primary_key=True, autoincrement=True)
    user_id = Column(INTEGER, ForeignKey("user.id"))
    book_name = Column(VARCHAR(30), nullable=False, index=True)
    author = Column(VARCHAR(30), index=True, nullable=False)
    department = Column(VARCHAR(30), index=True, nullable=False)
    price = Column(FLOAT, nullable=False)
    is_available = Column(BOOLEAN, default=True)
    
    user = relationship("User", back_populates="library")

    def __repr__(self) -> str:
        return f"{self.book_name} <{self.author}>"
