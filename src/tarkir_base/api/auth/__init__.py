__all__ = [
    'User',
    'blueprint',
    'is_authorized',
    'get_current_user',
    'log_out',
    'AuthException',
]

from flask_login import LoginManager

from tarkir_base.api import app

from .blueprint import blueprint
from .exceptions import AuthException
from .models import User
from .utils import (
    is_authorized,
    get_current_user,
    log_out,
)


login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
