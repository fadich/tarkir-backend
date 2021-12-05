__all__ = [
    'SpellAdminView',
    'SchoolAdminView',
    'ColorAdminView',
    'PassiveBonusAdminView',
    'SpellToSchoolAdminView',
    'SpellToColorAdminView',
    'PassiveBonusToSchoolAdminView',
]

from tarkir_base.api import (
    AdminModelView,
    ImageUploadField,
)

from spellbook.models import *


class SpellAdminView(AdminModelView):
    __model__ = Spell
    __index_view__ = True

    column_list = [
        'id',
        'name',
        'name_en',
        'type',
        'schools',
        'colors',
    ]
    column_editable_list = [
        'name',
        'name_en',
        'type',
    ]
    form_create_rules= form_edit_rules = (
        'name',
        'name_en',
        'type',
        'description',
        'requirements',
        'time_to_create',
        'cost',
        'duration',
        'items',
        'image',
    )
    form_overrides = {
        'image': ImageUploadField,
    }

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
        'items': {
            'class': 'form-control ckeditor',
        },
    }

    create_template = 'admin/ckeditor-create.html'
    edit_template = 'admin/ckeditor-edit.html'


class SchoolAdminView(AdminModelView):
    __model__ = School

    column_list = [
        'id',
        'name',
        'shortcut',
        'color',
    ]
    column_editable_list = [
        'name',
        'shortcut',
    ]
    form_create_rules= form_edit_rules = (
        'name',
        'shortcut',
        'description',
        'color',
        'image',
    )
    form_overrides = {
        'image': ImageUploadField,
    }

    column_searchable_list = [
        'name',
        'shortcut',
    ]

    form_widget_args = {
        'description': {
            'class': 'form-control ckeditor',
        },
    }

    create_template = 'admin/ckeditor-create.html'
    edit_template = 'admin/ckeditor-edit.html'


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
    form_create_rules= form_edit_rules = (
        'name',
        'name_en',
        'description',
        'cycle',
    )
    column_searchable_list = [
        'name',
        'name_en',
    ]

    form_widget_args = {
        'description': {
            'class': 'form-control ckeditor',
        },
    }

    create_template = 'admin/ckeditor-create.html'
    edit_template = 'admin/ckeditor-edit.html'


class ColorAdminView(AdminModelView):
    __model__ = Color

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
    form_create_rules= form_edit_rules = (
        'name',
        'shortcut',
        'hex_code',
    )
    column_searchable_list = [
        'name',
        'shortcut',
        'hex_code',
    ]


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
    page_size = 50


class SpellToColorAdminView(AdminModelView):
    __model__ = SpellToColor

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
    page_size = 50


class PassiveBonusToSchoolAdminView(AdminModelView):
    __model__ = PassiveBonusToSchool

    column_searchable_list = [
        'passive_bonus.name',
        'passive_bonus.name_en',
        'school.shortcut',
        'school.name',
    ]
    column_editable_list = [
        'passive_bonus',
        'school',
    ]
    column_filters = [
        'passive_bonus.cycle',
        'school.shortcut',
    ]
    page_size = 50
