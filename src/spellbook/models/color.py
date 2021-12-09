__all__ = [
    'Color',
]

from tarkir_base.database import (
    db,
    Model,
)


class Color(Model):
    __tablename__ = 'color'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False, unique=True)
    shortcut = db.Column(db.String(1), nullable=False, unique=True)
    hex_code = db.Column(db.String(16), nullable=False)

    schools = db.relationship('School', back_populates='color')
    spells = db.relationship('SpellToColor', back_populates='color')

    def __repr__(self):
        return f'{self.shortcut}'
