__all__ = [
    'School',
]

from tarkir_base.database import (
    db,
    Model,
)


class School(Model):
    __tablename__ = 'school'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False, unique=True)
    shortcut = db.Column(db.String(2), nullable=False, unique=True)
    color_id = db.Column(
        db.Integer(), db.ForeignKey('color.id'), nullable=False
    )
    description = db.Column(db.Text(), nullable=True)
    image = db.Column(
        db.String(1024), nullable=True,
    )

    color = db.relationship('Color', back_populates='schools')
    spells = db.relationship('SpellToSchool', back_populates='school')
    passive_bonuses = db.relationship('PassiveBonusToSchool', back_populates='school')

    def __repr__(self):
        return f'{self.shortcut}'
