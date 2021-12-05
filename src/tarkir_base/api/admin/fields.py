__all__ = [
    'FileUploadField',
    'ImageUploadField',
]

import os

from time import time
from typing import Optional, Callable

from flask_admin.form.upload import FileUploadField as FlaskFileUploadField

try:
    from wtforms.fields.core import _unset_value as unset_value
except ImportError:
    from wtforms.utils import unset_value


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.base_path is None:
            # pylint: disable=import-outside-toplevel
            from tarkir_base.api import app

            self.base_path = app.config['UPLOAD_FOLDER']

        self.namegen = ts_prefix_namegen(self.namegen)

    def process(self, formdata, data: Optional = None):
        if data is None:
            data = unset_value
            
        return super().process(formdata=formdata, data=data)


class ImageUploadField(FileUploadField):
    pass
