__all__ = [
    'craft',
]


from collections import Sequence
from typing import Iterable

from sqlalchemy import and_
from  sqlalchemy.sql.expression import func

from tarkir_base.database import db

from apps.spellbook.models import Color
from apps.spellcraft.models import EffectToColor


def craft(colors: Sequence[str], choices: int = 1) -> Iterable[EffectToColor]:
    color_ids =  db.select([Color.id, ]).where(and_(
        Color.shortcut == color for color in colors
    ))

    query = EffectToColor.query.filter(
        EffectToColor.color_id.in_(color_ids)
    ).order_by(func.random()).limit(choices)

    return (e.effect for e in query.all())
