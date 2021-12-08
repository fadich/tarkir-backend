__all__ = [
    'PassiveBonusAdminView',
]

from spellbook.models import PassiveBonus
from tarkir_base.api.admin import AdminModelView


class PassiveBonusAdminView(AdminModelView):
    __model__ = PassiveBonus

    column_list = [
        'id',
        'name',
        'name_en',
        'cycle',
        'schools',
    ]
    column_editable_list = [
        'name',
        'name_en',
        'cycle',
    ]
    column_sortable_list = ['id', ] + column_editable_list
    column_default_sort = ('id', False)
    column_searchable_list = [
        'name',
        'name_en',
    ]

    form_create_rules= form_edit_rules = (
        'name',
        'name_en',
        'description',
        'cycle',
    )

    form_widget_args = {
        'description': {
            'class': 'form-control ckeditor',
        },
    }
