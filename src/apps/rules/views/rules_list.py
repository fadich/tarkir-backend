__all__ = [
    'RulesListView',
]

from typing import Sequence

from tarkir_base.api.views import MethodView

from ..models import Rule


class RulesListView(MethodView):

    @property
    def rules(self) -> Sequence[Rule]:
        return Rule.query.all()

    def get(self):
        return self.render_template(
            'rules/rules-list.html',
            rules=self.rules
        )
