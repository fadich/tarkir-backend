__all__ = [
    'Application',
    'Blueprint',
]

from typing import Sequence, Type, Optional

from flask import Flask, Blueprint

from tarkir_base.utils.classes import SingletonMeta

AdminModelViewType = Type['AdminModelView']


class Application(Flask, metaclass=SingletonMeta):

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
    def init_admin(cls, admin, classes: Optional[Sequence[AdminModelViewType]] = None):
        for class_ in classes:
            categories = class_.__category__.split('/')
            for i in range(1, len(categories)):
                admin.add_sub_category(name=categories[i], parent_name=categories[i - 1])

            admin.add_view(
                class_(
                    model=class_.__model__,
                    session=admin.db.session,
                    name=class_.__model__.__name__,
                    category=categories[-1]
                )
            )
