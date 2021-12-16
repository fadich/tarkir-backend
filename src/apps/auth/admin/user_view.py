__all__ = [
    'UserAdminView',
]

from tarkir_base.admin import (
    AdminModelView,
    FileUploadField,
    PreviewImageMixin,
)

from apps.auth import User


class UserAdminView(PreviewImageMixin, AdminModelView):
    __model__ = User
    __category__ = 'User'

    IMAGE_FIELD_NAME = 'picture'
    IMAGE_PREVIEW_MAZ_HEIGHT = 64
    IMAGE_PREVIEW_MAZ_WIDTH = 128

    column_list = [
        'id',
        'picture',
        'name',
        'email',
        'google_id',
        'is_admin',
    ]
    column_editable_list = column_sortable_list = [
        'is_admin',
    ]
    column_default_sort = ('id', False)
    column_searchable_list = [
        'name',
        'email',
        'google_id',
    ]

    form_create_rules = form_edit_rules = (
        'is_admin',
    )
    form_overrides = {
        'picture': FileUploadField,
    }

    column_formatters = {
        'picture': PreviewImageMixin._image_to_list,
    }
