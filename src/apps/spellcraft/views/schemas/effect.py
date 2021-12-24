__all__ = [
    'EffectSchema',
]


from tarkir_base.api import ma, fields

from apps.spellcraft import models


class EffectSchema(ma.SQLAlchemyAutoSchema):
    cost = fields.Integer()
    time_to_create = fields.Integer()

    class Meta:
        model = models.Effect
