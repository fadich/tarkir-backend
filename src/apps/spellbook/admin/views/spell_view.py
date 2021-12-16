__all__ = [
    'SpellAdminView',
]

from tarkir_base.admin import (
    AdminModelView,
    ImageUploadField,
    PreviewImageMixin,
)

from apps.spellbook.models import Spell


class SpellAdminView(PreviewImageMixin, AdminModelView):
    __model__ = Spell
    __category__ = 'Spellbook/Spell'
    __index_view__ = True

    column_list = [
        'id',
        'name',
        'name_en',
        'type',
        'schools',
        'colors',
        'image',
    ]
    column_editable_list = [
        'name',
        'name_en',
        'type',
    ]
    column_sortable_list = ['id', ] + column_editable_list
    column_default_sort = ('id', False)
    column_searchable_list = [
        'name',
        'name_en',
    ]
    column_filters = [
        'type',
    ]

    form_create_rules= form_edit_rules = (
        'name',
        'name_en',
        'type',
        'description',
        'requirements',
        'time_to_create',
        'cost',
        'duration',
        'items',
        'image',
    )
    form_overrides = {
        'image': ImageUploadField,
    }

    form_widget_args = {
        'description': {
            'class': 'form-control ckeditor',
        },
        'items': {
            'class': 'form-control ckeditor',
        },
    }
