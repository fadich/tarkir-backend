import os

from gino_admin import create_admin_app

from tarkir import db, app_config

from spellbook import models as spellbook_models


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
PRESETS_FOLDER = os.path.join(CURRENT_PATH, 'presets')

db_models = [
    spellbook_models.Color,
    spellbook_models.School,
    spellbook_models.Spell,
    spellbook_models.SpellToColor,
    spellbook_models.SpellToSchool,
]


if __name__ == '__main__':
    import sys

    sys.exit(
        create_admin_app(
            host=app_config.admin_app_host,
            port=app_config.admin_app_port,
            db=db,
            db_models=db_models,
            config={
                'presets_folder': PRESETS_FOLDER,
                'db_uri': app_config.db_dsn,
                'ui': {
                    'colors': {
                        'buttons': 'orange',
                        'buttons_alert': 'pink',
                    }
                },
            },
        )
    )
