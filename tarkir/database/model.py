from tarkir.api import db


class Model(db.Model):
    __abstract__ = True

    def save(self, no_commit=False):
        db.session.add(self)

        if no_commit is False:
            db.session.commit()

        return self
