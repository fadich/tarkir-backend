__all__ = [
    'RuleToTagAdminView',
]


from tarkir_base.admin import AdminModelView

from apps.rules.models import RuleToTag


class RuleToTagAdminView(AdminModelView):
    __model__ = RuleToTag
    __category__ = 'Rules'

    column_list = [
        'rule',
        'tag',
    ]

    column_searchable_list = [
        'rule.name',
        'rule.description',
        'tag.name',
    ]
    column_editable_list = [
        'rule',
        'tag',
    ]
    column_filters = [
        'rule.name',
        'tag.name',
    ]
    column_default_sort = [('rule.name', False), ('tag.name', False)]
