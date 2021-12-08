__all__ = [
    'Config',
]


import json

import enum

from tarkir_base.database import (
    db,
    Model,
    validates,
)

from spellbook.utils import (
    ValidationError,
    validate_as_property,
)
from .config_helpers import *


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
        DataTypesEnum.BOOLEAN: to_bool,
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
