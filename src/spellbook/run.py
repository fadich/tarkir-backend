from tarkir_base.api import app

from spellbook.api import v1, v2
from spellbook.admin.views import *

app.register_blueprint(v1.blueprint, url_prefix='/') # TODO: remove it after design update
app.register_blueprint(v1.blueprint, url_prefix='/v1')
app.register_blueprint(v2.blueprint, url_prefix='/v2')

app.init_admin(
    classes=(
        SpellAdminView,
        SpellToSchoolAdminView,
        SpellToColorAdminView,
        PassiveBonusAdminView,
        PassiveBonusToSchoolAdminView,
        SchoolAdminView,
        ColorAdminView,
        ApplicationAdminView,
        ConfigAdminView,
        UploadedFileAdminView,
    )
)

app.run()
