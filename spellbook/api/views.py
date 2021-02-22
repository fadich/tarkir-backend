from tarkir.api import ApiView

from spellbook.models import Color
from spellbook.schemas import ColorSchema


class ColorsView(ApiView):
    color_schema = ColorSchema()

    @property
    def colors(self):
        return Color.query.all()

    def get(self):
        return self.color_schema.dump(self.colors, many=True)
