from typing import TypeVar, Generic
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session


Model = TypeVar("Model")
ModelUpdate = TypeVar("ModelUpdate")

class Crud(ABC, Generic[Model, ModelUpdate]):

    @abstractmethod 
    def create(self, db: Session, request: Model) -> Model:
        """create new entry"""
        pass
    
    @abstractmethod 
    def read(self, db: Session, id: int) -> Model:
        """get entry with id"""
        pass

    @abstractmethod 
    def update(self, db: Session, request: ModelUpdate) -> Model:
        """update existing entry"""
        pass

    @abstractmethod 
    def delete(self, db: Session, id: int) -> Model:
        """delete entry"""
        pass
