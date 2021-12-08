__all__ = [
    'ApiView',
    'ModelListView',
    'ModelView',
    'MethodView',
    'send_from_directory',
]

from typing import Type

from flask import jsonify, request, send_from_directory
from flask.views import MethodView
from flask_marshmallow import Schema
from flask_sqlalchemy import Model


class ApiView(MethodView):

    @property
    def request(self):
        return request

    def dispatch_request(self, *args, **kwargs):
        body = super().dispatch_request(*args, **kwargs)

        response = jsonify(body)
        response.headers['Access-Control-Allow-Origin'] = '*'

        return response


class ModelListView(ApiView):
    schema: Schema = None
    model: Type[Model] = None

    @property
    def records(self):
        return self.query.all()

    def get(self):
        return self.schema.dump(obj=self.records, many=True)


class ModelView(ApiView):
    id_key: str = None
    schema: Schema = None
    model: Type[Model] = None

    def get(self):
        records = self.model.query.get(self.request.args.get(self.id_key))

        return self.schema.dump(obj=records)
