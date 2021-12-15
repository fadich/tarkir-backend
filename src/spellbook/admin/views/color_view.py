__all__ = [
    'ColorAdminView',
]

from spellbook.models import Color
from tarkir_base.api.admin import AdminModelView


class ColorAdminView(AdminModelView):
    __model__ = Color
    __category__ = 'Spellbook'

    column_list = [
        'id',
        'name',
        'shortcut',
        'hex_code',
        'schools',
    ]
    column_editable_list = [
        'name',
        'shortcut',
        'hex_code',
    ]
    column_sortable_list = ['id', ] + column_editable_list
    column_default_sort = ('id', False)
    column_searchable_list = [
        'name',
        'shortcut',
        'hex_code',
    ]

    form_create_rules = form_edit_rules = (
        'name',
        'shortcut',
        'hex_code',
    )
