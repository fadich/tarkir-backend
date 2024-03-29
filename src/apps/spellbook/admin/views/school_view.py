__all__ = [
    'SchoolAdminView',
]

from tarkir_base.admin import (
    AdminModelView,
    ImageUploadField,
    PreviewImageMixin,
)

from apps.spellbook.models import School


class SchoolAdminView(PreviewImageMixin, AdminModelView):
    __model__ = School
    __category__ = 'Spellbook'

    column_list = [
        'id',
        'name',
        'shortcut',
        'color',
        'image',
    ]
    column_editable_list = [
        'name',
        'shortcut',
    ]
    column_sortable_list = ['id', ] + column_editable_list
    column_default_sort = ('id', False)
    column_searchable_list = [
        'name',
        'shortcut',
    ]

    form_create_rules= form_edit_rules = (
        'name',
        'shortcut',
        'description',
        'color',
        'image',
    )
    form_overrides = {
        'image': ImageUploadField,
    }

    form_widget_args = {
        'description': {
            'class': 'form-control ckeditor',
        },
    }
