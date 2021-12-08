__all__ = [
    'Application',
    'Blueprint',
]

from typing import Sequence, Type, Optional, Union

from flask import Flask, Blueprint
from flask_admin.contrib.sqla import ModelView as FlaskAdminModelView

from tarkir_base.api.admin import Admin, AdminModelView

ModelType = Type['Model']
ModelViewType = Type['ModelView']


class Application(Flask):

    def run(
        self, host=None, port=None, debug=None, load_dotenv=True, **options
    ):
        return super().run(
            host=host or self.config['API_HOST'],
            port=port or self.config['API_PORT'],
            debug=debug or self.config['DEBUG'],
            load_dotenv=load_dotenv,
            **options
        )

    @classmethod
    def init_admin(cls, admin: Admin, classes: Optional[Sequence[Union[ModelType, ModelViewType]]] = None):
        # pylint: disable=import-outside-toplevel
        from tarkir_base.database import Model

        for class_ in classes:
            if issubclass(class_, Model):
                admin.add_view(AdminModelView(class_, admin.db.session))
            elif issubclass(class_, FlaskAdminModelView):
                admin.add_view(class_(class_.__model__, admin.db.session))
            else:
                raise TypeError(f'Unsupported admin model type: {class_}')
