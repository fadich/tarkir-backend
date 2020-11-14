from tarkir import db, Model


__all__ = [
    'Color',
    'School',
    'Spell',
    'SpellToColor',
    'SpellToSchool',
]


class Color(Model):
    __tablename__ = 'color'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    shortcut = db.Column(db.String(1), nullable=False, unique=True)
    hex_code = db.Column(db.String(16), nullable=False)

    def __init__(self, **kw):
        super().__init__(**kw)
        self._spells = set()

    @property
    def spells(self):
        return self._spells

    def add_spell(self, spell):
        self._spells.add(spell)
        spell._colors.add(self)


class School(Model):
    __tablename__ = 'school'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    shortcut = db.Column(db.String(2), nullable=False, unique=True)
    color_id = db.Column(
        db.Integer(), db.ForeignKey('color.id'), nullable=False)
    description = db.Column(db.Text(), nullable=True)
    cycle_bonus_zero = db.Column(db.Text(), nullable=True)
    cycle_bonus_one = db.Column(db.Text(), nullable=True)
    cycle_bonus_two = db.Column(db.Text(), nullable=True)
    cycle_bonus_three = db.Column(db.Text(), nullable=True)

    def __init__(self, **kw):
        super().__init__(**kw)
        self._spells = set()

    @property
    def spells(self):
        return self._spells

    def add_spell(self, spell):
        self._spells.add(spell)
        spell._schools.add(self)


class Spell(Model):
    __tablename__ = 'spell'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    name_en = db.Column(db.String(128), nullable=True, unique=True)
    type = db.Column(db.String(256), nullable=True)
    description = db.Column(db.Text(), nullable=True)
    requirements = db.Column(db.Text(), nullable=True)
    time_to_create = db.Column(db.String(256), nullable=True)
    cost = db.Column(db.String(256), nullable=True)
    channel = db.Column(db.String(256), nullable=True)
    duration = db.Column(db.String(256), nullable=True)
    items = db.Column(db.Text(), nullable=True)

    def __init__(self, **kw):
        super().__init__(**kw)
        self._colors = set()
        self._schools = set()

    @property
    def colors(self):
        return self._colors

    def add_color(self, color):
        self._colors.add(color)
        color.spells.add(self)

    @property
    def schools(self):
        return self._schools

    def add_school(self, school):
        self._schools.add(school)
        school.spells.add(self)


class SpellToColor(Model):
    __tablename__ = 'spell_to_color'

    spell_id = db.Column(db.Integer, db.ForeignKey('spell.id'))
    color_id = db.Column(db.Integer, db.ForeignKey('color.id'))


class SpellToSchool(Model):
    __tablename__ = 'spell_to_school'

    spell_id = db.Column(db.Integer, db.ForeignKey('spell.id'))
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'))
    cycle = db.Column(db.Integer(), nullable=False)
