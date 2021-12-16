__all__ = [
    'ValidationError',
    'validate_as_property',
]

import re

from wtforms import ValidationError

PROPERTY_PATTERN = '^[a-z]+([a-z0-9-]?[a-z0-9]+){2,}$'


def validate_as_property(field_name: str, field_value: str) -> str:
    if not re.match(PROPERTY_PATTERN, field_value):
        raise ValidationError(
            f'{field_name} may contain only lowercase letters, '
            'dashes and digits and should be started/ended with a latter'
        )

    return field_value
