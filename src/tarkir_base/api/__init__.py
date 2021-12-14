__all__ = [
    'admin_app',
    'app',
    'app_config',
    'db',
    'ma',
    'Application',
    'Blueprint',
    'UserMixin',
]

from flask import Blueprint
from flask_basicauth import BasicAuth
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .admin import Admin, AdminIndexView
from .application import Application
from .auth import UserMixin
from .config import MainConfig


app_config = MainConfig()
app = Application(
    __name__,
    template_folder=app_config.FLASK_TEMPLATE_FOLDER,
    static_folder=app_config.STATIC_FOLDER,
    static_url_path='/static'
)

app.config.from_object(app_config)
app.url_map.strict_slashes = False

ma = Marshmallow(app)
db = SQLAlchemy(app)
ba = BasicAuth(app)
mi = Migrate(app, db)

admin_app = Admin(
    app=app,
    db=db,
    name='tarkir',
    template_mode='bootstrap3',
    index_view=AdminIndexView(
        name='Home',
        template='admin/home.html',
        url='/admin/'
    ),
)
