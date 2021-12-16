from typing import Type

from flask_admin import AdminIndexView as FlaskAdminIndexView
from flask_admin.contrib.sqla import ModelView as FlaskAdminModelView

from tarkir_base.api import app

from apps.auth import (
    AuthException,
    is_authorized,
    get_current_user,
)


ModelType = Type['Model']
ModelViewType = Type['ModelView']


class AccessAdminViewMixin:

    def is_accessible(self):
        if app.config['DEBUG']:
            return True

        if not is_authorized():
            raise AuthException('Unauthorized', code=401)

        user = get_current_user()
        if not user.is_admin:
            raise AuthException('Forbidden', code=403)

        return True


class AdminIndexView(AccessAdminViewMixin, FlaskAdminIndexView):
    pass


class AdminModelView(AccessAdminViewMixin, FlaskAdminModelView):
    __model__: ModelType
    __category__: str = 'Other'  # Split by `/` for subcategories

    page_size = 50

    create_template = 'admin/ckeditor-create.html'
    edit_template = 'admin/ckeditor-edit.html'
