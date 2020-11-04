from tarkir.web_api import Handler

from spellbook.models import Color


class ColorsHandler(Handler):
    model = Color

    async def get(self):
        colors = await self.model.query.gino.all()
        colors = [color.to_dict() for color in colors]

        return self.send_json(body=colors)
