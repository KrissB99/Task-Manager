from flask import session
from app.database.db_functions import objects_to_dicts
from app.database.models import Types

from app import db

def get_types():
    with db.session as db_session:  
        types = db_session.query(Types).filter(Types.user_id == session['id']).all()
        return objects_to_dicts(types)