__all__ = [
    'ApplicationAdminView',
]

from jinja2 import Markup

from spellbook.models import Application
from tarkir_base.api.admin import AdminModelView


class ApplicationAdminView(AdminModelView):
    __model__ = Application

    column_list = [
        'name',
        'config',
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

    column_formatters = {
        'config': lambda self, context, model, name: Markup(
            '<br />'.join([
                f"<code><b>{c.name}</b>: <i>({c.data_type.value})</i> {repr(c.value)}</code>"
                for c in model.config
            ])
        ),
    }