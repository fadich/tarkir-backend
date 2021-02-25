from tarkir.api import app

from spellbook.api.views import (
    ColorsView,
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


if __name__ == '__main__':
    app.init_admin()
    app.run()
