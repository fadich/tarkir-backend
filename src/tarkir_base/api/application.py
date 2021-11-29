from typing import Sequence, Type, Optional, Union

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView as FlaskAdminModelView
from flask_basicauth import BasicAuth
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from .config import MainConfig
from .exceptions import AuthException


ModelType = Type['Model']
ModelViewType = Type['ModelView']


class AdminModelView(FlaskAdminModelView):
    __model__: ModelType
    __index_view__: bool = False  # TODO: Implement index page

    def is_accessible(self):
        if not ba.authenticate():
            raise AuthException('Unauthorized')

        return True


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
    def init_admin(cls, classes: Optional[Sequence[Union[ModelType, ModelViewType]]] = None):
        # pylint: disable=import-outside-toplevel
        from tarkir_base.database import Model

        for class_ in classes:
            if issubclass(class_, Model):
                admin.add_view(AdminModelView(class_, db.session))
            elif issubclass(class_, FlaskAdminModelView):
                admin.add_view(class_(class_.__model__, db.session))
            else:
                raise TypeError(f'Unsupported admin model type: {class_}')


app_config = MainConfig()
app = Application(__name__, template_folder=app_config.FLASK_TEMPLATE_FOLDER)
admin = Admin(app, name='tarkir', template_mode='bootstrap3')

app.config.from_object(app_config)

ma = Marshmallow(app)
db = SQLAlchemy(app)
ba = BasicAuth(app)
