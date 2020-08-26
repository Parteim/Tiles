from flask import Blueprint, request, render_template, jsonify
from flask.views import MethodView, View
from flask_login import current_user

from app import db

# models
from .models import Element, TileStyles, Tile
from .schems import TileSchema, TileStylesSchema, ElementSchema
from Users.models import User
from Users.schems import UserSchema

MODULE_NAME = 'Tiles'

tiles = Blueprint(MODULE_NAME, __name__)


class SingleTile(MethodView):
    tile_schema = TileSchema()
    tiles_schema = TileSchema(many=True)

    def get(self, tile_id):
        print(request.url)
        tile = Tile.query.get(tile_id)

        response = self.tile_schema.dump(tile) or {'status': 'tile not exist'}

        return jsonify(response)

    def post(self):
        content = request.get_json(force=True)

        user = User.query.filter(User.email == content['tile']['author']).first()

        print(user)

        tile_styles = TileStyles(
            background=content['tile']['styles']['background'],
            border=content['tile']['styles']['border'],
        )

        tile = Tile(
            author=user,
            title=content['tile']['title'],
            styles=tile_styles,
            tile_type=content['tile']['type'],
        )

        element = Element(
            tile=tile,
            content_type=content['tile']['elements'][0]['content_type'],
            columns=content['tile']['elements'][0]['columns'],
            rows=content['tile']['elements'][0]['rows'],
            text=content['tile']['elements'][0]['text'],
        )

        db.session.add_all([
            tile_styles,
            tile,
            element,
        ])
        db.session.commit()

        output_tile = Tile.query.all()[-1]

        response = {
            'status': 'Successful',
            'username': user.username,
            'tile': self.tile_schema.dump(output_tile),
        }

        return jsonify(response)


tile = SingleTile.as_view('tile')
tiles.add_url_rule('/get-tile/<int:tile_id>/', view_func=tile, methods=['GET', ])
tiles.add_url_rule('/create-tile/', view_func=tile, methods=['POST', ])
