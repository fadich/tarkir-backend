__all__ = [
    'PassiveBonusToSchoolAdminView',
]


from tarkir_base.admin import AdminModelView

from apps.spellbook.models import PassiveBonusToSchool


class PassiveBonusToSchoolAdminView(AdminModelView):
    __model__ = PassiveBonusToSchool
    __category__ = 'Spellbook/Passive Bonus'

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
