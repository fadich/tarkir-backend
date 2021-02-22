from tarkir import db, Model


__all__ = [
    'Color',
    'School',
    'Spell',
    'SpellToColor',
    'SpellToSchool',
]


class SpellToColor(Model):
    __tablename__ = 'spell_to_color'

    spell_id = db.Column(
        db.Integer, db.ForeignKey('spell.id'), primary_key=True
    )
    color_id = db.Column(
        db.Integer, db.ForeignKey('color.id'), primary_key=True
    )

    spell = db.relationship(
        'Spell', back_populates=db.backref('colors', lazy=True)
    )
    color = db.relationship(
        'Color', back_populates=db.backref('spells', lazy=True)
    )


class SpellToSchool(Model):
    __tablename__ = 'spell_to_school'

    spell_id = db.Column(
        db.Integer, db.ForeignKey('spell.id'), primary_key=True
    )
    school_id = db.Column(
        db.Integer, db.ForeignKey('school.id'), primary_key=True
    )
    cycle = db.Column(db.Integer(), nullable=False, default=lambda: 0)

    spell = db.relationship(
        'Spell', back_populates=db.backref('schools', lazy=True)
    )
    school = db.relationship(
        'School', back_populates=db.backref('spells', lazy=True)
    )


class Color(Model):
    __tablename__ = 'color'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False, unique=True)
    shortcut = db.Column(db.String(1), nullable=False, unique=True)
    hex_code = db.Column(db.String(16), nullable=False)

    schools = db.relationship('School', backref=db.backref('color', lazy=True))
    spells = db.relationship(
        'SpellToColor', back_populates=db.backref('spell', lazy=True)
    )


class School(Model):
    __tablename__ = 'school'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False, unique=True)
    shortcut = db.Column(db.String(2), nullable=False, unique=True)
    description = db.Column(db.Text(), nullable=True)
    cycle_bonus_zero = db.Column(db.Text(), nullable=True)
    cycle_bonus_one = db.Column(db.Text(), nullable=True)
    cycle_bonus_two = db.Column(db.Text(), nullable=True)
    cycle_bonus_three = db.Column(db.Text(), nullable=True)
    color_id = db.Column(
        db.Integer(), db.ForeignKey('color.id'), nullable=False
    )

    color = db.relationship('Color', backref=db.backref('schools', lazy=True))
    spells = db.relationship(
        'SpellToSchool', backref=db.backref('school', lazy=True)
    )


class Spell(Model):
    __tablename__ = 'spell'

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

    colors = db.relationship(
        'SpellToColor', backref=db.backref('spell', lazy=True)
    )
    schools = db.relationship(
        'SpellToSchool', backref=db.backref('spell', lazy=True)
    )
