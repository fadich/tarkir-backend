from tarkir.web_api import Application, Route

from .handlers import ColorsHandler


spellbook_api = Application()
spellbook_api.add_route(
    Route('/colors', spellbook_api.METHOD_GET, ColorsHandler)
)

if __name__ == '__main__':
    spellbook_api.run_app(
        host='0.0.0.0',
        port=5000)
