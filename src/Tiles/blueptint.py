from flask import Blueprint, request, render_template, jsonify

# models
from Tiles.models import Element, TileStyles, Tile

MODULE_NAME = 'Tiles'

tiles = Blueprint(MODULE_NAME, __name__)


@tiles.route('/create-tile', methods=['POST'])
def create_tile():

    return 'created'
