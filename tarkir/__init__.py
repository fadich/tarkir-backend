import logging

from .conf import config
from .database import db

__all__ = (
    'db',
    'config',
)


logging.basicConfig(level=logging.DEBUG if config.debug else logging.WARNING)
