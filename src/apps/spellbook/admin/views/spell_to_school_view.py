__all__ = [
    'SpellToSchoolAdminView',
]

from tarkir_base.admin import AdminModelView

from apps.spellbook.models import SpellToSchool


class SpellToSchoolAdminView(AdminModelView):
    __model__ = SpellToSchool
    __category__ = 'Spellbook/Spell'

    column_searchable_list = [
        'spell.name',
        'school.shortcut',
        'school.name',
    ]
    column_editable_list = [
        'spell',
        'school',
        'cycle',
    ]
    column_filters = [
        'school.shortcut',
        'cycle',
        'school.name',
    ]
    column_default_sort = [('school.id', False), ('cycle', False), ('spell.name', False)]
