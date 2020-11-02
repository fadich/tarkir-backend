from tarkir import db


class Color(db.Model):
    __tablename__ = 'color'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    shortcut = db.Column(db.String(1), nullable=False, unique=True)
    hex_code = db.Column(db.String(16), nullable=False)


class School(db.Model):
    __tablename__ = 'school'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    shortcut = db.Column(db.String(2), nullable=False, unique=True)
    color_id = db.Column(db.Integer, db.ForeignKey('color.id'), nullable=False)
