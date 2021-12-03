from tarkir_base.api import app

from spellbook.views import (
    IndexView,
    ColorsView,
    SchoolView,
)


app.add_url_rule(
    '/schools',
    view_func=IndexView.as_view(IndexView.__name__)
)
app.add_url_rule(
    '/colors',
    view_func=ColorsView.as_view(ColorsView.__name__)
)
app.add_url_rule(
    '/spells',
    view_func=SchoolView.as_view(SchoolView.__name__)
)


if __name__ == '__main__':
    from spellbook.views import (
        SpellAdminView,
        SchoolAdminView,
        ColorAdminView,
        PassiveBonusAdminView,
        SpellToSchoolAdminView,
        SpellToColorAdminView,
        PassiveBonusToSchoolAdminView,
    )

    app.init_admin(
        classes=(
            SpellAdminView,
            SpellToSchoolAdminView,
            SpellToColorAdminView,
            PassiveBonusAdminView,
            PassiveBonusToSchoolAdminView,
            SchoolAdminView,
            ColorAdminView,
        )
    )
    app.run()
