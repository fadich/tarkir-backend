from marshmallow import Schema, fields


class ColorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    shortcut = fields.Str()
    hex_code = fields.Str()


class SchoolSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    shortcut = fields.Str()
    description = fields.Str()
    cycle_bonus_zero = fields.Str()
    cycle_bonus_one = fields.Str()
    cycle_bonus_two = fields.Str()
    cycle_bonus_three = fields.Str()
    color = fields.Nested(ColorSchema)


class SpellToSchoolSchema(Schema):
    cycle = fields.Int()


class SpellSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    name_en = fields.Str()
    type = fields.Str()
    requirements = fields.Str()
    time_to_create = fields.Str()
    duration = fields.Str()
    items = fields.Str()
    cycle = fields.Nested(SpellToSchoolSchema)
    colors = fields.Nested(ColorSchema, many=True)
    schools = fields.Nested(SchoolSchema, many=True)


class IndexSchema(SchoolSchema):
    spells = fields.Nested(SpellSchema, many=True)
