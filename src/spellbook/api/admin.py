__all__ = [
    'SpellAdminView',
    'SchoolAdminView',
    'ColorAdminView',
]


from tarkir_base.api import AdminModelView

from spellbook.models import *


class SpellAdminView(AdminModelView):
    __model__ = Spell
    __index_view__ = True

    column_list = [
        'id',
        'name',
        'name_en',
        'type',
    ]
    column_searchable_list = [
        'name',
        'name_en',
    ]
    column_filters = [
        'type',
    ]
    page_size = 50


class SchoolAdminView(AdminModelView):
    __model__ = School


class ColorAdminView(AdminModelView):
    __model__ = Color
