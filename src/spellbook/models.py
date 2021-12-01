__all__ = [
    'Color',
    'School',
    'Spell',
    'SpellToColor',
    'SpellToSchool',
    'PassiveBonus',
    'PassiveBonusToSchool',
]


from tarkir_base.database import db, Model


class Color(Model):
    __tablename__ = 'color'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False, unique=True)
    shortcut = db.Column(db.String(1), nullable=False, unique=True)
    hex_code = db.Column(db.String(16), nullable=False)

    schools = db.relationship('School', back_populates='color')
    spells = db.relationship('SpellToColor', back_populates='color')

    def __repr__(self):
        return f'{self.shortcut}'


class School(Model):
    __tablename__ = 'school'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False, unique=True)
    shortcut = db.Column(db.String(2), nullable=False, unique=True)
    color_id = db.Column(
        db.Integer(), db.ForeignKey('color.id'), nullable=False
    )
    description = db.Column(db.Text(), nullable=True)

    color = db.relationship('Color', back_populates='schools')
    spells = db.relationship('SpellToSchool', back_populates='school')
    passive_bonuses = db.relationship('PassiveBonusToSchool', back_populates='school')

    def __repr__(self):
        return f'{self.shortcut}'


class Spell(Model):
    __tablename__ = 'spell'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False, unique=True)
    name_en = db.Column(db.String(256), nullable=True, unique=True)
    type = db.Column(db.String(1024), nullable=True)
    description = db.Column(db.Text(), nullable=True)
    requirements = db.Column(db.Text(), nullable=True)
    time_to_create = db.Column(db.String(1024), nullable=True)
    cost = db.Column(db.String(1024), nullable=True)
    duration = db.Column(db.String(1024), nullable=True)
    items = db.Column(db.Text(), nullable=True)

    colors = db.relationship('SpellToColor', back_populates='spell')
    schools = db.relationship('SpellToSchool', back_populates='spell')

    def __repr__(self):
        return f'{self.name}'


class PassiveBonus(Model):
    __tablename__ = 'passive_bonus'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False, unique=True)
    name_en = db.Column(db.String(256), nullable=True, unique=True)
    description = db.Column(db.Text(), nullable=True)
    cycle = db.Column(db.Integer(), nullable=False, default=lambda: 0)

    schools = db.relationship('PassiveBonusToSchool', back_populates='passive_bonus')

    def __repr__(self):
        return f'{self.name}'


class SpellToColor(Model):
    __tablename__ = 'spell_to_color'

    spell_id = db.Column(
        db.Integer, db.ForeignKey('spell.id'), primary_key=True,
        on_delete='CASCADE'
    )
    color_id = db.Column(
        db.Integer, db.ForeignKey('color.id'), primary_key=True,
        on_delete='CASCADE'
    )

    spell = db.relationship('Spell', back_populates='colors')
    color = db.relationship('Color', back_populates='spells')

    def __repr__(self):
        return f'{self.color.shortcut}'


class SpellToSchool(Model):
    __tablename__ = 'spell_to_school'

    spell_id = db.Column(
        db.Integer, db.ForeignKey('spell.id'), primary_key=True,
        on_delete='CASCADE'
    )
    school_id = db.Column(
        db.Integer, db.ForeignKey('school.id'), primary_key=True,
        on_delete='CASCADE'
    )
    cycle = db.Column(db.Integer(), nullable=False, default=lambda: 0)

    spell = db.relationship('Spell', back_populates='schools')
    school = db.relationship('School', back_populates='spells')

    def __repr__(self):
        return f'{self.school.shortcut}'


class PassiveBonusToSchool(Model):
    __tablename__ = 'passive_bonus_to_school'

    passive_bonus_id = db.Column(
        db.Integer, db.ForeignKey('passive_bonus.id'), primary_key=True,
        on_delete='CASCADE'
    )
    school_id = db.Column(
        db.Integer, db.ForeignKey('school.id'), primary_key=True,
        on_delete='CASCADE'
    )

    passive_bonus = db.relationship('PassiveBonus', back_populates='schools')
    school = db.relationship('School', back_populates='passive_bonuses')

    def __repr__(self):
        return f'{self.school.shortcut}'
