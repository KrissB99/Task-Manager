from flask import session
from app.database.db_functions import objects_to_dicts
from app.database.models import Types

from app import db

# TYPES

def get_types():
    with db.session as db_session:  
        types = db_session.query(Types).filter(Types.user_id == session['id']).all()
        return objects_to_dicts(types)

def add_type(name):  
    new_type = Types(name=name, user_id=session['id'])
    created_type = db.add(new_type)
    return {'detail': 'Type succesfully added!', 'type': created_type}

def change_type(id, data):
    type = db.get_by_id(Types, id)
    db.update(type, data)
    return {'detail': 'Type changed succesfully!'}

def remove_type(id):
    type = db.get_by_id(Types, id)
    db.delete(type)
    return {'detail': 'Type succesfully remov'}

# TASKS

def add_task(data):
    ...

def change_task(id, data):
    ...

def remove_task(id):
    ...