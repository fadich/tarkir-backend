__all__ = [
    'SpellAdminView',
    'SchoolAdminView',
    'ColorAdminView',
    'SpellToSchoolAdminView',
    'SpellToColorAdminView',
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
    form_widget_args = {
        'description': {
            'class': 'form-control ckeditor',
        },
        'requirements': {
            'class': 'form-control ckeditor',
        },
        'items': {
            'class': 'form-control ckeditor',
        },
    }

    create_template = 'admin/ckeditor-create.html'
    edit_template = 'admin/ckeditor-edit.html'


class SchoolAdminView(AdminModelView):
    __model__ = School

    form_widget_args = {
        'description': {
            'class': 'form-control ckeditor',
        },
    }

    create_template = 'admin/ckeditor-create.html'
    edit_template = 'admin/ckeditor-edit.html'


class ColorAdminView(AdminModelView):
    __model__ = Color


class SpellToSchoolAdminView(AdminModelView):
    __model__ = SpellToSchool

    column_searchable_list = [
        'spell.name',
    ]
    column_filters = [
        'school.shortcut',
        'cycle',
        'school.name',
    ]
    page_size = 50


class SpellToColorAdminView(AdminModelView):
    __model__ = SpellToColor

    column_searchable_list = [
        'spell.name',
    ]
    column_filters = [
        'color.shortcut',
        'color.name',
    ]
    page_size = 50
