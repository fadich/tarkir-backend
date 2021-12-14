__all__ = [
    'admin_app',
    'app',
    'app_config',
    'db',
    'login_manager',
    'ma',
    'oauth_client',
    'Application',
    'Blueprint',
    'UserMixin',
]

from flask import Blueprint
from flask_basicauth import BasicAuth
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from oauthlib.oauth2 import WebApplicationClient

from .admin import Admin, AdminIndexView
from .application import Application
from .auth import UserMixin
from .config import MainConfig


app_config = MainConfig()
login_manager = LoginManager()
oauth_client = WebApplicationClient(app_config.TK_GOOGLE_CLIENT_ID)

app = Application(
    __name__,
    template_folder=app_config.FLASK_TEMPLATE_FOLDER,
    static_folder=app_config.STATIC_FOLDER,
    static_url_path='/static'
)

app.url_map.strict_slashes = False

app.config.from_object(app_config)
login_manager.init_app(app)

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
