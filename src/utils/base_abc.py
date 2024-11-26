from typing import TypeVar, Generic
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

Model = TypeVar("Model")
ModelUpdate = TypeVar("ModelUpdate")


class BaseCrud(ABC, Generic[Model, ModelUpdate]):
    @abstractmethod
    async def create(self, db: Session, request: Model) -> Model | None:
        """create new entry"""
        pass

    @abstractmethod
    async def read(self, db: Session, id: int) -> Model | None:
        """get entry with id"""
        pass

    @abstractmethod
    async def update(self, db: Session, id: int, request: ModelUpdate) -> Model | None:
        """update existing entry"""
        pass

    @abstractmethod
    async def delete(self, db: Session, id: int) -> bool:
        """delete entry"""
        pass
