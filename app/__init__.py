from flask import Blueprint, Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '783fbaf9c60eaaa9a455b1f839699d0af9d6a87caeab71efa13b71cb85a61ca4'

db = SQLAlchemy(app)

# Blueprint configuration

from app.admin import admin
from app.auth import auth
from app.home_page import main

app.register_blueprint(admin)
app.register_blueprint(auth)
app.register_blueprint(main)
