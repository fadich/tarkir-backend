__all__ = [
    'to_none',
    'to_bool',
]


def to_none(value):
    if value:
        raise ValueError(f'Value "{value}" is not empty value')

    return None


def to_bool(value):
    str_val = str(value).lower()
    if str_val in ['true', '1', 'yes']:
        return True
    elif str_val in ['false', '0', 'no']:
        return False

    raise ValueError(f'Value "{value}" is not valid boolean-value')
