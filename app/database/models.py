from sqlalchemy import BLOB, Column, Float, LargeBinary, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime

class Base(DeclarativeBase):
    __allow_unmapped__ = True
    
    def to_date(date: datetime) -> datetime.strftime:
        return date.strftime('%d.%m.%Y %H: %M')

class Permissions(Base):
    'Model for permissions'
    
    __tablename__ = 'permissions'
    
    id: int = Column(Integer, primary_key=True)
    level: int = Column(Integer, nullable=True)
    name: str = Column(String, nullable=True)
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'level': self.level, 
            'name': self.name
        }
    
    def __repr__(self) -> str:
        return f'Permission(id: {self.id}, level: {self.level}, name: {self.name})'
    
class Types(Base):
    'Model for types'
    
    __tablename__ = 'types'
    
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, nullable=False) 
    
    # Foreign Keys
    user_id: int = Column(Integer, ForeignKey('users.id'))
    
    def to_dict(self) -> dict: 
        return {
            'id': self.id, 
            'name': self.name,
            'user': self.user_id
        }
        
    def __repr__(self) -> str:
        return f'Type(id: {self.id}, name: {self.name}, user: {self.user_id})'

class Users(Base):
    'Model for users'
    
    __tablename__ = 'users'
    
    id: int = Column(Integer, primary_key=True, index=True)
    login: str = Column(String(30), nullable=False, unique=True)
    email: str = Column(String(120), nullable=False, unique=True)
    password: BLOB = Column(BLOB, nullable=False)
    salt: LargeBinary = Column(LargeBinary, nullable=False)
    
    # Foreign keys
    permission_id = Column(Integer, ForeignKey('permissions.id'))
    
    # Relationships
    permission: Permissions = relationship('permissions')
    types: Types = relationship('types', uselist=True)
    
    def to_dict(self) -> dict:
        return {
            'id': self.id, 
            'email': self.email,
            'login': self.login,
            'permission': self.permission.to_dict()
        }
        
    def __repr__(self) -> str:
        return f'User(id: {self.id}, email: {self.email}, login: {self.login}, \
                      permission: {self.permission.name})'
    
    
class Tasks(Base):
    'Model for tasks'
    
    __tablename__ = 'tasks'
    
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, nullable=False)
    description: str = Column(String, nullable=True)
    importance: str = Column(String, default='low')
    creation_date: datetime = Column(DateTime, default=datetime.now)
    deadline: datetime = Column(DateTime, nullable=True)
    end_date: datetime = Column(DateTime, nullable=True)
    progress: float = Column(Float, nullable=False, default=0)
    
    # Foreign keys
    user_id: int = Column(String, ForeignKey('users.id'))
    type_id: int = Column(Integer, ForeignKey('types.id'))
    
    # Relationships
    user: Users = relationship('users')
    type: Types = relationship('types')
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description, 
            'importance': self.importance,
            'creation_date': self.creation_date.to_date(), 
            'deadline': self.deadline.to_date(),
            'end_date': self.end_date.to_date(),
            'progress': self.progress
        }
        
    def __repr__(self) -> str:
        return f'Task(id: {self.id}, name: {self.name}, description: {self.description}, \
                      importance: {self.importance}, creation_date: {self.creation_date.to_date()}, \
                      deadline: {self.deadline.to_date()}, end_date: {self.end_date.to_date()},  \
                      progress: {self.progress})'
