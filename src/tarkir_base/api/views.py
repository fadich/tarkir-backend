__all__ = [
    'ApiView',
    'ModelListView',
    'ModelView',
    'MethodView',
    'send_from_directory',
]

from typing import Type

from flask import (
    jsonify,
    request,
    redirect,
    send_from_directory,
)
from flask.views import MethodView
from flask_marshmallow import Schema
from flask_sqlalchemy import Model
from werkzeug.sansio.response import Response


class ApiView(MethodView):

    @property
    def request(self):
        return request

    def redirect(self, location: str, code: int = 302, Response = None):
        return redirect(
            location=location,
            code=code,
            Response=Response
        )

    def dispatch_request(self, *args, **kwargs):
        body = super().dispatch_request(*args, **kwargs)

        if isinstance(body, Response):
            return body

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
