__all__ = [
    'blueprint',
]

from tarkir_base.api import Blueprint


from .views import *


blueprint = Blueprint(
    name='spellcraft',
    import_name=__name__,
)

blueprint.add_url_rule('/', view_func=CraftView.as_view(CraftView.__name__))
