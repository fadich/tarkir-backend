from tarkir.api import ma

from spellbook import models


class ColorSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = models.Color
        include_fk = True


class SchoolSchema(ma.SQLAlchemyAutoSchema):
    colors = ma.Nested(ColorSchema, many=True)

    class Meta:
        model = models.School
        include_fk = True


class SpellsSchema(ma.SQLAlchemyAutoSchema):
    colors = ma.Nested(ColorSchema, many=True)
    schools = ma.Nested(SchoolSchema, many=True)

    class Meta:
        model = models.Spell
        include_fk = True
