__all__ = [
    'blueprint',
]

from tarkir_base.api import Blueprint


from .views import *


blueprint = Blueprint(
    name='rules',
    import_name=__name__,
)

blueprint.add_url_rule('/', view_func=RulesListView.as_view(RulesListView.__name__))
