__all__ = [
    'UserMixin',
]


from flask_login import UserMixin as FlaskUserMixin


class UserMixin(FlaskUserMixin):
    pass
