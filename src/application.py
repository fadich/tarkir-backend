from tarkir_base.admin import admin
from tarkir_base.api import app

from apps.auth import blueprint as auth_blueprint
from apps.auth.admin import (
    UserAdminView,
)
from apps.configuration.admin import (
    ApplicationAdminView,
    ConfigAdminView,
    UploadedFileAdminView,
)
from apps.rules import blueprint as rules_blueprint
from apps.rules.admin import (
    RuleAdminView,
    RuleToTagAdminView,
    TagAdminView,
)
from apps.spellbook import blueprint_v1, blueprint_v2
from apps.spellbook.admin import (
    ColorAdminView,
    PassiveBonusAdminView,
    PassiveBonusToSchoolAdminView,
    SchoolAdminView,
    SpellAdminView,
    SpellToColorAdminView,
    SpellToSchoolAdminView,
)
from apps.spellcraft import blueprint as spellcraft_blueprint
from apps.spellcraft.admin import (
    EffectAdminView,
    EffectToColorAdminView,
)

app.register_blueprint(auth_blueprint, url_prefix='/auth')

app.register_blueprint(rules_blueprint, url_prefix='/rules')

app.register_blueprint(blueprint_v1, url_prefix='/')  # TODO: remove it after design update
app.register_blueprint(blueprint_v1, url_prefix='/spellbook/v1/')
app.register_blueprint(blueprint_v2, url_prefix='/spellbook/v2/')

app.register_blueprint(spellcraft_blueprint, url_prefix='/spellcraft/')

app.init_admin(
    admin=admin,
    classes=(
        # Spellbook
        SchoolAdminView,
        ColorAdminView,
        SpellAdminView,
        SpellToSchoolAdminView,
        SpellToColorAdminView,
        PassiveBonusAdminView,
        PassiveBonusToSchoolAdminView,

        # Rules
        RuleAdminView,
        RuleToTagAdminView,
        TagAdminView,

        # Spellcraft
        EffectAdminView,
        EffectToColorAdminView,

        # Configuration
        ApplicationAdminView,
        ConfigAdminView,
        UploadedFileAdminView,

        # User
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
