__all__ = [
    'FileUploadField',
    'ImageUploadField',
]

import os

from time import time
from typing import Optional, Callable

from flask_admin.form.upload import (
    FileUploadField as FlaskFileUploadField,
    ImageUploadField as FlaksImageUploadField
)

try:
    from wtforms.fields.core import _unset_value as unset_value
except ImportError:
    from wtforms.utils import unset_value

from tarkir_base.api import app


def ts_prefix_namegen(namegen_cb: Callable):
    """File name generator wrapper to add timestamp file prefix"""

    def wrap(obj, file_data):
        filepath = namegen_cb(obj=obj, file_data=file_data)
        filename = os.path.basename(filepath)
        dirname = os.path.dirname(filepath)

        ts_prefix = str(int(time() * 1000))
        filename = f'{ts_prefix}-{filename}'

        return os.path.join(dirname, filename)

    return wrap


class FileUploadField(FlaskFileUploadField):
    UPLOAD_FIR = 'upload'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.base_path is None:
            self.base_path = os.path.join(
                app.config['FLASK_STATIC_FOLDER'],
                self.UPLOAD_FIR
            )

        self.namegen = ts_prefix_namegen(self.namegen)

    def process(self, formdata, data: Optional = None):
        if data is None:
            data = unset_value

        return super().process(formdata=formdata, data=data)

    def _save_file(self, data, filename):
        return os.path.join(
            self.UPLOAD_FIR,
            super()._save_file(data=data, filename=filename)
        )


class ImageUploadField(FileUploadField, FlaksImageUploadField):

    def _save_file(self, data, filename):
        return os.path.join(
            self.UPLOAD_FIR,
            FlaksImageUploadField._save_file(self=self, data=data, filename=filename)
        )
