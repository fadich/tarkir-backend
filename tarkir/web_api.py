import json

from logging import getLogger

from aiohttp import web, hdrs

from .database import connect_db, disconnect_db


__all__ = (
    'Route',
    'Handler',
    'Application',
)


class Handler(web.View):

    def send_json(self, body, status_code: int = 200):
        body = json.dumps(body)

        return web.Response(body=body, status=status_code, headers={
            hdrs.CONTENT_TYPE: 'application/json; charset=utf-8',
        })


class Route:

    __slots__ = ('path', 'method', 'handler')

    def __init__(self, path: str, method: str, handler: Handler):
        self.path = path
        self.method = method
        self.handler = handler

    def __str__(self):
        method = f'[{self.method}]'
        return f'{method:>12} `{self.path}` -> {self.handler.__name__}()'

    def __hash__(self):
        return hash(f'{self.method} {self.path}')


class Application:
    METHOD_CONNECT = hdrs.METH_CONNECT
    METHOD_HEAD = hdrs.METH_HEAD
    METHOD_GET = hdrs.METH_GET
    METHOD_DELETE = hdrs.METH_DELETE
    METHOD_OPTIONS = hdrs.METH_OPTIONS
    METHOD_PATCH = hdrs.METH_PATCH
    METHOD_POST = hdrs.METH_POST
    METHOD_PUT = hdrs.METH_PUT
    METHOD_TRACE = hdrs.METH_TRACE

    HTTP_METHODS = (
        METHOD_CONNECT,
        METHOD_HEAD,
        METHOD_GET,
        METHOD_DELETE,
        METHOD_OPTIONS,
        METHOD_PATCH,
        METHOD_POST,
        METHOD_PUT,
        METHOD_TRACE,
        # etc ...
    )

    def __init__(self):
        self._app = web.Application()

        self._routes = set()
        self._logger = getLogger(self.__class__.__name__)

    def add_route(self, route: Route):
        self._routes.add(route)

    def remove_route(self, route: Route):
        self._routes.remove(route)

    def run_app(self, **kwargs):
        self._register_routes()

        self._app.on_startup.extend(
            (connect_db, )
        )

        self._app.on_cleanup.extend(
            (disconnect_db, )
        )

        web.run_app(self._app, **kwargs)

    def _register_routes(self):
        app_routes = []
        for route in self._routes:
            if route.method.upper() not in self.HTTP_METHODS:
                raise ValueError(f'Method "{route.method}" as not allowed')

            method = getattr(web, route.method.lower())
            app_routes.append(method(route.path, route.handler))
            self._logger.info('route %s registered', route)

        self._app.add_routes(app_routes)
