from datetime import datetime
from app import db

def to_date(date) -> datetime:
    return date.strftime('%d.%m.%Y %H: %M')

def add_rows(objects: db.Model) -> None:
    """Function to add new objects to db

    Args:
        objects (db.Model): generator with data
    """
    db.session.add_all(list(objects))
    db.session.commit()
    
def get_rows(object: db.Model) -> list:
    """Function to get all rows from the specific table

    Args:
        object (db.Model): class of model
        
    Returns:
        list: list with rows of specific table
    """
    return object.query.all()

def add_to_db(item: db.Model) -> None:
    """Function to add an item to db

    Args:
        item (db.Model): row to add to db
    """
    db.session.add(item)
    db.session.commit()
    
def delete_from_db(item: db.Model) -> None:
    """Function to delete from db

    Args:
        item (db.Model): Row to delete from db
    """
    db.session.delete(item)
    db.session.commit()
    
def modify_db(object: db.Model, attr: dict) -> None:
    """Function to modify data from db

    Args:
        object (db.Model): name of the specific model
        attr (dict): dictionary with column name and values to modify
    """
    for key, value in attr.items():
        if value == 'True' or value == '': bool(value)
        if key == 'date': value = datetime.strptime(value, 'A%Y-%m-%d %H:%M:%S.%f')
        setattr(object, key, value)
    db.session.commit()