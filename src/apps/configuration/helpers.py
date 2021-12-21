__all__ = [
    'get_configuration',
]


from typing import Optional, Dict, Any

from .exceptions import NotFoundError
from .models import (
    Application,
)


def get_configuration(app_label: str) -> Dict[str, Any]:
    """Returns application config dict.

    >>> get_configuration('spellbook')
    {'default-school-image': '/static/1638973438197-School-3.jpg',
     'default-spell-image': '/static/1638973206888-Spell-5.jpg'}

    :param app_label: Target application name

    :return: Dict of target Application config
    """

    app: Optional[Application] = Application.query.filter(Application.name == app_label).first()
    if app is None:
        raise NotFoundError(f'Application `{app_label}` does not found')

    return {
        conf.name: conf.value for conf in app.config
    }
