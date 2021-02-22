from tarkir.api import web_app

from spellbook.api.views import ColorsView


web_app.add_url_rule('/colors', view_func=ColorsView.as_view('colors'))


if __name__ == '__main__':
    web_app.run()
