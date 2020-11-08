from tarkir.web_api import Handler

from spellbook.models import *

from .schemas import ColorSchema, SchoolSchema, SpellSchema, IndexSchema


__all__ = [
    # 'IndexHandler',
    'ColorsHandler',
    'SchoolsHandler',
    'SpellsHandler',
]


# class IndexHandler(Handler):
#     schema = IndexSchema()
#
#     # async def get(self):
#
#     async def get(self):
#         loader = School \
#             .distinct(School.id) \
#             .load(color=Color) \
#             .load(cycle=SpellToSchool.distinct(SpellToSchool.cycle)) \
#             .load(add_spell=Spell.distinct(Spell.id)) \
#             .load(add_color=Color.distinct(Color.id))
#
#         query = School \
#             .outerjoin(SpellToSchool) \
#             .outerjoin(Spell) \
#             .outerjoin(SpellToColor) \
#             .outerjoin(Color) \
#             .select()
#
#         query = query.gino.load(loader)
#
#         res = await query.all()
#
#         return self.send_json(res)


class ColorsHandler(Handler):
    schema = ColorSchema()

    async def get(self):
        colors = await Color.all()
        return self.send_json(colors)


class SchoolsHandler(Handler):
    schema = SchoolSchema()

    async def get(self):
        loader = School.load(color=Color)

        query = School.join(Color, School.color_id == Color.id).select()
        query = query.gino.load(loader)

        return self.send_json(await query.all())


class SpellsHandler(Handler):
    schema = SpellSchema()

    async def get(self):
        school_id = self.request.query.get('school-id')

        loader = Spell \
            .distinct(Spell.id) \
            .load(cycle=SpellToSchool.distinct(SpellToSchool.cycle)) \
            .load(add_color=Color.distinct(Color.id)) \
            .load(add_school=School.distinct(School.id))

        query = Spell \
            .outerjoin(SpellToColor) \
            .outerjoin(Color) \
            .outerjoin(SpellToSchool) \
            .outerjoin(School) \
            .select()

        if school_id and school_id.isdigit():
            school_id = int(school_id)
            query = query.where(School.id == school_id)

        query = query.gino.load(loader)

        return self.send_json(await query.all())
