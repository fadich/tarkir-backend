from flask import jsonify
from flask.views import MethodView


class ApiView(MethodView):

    def dispatch_request(self, *args, **kwargs):
        return jsonify(super().dispatch_request(*args, **kwargs))
