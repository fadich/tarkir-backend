from os import getenv

from sqlalchemy.engine.url import URL

from .base import SingletonMeta


class Config(metaclass=SingletonMeta):

    @property
    def debug(self):
        return getenv('TR_DEBUG', 1)

    @property
    def db_host(self):
        return getenv('TR_DB_HOST', 'localhost')

    @property
    def db_port(self):
        return getenv('TR_DB_PORT', 5432)

    @property
    def db_username(self):
        return getenv('TR_DB_USERNAME', 'postgres')

    @property
    def db_password(self):
        return getenv('TR_DB_PASSWORD', 'my_secret_password')

    @property
    def db_name(self):
        return getenv('TR_DB_NAME', 'postgres')

    @property
    def admin_app_host(self):
        return getenv('TR_ADMIN_APP_HOST', '0.0.0.0')

    @property
    def admin_app_port(self):
        return getenv('TR_ADMIN_APP_PORT', 4999)

    @property
    def api_server_host(self):
        return getenv('TR_API_SERVER_HOST', '0.0.0.0')

    @property
    def api_server_port(self):
        return getenv('TR_API_SERVER_PORT', 5000)

    @property
    def db_driver(self):
        return 'postgres'

    @property
    def db_dsn(self):
        dsn = URL(
            host=self.db_host,
            port=self.db_port,
            username=self.db_username,
            password=self.db_password,
            database=self.db_name,
            drivername=self.db_driver)

        return str(dsn)


config = Config()
