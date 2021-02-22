from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from .config import MainConfig


class Application(Flask):

    def run(
        self, host=None, port=None, debug=None, load_dotenv=True, **options
    ):
        db.create_all()
        db.session.commit()

        return super().run(
            host=host,
            port=port,
            debug=debug,
            load_dotenv=load_dotenv,
            **options
        )

    @classmethod
    def jsonify(cls, *args, **kwargs):
        return jsonify(*args, **kwargs)


web_app = Application(__name__)
app_config = MainConfig()

web_app.config.from_object(app_config)

ma = Marshmallow(web_app)
db = SQLAlchemy(web_app)
