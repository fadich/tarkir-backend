from tarkir.api import app

from spellbook.api.views import (
    ColorsView,
    SpellsView,
    SchoolsView,
    SchoolTreeView,
)


app.add_url_rule(
    '/',
    view_func=SchoolTreeView.as_view(SchoolTreeView.__name__)
)
app.add_url_rule(
    '/colors',
    view_func=ColorsView.as_view(ColorsView.__name__)
)
app.add_url_rule(
    '/schools',
    view_func=SchoolsView.as_view(SchoolsView.__name__)
)
app.add_url_rule(
    '/spells',
    view_func=SpellsView.as_view(SpellsView.__name__)
)


if __name__ == '__main__':
    app.init_admin()
    app.run()
