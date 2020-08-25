from flask import Blueprint, request, render_template, jsonify
from flask.views import MethodView

# models
from .models import Element, TileStyles, Tile
from .schems import TileSchema, TileStylesSchema, ElementSchema

MODULE_NAME = 'Tiles'

tiles = Blueprint(MODULE_NAME, __name__)


class SingleTile(MethodView):

    def get(self, tile_id):
        return

    def post(self):
        content = request.get_json(force=True)

        tile = {
            'author': '',
            'title': '',
            'styles': '',
            'elements': [],
        }

        styles = {
            'background': '',
            'border': '',
            'tile': '',
        }

        element = {
            'tile': '',
            'content_type': '',
            'columns': '',
            'rows': '',
            'text': '',
        }

        response = {
            'status': 'Successful',
            'username': content['username'],
        }

        return jsonify(response)


tile = SingleTile.as_view('tile')
tiles.add_url_rule('/get-tile/<int:tile_id>/', view_func=tile, methods=['GET', ])
tiles.add_url_rule('/create-tile/', view_func=tile, methods=['POST', ])
