from app.main import main
from flask import render_template, session

@main.route('/')
def home_page():
    return render_template('home_page.html', title="Task Manager")

@main.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html', title="Task Manager - dashboard")