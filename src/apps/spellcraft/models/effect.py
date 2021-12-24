__all__ = [
    'Effect',
    'EffectToColor',
]

from tarkir_base.database import (
    db,
    Model,
)

from apps.spellbook.models import Color


class Effect(Model):
    __tablename__ = 'effect'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False, unique=True)
    type = db.Column(db.String(1024), nullable=True)
    description = db.Column(db.Text(), nullable=True)
    # time_to_create = db.Column(db.String(1024), nullable=True)
    # cost = db.Column(db.String(1024), nullable=True)
    duration = db.Column(db.String(1024), nullable=True)
    image = db.Column(
        db.String(1024), nullable=True,
    )

    colors = db.relationship('EffectToColor', back_populates='effect')

    @property
    def cost(self):
        return 1 + len(self.colors)

    @property
    def time_to_create(self):
        return len(self.colors)

    def __repr__(self):
        return f'{self.name}'


class EffectToColor(Model):
    __tablename__ = 'effect_to_color'

    effect_id = db.Column(
        db.Integer, db.ForeignKey('effect.id'), primary_key=True,
        on_delete='CASCADE'
    )
    color_id = db.Column(
        db.Integer, db.ForeignKey('color.id'), primary_key=True,
        on_delete='CASCADE'
    )

    effect = db.relationship('Effect', back_populates='colors')
    color = db.relationship('Color')

    def __repr__(self):
        return f'{self.color.shortcut}'
