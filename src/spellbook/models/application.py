__all__ = [
    'Application',
]

from spellbook.utils import validate_as_property
from tarkir_base.database import (
    db,
    Model,
    validates,
)


class Application(Model):
    __tablename__ = 'application'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False, unique=True)

    config = db.relationship('Config', back_populates='application')

    @property
    def label(self):
        return self.name

    def __str__(self):
        return f'{self.name}'

    @validates('name')
    def validate_name(self, field, value):
        return validate_as_property(field, value)
