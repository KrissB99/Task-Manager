from flask import jsonify, redirect, request, session, jsonify
from app import db
from app.auth import auth, crud
from app.helpers.security import Security
from app.database.models import Users

@auth.route('/users/')
def users():
    return jsonify(crud.get_users())

@auth.route('/users/<int:id>')
def user(id: int):
    return crud.get_user(id=id)

@auth.route('/users', methods=['POST'])
def register():
    data = request.json
    
    # Check if email exists in db
    users = crud.get_users()
    if users:
        for user in users:
            if data['email'] == user['email']:
                return {'detail': 'User with this email already exists. Please use different email.'}, 409
        
    # Hash password and generate salt
    data['password'], data['salt'] = Security.hash_password(data['password'])
    
    # Add user to db
    return crud.create_user(data)

@auth.route('/login', methods=['POST'])
def login():
    #  Get data from request
    data = request.json
    
    # Search for user
    user = crud.get_user(email=data['email'])
    
    # if user exist
    if user: 
        if Security.check_password(data['email'], data['password']):
            # Put data to session
            session['id'] = user['id']
            session['email'] = user['email']
            session['login'] = user['login']
            session['admin'] = user['admin']
            
            # If email and password match
            return {'detail': 'Logged in succesfully!'}
        
        # If email exist but wrong password
        return {'detail': 'Wrong password! 😥'}
    
    # If user doesn't exist
    return {'detail': 'There is no user with such an email in the database! 😥'}

@auth.route('/logout')
def logout():
    # Clear session
    session['id'] = None
    session['email'] = None
    session['login'] = None
    session['admin'] = None
    return redirect('/auth/log-in')
    
@auth.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id: int):
    return crud.delete_user(id)