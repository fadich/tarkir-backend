from tarkir.web_api import Application, Route

from .spellbook.handlers import (
    ColorsHandler,
    SchoolsHandler,
    # IndexHandler,
    SpellsHandler,
)


app = Application()

# app.add_route(
#     Route('/', app.METHOD_GET, IndexHandler)
# )
app.add_route(
    Route('/colors', app.METHOD_GET, ColorsHandler)
)
app.add_route(
    Route('/schools', app.METHOD_GET, SchoolsHandler)
)
app.add_route(
    Route('/spells', app.METHOD_GET, SpellsHandler)
)
