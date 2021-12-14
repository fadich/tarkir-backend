__all__ = [
    'User',
]

from tarkir_base.api import UserMixin
from tarkir_base.database import (
    db,
    Model,
)


class User(Model, UserMixin):
    __tablename__ = 'user'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.Text(), nullable=False, unique=False)
    email = db.Column(db.String(1024), nullable=False, unique=True)
    picture = db.Column(db.Text(), nullable=True, unique=False)
    is_admin = db.Column(db.Boolean(), nullable=False, default=lambda: False)

    def __repr__(self):
        return f'{self.email}'
