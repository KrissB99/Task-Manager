from flask import session

def clear_session() -> None:
    session['id'] =  None 
    session['email'] = None
    session['login'] = None
    session['admin'] = None
    
def update_session(user: dict) -> None:
    session['id'] = user.id
    session['email'] = user.email
    session['login'] = user.login
    session['admin'] = user.admin