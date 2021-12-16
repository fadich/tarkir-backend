__all__ = [
    'UploadedFile',
]

import os

from tarkir_base.api import app
from tarkir_base.database import (
    db,
    Model,
)


class UploadedFile(Model):
    __tablename__ = 'uploaded_file'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    file = db.Column(
        db.String(1024), nullable=True,
    )
    name = db.Column(db.String(256), nullable=True)

    def __str__(self):
        return f'{self.file}'

    @property
    def fullpath(self):
        return os.path.join(
            app.static_url_path,
            self.file
        )
