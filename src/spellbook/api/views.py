from tarkir.api.views import ModelListView

from spellbook.models import Color, School
from spellbook.schemas import (
    ColorSchema,
    SchoolTreeSchema,
)


class SchoolTreeView(ModelListView):
    schema = SchoolTreeSchema()
    model = School

    def get(self):
        school_tree = super().get()

        return list(map(self.reformat_school, school_tree))

    @classmethod
    def reformat_school(cls, school: dict):
        return {
            **school,
            'spells': {
                f'{school["shortcut"]}{spell["cycle"]}': spell
                for spell in school['spells']
            }
        }


class ColorsView(ModelListView):
    schema = ColorSchema()
    model = Color
