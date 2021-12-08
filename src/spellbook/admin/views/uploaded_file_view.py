__all__ = [
    'UploadedFileAdminView',
]

from spellbook.admin.mixins import PreviewImageMixin
from spellbook.models import UploadedFile
from tarkir_base.api import AdminModelView, FileUploadField


class UploadedFileAdminView(PreviewImageMixin, AdminModelView):
    __model__ = UploadedFile

    IMAGE_FIELD_NAME = 'file'
    IMAGE_PREVIEW_MAZ_HEIGHT = 64
    IMAGE_PREVIEW_MAZ_WIDTH = 128

    column_list = [
        'id',
        'file',
        'fullpath',
        'name',
    ]
    column_editable_list = column_sortable_list = [
        'name',
    ]
    column_default_sort = ('id', False)
    column_searchable_list = [
        'file',
        'name',
    ]

    form_create_rules = form_edit_rules = (
        'file',
        'name',
    )
    form_overrides = {
        'file': FileUploadField,
    }

    column_formatters = {
        'file': PreviewImageMixin._image_to_list,
        'fullpath': lambda self, context, model, name: Markup(
            f'<a href="{model.fullpath}" target="_blank">{model.fullpath}</a>'
        ),

    }
