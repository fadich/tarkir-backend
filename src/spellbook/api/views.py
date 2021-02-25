from collections import defaultdict

from tarkir.api.views import ModelView, ModelListView

from spellbook.models import Color, School
from spellbook.schemas import (
    ColorSchema,
    SchoolTreeSchema,
)


class SchoolFormatterMixin:

    @classmethod
    def reformat_school(cls, school: dict):
        spells = defaultdict(list)
        for spell in school['spells']:
            spell['spell']['schools'] = [
                {
                    'cycle': school['cycle'],
                    **school['school'],
                } for school in spell['spell']['schools']
            ]

            spell = {
                'cycle': spell['cycle'],
                **spell['spell'],
            }
            spells[f'{school["shortcut"]}{spell["cycle"]}'].append(spell)

        return {
            **school,
            'spells': spells,
        }


class SchoolView(ModelView, SchoolFormatterMixin):
    id_key = 'school-id'
    schema = SchoolTreeSchema()
    model = School

    def get(self):
        school = super().get()

        return self.reformat_school(school)


class SchoolsTreeView(ModelListView, SchoolFormatterMixin):
    schema = SchoolTreeSchema()
    model = School

    def get(self):
        school_tree = super().get()

        return list(map(self.reformat_school, school_tree))


class ColorsView(ModelListView):
    schema = ColorSchema()
    model = Color
