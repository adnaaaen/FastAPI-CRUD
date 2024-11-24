from sqlalchemy import Column, VARCHAR, INTEGER, BOOLEAN, FLOAT
from database import Base



class Book(Base):
    __tablename__ = "books"

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(30), nullable=False, index=True)
    author = Column(VARCHAR(30), index=True, nullable=False)
    department = Column(VARCHAR(30), index=True, nullable=False)
    price = Column(FLOAT, nullable=False)
    is_available = Column(BOOLEAN, default=True)

    def __repr__(self) -> str:
        return f"{self.id} <{self.name}>"

