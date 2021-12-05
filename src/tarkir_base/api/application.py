from typing import Sequence, Type, Optional, Union

from flask import Flask
from flask_admin import Admin, AdminIndexView as FlaskAdminIndexView
from flask_admin.contrib.sqla import ModelView as FlaskAdminModelView
from flask_basicauth import BasicAuth
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import MainConfig
from .exceptions import AuthException

ModelType = Type['Model']
ModelViewType = Type['ModelView']


class AccessAdminViewMixin:

    def is_accessible(self):
        if not ba.authenticate():
            raise AuthException('Unauthorized')

        return True


class AdminIndexView(AccessAdminViewMixin, FlaskAdminIndexView):
    pass


class AdminModelView(AccessAdminViewMixin, FlaskAdminModelView):
    __model__: ModelType


class Application(Flask):

    def run(
        self, host=None, port=None, debug=None, load_dotenv=True, **options
    ):
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
app = Application(
    __name__,
    template_folder=app_config.FLASK_TEMPLATE_FOLDER,
    static_folder=app_config.STATIC_FOLDER,
    static_url_path='/static'
)
app.url_map.strict_slashes = False
admin = Admin(
    app=app,
    name='tarkir',
    template_mode='bootstrap3',
    index_view=AdminIndexView(
        name='Home',
        template='admin/home.html',
        url='/admin/'
    )
)

app.config.from_object(app_config)

ma = Marshmallow(app)
db = SQLAlchemy(app)
ba = BasicAuth(app)
mi = Migrate(app, db)
