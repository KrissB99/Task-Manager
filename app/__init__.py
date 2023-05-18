from flask import Flask
from .database import DataBase
import os

app = Flask(__name__)
app.secret_key = '783fbaf9c60eaaa9a455b1f839699d0af9d6a87caeab71efa13b71cb85a61ca4'

main_path = os.getcwd()
db = DataBase(f"sqlite:///{main_path}/app/database/data.db")

# Blueprint configuration
from app.admin import admin
from app.auth import auth
from app.home_page import main

# Bluepring registration
app.register_blueprint(admin)
app.register_blueprint(auth)
app.register_blueprint(main)
