from typing import Type

from flask import jsonify
from flask.views import MethodView
from flask_admin.contrib.sqla import ModelView as FlaskAdminModelView
from flask_marshmallow import Schema
from flask_sqlalchemy import Model


class ApiView(MethodView):

    def dispatch_request(self, *args, **kwargs):
        return jsonify(super().dispatch_request(*args, **kwargs))


class ModelListView(ApiView):
    schema: Schema = None
    model: Type[Model] = None

    def get(self):
        records = self.model.query.all()

        return self.schema.dump(obj=records, many=True)


class AdminModelView(FlaskAdminModelView):
    pass
