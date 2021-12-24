__all__ = [
    'EffectAdminView',
]

from tarkir_base.admin import (
    AdminModelView,
    ImageUploadField,
    PreviewImageMixin,
)

from ..models import Effect


class EffectAdminView(PreviewImageMixin, AdminModelView):
    __model__ = Effect
    __category__ = 'Spellcraft'
    __index_view__ = True

    column_list = [
        'id',
        'name',
        'type',
        'time_to_create',
        'cost',
        'colors',
        'image',
    ]
    column_editable_list = [
        'name',
        'type',
    ]
    column_sortable_list = ['id', ] + column_editable_list
    column_default_sort = ('id', False)
    column_searchable_list = [
        'name',
    ]
    column_filters = [
        'type',
    ]

    form_create_rules= form_edit_rules = (
        'name',
        'type',
        'description',
        'duration',
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
