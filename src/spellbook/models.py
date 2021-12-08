__all__ = [
    'Color',
    'School',
    'Spell',
    'SpellToColor',
    'SpellToSchool',
    'PassiveBonus',
    'PassiveBonusToSchool',
    'Application',
    'Config',
    'UploadedFile',
]

import json

import enum

import os

from tarkir_base.api import app
from tarkir_base.database import (
    db,
    Model,
    validates,
)

from spellbook.utils import (
    ValidationError,
    validate_as_property,
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


class Spell(Model):
    __tablename__ = 'spell'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False, unique=True)
    name_en = db.Column(db.String(256), nullable=True, unique=True)
    type = db.Column(db.String(1024), nullable=True)
    description = db.Column(db.Text(), nullable=True)
    requirements = db.Column(db.Text(), nullable=True)
    time_to_create = db.Column(db.String(1024), nullable=True)
    cost = db.Column(db.String(1024), nullable=True)
    duration = db.Column(db.String(1024), nullable=True)
    items = db.Column(db.Text(), nullable=True)
    image = db.Column(
        db.String(1024), nullable=True,
    )

    colors = db.relationship('SpellToColor', back_populates='spell')
    schools = db.relationship('SpellToSchool', back_populates='spell')

    def __repr__(self):
        return f'{self.name}'


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


class SpellToColor(Model):
    __tablename__ = 'spell_to_color'

    spell_id = db.Column(
        db.Integer, db.ForeignKey('spell.id'), primary_key=True,
        on_delete='CASCADE'
    )
    color_id = db.Column(
        db.Integer, db.ForeignKey('color.id'), primary_key=True,
        on_delete='CASCADE'
    )

    spell = db.relationship('Spell', back_populates='colors')
    color = db.relationship('Color', back_populates='spells')

    def __repr__(self):
        return f'{self.color.shortcut}'


class SpellToSchool(Model):
    __tablename__ = 'spell_to_school'

    spell_id = db.Column(
        db.Integer, db.ForeignKey('spell.id'), primary_key=True,
        on_delete='CASCADE'
    )
    school_id = db.Column(
        db.Integer, db.ForeignKey('school.id'), primary_key=True,
        on_delete='CASCADE'
    )
    cycle = db.Column(db.Integer(), nullable=False, default=lambda: 0)

    spell = db.relationship('Spell', back_populates='schools')
    school = db.relationship('School', back_populates='spells')

    def __repr__(self):
        return f'{self.school.shortcut}'


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


def to_none(value):
    if value:
        raise ValueError(f'Value "{value}" is not empty value')

    return None


class Config(Model):
    __tablename__ = 'config'
    __table_args__ = (
        db.UniqueConstraint('application_id', 'name', name='unique_application_config'),
    )

    class DataTypesEnum(enum.Enum):
        NULL = 'null'
        INT = 'int'
        FLOAT = 'float'
        STRING = 'string'
        BOOLEAN = 'boolean'
        JSON = 'json'

        @classmethod
        def has_key(cls, value):
            return value in cls.__members__.keys()

    TYPES_MAP = {
        DataTypesEnum.NULL: to_none,
        DataTypesEnum.INT: int,
        DataTypesEnum.FLOAT: float,
        DataTypesEnum.STRING: str,
        DataTypesEnum.BOOLEAN: bool,
        DataTypesEnum.JSON: json.loads,
    }

    # pylint: disable=invalid-name
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    application_id = db.Column(
        db.Integer(), db.ForeignKey('application.id'), nullable=False
    )
    raw_value = db.Column(db.Text(), nullable=True)
    data_type = db.Column(db.Enum(DataTypesEnum), default=lambda: Config.DataTypesEnum.NULL, nullable=False)

    application = db.relationship('Application', back_populates='config')

    @property
    def value(self):
        return self.TYPES_MAP[self.data_type](self.raw_value)

    @value.setter
    def value(self, value):
        self.raw_value = value

    @property
    def python_value(self):
        return self.value, type(self.value)

    def __str__(self):
        return f'{self.application.label}:{self.name}'

    @validates('name')
    def validate_name(self, field, value):
        return validate_as_property('Property name', value)

    @validates('data_type')
    def validate_data_type(self, field, value):
        if self.DataTypesEnum.has_key(value):
            return value

        raise ValidationError(f'Invalid value type "{value}"')


class UploadedFile(Model):
    __tablename__ = 'uploaded_file'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    file = db.Column(
        db.String(1024), nullable=True,
    )
    name = db.Column(db.String(256), nullable=True)

    def __str__(self):
        return f'{self.file}'

    @property
    def fullpath(self):
        return os.path.join(
            app.static_url_path,
            self.file
        )
