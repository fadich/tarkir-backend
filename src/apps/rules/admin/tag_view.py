__all__ = [
    'TagAdminView',
]

from tarkir_base.admin import AdminModelView

from apps.rules.models import Tag


class TagAdminView(AdminModelView):
    __model__ = Tag
    __category__ = 'Rules'

    column_list = [
        'id',
        'name',
    ]
    column_editable_list = [
        'name',
    ]
    column_sortable_list = ['id', ] + column_editable_list
    column_default_sort = ('id', False)
    column_searchable_list = [
        'name',
    ]

    form_create_rules = form_edit_rules = (
        'name',
    )
