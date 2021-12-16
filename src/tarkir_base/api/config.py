import uuid

from os import getenv

from sqlalchemy.engine.url import URL

from tarkir_base.utils.classes import SingletonMeta


class MainConfig(metaclass=SingletonMeta):
    DEBUG = bool(int(getenv('TK_DEBUG', '1')))

    BASE_URL = getenv('BASE_URL', 'https://localhost:5000')
    SECRET_KEY = getenv('TK_SECRET_KEY', uuid.uuid4().hex)

    DB_HOST = getenv('TK_DB_HOST', 'localhost')
    DB_PORT = int(getenv('TK_DB_PORT', '5434'))
    DB_USERNAME = getenv('TK_DB_USERNAME', 'postgres')
    DB_PASSWORD = getenv('TK_DB_PASSWORD', 'my_secret_password')
    DB_NAME = getenv('TK_DB_NAME', 'postgres')
    DB_DRIVER = 'postgres'

    API_HOST = getenv('TK_ADMIN_APP_HOST', '0.0.0.0')
    API_PORT = int(getenv('TK_ADMIN_APP_PORT', '5000'))

    FLASK_ADMIN_SWATCH = getenv('TK_FLASK_ADMIN_SWATCH', 'cerulean')

    GOOGLE_CLIENT_ID = getenv('GOOGLE_CLIENT_ID', None)
    GOOGLE_CLIENT_SECRET = getenv('GOOGLE_CLIENT_SECRET', None)
    GOOGLE_DISCOVERY_URL = (
        'https://accounts.google.com/.well-known/openid-configuration'
    )

    FLASK_TEMPLATE_FOLDER = getenv('FLASK_TEMPLATE_FOLDER', 'templates')
    FLASK_STATIC_FOLDER = getenv('FLASK_STATIC_FOLDER', 'static')
    MAX_CONTENT_LENGTH = getenv('MAX_CONTENT_LENGTH', 1024 * 1024 * 1024 * 16)  # 16MB

    @property
    def SQLALCHEMY_DATABASE_URI(self):  # Noqa, pylint: disable=invalid-name
        return str(
            URL(
                host=self.DB_HOST,
                port=self.DB_PORT,
                username=self.DB_USERNAME,
                password=self.DB_PASSWORD,
                database=self.DB_NAME,
                drivername=self.DB_DRIVER
            )
        )
