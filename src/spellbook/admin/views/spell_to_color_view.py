__all__ = [
    'SpellToColorAdminView',
]

from spellbook.models import SpellToColor
from tarkir_base.api.admin import AdminModelView


class SpellToColorAdminView(AdminModelView):
    __model__ = SpellToColor
    __category__ = 'Spellbook/Spell'

    column_searchable_list = [
        'spell.name',
        'color.shortcut',
        'color.name',
    ]
    column_filters = [
        'color.shortcut',
        'color.name',
    ]
    column_editable_list = [
        'spell',
        'color',
    ]
    column_default_sort = ('spell.name', False)
