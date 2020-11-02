from gino_admin import create_admin_app

from tarkir import db, config

from spellbook import models as spellbook_models


db_models = [
    spellbook_models.Color,
    spellbook_models.School,
]


if __name__ == '__main__':
    import sys

    sys.exit(
        create_admin_app(
            host=config.admin_app_host,
            port=config.admin_app_port,
            db=db,
            db_models=db_models,
            config={
                'db_uri': config.db_dsn,
                'ui': {
                    'colors': {
                        'buttons': 'orange',
                        'buttons_alert': 'pink',
                    }
                },
            },
        )
    )
