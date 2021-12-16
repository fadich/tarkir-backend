__all__ = [
    'RuleAdminView',
]

from tarkir_base.admin import (
    AdminModelView,
    ImageUploadField,
    PreviewImageMixin,
)

from apps.rules.models import Rule


class RuleAdminView(PreviewImageMixin, AdminModelView):
    __model__ = Rule
    __category__ = 'Rules'

    column_list = [
        'id',
        'image',
        'name',
        'tags',
    ]
    column_editable_list = [
        'name',
    ]
    column_sortable_list = ['id', ] + column_editable_list
    column_default_sort = ('id', False)
    column_searchable_list = [
        'name',
        'description',
    ]

    form_create_rules= form_edit_rules = (
        'name',
        'description',
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
