__all__ = [
    'User',
]

from tarkir_base.database import (
    db,
    Model,
)
from .mixins import UserMixin


class User(Model, UserMixin):
    __tablename__ = 'user'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    google_id = db.Column(db.Integer(), index=True, unique=True)
    name = db.Column(db.Text(), nullable=False, unique=False)
    email = db.Column(db.String(1024), nullable=False, unique=True)
    picture = db.Column(db.Text(), nullable=True, unique=False)
    is_admin = db.Column(db.Boolean(), nullable=False, default=lambda: False)

    def __repr__(self):
        return f'{self.email}'
