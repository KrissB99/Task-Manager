from app.auth import auth
from flask import render_template

@auth.route('/')
def home_page():
    return render_template('home_page.html', title="Task Manager")

@auth.route('/register')
def registration():
    return render_template('register.html', title="Task Manager - Register")

@auth.route('/login')
def login():
    return render_template('login.html', title="Task Manager - Login")
