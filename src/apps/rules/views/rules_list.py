__all__ = [
    'RulesListView',
]

from typing import Sequence

from tarkir_base.api.views import MethodView
from apps.configuration import get_application_config

from ..models import Rule


class RulesListView(MethodView):

    @property
    def rules(self) -> Sequence[Rule]:
        return Rule.query.order_by(Rule.name).all()

    @property
    def config(self):
        return get_application_config('rules')

    def get(self):
        return self.render_template(
            'rules/rules-list.html',
            rules=self.rules,
            default_rule_image=self.config.get('default-rule-image')
        )
