__all__ = [
    'Rule',
    'RuleToTag',
]

from tarkir_base.database import (
    db,
    Model,
)


class Rule(Model):
    __tablename__ = 'rule'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False, unique=True)
    image = db.Column(
        db.String(1024), nullable=True,
    )
    description = db.Column(db.Text(), nullable=True)

    tags = db.relationship('RuleToTag', back_populates='rule')

    def __repr__(self):
        return f'{self.name}'


class RuleToTag(Model):
    __tablename__ = 'rule_to_tag'

    rule_id = db.Column(
        db.Integer, db.ForeignKey('rule.id'), primary_key=True,
        on_delete='CASCADE'
    )
    tag_id = db.Column(
        db.Integer, db.ForeignKey('tag.id'), primary_key=True,
        on_delete='CASCADE'
    )

    rule = db.relationship('Rule', back_populates='tags')
    tag = db.relationship('Tag', back_populates='rules')

    def __repr__(self):
        return f'{self.tag.name}'

