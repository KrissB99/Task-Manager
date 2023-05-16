from flask import Blueprint

auth = Blueprint('auth', __name__, template_folder='templates', url_prefix='/')

from app.auth import views