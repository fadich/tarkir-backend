__all__ = [
    'get_current_user',
    'is_authorized',
    'log_out',
]

import flask_login
from flask_login import AnonymousUserMixin

from .models import User


def get_current_user() -> User:
    return flask_login.current_user


def is_authorized() -> bool:
    user = get_current_user()

    return not (user is None or isinstance(user, AnonymousUserMixin))


def log_out() -> bool:
    return flask_login.logout_user()
