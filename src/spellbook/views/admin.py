__all__ = [
    'SpellAdminView',
    'SchoolAdminView',
    'ColorAdminView',
    'PassiveBonusAdminView',
    'SpellToSchoolAdminView',
    'SpellToColorAdminView',
    'PassiveBonusToSchoolAdminView',
    'ConfigAdminView',
    'ApplicationAdminView',
    'UploadedFileAdminView',
]

from flask import url_for
from jinja2 import Markup
from wtforms import ValidationError

from tarkir_base.api import (
    AdminModelView,
    ImageUploadField,
    FileUploadField,
)

from spellbook.models import *


class PreviewImageMixin:
    IMAGE_PREVIEW_MAZ_WIDTH = 48
    IMAGE_PREVIEW_MAZ_HEIGHT = 32

    IMAGE_FIELD_NAME = 'image'

    def _image_to_list(self, context, model, name):
        image = getattr(model, self.IMAGE_FIELD_NAME)

        if not image:
            return Markup('<div style="text-align: center;">&ndash;</div>')

        return Markup(
            (
                '<div style="text-align: center;">'
                '<img src="{src}" style="max-width:{width}px; max-height:{height}px; object-fit:contain;">'
                '</div>'
            ).format(
                src=url_for('static', filename=image),
                width=self.IMAGE_PREVIEW_MAZ_WIDTH,
                height=self.IMAGE_PREVIEW_MAZ_HEIGHT
            )
        )

    column_formatters = {
        IMAGE_FIELD_NAME: _image_to_list
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


class ConfigAdminView(AdminModelView):
    __model__ = Config

    class RawValueDataTypeValidator:

        def __call__(self, form, field):
            key = Config.DataTypesEnum[form.data['data_type']]

            try:
                return Config.TYPES_MAP[key](field.raw_data[0])
            except (TypeError, ValueError) as e:
                raise ValidationError(f'Error on value type converting: {e}')

    column_list = [
        'application',
        'name',
        'data_type',
        'raw_value',
        'python_value',
    ]
    column_editable_list = [
        'application',
        'name',
    ]
    column_sortable_list = [
        'application',
        'name',
        'data_type',
        'raw_value',
    ]
    column_default_sort = ('application.name', False)
    column_searchable_list = [
        'application.name',
        'name',
    ]

    form_create_rules = form_edit_rules = (
        'application',
        'name',
        'data_type',
        'raw_value',
    )
    form_args = {
        'raw_value': {
            'validators': [
                RawValueDataTypeValidator()
            ]
        }
    }


class ApplicationAdminView(AdminModelView):
    __model__ = Application

    column_list = [
        'name',
    ]
    column_editable_list = column_sortable_list = [
        'name',
    ]
    column_default_sort = ('id', False)
    column_searchable_list = [
        'name',
    ]

    form_create_rules = form_edit_rules = (
        'name',
    )


class UploadedFileAdminView(PreviewImageMixin, AdminModelView):
    __model__ = UploadedFile

    IMAGE_FIELD_NAME = 'file'
    IMAGE_PREVIEW_MAZ_HEIGHT = 64
    IMAGE_PREVIEW_MAZ_WIDTH = 128

    column_list = [
        'id',
        'file',
        'fullpath',
        'name',
    ]
    column_editable_list = column_sortable_list = [
        'name',
    ]
    column_default_sort = ('id', False)
    column_searchable_list = [
        'file',
        'name',
    ]

    form_create_rules = form_edit_rules = (
        'file',
        'name',
    )
    form_overrides = {
        'file': FileUploadField,
    }

    column_formatters = {
        IMAGE_FIELD_NAME: PreviewImageMixin._image_to_list,
        'fullpath': lambda self, context, model, name: Markup(
            f'<a href="{model.fullpath}" target="_blank">{model.fullpath}</a>'
        ),
    }
