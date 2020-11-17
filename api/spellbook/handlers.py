from collections import defaultdict
from tarkir.web_api import Handler

from spellbook.models import (
    Color,
    School,
    Spell,
    SpellToColor,
    SpellToSchool,
)

from .schemas import (
    ColorSchema,
    SchoolSchema,
    create_spell_school_schema,
)


__all__ = [
    'ColorsHandler',
    'SchoolsHandler',
    'SpellsHandler',
]


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
        query = query.order_by(School.id).gino.load(loader)

        return self.send_json(await query.all())


class SpellsHandler(Handler):

    async def get(self):
        school_id = self.request.query.get('school-id')

        loader = SpellToSchool \
            .load(school=School.on(SpellToSchool.school_id == School.id))
        query = SpellToSchool.join(School).select()
        if school_id and school_id.isdigit():
            query = query.where(School.id == int(school_id))
        elif school_id:
            query = query.where(School.shortcut == school_id)

        res = await query.gino.load(loader).all()
        self.schema = create_spell_school_schema(res)

        result_dict = defaultdict(list)
        for item in res:
            key = f'{item.school.shortcut}{item.cycle}'
            result_dict[key] = await self.get_full_spells(
                item.school.id, item.cycle)

        return self.send_json(result_dict)

    @classmethod
    async def get_full_spells(cls, school_id, cycle):
        loader = Spell \
            .distinct(Spell.id) \
            .load(add_color=Color.distinct(Color.id)) \
            .load(sts=SpellToSchool.distinct(SpellToSchool.cycle))

        query = Spell \
            .join(SpellToColor) \
            .join(Color) \
            .join(SpellToSchool) \
            .select() \
            .where(SpellToSchool.school_id == school_id) \
            .where(SpellToSchool.cycle == cycle)

        spells = await query.gino.load(loader).all()

        loader = School \
            .load(color=Color.distinct(Color.id)) \
            .load(
                sts=SpellToSchool.on(
                    SpellToSchool.school_id == School.id
                )
            )

        query = School \
            .join(Color, School.color_id == Color.id) \
            .join(SpellToSchool, School.id == SpellToSchool.school_id) \
            .select()

        schools = await query.gino.load(loader).all()
        for spell in spells:
            for school in schools:
                if school.sts.spell_id == spell.id \
                        and school.sts.cycle == spell.sts.cycle:
                    spell.add_school(school)
                    break

        return spells
