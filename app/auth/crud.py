from typing import Any
from app.database.db_functions import object_to_dict, objects_to_dicts
from app.database.models import Users
from app import db

# CRUD for Users table

def get_users() -> list[dict]:
    """Get all users from db

    Returns:
        list[dict]: list with dictionaries with info about users
    """
    users = db.get(Users)
    return users
    
def get_user(id: int = None, email: str = None, login: str = None):
    """Get user from db by its credentials

    Args:
        id (int, optional): Rows id from db. Defaults to None.
        email (str, optional): Users email. Defaults to None.
        login (str, optional): Users login. Defaults to None.

    Returns:
        dict: Returns dict with info about giving object
    """
    with db.session as session:
        if id != None:  
            user = db.get_by_id(Users, id)
        elif email != None: 
            user = session.query(Users).filter(Users.email == email).first()
        elif login != None: 
            user = session.query(Users).filter(Users.login == login).first()
        else: 
            return False
        if user:
            return object_to_dict(user)
    return None
    
def create_user(data: dict) -> list[dict, Users]:
    try:
        new_user = db.add(Users.create_user(data))
        return {'detail': 'User succesfully created! 👍'}, new_user
    except:
        return {'detail': 'Something went wrong! 👎'}
    
def update_user(id: int, data: dict) -> list[dict, Users]:
    try:
        updated_user = db.update(Users, id, data)
        # TO DO - session
        return {'detail': 'Info about user succesfully updated! 👍'}, updated_user
    except:
        return {'detail': 'Something went wrong! 👎'}
    
def delete_user(id: int) -> None:
    try:
        db.delete(Users, id)
        # TO DO - session
        return {'detail': 'User succesfully deleted! 👍'}
    except:
        return {'detail': 'Something went wrong! 👎'}