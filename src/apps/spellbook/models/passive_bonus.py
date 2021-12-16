__all__ = [
    'PassiveBonus',
    'PassiveBonusToSchool',
]

from tarkir_base.database import (
    db,
    Model,
)


class PassiveBonus(Model):
    __tablename__ = 'passive_bonus'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False, unique=True)
    name_en = db.Column(db.String(256), nullable=True, unique=True)
    description = db.Column(db.Text(), nullable=True)
    cycle = db.Column(db.Integer(), nullable=False, default=lambda: 0)

    schools = db.relationship('PassiveBonusToSchool', back_populates='passive_bonus')

    def __repr__(self):
        return f'{self.name}'


class PassiveBonusToSchool(Model):
    __tablename__ = 'passive_bonus_to_school'

    passive_bonus_id = db.Column(
        db.Integer, db.ForeignKey('passive_bonus.id'), primary_key=True,
        on_delete='CASCADE'
    )
    school_id = db.Column(
        db.Integer, db.ForeignKey('school.id'), primary_key=True,
        on_delete='CASCADE'
    )

    passive_bonus = db.relationship('PassiveBonus', back_populates='schools')
    school = db.relationship('School', back_populates='passive_bonuses')

    def __repr__(self):
        return f'{self.school.shortcut}'
