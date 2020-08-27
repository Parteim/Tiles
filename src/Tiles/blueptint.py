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
    user_schema = UserSchema()
    tile_schema = TileSchema()
    tiles_schema = TileSchema(many=True)
    tile_styles_schema = TileStylesSchema()
    tile_element_schema = ElementSchema()

    def compose_response_tile(self, tile):
        response = self.tile_schema.dump(tile)
        author = self.user_schema.dump(
            User.query.get(response['author'])
        )
        response['author'] = author
        styles = self.tile_styles_schema.dump(
            TileStyles.query.get(response['styles'])
        )
        response['styles'] = styles

        elements = []
        for element_id in response['elements']:
            element = self.tile_element_schema.dump(
                Element.query.get(element_id)
            )
            elements.append(element)
        response['elements'] = elements

        return jsonify(response)

    def get(self, tile_id):
        tile = Tile.query.get(tile_id)

        if tile is None:
            return {'error': 'tile not exist'}

        return self.compose_response_tile(tile)

    def post(self):
        content = request.get_json(force=True)

        user = User.query.filter(User.email == content['tile']['author']).first()

        print(user)

        tile = Tile(
            author=user,
            title=content['tile']['title'],
            tile_type=content['tile']['type'],
        )

        tile_styles = TileStyles(
            background=content['tile']['styles']['background'],
            border=content['tile']['styles']['border'],
            tile=tile,
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

        created_tile = Tile.query.all()[-1]

        return self.compose_response_tile(created_tile)


tile = SingleTile.as_view('tile')
tiles.add_url_rule('/get-tile/<int:tile_id>/', view_func=tile, methods=['GET', ])
tiles.add_url_rule('/create-tile/', view_func=tile, methods=['POST', ])
