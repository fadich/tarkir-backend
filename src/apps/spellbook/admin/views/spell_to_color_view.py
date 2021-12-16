__all__ = [
    'SpellToColorAdminView',
]

from tarkir_base.admin import AdminModelView

from apps.spellbook.models import SpellToColor


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
