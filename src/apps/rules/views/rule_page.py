__all__ = [
    'RulePageView',
]

from typing import Sequence

from tarkir_base.api.views import MethodView
from apps.configuration import get_application_config

from ..models import Rule


class RulePageView(MethodView):

    @property
    def config(self):
        return get_application_config('rules')

    def get(self, rule_id: int):
        rule = Rule.query.get(rule_id)

        return self.render_template(
            'rules/rule-page.html',
            rule=rule,
        )
