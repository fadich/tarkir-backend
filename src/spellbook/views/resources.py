from tarkir_base.api import app
from tarkir_base.api.views import MethodView, send_from_directory


class GetResourceView(MethodView):

    def get(self, filepath: str):
        return send_from_directory(
            app.config['UPLOAD_FOLDER'],
            filename=filepath
        )
