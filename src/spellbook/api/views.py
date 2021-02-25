from tarkir.api.views import ModelListView

from spellbook.models import Color, School, Spell
from spellbook.schemas import (
    ColorSchema,
    SpellSchema,
    SchoolSchema,
    SchoolTreeSchema,
)


class SchoolTreeView(ModelListView):
    schema = SchoolTreeSchema()
    model = School


class ColorsView(ModelListView):
    schema = ColorSchema()
    model = Color


class SchoolsView(ModelListView):
    schema = SchoolSchema()
    model = School


class SpellsView(ModelListView):
    schema = SpellSchema()
    model = Spell
