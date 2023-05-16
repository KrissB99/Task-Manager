from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app import db
from app.database.db_functions import *

class Permissions(db.Model):
    'Model for permissions'
    
    __table_name__ = 'permissions'
    __allow_unmapped__ = True
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    level = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String)
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'level': self.level, 
            'name': self.name
        }
    
    def __repr__(self) -> str:
        return f'Permission(id: {self.id}, level: {self.level}, name: {self.name})'
    

class Users(db.Model):
    'Model for users'
    
    __table_name__ = 'users'
    __allow_unmapped__ = True
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    login = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    salt = db.Column(db.LargeBinary, nullable=False)
    
    # Foreign keys
    permission_id = db.Column(db.Integer, ForeignKey('permissions.id'))
    
    # Relationships
    permission: Permissions = relationship('permissions')
    
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
                      

class Types(db.Model):
    'Model for types'
    
    __table_name__ = 'types'
    __allow_unmapped__ = True
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String) 
    
    # Foreign Keys
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    
    # Relations
    user: Users = relationship('users')
    
    def to_dict(self) -> dict: 
        return {
            'id': self.id, 
            'name': self.name,
            'user': self.user.to_dict()
        }
        
    def __repr__(self) -> str:
        return f'Type(id: {self.id}, name: {self.name}, user: {self.user.to_dict()})'
    
    
class Tasks(db.Model):
    'Model for tasks'
    
    __table_name__ = 'tasks'
    __allow_unmapped__ = True
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    importance = db.Column(db.String, default='low')
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    deadline = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    progress = db.Column(db.Float, nullable=False, default=0)
    
    # Foreign keys
    user_id = db.Column(db.String, ForeignKey('users.id'))
    type_id = db.Column(db.Integer, ForeignKey('types.id'))
    
    # Relationships
    user: Users = relationship('users')
    type: Types = relationship('types')
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description, 
            'importance': self.importance,
            'creation_date': to_date(self.creation_date), 
            'deadline': to_date(self.deadline),
            'end_date': to_date(self.end_date),
            'progress': self.progress
        }
        
    def __repr__(self) -> str:
        return f'Task(id: {self.id}, name: {self.name}, description: {self.description}, \
                      importance: {self.importance}, creation_date: {to_date(self.creation_date)}, \
                      deadline: {to_date(self.deadline)}, end_date: {to_date(self.end_date)},  \
                      progress: {self.progress})'
