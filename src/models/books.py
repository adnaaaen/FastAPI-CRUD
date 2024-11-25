from sqlalchemy import Column, VARCHAR, INTEGER, BOOLEAN, FLOAT, DATETIME
from src.db import Base
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
    update_at = Column(DATETIME, default=datetime.now())

    # def __repr__(self) -> str:
    #     return f"{self.id} <{self.name}>"


if __name__ == "__main__":
    from src.db import engine

    Base.metadata.create_all(bind=engine)

    new_book = Book(1, "Science", "Adnan", "Computer science", 2100)
    print(type(new_book))
    print(new_book)
