__all__ = [
    'SchoolView',
    'IndexView',
    'ColorsView',
]

from tarkir_base.api.views import ModelView, ModelListView

from spellbook.models import Color, School
from spellbook.schemas import (
    ColorSchema,
    SchoolTreeSchema,
)
from .mixins import SchoolFormatterMixin


class IndexView(ModelListView, SchoolFormatterMixin):
    schema = SchoolTreeSchema()
    model = School

    @property
    def records(self):
        return self.model.query.order_by(self.model.id).all()

    def get(self):
        school_tree = super().get()

        return list(map(self.reformat_school, school_tree))


class SchoolView(ModelView, SchoolFormatterMixin):
    id_key = 'school-id'
    schema = SchoolTreeSchema()
    model = School

    def get(self):
        school = super().get()

        return self.reformat_school(school)


class ColorsView(ModelListView):
    schema = ColorSchema()
    model = Color
