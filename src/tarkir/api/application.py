from flask import Flask
from flask_admin import Admin
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from tarkir.api.views import AdminModelView
from tarkir.utils.classes import get_subclasses

from .config import MainConfig


class Application(Flask):

    def run(
        self, host=None, port=None, debug=None, load_dotenv=True, **options
    ):
        db.create_all()
        db.session.commit()  # pylint: disable=no-member

        return super().run(
            host=host or self.config['API_HOST'],
            port=port or self.config['API_PORT'],
            debug=debug or self.config['DEBUG'],
            load_dotenv=load_dotenv,
            **options
        )

    @classmethod
    def init_admin(cls):
        # pylint: disable=import-outside-toplevel
        from tarkir.database import Model

        for subclass in get_subclasses(Model):
            admin.add_view(AdminModelView(subclass, db.session))


app_config = MainConfig()
app = Application(__name__)
admin = Admin(app, name='tarkir', template_mode='bootstrap3')

app.config.from_object(app_config)

ma = Marshmallow(app)
db = SQLAlchemy(app)
