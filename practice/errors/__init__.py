from flask import Blueprint

bp = Blueprint('errors', __name__)

from practice.errors import handlers