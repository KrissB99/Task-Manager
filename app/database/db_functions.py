import contextlib
from typing import TypeVar, Union, Type, Any

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .models import Base, Tasks, Users, Types

DataBaseObject = TypeVar('DataBaseObject', Users, Types, Tasks)
DataBaseModel = TypeVar('DataBaseModel', bound=Base)

class DataBase: 
    
    def __init__(self, url: str) -> None:
        self._engine = create_engine(url)
        
    def _use_session(self, method: str, data: Union[DataBaseObject, list[DataBaseObject]]) -> Union[DataBaseObject, list[DataBaseObject]]:
        """Use specific method with db session

        Args:
            method (str): session method
            data (Union[DataBaseObject, list[DataBaseObject]]): object from ORM or list of ORM objects

        Returns:
            Union[DataBaseObject, list[DataBaseObject]]: data with ids
        """
        if data:
            with Session(self._engine) as session: 
                _method = getattr(session, method)
                _method(data)
                session.commit()
                if method == 'add':
                    if isinstance(data, list):
                        for obj in data:
                            session.refresh(obj)
                    else:
                        session.refresh(data)
        return data
    
    def get(self, model: Type[DataBaseModel]) -> list[DataBaseModel]:
        """Method returning all rows from specific table

        Args:
            model (Type[DataBaseModel]): ORM model

        Returns:
            list[DataBaseModel]: list of db objects (dict)
        """
        with Session(self._engine) as session: 
            return [object.to_dict() for object in session.query(model).all()]
        
    def get_by_id(self, model: Type[DataBaseModel], id: int, as_dict: bool = True) -> dict[str, Any]:
        """Method returning element from specific table by id

        Args:
            model (Type[DataBaseModel]): ORM model
            id (int): row id
            as_dict (bool, optional): Defailts to "True". Returns element as dict

        Returns:
            dict[str, Any]: element from specific table
        """
        with Session(self._engine) as session:
            object = session.query(model).filter(model.id == id).first()
            if object:
                return object.to_dict() if as_dict else object
    
    def add(self, _object: DataBaseObject) -> DataBaseObject:
        """Add object to db

        Args:
            _object (DataBaseObject): ORM object

        Returns:
            DataBaseObject: Created object as dict
        """
        object = self._use_session('add', _object)
        return object.to_dict()
    
    def delete(self, model: Type[DataBaseModel], id: int) -> None:
        """Delete object from db

        Args:
            model (Type[DataBaseModel]): ORM model
            id (int): objects id
        """
        _object = self.get_by_id(model, id, as_dict=False)
        self._use_session('delete', _object)
        
    def update(self, model: Type[DataBaseModel], id: int, data: dict[str, Any]) -> DataBaseObject:
        """Update data from db

        Args:
            model (Type[DataBaseModel]): ORM model
            id (int): objects id
            data (dict[str, Any]): data to update

        Returns:
            DataBaseObject: updated ORM object
        """
        with Session(self._engine) as session:
            session.query(model).filter(model.id == id).update(data)
            _object = session.query(model).filter(model.id == id).first()
            session.commit()
            session.refresh(_object)
        return _object.to_dict()
    
    @property
    @contextlib.contextmanager
    def session(self) -> Session:
        try:
            s = Session(self._engine)
            yield s
        finally:
            s.close()
            
    def create(self) -> None:
        Base.metadata.create_all(self._engine)
        
def object_to_dict(object: Type[DataBaseObject]) -> dict:
    if object:
        return object.to_dict()
    return None

def objects_to_dicts(objects: Type[DataBaseModel]) -> list[dict]:
    if objects:
        return [element.to_dict() for element in objects]
    return None