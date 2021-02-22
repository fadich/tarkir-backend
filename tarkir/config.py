from os import getenv

from sqlalchemy.engine.url import URL

from tarkir.base import SingletonMeta


class MainConfig(metaclass=SingletonMeta):
    DEBUG = int(getenv('TR_DEBUG', 1)) != 0

    DB_HOST = getenv('TR_DB_HOST', 'localhost')
    DB_PORT = getenv('TR_DB_PORT', 5434)
    DB_USERNAME = getenv('TR_DB_USERNAME', 'postgres')
    DB_PASSWORD = getenv('TR_DB_PASSWORD', 'my_secret_password')
    DB_NAME = getenv('TR_DB_NAME', 'postgres')
    DB_DRIVER = 'postgres'

    ADMIN_APP_HOST = getenv('TR_ADMIN_APP_HOST', '0.0.0.0')
    ADMIN_APP_PORT = getenv('TR_ADMIN_APP_PORT', 4999)

    API_APP_HOST = getenv('TR_ADMIN_APP_HOST', '0.0.0.0')
    API_APP_PORT = getenv('TR_ADMIN_APP_PORT', 5000)

    @property
    def SQLALCHEMY_DATABASE_URI(self):  # Noqa
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
