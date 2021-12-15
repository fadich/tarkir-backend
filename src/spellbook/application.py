from tarkir_base.api import app, admin_app
from tarkir_base.api.auth import blueprint as auth_blueprint

from spellbook.api import v1, v2
from spellbook.admin.views import *


app.register_blueprint(auth_blueprint, url_prefix='/auth')

app.register_blueprint(v1.blueprint, url_prefix='/')  # TODO: remove it after design update
app.register_blueprint(v1.blueprint, url_prefix='/api/v1/')
app.register_blueprint(v2.blueprint, url_prefix='/api/v2/')

app.init_admin(
    admin=admin_app,
    classes=(
        SchoolAdminView,
        ColorAdminView,
        SpellAdminView,
        SpellToSchoolAdminView,
        SpellToColorAdminView,
        PassiveBonusAdminView,
        PassiveBonusToSchoolAdminView,
        ApplicationAdminView,
        ConfigAdminView,
        UserAdminView,
        UploadedFileAdminView,
    )
)


if __name__ == '__main__':
    import os

    ssl_context = None
    if int(os.getenv('TK_USE_SSL', '0')):
        ssl_context = ('certs/localhost.crt', 'certs/localhost.key')

    app.run(
        ssl_context=ssl_context
    )
