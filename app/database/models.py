from sqlalchemy import Boolean, Column, Float, LargeBinary, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

DecBase = declarative_base()

class Base(DecBase):
    __allow_unmapped__ = True
    __abstract__ = True
    
    def to_date(self, date: datetime) -> str:
        if date:
            return date.strftime('%d.%m.%Y %H: %M')
        else: 
            return None
    
class Types(Base):
    'Model for types'
    
    __tablename__ = 'types'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False) 
    
    # Foreign Keys
    user_id = Column(Integer, ForeignKey('users.id'))
    
    # Relationships
    user = relationship('Users', back_populates='types')
    tasks = relationship('Tasks', back_populates='task_type')
    
    def to_dict(self) -> dict: 
        return {
            'id': self.id, 
            'name': self.name,
            'user': self.user_id,
            'tasks': [task.to_dict() for task in self.tasks]
        }
        
    def __repr__(self) -> str:
        return f'Type(id: {self.id}, name: {self.name}, user: {self.user_id})'


class Tasks(Base):
    'Model for tasks'
    
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    importance = Column(String, default='low')
    creation_date = Column(DateTime, default=datetime.now)
    deadline = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    progress = Column(Float, nullable=False, default=0)
    
    # Foreign keys
    type_id = Column(Integer, ForeignKey('types.id'))
    
    # Relationships
    task_type = relationship('Types', back_populates="tasks")
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description, 
            'importance': self.importance,
            'creation_date': self.to_date(self.creation_date), 
            'deadline': self.to_date(self.deadline),
            'end_date': self.to_date(self.end_date),
            'progress': self.progress
        }
        
    def __repr__(self) -> str:
        return f'Task(id: {self.id}, name: {self.name}, description: {self.description}, \
                      importance: {self.importance}, creation_date: {self.creation_date.to_date()}, \
                      deadline: {self.deadline.to_date()}, end_date: {self.end_date.to_date()},  \
                      progress: {self.progress})'


class Users(Base):
    'Model for users'
    
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String(30), nullable=True)
    email = Column(String(120), nullable=False, unique=True)
    password = Column(String, nullable=False)
    salt = Column(LargeBinary, nullable=False)
    admin = Column(Boolean, default=0)

    # Relationships 
    types = relationship('Types', back_populates='user')
    
    @classmethod
    def create_user(cls, data: dict):
        user = cls(login = data.pop('login', None), password = data['password'], 
                   email = data['email'], salt = data['salt'])
        return user
    
    def to_dict(self) -> dict:
        return {
            'id': self.id, 
            'email': self.email,
            'login': self.login,
            'admin': self.admin,
            'types': [type.to_dict() for type in self.types],
        }
        
    def __repr__(self) -> str:
        return f'User(id: {self.id}, email: {self.email}, login: {self.login}, admin: {self.admin})'
    
