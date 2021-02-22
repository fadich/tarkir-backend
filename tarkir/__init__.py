import logging

from .api import web_app, db, ma
from .config import MainConfig
from .database import Model

__all__ = (
    'web_app',
    'db',
    'ma',
    'app_config',
    'Model',
    'config',
)


app_config = MainConfig()

logging.basicConfig(
    level=logging.DEBUG if app_config.DEBUG else logging.WARNING
)

web_app.config.from_object(app_config)
