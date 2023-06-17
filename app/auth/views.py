from app.auth import auth
from flask import render_template

@auth.route('/register')
def registration():
    return render_template('register.html', title="Task Manager - Register")

@auth.route('/log-in')
def sign_in():
    return render_template('login.html', title="Task Manager - Login")

@auth.route('/user-panel')
def user_panel():
    return render_template('user_panel.html', title="Task Manager - User Panel")
