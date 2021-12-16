__all__ = [
    'PassiveBonusAdminView',
]

from tarkir_base.admin import AdminModelView

from apps.spellbook.models import PassiveBonus


class PassiveBonusAdminView(AdminModelView):
    __model__ = PassiveBonus
    __category__ = 'Spellbook/Passive Bonus'

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
