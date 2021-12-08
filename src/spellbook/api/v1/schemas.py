# TODO: Split by views (move to api module)

from tarkir_base.api import ma

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


class PassiveBonusSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = models.PassiveBonus
        include_fk = True


class SpellToSchoolSchema(ma.SQLAlchemyAutoSchema):
    school = ma.Nested(SchoolSchema)

    class Meta:
        fields = (
            'school',
            'cycle',
        )

        model = models.SpellToSchool
        include_fk = True


class SpellToColorSchema(ma.SQLAlchemyAutoSchema):
    color = ma.Nested(ColorSchema)

    class Meta:
        fields = (
            'color',
        )

        model = models.SpellToColor
        include_fk = True


class PassiveBonusToSchoolSchema(ma.SQLAlchemyAutoSchema):
    school = ma.Nested(SchoolSchema)

    class Meta:
        fields = (
            'school',
        )

        model = models.PassiveBonusToSchool
        include_fk = True


class SpellTreeSchema(SpellSchema):
    colors = ma.Nested(SpellToColorSchema, many=True)
    schools = ma.Nested(SpellToSchoolSchema, many=True)

    class Meta:
        model = models.Spell
        include_fk = True


class PassiveBonusTreeSchema(SpellSchema):
    schools = ma.Nested(PassiveBonusToSchoolSchema, many=True)

    class Meta:
        model = models.PassiveBonus
        include_fk = True


class SchoolToSpellSchema(ma.SQLAlchemyAutoSchema):
    spell = ma.Nested(SpellTreeSchema)

    class Meta:
        fields = (
            'spell',
            'cycle',
        )

        model = models.SpellToSchool
        include_fk = True


class SchoolToPassiveBonusSchema(ma.SQLAlchemyAutoSchema):
    passive_bonus = ma.Nested(PassiveBonusTreeSchema)

    class Meta:
        fields = (
            'passive_bonus',
        )

        model = models.PassiveBonusToSchool
        include_fk = True


class SchoolTreeSchema(SchoolSchema):
    color = ma.Nested(ColorSchema)
    spells = ma.Nested(SchoolToSpellSchema, many=True)
    passive_bonuses = ma.Nested(SchoolToPassiveBonusSchema, many=True)

    class Meta:
        model = models.Spell
        include_fk = True
