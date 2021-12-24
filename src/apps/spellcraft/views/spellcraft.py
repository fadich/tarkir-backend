__all__ = [
    'CraftView',
]

from typing import Sequence

from tarkir_base.api.views import MethodView

# from apps.configuration import get_application_config
from apps.spellbook.models import Color
from apps.spellcraft.utils import craft

from .schemas import EffectSchema



class CraftView(MethodView):

    @property
    def colors(self) -> Sequence[Color]:
        return Color.query.all()

    def get(self):
        return self.render_template(
            'spellcraft/craft.html',
            colors=self.colors,
        )

    def post(self):
        schema = EffectSchema()
        form = self.request.form
        form_keys = self.request.form.keys()

        colors = []
        for color in ['W', 'U', 'B', 'R', 'G']:
            if color in form_keys:
                colors.append(color)

        effects = craft(
            colors=colors or ['Z', ],
            choices=form.get('choices', 1)
        )

        return {
            'effects': schema.dump(obj=effects, many=True)
        }
