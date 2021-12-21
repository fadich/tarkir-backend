__all__ = [
    'ApiView',
    'ModelListView',
    'ModelView',
    'MethodView',
    'send_from_directory',
]

import os
from typing import Type, Optional

from flask import (
    jsonify,
    request,
    redirect,
    url_for,
    render_template,
    send_from_directory,
)
from flask.views import MethodView as FlaskMethodView
from flask_marshmallow import Schema
from flask_sqlalchemy import Model
from sqlalchemy.orm import Query
from werkzeug.sansio.response import Response

from . import app


class MethodView(FlaskMethodView):
    __scope__: Optional[str] = None

    @property
    def request(self):
        return request

    @property
    def redirect_non_permitted_url(self) -> Optional[str]:
        return None

    def check_permission(self) -> bool:
        return True

    def dispatch_request(self, *args, **kwargs):
        if not self.check_permission():
            if self.redirect_non_permitted_url is not None:
                return self.redirect(self.redirect_non_permitted_url, 301)

            return 'Not permitted', 403

        return super().dispatch_request(*args, **kwargs)

    @classmethod
    def get_full_url(cls, scope: Optional[str] = None):
        if scope is None:
            scope = cls.__scope__

        endpoint = cls.__name__
        if scope is not None:
            endpoint = f'{scope}.{endpoint}'

        return os.path.join(app.config['BASE_URL'], cls.url_for(endpoint=endpoint)[1:])

    @staticmethod
    def redirect(location: str, code: int = 302, Response = None):
        return redirect(
            location=location,
            code=code,
            Response=Response
        )

    @staticmethod
    def render_template(template_name_or_list, **context):
        return render_template(
            template_name_or_list,
            **context
        )

    @staticmethod
    def url_for(endpoint, **values):
        return url_for(endpoint, **values)


class ApiView(MethodView):

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
    def query(self) -> Query:
        return self.model.query

    def get(self):
        return self.schema.dump(obj=self.query.all(), many=True)


class ModelView(ApiView):
    id_key: str = None
    schema: Schema = None
    model: Type[Model] = None

    def get(self):
        records = self.model.query.get(self.request.args.get(self.id_key))

        return self.schema.dump(obj=records)
