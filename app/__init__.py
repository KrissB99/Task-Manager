from flask import Flask
from .database import DataBase
import os

from app.const_vars import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

main_path = os.getcwd()
db = DataBase(f"sqlite:///{main_path}/app/database/data.db")

# Blueprint configuration
from app.admin import admin
from app.auth import auth
from app.main import main

# Bluepring registration
app.register_blueprint(admin)
app.register_blueprint(auth)
app.register_blueprint(main)
