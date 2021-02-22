from tarkir import web_app

from spellbook.models import Color
# from spellbook.schemas import ColorSchema


@web_app.route('/colors')
def get_colors():
    colors = Color.query.all()
    return web_app.jsonify(colors)

    # return web_app.jsonify(
    #     ColorSchema().dump(colors, many=True)
    # )


if __name__ == '__main__':
    web_app.run()
