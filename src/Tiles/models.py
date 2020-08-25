from app import db


class Tile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', back_populates='tiles')
    title = db.Column(db.String(150))
    tile_type = db.Column(db.String(30))
    styles = db.relationship('TileStyles', uselist=False, back_populates='tile')

    elements = db.relationship('Element', back_populates='tile')

    def __init__(self, author, tile_type, styles, title=None):
        self.author = author
        self.tile_type = tile_type
        self.styles = styles

        if title:
            self.title = title

    def __repr__(self):
        return f'id: {self.id}; author: {self.author}; title: {self.title}'


class TileStyles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    background = db.Column(db.String(255))
    border = db.Column(db.String(255))
    filters = db.Column(db.String(255))

    tile_id = db.Column(db.Integer, db.ForeignKey('tile.id'))
    tile = db.relationship('Tile', back_populates='styles')

    def __repr__(self):
        return f'id: {self.id}; tile: {self.tile.title or self.tile};'


class Element(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    tile_id = db.Column(db.Integer, db.ForeignKey('tile.id'))
    tile = db.relationship('Tile', back_populates='elements')

    content_type = db.Column(db.String(50))

    columns = db.Column(db.String(5))
    rows = db.Column(db.String(5))

    text = db.Column(db.Text)
    images = db.relationship('TileContentImage', uselist=False, back_populates='element')
    files = db.relationship('TileContentFile', uselist=False, back_populates='element')
    links = db.relationship('TileContentLink', uselist=False, back_populates='element')
    videos = db.relationship('TileContentVideo', uselist=False, back_populates='element')

    def __init__(self, tile, content_type, columns, rows, text=None):
        self.tile = tile
        self.content_type = content_type
        self.columns = columns
        self.rows = rows

        if text:
            self.text = text

    def __repr__(self):
        return f'id: {self.id};  tile: {self.tile.title or self.tile};'


class TileElementContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    path = db.Column(db.String(255))

    element_id = db.Column(db.Integer, db.ForeignKey('element.id'))
    element = db.relationship('Element', back_populates='images')

    def __init__(self, content, element):
        self.content = content
        self.element = element

    def __repr__(self):
        return f'id: {self.id}; path: {self.path}; element: {self.element};'


class TileContentImage(TileElementContent):
    element = db.relationship('Element', back_populates='images')


class TileContentFile(TileElementContent):
    element = db.relationship('Element', back_populates='files')


class TileContentVideo(TileElementContent):
    element = db.relationship('Element', back_populates='videos')


class TileContentLink(TileElementContent):
    element = db.relationship('Element', back_populates='links')
