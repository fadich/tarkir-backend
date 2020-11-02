from gino import Gino
from sqlalchemy import create_engine

from .conf import config


db = Gino()

create_engine(config.db_dsn)


async def connect_db(*args, **kwargs):
    await db.set_bind(config.db_dsn, echo=True)


async def disconnect_db(*args, **kwargs):
    await db.pop_bind().close()
