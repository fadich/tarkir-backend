__all__ = [
    'SpellAdminView',
    'SchoolAdminView',
    'ColorAdminView',
    'PassiveBonusAdminView',
    'SpellToSchoolAdminView',
    'SpellToColorAdminView',
    'PassiveBonusToSchoolAdminView',
]

from flask import url_for
from jinja2 import Markup

from tarkir_base.api import (
    AdminModelView,
    ImageUploadField,
)

from spellbook.models import *


class PreviewImageMixin:
    IMAGE_PREVIEW_MAZ_WIDTH = 48
    IMAGE_PREVIEW_MAZ_HEIGHT = 32

    def _image_to_list(self, context, model, name):
        if not model.image:
            return Markup('<div style="text-align: center;">&ndash;</div>')

        return Markup(
            (
                '<div style="text-align: center;">'
                '<img src="{src}" style="max-width:{width}px; max-height:{height}px; object-fit:contain;">'
                '</div>'
            ).format(
                src=url_for('static', filename=model.image),
                width=self.IMAGE_PREVIEW_MAZ_WIDTH,
                height=self.IMAGE_PREVIEW_MAZ_HEIGHT
            )
        )

    column_formatters = {
        'image': _image_to_list
    }


class SpellAdminView(PreviewImageMixin, AdminModelView):
    __model__ = Spell
    __index_view__ = True

    column_list = [
        'id',
        'name',
        'name_en',
        'type',
        'schools',
        'colors',
        'image',
    ]
    column_editable_list = [
        'name',
        'name_en',
        'type',
    ]
    column_sortable_list = ['id', ] + column_editable_list
    column_default_sort = ('id', False)
    column_searchable_list = [
        'name',
        'name_en',
    ]
    column_filters = [
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


class SchoolAdminView(PreviewImageMixin, AdminModelView):
    __model__ = School

    column_list = [
        'id',
        'name',
        'shortcut',
        'color',
        'image',
    ]
    column_editable_list = [
        'name',
        'shortcut',
    ]
    column_sortable_list = ['id', ] + column_editable_list
    column_default_sort = ('id', False)
    column_searchable_list = [
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
    column_default_sort = ('spell.name', False)


class PassiveBonusToSchoolAdminView(AdminModelView):
    __model__ = PassiveBonusToSchool

    column_list = [
        'passive_bonus',
        'school',
        'passive_bonus.cycle',
    ]

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
    column_default_sort = [('school.id', False), ('passive_bonus.cycle', False)]
