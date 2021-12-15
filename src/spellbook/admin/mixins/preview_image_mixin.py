__all__ = [
    'PreviewImageMixin',
]


from flask import url_for
from jinja2 import Markup


class PreviewImageMixin:
    IMAGE_PREVIEW_MAZ_WIDTH = 48
    IMAGE_PREVIEW_MAZ_HEIGHT = 32

    IMAGE_FIELD_NAME = 'image'

    def _image_to_list(self, context, model, name):
        image = getattr(model, self.IMAGE_FIELD_NAME)

        if not image:
            return Markup('<div style="text-align: center;">&ndash;</div>')

        if not (image.startswith('http://') or image.startswith('https://')):
            image = url_for('static', filename=image)

        return Markup(
            (
                '<div style="text-align: center;">'
                '<img src="{src}" style="max-width:{width}px; max-height:{height}px; object-fit:contain;">'
                '</div>'
            ).format(
                src=image,
                width=self.IMAGE_PREVIEW_MAZ_WIDTH,
                height=self.IMAGE_PREVIEW_MAZ_HEIGHT
            )
        )

    column_formatters = {
        IMAGE_FIELD_NAME: _image_to_list
    }
