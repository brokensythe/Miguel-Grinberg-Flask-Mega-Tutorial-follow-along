from flask import Blueprint

bp = Blueprint('main', __name__)

from practice.main import routes