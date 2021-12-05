import uuid

from os import getenv

from sqlalchemy.engine.url import URL

from tarkir_base.utils.classes import SingletonMeta


class MainConfig(metaclass=SingletonMeta):
    DEBUG = int(getenv('TR_DEBUG', '1')) != 0

    SECRET_KEY = getenv('TR_SECRET_KEY', uuid.uuid4().hex)

    DB_HOST = getenv('TR_DB_HOST', 'localhost')
    DB_PORT = int(getenv('TR_DB_PORT', '5434'))
    DB_USERNAME = getenv('TR_DB_USERNAME', 'postgres')
    DB_PASSWORD = getenv('TR_DB_PASSWORD', 'my_secret_password')
    DB_NAME = getenv('TR_DB_NAME', 'postgres')
    DB_DRIVER = 'postgres'

    API_HOST = getenv('TR_ADMIN_APP_HOST', '0.0.0.0')
    API_PORT = int(getenv('TR_ADMIN_APP_PORT', '5000'))

    FLASK_ADMIN_SWATCH = getenv('TR_FLASK_ADMIN_SWATCH', 'cerulean')
    FLASK_TEMPLATE_FOLDER = getenv('FLASK_TEMPLATE_FOLDER', 'templates')

    BASIC_AUTH_USERNAME = getenv('TR_BASIC_AUTH_USERNAME', '')
    BASIC_AUTH_PASSWORD = getenv('TR_BASIC_AUTH_PASSWORD', '')

    STATIC_FOLDER = getenv('STATIC_FOLDER', '/tmp/tarkir-upload')
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
