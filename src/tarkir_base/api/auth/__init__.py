__all__ = [
    'User',
    'blueprint',
    'is_authorized',
    'get_current_user',
    'log_out',
]

from flask_login import LoginManager

from tarkir_base.api import app

from .models import User
from .blueprint import blueprint
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
