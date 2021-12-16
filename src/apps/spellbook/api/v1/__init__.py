__all__ = [
    'blueprint',
]

from tarkir_base.api.application import Blueprint

from .views import *


blueprint = Blueprint(
    name='v1',
    import_name=__name__
)

blueprint.add_url_rule(
    '/schools',
    view_func=IndexView.as_view(IndexView.__name__)
)
blueprint.add_url_rule(
    '/colors',
    view_func=ColorsView.as_view(ColorsView.__name__)
)
blueprint.add_url_rule(
    '/spells',
    view_func=SchoolView.as_view(SchoolView.__name__)
)
