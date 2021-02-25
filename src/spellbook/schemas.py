from tarkir.api import ma

from spellbook import models


class ColorSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = models.Color
        include_fk = True


class SchoolSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = models.School
        include_fk = True


class SpellSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = models.Spell
        include_fk = True


class SpellToSchoolExtendedSchema(ma.SQLAlchemyAutoSchema):
    school = ma.Nested(SchoolSchema)

    class Meta:
        fields = (
            'school',
            'cycle',
        )

        model = models.SpellToSchool
        include_fk = True


class SpellToColorExtendedSchema(ma.SQLAlchemyAutoSchema):
    color = ma.Nested(ColorSchema)

    class Meta:
        fields = (
            'color',
        )

        model = models.SpellToColor
        include_fk = True


class SpellTreeSchema(SpellSchema):
    colors = ma.Nested(SpellToColorExtendedSchema, many=True)
    schools = ma.Nested(SpellToSchoolExtendedSchema, many=True)

    class Meta:
        model = models.Spell
        include_fk = True


class SchoolToSpellExtendedSchema(ma.SQLAlchemyAutoSchema):
    spell = ma.Nested(SpellTreeSchema)

    class Meta:
        fields = (
            'spell',
            'cycle',
        )

        model = models.SpellToSchool
        include_fk = True


class SchoolTreeSchema(SchoolSchema):
    color = ma.Nested(ColorSchema)
    spells = ma.Nested(SchoolToSpellExtendedSchema, many=True)

    class Meta:
        model = models.Spell
        include_fk = True
