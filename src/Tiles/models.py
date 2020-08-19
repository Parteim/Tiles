from app import db


class Tile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(10), default='God')
    tile_type = db.Column(db.String(30))
    styles = db.relationship('TileStyles', uselist=False, backref='tile')

    elements = db.relationship('Elements', backref='tile')


class TileStyles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    background = db.Column(db.String(255))
    border = db.Column(db.String(255))
    filters = db.Column(db.String(255))

    tile_id = db.Column(db.Integer, db.ForeignKey('tile.id'))
    tile = db.relationship('Tile', backref='styles')


class Element(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    tile_id = db.Column(db.Integer, db.ForeignKey('tile.id'))
    tile = db.relationship('Tile', backref='elements')

    content_type = db.Column(db.String(50))

    columns = db.Column(db.String(5))
    rows = db.Column(db.String(5))

    text = db.Column(db.Text)
    images = db.Column(db.Integer)
    files = db.Column(db.Integer)
    links = db.Column(db.Integer)
    videos = db.Column(db.Integer)
