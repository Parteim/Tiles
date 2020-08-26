from .models import Tile, TileStyles, Element, TileContentVideo, TileContentLink, TileContentImage, TileContentFile
from Users.models import User
from app import ma


class TileSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tile

    id = ma.auto_field()
    author = ma.HyperlinkRelated(User)
    title = ma.auto_field()

    tile_type = ma.auto_field()

    styles = ma.auto_field()
    elements = ma.auto_field()


class TileStylesSchema(ma.SQLAlchemySchema):
    class Meta:
        model = TileStyles

    id = ma.auto_field()

    tile = ma.auto_field()

    background = ma.auto_field()
    border = ma.auto_field()


class ElementSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Element

    id = ma.auto_field()
    tile = ma.auto_field()
    content_type = ma.auto_field()

    columns = ma.auto_field()
    rows = ma.auto_field()

    text = ma.auto_field()
    images = ma.auto_field()
    files = ma.auto_field()
    links = ma.auto_field()
    videos = ma.auto_field()

