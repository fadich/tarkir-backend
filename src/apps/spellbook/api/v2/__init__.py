__all__ = [
    'blueprint',
]

from tarkir_base.api.application import Blueprint

from .views import *


blueprint = Blueprint(
    name='spellbook_v2',
    import_name=__name__
)
