__all__ = [
    'SpellToSchoolAdminView',
]

from spellbook.models import SpellToSchool
from tarkir_base.api import AdminModelView


class SpellToSchoolAdminView(AdminModelView):
    __model__ = SpellToSchool

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
