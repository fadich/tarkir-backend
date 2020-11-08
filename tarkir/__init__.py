import logging

from .conf import config
from .database import db, Model

__all__ = (
    'db',
    'Model',
    'config',
)


logging.basicConfig(level=logging.DEBUG if config.debug else logging.WARNING)
