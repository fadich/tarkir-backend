__all__ = [
    'Tag',
]

from tarkir_base.database import (
    db,
    Model,
)


class Tag(Model):
    __tablename__ = 'tag'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False, unique=True)

    rules = db.relationship('RuleToTag', back_populates='tag')

    def __repr__(self):
        return f'{self.name}'
