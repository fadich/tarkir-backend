from tarkir_base.api import app, admin_app, login_manager

from spellbook.api import v1, v2
from spellbook.admin.views import *
from spellbook.models import User


app.register_blueprint(v1.blueprint, url_prefix='/')  # TODO: remove it after design update
app.register_blueprint(v1.blueprint, url_prefix='/api/v1/')
app.register_blueprint(v2.blueprint, url_prefix='/api/v2/')

app.init_admin(
    admin=admin_app,
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


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == '__main__':
    import os

    ssl_context = None
    if int(os.getenv('TK_USE_SSL', '0')):
        ssl_context = ('certs/localhost.crt', 'certs/localhost.key')

    app.run(
        ssl_context=ssl_context
    )
