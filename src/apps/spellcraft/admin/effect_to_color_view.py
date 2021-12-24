__all__ = [
    'EffectToColorAdminView',
]

from tarkir_base.admin import AdminModelView

from ..models import EffectToColor


class EffectToColorAdminView(AdminModelView):
    __model__ = EffectToColor
    __category__ = 'Spellcraft'

    column_searchable_list = [
        'effect.name',
        'color.shortcut',
        'color.name',
    ]
    column_filters = [
        'color.shortcut',
        'color.name',
    ]
    column_editable_list = [
        'effect',
        'color',
    ]
    column_default_sort = ('color.name', False)
