from tarkir_base.admin import admin
from tarkir_base.api import app

from apps.auth import blueprint as auth_blueprint
from apps.auth.admin import *
from apps.configuration.admin import *
from apps.rules import blueprint as rules_blueprint
from apps.rules.admin import *
from apps.spellbook import blueprint_v1, blueprint_v2
from apps.spellbook.admin import *

app.register_blueprint(auth_blueprint, url_prefix='/auth')

app.register_blueprint(rules_blueprint, url_prefix='/rules')

app.register_blueprint(blueprint_v1, url_prefix='/')  # TODO: remove it after design update
app.register_blueprint(blueprint_v1, url_prefix='/spellbook/v1/')
app.register_blueprint(blueprint_v2, url_prefix='/spellbook/v2/')

app.init_admin(
    admin=admin,
    classes=(
        SchoolAdminView,
        ColorAdminView,
        SpellAdminView,
        SpellToSchoolAdminView,
        SpellToColorAdminView,
        PassiveBonusAdminView,
        PassiveBonusToSchoolAdminView,
        RuleAdminView,
        RuleToAdminAdminView,
        TagAdminView,
        ApplicationAdminView,
        ConfigAdminView,
        UploadedFileAdminView,
        UserAdminView,
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
