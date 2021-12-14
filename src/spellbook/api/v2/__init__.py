__all__ = [
    'blueprint',
]

from tarkir_base.api.application import Blueprint

from .views import *


blueprint = Blueprint(
    name='v2',
    import_name=__name__
)

blueprint.add_url_rule(
    '/login',
    view_func=LoginView.as_view(LoginView.__name__)
)
