__all__ = [
    'ConfigAdminView',
]

from wtforms import ValidationError

from spellbook.models import Config
from tarkir_base.api.admin import AdminModelView


class ConfigAdminView(AdminModelView):
    __model__ = Config
    __category__ = 'Configuration'

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
