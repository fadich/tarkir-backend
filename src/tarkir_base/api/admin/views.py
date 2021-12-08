from typing import Type

from tarkir_base.api.exceptions import AuthException

from flask_admin import AdminIndexView as FlaskAdminIndexView
from flask_admin.contrib.sqla import ModelView as FlaskAdminModelView

ModelType = Type['Model']
ModelViewType = Type['ModelView']


class AccessAdminViewMixin:

    def is_accessible(self):
        from tarkir_base.api import ba

        if not ba.authenticate():
            raise AuthException('Unauthorized')

        return True


class AdminIndexView(AccessAdminViewMixin, FlaskAdminIndexView):
    pass


class AdminModelView(AccessAdminViewMixin, FlaskAdminModelView):
    __model__: ModelType

    page_size = 50
