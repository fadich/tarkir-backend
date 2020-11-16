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


class SpellSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    name_en = fields.Str()
    type = fields.Str()
    requirements = fields.Str()
    time_to_create = fields.Str()
    cost = fields.Str()
    duration = fields.Str()
    items = fields.Str()
    colors = fields.Nested(ColorSchema, many=True)
    schools = fields.Nested(SchoolSchema, many=True)


def create_spell_school_schema(results):
    props = {}
    for result in results:
        cycle = result.cycle
        shortcut = result.school.shortcut
        prop_name = f'{shortcut}{cycle}'
        props[prop_name] = fields.Nested(SpellSchema, many=True)

    return type('SpellToSchoolSchema', (Schema, ), props)()
