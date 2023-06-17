from datetime import datetime
from flask import session
from requests import Session
from app.database.db_functions import objects_to_dicts
from app.database.models import Types, Tasks

from app import db

# TYPES

def get_types():
    with db.session as db_session:  
        types = db_session.query(Types).filter(Types.user_id == session['id']).all()
        return objects_to_dicts(types)

def add_type(name: str):  
    new_type = Types(name=name, user_id=session['id'])
    created_type = db.add(new_type)
    return {'detail': 'Type succesfully added!', 'type': created_type}

def change_type(id: int, data: dict):
    type = db.get_by_id(Types, id, as_dict=False)
    db.update(Types, type, data)
    return {'detail': 'Type changed succesfully!'}

def remove_type(type_id: int):
    db.delete(Types, type_id)
    return {'detail': 'Type succesfully removed'}

# TASKS

def add_task(data: dict):
    new_task = Tasks(name=data['name'], 
                     type_id=data['type_id'], 
                     importance=data['importance'])
    created_task = db.add(new_task)
    return {'detail': 'Task succesfully added!', 'task': created_task}

def change_progress(id: int, data: dict):
    task = db.get_by_id(Tasks, id, as_dict=False)
    db.update(Tasks, task, data)
    if data['progress'] == 0: 
        return {'detail': 'Task succesfully marked as done'}
    else: 
        return {'detail': 'Task succesfully marked as to do'}

def remove_task(task_id: int):
    db.delete(Tasks, task_id)
    return {'detail': 'Type succesfully removed'}
    